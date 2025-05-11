from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

from pom.base_page import BasePage


class AdminPage(BasePage):
    def __init__(self, browser, base_url):
        super().__init__(browser, base_url, path="/administration")

        self.admin_modal = super().get_element('#form-login',"css")
        
        self.input_login = super().get_element('#input-username',"css")
    
        self.input_password = super().get_element('#input-password',"css")

        self.button_login = super().get_element('#form-login > div.text-end > button',"css")

        load_dotenv()

        self.load_env = {"login":os.getenv("LOGIN"),"password":os.getenv("PASSWORD")}
    
    
    def login(self):
        super().input_value(self.input_login, self.load_env.get("login"))
        super().input_value(self.input_password, self.load_env.get("password"))
        super().click_element(self.button_login)

        self.title_admin = super().get_element('#content > div.page-header > div > h1',"css")
      
        self.button_logout = super().get_element('#nav-logout',"css")

    def logout(self):
        super().click_element(self.button_logout)
        
        super().get_element('#input-username',"css")
    