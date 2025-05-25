from pom.base_page import BasePage,OpenPageMixin
import allure
@allure.epic("Работаем со странице каталога.")
class CatalogPage(BasePage,OpenPageMixin):
   @allure.step("Открываем страницу каталого.")
   def __init__(self, browser, base_url):
         super().__init__(browser, base_url, path="/en-gb/catalog")
         try:
            self.logger.info("Open page catalog")
            self.open_page(self.path)    
            self.catalog_list = super().get_element("#column-left > div.list-group.mb-3","Список в каталоге")
            self.button_continue = super().get_element("#content > div > a","Кнопка далее")
            self.content_text = super().get_element("#content > h1","Описание")
            self.home = super().get_element("#error-not-found > ul > li:nth-child(1) > a", "Кнопка домой")
            self.cameras = super().get_element("#column-left > div.list-group.mb-3 > a:nth-child(7)", "Камеры")
         except Exception as e:
            error_msg ="Error open page Catalog."
            self.logger.error(error_msg, exc_info=True)
            allure.attach(
            self.browser.get_screenshot_as_png(),
            name="error_Catalog_page",
            attachment_type=allure.attachment_type.PNG)
            raise AssertionError(error_msg) from e 
 