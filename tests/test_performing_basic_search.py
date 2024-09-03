import allure
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.search_data_cat_page import SearchDataCatPage

@allure.epic("UI")
@allure.feature('Выполнение основного поиска')
@allure.title('Отображается главная страница')
def test_displayed_main_page(browser):
    BasePage(browser).open_main_page()
    MainPage(browser).displayed_main_page()

@allure.epic("UI")
@allure.feature('Выполнение основного поиска')
@allure.title('Отображается данные "Кошка" в поле "Поиск"')
def test_displayed_cat_search_field(browser):
    BasePage(browser).open_main_page()
    MainPage(browser).input_cat_search(). \
        displayed_data_cat()


@allure.epic("UI")
@allure.feature('Выполнение основного поиска')
@allure.title('Отображается страница поиска "Кошка"')
def test_displayed_cat_page(browser):
    BasePage(browser).open_main_page()
    MainPage(browser).input_cat_search(). \
        click_search_google()
    SearchDataCatPage(browser).displayed_cat_found_resource()