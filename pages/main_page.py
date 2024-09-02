import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    MAIN_LOGO = (By.XPATH, '//img[@alt="Google"]')
    SEARCH_FIELD = (By.CSS_SELECTOR, '#APjFqb')


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
