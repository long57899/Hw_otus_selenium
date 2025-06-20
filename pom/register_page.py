from pom.base_page import BasePage,OpenPageMixin
import allure
class RegisterPage(BasePage,OpenPageMixin):
    def __init__(self, browser, base_url):
        super().__init__(browser, base_url, path="/index.php?route=account/register")
        self.open_page(self.path)
        self.input_first_name =  super().get_element('#input-firstname')
        self.input_last_name = super().get_element('#input-lastname')
        self.input_email = super().get_element('#input-email')
        self.input_password = super().get_element('#input-password')
        self.newsletter = super().get_element('#input-password')
        self.agree = super().get_element('input[name="agree"]')
        self.continue_button = super().get_element('#form-register > div > button')

    allure.step("Регистрация пользователя с данными {user_data}.")
    def register(self, user_data:dict):
        '''Регистрация нового человека.'''
        self.logger.info("Start register customer.") 
        self.logger.info("Begin to input data of customer.")

        self.input_first_name.send_keys(user_data.get("first_name"))
        self.input_last_name.send_keys(user_data.get("last_name"))
        self.input_email.send_keys(user_data.get("email"))
        self.input_password.send_keys(user_data.get("password"))

        self.logger.info("End to input data of customer.") 
        super().click_element(self.agree)

        self.logger.info("End to register customer.") 
        super().click_element(self.continue_button)

    @property
    def result(self):
        return super().get_element("#content > h1")
        
        
        