from selene import browser, query


class CartPage:
    product_name = '.product-name'

    def get_product_name(self):
        return browser.element(self.product_name).get(query.text)


cart_page = CartPage()
