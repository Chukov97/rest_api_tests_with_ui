import allure
import requests
from utils.logger import log
from jsonschema import validate


class Api:
    """Основной класс для работы с API"""
    _URL = 'https://demowebshop.tricentis.com'
    _TIMEOUT = 10

    def __init__(self):
        self.response = None

    # METHODS API

    @allure.step("Отправить POST-запрос")
    def post(self, url: str, endpoint: str, params: dict = None,
             json_body: dict = None, headers: dict = None):
        with allure.step(f"POST-запрос на url: {url}{endpoint}"
                         f"\n тело запроса: \n {json_body}"):
            self.response = requests.post(url=f"{url}{endpoint}",
                                          headers=headers,
                                          params=params,
                                          json=json_body,
                                          timeout=self._TIMEOUT,
                                          allow_redirects=False)
        log(response=self.response, request_body=json_body)
        return self

    @allure.step("Отправить GET-запрос")
    def get(self, url: str, endpoint: str, params: dict = None, headers: dict = None):
        with allure.step(f"GET запрос на url: {url}{endpoint}"):
            self.response = requests.get(url=f"{url}{endpoint}",
                                         headers=headers,
                                         params=params,
                                         timeout=self._TIMEOUT,
                                         allow_redirects=False)
        log(response=self.response)
        return self

    @allure.step("Отправить PUT запрос")
    def put(self, url: str, endpoint: str, params: dict = None, json_body: dict = None, headers: dict = None):
        with allure.step(f"PUT запрос на url: {url}{endpoint}"
                         f"\n тело запроса: \n {json_body}"):
            self.response = requests.put(url=f"{url}{endpoint}",
                                         headers=headers,
                                         params=params,
                                         json=json_body,
                                         timeout=self._TIMEOUT,
                                         allow_redirects=False)
        log(response=self.response, request_body=json_body)
        return self

    @allure.step("Отправить DELETE запрос")
    def delete(self, url: str, endpoint: str, headers: dict = None):
        with allure.step(f"DELETE запрос на url: {url}{endpoint}"):
            self.response = requests.delete(url=f"{url}{endpoint}",
                                            headers=headers,
                                            timeout=self._TIMEOUT,
                                            allow_redirects=False)
        log(response=self.response)
        return self

    @allure.step("Получить cookies")
    def get_cookies(self, name_cookies=None):
        cookies = self.response.cookies.get(name_cookies)
        return cookies

        # ASSERTIONS:

    @allure.step("Статус код ответа равен {expected_code}")
    def status_code_should_be(self, expected_code: int):
        """Проверяем статус код ответа actual_code на соответствие expected_code"""
        actual_code = self.response.status_code
        assert expected_code == actual_code, f"\nОжидаемый результат: {expected_code} " \
                                             f"\nФактический результат: {actual_code}"
        return self

    @allure.step("ОР: Cхема ответа json валидна")
    def json_schema_should_be_valid(self, json_schema):
        """Проверяем полученный ответ на соответствие json схеме"""
        validate(self.response.json(), json_schema)
        return self

    @allure.step("ОР: В поле ответа содержится искомое значение")
    def have_value_in_response_parameter(self, parameter_name: str, expected_value: str):

        api_data = self.response.json()
        actual_value = self.find_value_from_nested_dict(api_data, parameter_name)

        assert actual_value == expected_value, f"\nОжидаемый результат: {expected_value} " \
                                               f"\nФактический результат: {actual_value}"

    def find_value_from_nested_dict(self, dictionary, parameter_name):
        if parameter_name in dictionary:
            return dictionary[parameter_name]

        for value in dictionary.values():
            if isinstance(value, dict):
                nested_value = self.find_value_from_nested_dict(value, parameter_name)

                if nested_value is not None:
                    return nested_value

        return f'Параметр не найден'
