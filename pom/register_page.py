from pom.base_page import BasePage

class RegisterPage(BasePage):
   
    def __init__(self, browser, base_url):
        super().__init__(browser, base_url, path="/index.php?route=account/register")
        
        self.input_first_name =  super().get_element('#input-firstname',"css")

        self.input_last_name = super().get_element('#input-lastname',"css")
    
        self.input_email = super().get_element('#input-email',"css")

        self.input_password = super().get_element('#input-password',"css")

        self.newsletter = super().get_element('#input-password',"css")

        self.agree = super().get_element('input[name="agree"]',"css")

        self.continue_button = super().get_element('#form-register > div > button',"css")

    def register(self, first_name, last_name,email,password):
        self.input_first_name.send_keys(first_name)
        self.input_last_name.send_keys(last_name)
        self.input_email.send_keys(email)
        self.input_password.send_keys(password)
        super().click_element(self.agree)
        super().click_element(self.continue_button)
        
        
        