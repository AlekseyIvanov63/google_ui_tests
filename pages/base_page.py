from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.actions = ActionChains(browser)
        self.logger = browser.logger
        self.class_name = type(self).__name__

    def open_main_page(self):
        self.logger.info("Opening url %s" % self.class_name)
        self.browser.get(self.browser.url)
        return self

    def wait_element(self, locator, timeout=9):
        self.logger.info("%s: Wait element: %s" % (self.class_name, str(locator)))
        return WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))

    def click(self, locator, timeout=10):
        self.logger.info("%s: Clicking element: %s" % (self.class_name, str(locator)))
        self.actions.move_to_element(WebDriverWait(self.browser, timeout)
                                     .until(EC.visibility_of_element_located(locator))) \
            .pause(0.8).click().perform()

    def input_value(self, locator, text, timeout=7):
        self.logger.info("%s: Input '%s' in input %s" % (self.class_name, text, locator))
        WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator)).click()
        WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator)).clear()
        for l in text:
            WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator)).send_keys(l)
