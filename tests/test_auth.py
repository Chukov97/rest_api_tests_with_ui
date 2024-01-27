import allure
from selene import browser
from pages.main_page import main_page
from pages.base_page import base_page
from api.demowebshop_api import demo_web_shop_api
from test_data.auth_data import VALID_CREDENTIALS


@allure.title('Проверка успешной авторизации')
def test_valid_auth(browser_management):
    with allure.step('Авторизация через API'):
        response = demo_web_shop_api.login_user(VALID_CREDENTIALS.model_dump())
        cookie = response.get_cookies('NOPCOMMERCE.AUTH')
    with allure.step('Открытие главной страницы'):
        main_page.open_page()
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})
        main_page.open_page()
    with allure.step('Проверка авторизации'):
        user_name = main_page.get_user_name()
        base_page.assert_equals(VALID_CREDENTIALS.Email, user_name,
                                f'Имя пользователя {user_name}, а должно быть {VALID_CREDENTIALS.Email}')

