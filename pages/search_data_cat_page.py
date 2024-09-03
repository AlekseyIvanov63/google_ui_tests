import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep


class SearchDataCatPage(BasePage):
    FIRST_FOUND_RESOURCE =  (By.XPATH, '//h3[text()="Кошка"]')
    SECOND_FOUND_RESOURCE = (By.XPATH, '//h3[text()="кошка"]')

    @allure.step('Посмотреть отображение найденных ресурсов по данным "Кошка"')
    def displayed_cat_found_resource(self):
        self.browser.refresh()
        assert self.wait_element(self.FIRST_FOUND_RESOURCE).is_displayed()
        assert self.wait_element(self.SECOND_FOUND_RESOURCE).is_displayed()
