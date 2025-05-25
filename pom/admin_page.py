from pom.base_page import BasePage,OpenPageMixin
import allure

@allure.epic("Страница администратора.")
class AdminMainPage(BasePage,OpenPageMixin):
    def __init__(self, browser, base_url):
        super().__init__(browser, base_url, path="/administration")
        self.open_page(self.path)
        self.admin_modal = super().get_element('#form-login',"Форма логинации")
        self.input_login = super().get_element('#input-username', "Поле ввода Логина")
        self.input_password = super().get_element('#input-password', "Поле ввода Пароля")
        self.button_login = super().get_element('#form-login > div.text-end > button', "Кнопка Логина")

    @allure.feature("Логинация")
    @allure.step("Захожу на проект с данными {login_data}.")
    def login(self,login_data:dict):
        '''Логинация на страницу Администратора.'''
        try:
            login_field = self.input_login
            password_field = self.input_password

            self.logger.info("Start to login on Opencart.")
            self.logger.info(f"Start to input {login_data} on Opencart.")
            super().input_value(login_field, login_data.get("login", ""))
            super().input_value(password_field, login_data.get("password", ""))
            self.logger.info(f"End to input {login_data} on Opencart.")
            self.button_login["element"].click()
            self.logger.info("Login successful")

        except Exception as e:
            error_msg = f"Ошибка логина: {str(e)}"
            self.logger.error(error_msg, exc_info=True)
            allure.attach(
                self.browser.get_screenshot_as_png(),
                name="login_error",
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(error_msg) from e

    @allure.feature("Выход из проекта.")
    @allure.step("Выхожу из проекта.")
    def logout(self):
        try:
            self.logger.info("Logout from Opencart.")
            button_logout = super().get_element('#nav-logout',"Кнопка для выхода из проекта.")
            super().click_element(button_logout)

        except Exception as e:
            error_msg ="Проблема выхода из проекта."
            self.logger.error(error_msg, exc_info=True)
            allure.attach(
            self.browser.get_screenshot_as_png(),
            name="logout_error",
            attachment_type=allure.attachment_type.PNG)
            raise AssertionError(error_msg) from e


    @property
    def title_admin(self):
        title = self.get_element('#content > div.page-header > div > h1' , "Название титульной страницы.")
        return title.get("element")
  



    