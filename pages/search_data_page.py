import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SearchDataCatPage(BasePage):
    CAT_FOUND_RESOURCE =  (By.XPATH, '//h3[text()="Кошка"]')
    SEARCH_FIELD = (By.CSS_SELECTOR, '#APjFqb')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '#tsf > div:nth-child(1) > div.A8SBwf.emcav > div.RNNXgb > button > div > span > svg')
    CHERRY_FOUND_RESOURCE = (By.XPATH, '//h3[text()="Вишня войлочная"]')
    TIRE_FOUND_RESOURCE = (By.XPATH, '//h3[contains(text(),"шины R15")]')


    @allure.step('Посмотреть отображение найденных ресурсов по данным "Кошка"')
    def displayed_cat_found_resource(self):
        self.browser.set_page_load_timeout(3)
        assert self.wait_element(self.CAT_FOUND_RESOURCE).is_displayed()


    @allure.step('Ввод данных "вишня войлочная" в поле "Поиск"')
    def input_data_cherry(self):
        self.input_value(self.SEARCH_FIELD, 'вишня войлочная')
        return self

    @allure.step('Посмотреть отображение данных "вишня войлочная" в поле "Поиск"')
    def displayed_cherry_search_field(self):
        assert self.browser.find_element(*self.SEARCH_FIELD).get_attribute('value') == "вишня войлочная"


    @allure.step('Кликнуть кнопку "Поиск"')
    def click_search_button(self):
        self.click(self.SEARCH_BUTTON)
        return self

    @allure.step('Посмотреть отображение найденных ресурсов по данным "вишня войлочная"')
    def displayed_cherry_found_resource(self):
        self.browser.set_page_load_timeout(3)
        assert self.wait_element(self.CHERRY_FOUND_RESOURCE).is_displayed()

    @allure.step('Ввод данных "шины R15" в поле "Поиск"')
    def input_data_tire(self):
        self.input_value(self.SEARCH_FIELD, 'шины R15')
        return self

    @allure.step('Посмотреть отображение данных "шины R15" в поле "Поиск"')
    def displayed_tire_search_field(self):
        assert self.browser.find_element(*self.SEARCH_FIELD).get_attribute('value') == "шины R15"

    @allure.step('Посмотреть отображение найденных ресурсов по данным "шины R15"')
    def displayed_tire_found_resource(self):
        self.browser.set_page_load_timeout(3)
        assert self.wait_element(self.TIRE_FOUND_RESOURCE).is_displayed()
