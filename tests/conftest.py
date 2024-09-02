import time
import pytest
import datetime
import logging
import allure
import json
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.firefox.options import Options as FFOptions


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.outcome != 'passed':
        item.status = 'failed'
    else:
        item.status = 'passed'


def pytest_addoption(parser):
    parser.addoption("--browser", "-B", action="store", default="chrome")
    parser.addoption("--url", "-U", action="store", default="https://www.google.com/")
    parser.addoption("--log_level", action="store", default="INFO")
    parser.addoption("--executor", action="store", default="") #127.0.0.1
    parser.addoption("--bv")
    parser.addoption("--video", action="store")


@allure.step("Waiting for availability {url}")
def wait_url_data(url, timeout=10):
    while timeout:
        response = requests.get(url)
        if not response.ok:
            time.sleep(1)
            timeout -= 1
        else:
            if "video" in url:
                return response.content
            else:
                return response.text
    return None


@pytest.fixture()
def browser(request):
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    log_level = request.config.getoption("--log_level")
    executor = request.config.getoption("--executor")
    version = request.config.getoption("--bv")
    executor_url = f"http://{executor}:4444/wd/hub"
    video = request.config.getoption("--video")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"../google_ui_tests/logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info("===> Test %s started at %s" % (request.node.name, datetime.datetime.now()))
    if executor:
        if browser == "chrome":
            options = ChromeOptions()
        elif browser == "firefox":
            options = FirefoxOptions()

        caps = {
            "browserName": browser,
            "browserVersion": "100.0",
            "selenoid:options": {
                "enableVideo": False,
            },
        }

        for k, v in caps.items():
            options.set_capability(k, v)

        logger.info("Browser %s started" % browser)

        driver = webdriver.Remote(
            command_executor=executor_url,
            options=options
        )
    else:
        if browser == "chrome":
            options = ChromeOptions()
            options.add_argument("--use-fake-ui-for-media-stream")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--use-fake-device-for-media-stream")
            driver = webdriver.Chrome(options=options,
                                      service=ChromiumService())
        elif browser == "firefox":
            driver = webdriver.Firefox(options=FFOptions(),
                                       service=FFService(executable_path='/snap/bin/firefox.geckodriver'))
        else:
            driver = webdriver.Safari()

    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name

    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name

    driver.maximize_window()
    driver.get(url)
    driver.url = url

    allure.attach(
        name=driver.session_id,
        body=json.dumps(driver.capabilities, indent=4, ensure_ascii=False),
        attachment_type=allure.attachment_type.JSON)

    driver.test_name = request.node.name
    driver.log_level = logging.DEBUG

    yield driver

    if request.node.status == "failed":
        allure.attach(
            name="failure_screenshot",
            body=driver.get_screenshot_as_png(),
            attachment_type=allure.attachment_type.PNG
        )

    def fin():
        video_url = f"http://{executor}:8080/video/{driver.session_id}.mp4"

        if request.node.status == "failed":
            if video:
                allure.attach(
                    body=wait_url_data(video_url),
                    name="video_for_" + driver.session_id,
                    attachment_type=allure.attachment_type.MP4,
                )

        if video and wait_url_data(video_url):
            requests.delete(url=video_url)

        driver.quit()
        logger.info("===> Test %s finished at %s" % (request.node.name, datetime.datetime.now()))

    request.addfinalizer(fin)
    return driver
