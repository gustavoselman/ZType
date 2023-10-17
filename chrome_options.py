from selenium.webdriver.chrome.options import Options

def get_chrome_options():
    options = Options()
    options.add_argument("--ignore-certificate-errors")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    return options
