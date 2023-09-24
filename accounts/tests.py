from django.test import LiveServerTestCase
from django.urls import reverse_lazy
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Create your tests here.

class TestLogin(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        service = Service(executable_path='/Users/hiroto/Downloads/chromedriver')
        cls.selenium = WebDriver(service=service)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()
    
    def test_login(self):
        self.selenium.get('http://localhost:8000' + str(reverse_lazy('account_login')))

        username_input = self.selenium.find_element(By.NAME,'login')
        username_input.send_keys('kage')
        password_input = self.selenium.find_element(By.NAME,'password')
        password_input.send_keys('summerdevelop')
        self.selenium.find_element(By.CLASS_NAME,'btn').click()

        self.assertEqual('Log In | Private Diary', self.selenium.title)