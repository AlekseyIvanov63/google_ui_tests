import allure
from elements.base_element import BaseElement
from elements.main_elements import MainElement

@allure.epic("UI")
@allure.feature('Выполнение основного поиска')
@allure.title('Посмотреть отображение главной страницы')
def test_displayed_main_page(browser):
    BaseElement(browser).open_main_page()
    MainElement(browser).displayed_main_page()
