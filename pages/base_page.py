class BasePage:

    @staticmethod
    def assert_equals(expected, actual, actual_msg):
        assert expected == actual, actual_msg


base_page = BasePage()
