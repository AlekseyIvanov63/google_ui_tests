import allure
from selenium.webdriver.common.by import By
from elements.base_element import BaseElement


class MainElement(BaseElement):
    MAIN_LOGO = (By.XPATH, '//img[@alt="Google"]')


    @allure.step('Посмотреть отображение логотива главной старницы')
    def displayed_main_page(self):
        assert self.wait_element(self.MAIN_LOGO).is_displayed()
