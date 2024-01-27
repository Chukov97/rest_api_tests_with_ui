import allure

from api.base_api import Api


class DemoWebShop(Api):
    """ENDPOINT"""
    _ENDPOINT_LOGIN = '/login/'
    _ENDPOINT_ADD_TO_CART = '/addproducttocart/catalog/31/1/1'

    @allure.step('Авторизация юзера')
    def login_user(self, param_request_body):
        return self.post(url=Api._URL, endpoint=self._ENDPOINT_LOGIN, json_body=param_request_body)

    @allure.step('Добавление товара в корзину')
    def add_product_to_cart(self, param_request_body=None):
        return self.post(url=Api._URL, endpoint=self._ENDPOINT_ADD_TO_CART, json_body=param_request_body)


demo_web_shop_api = DemoWebShop()
