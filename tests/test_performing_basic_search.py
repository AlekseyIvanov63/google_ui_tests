import allure
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.search_data_page import SearchDataCatPage

@allure.epic("UI")
@allure.feature('Выполнение основного поиска')
@allure.title('Отображается главная страница')
def test_displayed_main_page(browser):
    BasePage(browser).open_main_page()
    MainPage(browser).displayed_main_page()

@allure.epic("UI")
@allure.feature('Выполнение основного поиска')
@allure.title('Отображаются данные "Кошка" в поле "Поиск"')
def test_displayed_cat_search_field(browser):
    BasePage(browser).open_main_page()
    MainPage(browser).input_cat_search(). \
        displayed_data_cat()


@allure.epic("UI")
@allure.feature('Выполнение основного поиска')
@allure.title('Отображается страница с результатами поиска "Кошка"')
def test_displayed_cat_page(browser):
    BasePage(browser).open_main_page()
    MainPage(browser).input_cat_search(). \
        click_search_google()
    SearchDataCatPage(browser).displayed_cat_found_resource()


@allure.epic("UI")
@allure.feature('Выполнение основного поиска')
@allure.title('Отображаются данные "вишня войлочная" в поле "Поиск"')
def test_displayed_cherry_search_field(browser):
    BasePage(browser).open_main_page()
    MainPage(browser).input_cat_search(). \
        click_search_google()
    SearchDataCatPage(browser).input_data_cherry(). \
        displayed_cherry_search_field()


@allure.epic("UI")
@allure.feature('Выполнение основного поиска')
@allure.title('Отображается страница с результатами поиска "вишня войлочная"')
def test_displayed_cherry_page(browser):
    BasePage(browser).open_main_page()
    MainPage(browser).input_cat_search(). \
        click_search_google()
    SearchDataCatPage(browser).input_data_cherry(). \
        click_search_button(). \
        displayed_cherry_found_resource()


@allure.epic("UI")
@allure.feature('Выполнение основного поиска')
@allure.title('Отображаются данные "шины R15" в поле "Поиск"')
def test_displayed_tire_search_field(browser):
    BasePage(browser).open_main_page()
    MainPage(browser).input_cat_search(). \
        click_search_google()
    SearchDataCatPage(browser).input_data_cherry(). \
        click_search_button(). \
        input_data_tire(). \
        displayed_tire_search_field()


@allure.epic("UI")
@allure.feature('Выполнение основного поиска')
@allure.title('Отображается страница с результатами поиска "шины R15"')
def test_displayed_tire_page(browser):
    BasePage(browser).open_main_page()
    MainPage(browser).input_cat_search(). \
        click_search_google()
    SearchDataCatPage(browser).input_data_cherry(). \
        click_search_button(). \
        input_data_tire(). \
        click_search_button(). \
        displayed_tire_found_resource()
