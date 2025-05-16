from pom.base_page import BasePage,OpenPageMixin

class AdminMainPage(BasePage,OpenPageMixin):
    def __init__(self, browser, base_url):
        super().__init__(browser, base_url, path="/administration")
        self.open_page(self.path)
        self.admin_modal = super().get_element('#form-login')
        self.input_login = super().get_element('#input-username')
        self.input_password = super().get_element('#input-password')
        self.button_login = super().get_element('#form-login > div.text-end > button')

    def login(self,login_data:dict):
        super().input_value(self.input_login, login_data.get("login"))
        super().input_value(self.input_password, login_data.get("password"))
        super().click_element(self.button_login)

    def logout(self):
        button_logout = super().get_element('#nav-logout')
        super().click_element(button_logout)
        super().get_element('#input-username')

    @property
    def title_admin(self):
        return self.get_element('#content > div.page-header > div > h1')
    
  



    