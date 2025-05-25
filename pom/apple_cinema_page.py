from pom.base_page import BasePage,OpenPageMixin
import allure
@allure.epic("Работаем на странице Эпл")
class AppleCinemaPage(BasePage,OpenPageMixin):
    @allure.step("Открываем страницу Эпл")
    def __init__(self, browser, base_url):
        super().__init__(browser, base_url, path="/en-gb/product/desktops/apple-cinema")
        self.logger.info("Open page Apple.")
        try:
            self.open_page(self.path)
            self.add_to_wish_list = super().get_element('//*[@id="content"]/div[1]/div[2]/form/div/button[1]/i',"Добавить в список желаемого")
            self.select_color = super().get_element('//*[@id="input-option-217"]', "Выбор цвета")
            self.button_cart = super().get_element('//*[@id="button-cart"]', "Кнопка корзины")
            self.tab_description = super().get_element('//*[@id="tab-description"]', "Описание")
            self.tab_review = super().get_element('//*[@id="content"]/div[1]/ul/li[3]/a', "Отзывы")
        except Exception as e:
            error_msg ="Error open page Apple cinema."
            self.logger.error(error_msg, exc_info=True)
            allure.attach(
            self.browser.get_screenshot_as_png(),
            name="error_Ac_page",
            attachment_type=allure.attachment_type.PNG)
            raise AssertionError(error_msg) from e     