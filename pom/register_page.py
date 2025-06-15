from pom.base_page import BasePage,OpenPageMixin
import allure

@allure.epic("Работа со страницей регистрации.")
class RegisterPage(BasePage,OpenPageMixin):
    @allure.step("Открываю страницу регистрации.")
    def __init__(self, browser, base_url):
        super().__init__(browser, base_url, path="/index.php?route=account/register")
        self.open_page(self.path)
        self.input_first_name =  super().get_element('#input-firstname',"Поле ввода имени пользователя")
        self.input_last_name = super().get_element('#input-lastname',"Поле ввода фамилии пользователя")
        self.input_email = super().get_element('#input-email',"Поле ввода почты пользователя")
        self.input_password = super().get_element('#input-password',"Поле ввода пароля пользователя")
        self.newsletter = super().get_element('#input-newsletter', "Чекбокс подписки." )
        self.agree = super().get_element('input[name="agree"]', "Чекбокс согласия на обработку данных.")
        self.continue_button = super().get_element('#form-register > div > button', "Кнопка регистрации.")

    allure.step("Регистрация пользователя с данными {user_data}.")
    def register(self, user_data:dict):
        '''Регистрация нового человека.'''
        self.logger.info("Start register customer.") 
        self.logger.info("Begin to input data of customer.")
        try:
            super().input_value(self.input_first_name,user_data.get("first_name"))
            super().input_value(self.input_last_name,user_data.get("last_name"))
            super().input_value(self.input_email,user_data.get("email"))
            super().input_value(self.input_password,user_data.get("password"))

            self.logger.info("End to input data of customer.") 
            super().click_element(self.agree)

            self.logger.info("End to register customer.") 
            super().click_element(self.continue_button)
        except Exception as e:
            error_msg ="Error with register new customer."
            self.logger.error(error_msg, exc_info=True)
            allure.attach(
            self.browser.get_screenshot_as_png(),
            name="error_register_customer",
            attachment_type=allure.attachment_type.PNG)
            raise AssertionError(error_msg) from e 

    @allure.step("Получения Результата.")
    def result(self):
        result_dict = super().get_element("#content > h1", "Результат")
        return result_dict["element"]
        
        
        