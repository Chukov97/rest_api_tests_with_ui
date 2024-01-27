from selene import browser, query


class MainPage:
    user_name = 'a.account'
    cart = '.cart-label'

    def open_page(self):
        browser.open('/')
        return self

    def get_user_name(self):
        return browser.element(self.user_name).get(query.text)

    def click_to_cart(self):
        return browser.element(self.cart).click()


main_page = MainPage()
