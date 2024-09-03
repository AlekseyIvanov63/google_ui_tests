import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    MAIN_LOGO = (By.XPATH, '//img[@alt="Google"]')
    SEARCH_FIELD = (By.CSS_SELECTOR, '#APjFqb')
    SEARCH_GOOGLE_BUTTON = (By.CSS_SELECTOR, 'div:nth-child(1) > div.A8SBwf > div.FPdoLc.lJ9FBc > center > input.gNO89b')


    @allure.step('Посмотреть отображение логотива главной старницы')
    def displayed_main_page(self):
        assert self.wait_element(self.MAIN_LOGO).is_displayed()


    @allure.step('Посмотреть отображение логотива главной старницы')
    def input_cat_search(self):
        self.input_value(self.SEARCH_FIELD, 'Кошка')
        return self

    @allure.step('Посмотреть отображение данных "Кошка" в поле "Поиск"')
    def displayed_data_cat(self):
            assert self.browser.find_element(*self.SEARCH_FIELD).get_attribute('value') == "Кошка"

    @allure.step('Кликнуть кнопку "Поиск в Google"')
    def click_search_google(self):
        self.click(self.SEARCH_GOOGLE_BUTTON)
        return self
