from pom.base_page import BasePage,OpenPageMixin

class AppleCinemaPage(BasePage,OpenPageMixin):
    def __init__(self, browser, base_url):
        super().__init__(browser, base_url, path="/en-gb/product/desktops/apple-cinema")
        self.open_page(self.path)
        self.add_to_wish_list = super().get_element('//*[@id="content"]/div[1]/div[2]/form/div/button[1]/i')
        self.select_color = super().get_element('//*[@id="input-option-217"]')
        self.button_cart = super().get_element('//*[@id="button-cart"]')
        self.tab_description = super().get_element('//*[@id="tab-description"]')
        self.tab_review = super().get_element('//*[@id="content"]/div[1]/ul/li[3]/a')   