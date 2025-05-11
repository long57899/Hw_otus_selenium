import pytest
from selenium import webdriver
from selenium.webdriver.chromium.options import ChromiumOptions
from selenium.webdriver.chromium.service import ChromiumService
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.options import Options as FFOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from dotenv import load_dotenv
import os

load_dotenv(override=True)  

def pytest_addoption(parser):
    parser.addoption("--browser", help="Browser to run tests" , default="ch")
    parser.addoption("--headless", action="store_true", help="Activate headless mode")
    parser.addoption(
        "--drivers", help="Drivers storage", default=f"{os.getenv("DRIVERS")}"
    )
    parser.addoption(
        "--base_url", help="Base application url", default=f"{os.getenv("LOCAL_IP")}:{os.getenv("OPENCART_PORT")}"
    )

@pytest.fixture(scope="session")
def base_url(request):
    return "http://" + request.config.getoption("--base_url")

@pytest.fixture(scope="session")
def browser(request):
    driver = None
    browser_name = request.config.getoption("--browser")
    drivers_storage = request.config.getoption("--drivers")
    headless = request.config.getoption("--headless")

    if browser_name in ["ch", "chrome"]:
        options = ChromeOptions()
        if headless:
            options.add_argument("headless=new")
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )
    elif browser_name in ["ff", "firefox"]:
        options = FFOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
    elif browser_name in ["ya", "yandex"]:
        options = ChromiumOptions()
        options.binary_location = f"{os.getenv("YANDEX_BROWSER")}"
        if headless:
            options.add_argument("headless=new")
        driver = webdriver.Chrome(
            options=options,
            service=ChromiumService(executable_path=f"{drivers_storage}/yandexdriver.exe"),
        )
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    yield driver

    driver.quit()

@pytest.fixture(scope="session")
def load_env():
    load_dotenv()
    return {"login":os.getenv("LOGIN"), "password":os.getenv("PASSWORD")} 

