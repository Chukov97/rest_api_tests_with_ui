import allure
from selene import browser
from pages.main_page import main_page
from pages.base_page import base_page
from pages.cart_page import cart_page
from api.demowebshop_api import demo_web_shop_api
from test_data.auth_data import VALID_CREDENTIALS


@allure.title('Проверка добавления товара в корзину')
def test_add_product_to_cart(browser_management):
    with allure.step('Авторизвция через API'):
        response = demo_web_shop_api.login_user(VALID_CREDENTIALS.model_dump())
        cookie = response.get_cookies('NOPCOMMERCE.AUTH')
    with allure.step('Открытие главной страницы'):
        main_page.open_page()
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})
    with allure.step('Добавление товара в корзину'):
        demo_web_shop_api.add_product_to_cart(param_request_body=None)
    with allure.step('Открытие главной страницы'):
        main_page.open_page()
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})
        main_page.open_page()
    with allure.step('Переход в корзину'):
        main_page.click_to_cart()
    with allure.step('Проверка товара в корзине'):
        product_name = cart_page.get_product_name()
        base_page.assert_equals('14.1-inch Laptop', product_name,
                                f'Наименование товара {product_name}, а должно быть "14.1-inch Laptop"')
