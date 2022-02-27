from selenium.webdriver.common.by import By

from .BasePage import BasePage
from .ProductsForm import ProductsForm
from .RegisterForm import RegisterForm


class AdminPage(BasePage):
    ADMIN_LOGIN = (
    By.CSS_SELECTOR, "#content > div > div > div > div > div.panel-body > form > div.text-right > button")
    ADMIN_PASSWORD_FORGET = (
    By.CSS_SELECTOR, "#content > div > div > div > div > div.panel-body > form > div:nth-child(2) > span > a")
    CATALOG_ADMIN = (By.CSS_SELECTOR, "#menu-catalog > a")
    MAIN_PAGE = (By.CSS_SELECTOR, "#footer > a")
    ADMIN_USERNAME = (By.CSS_SELECTOR, "#input-username")
    PRODUCTS_LINK = (By.CSS_SELECTOR, "#collapse1 > li:nth-child(2) > a")
    BUTTON_PLUS = (By.CSS_SELECTOR, "#content > div.page-header > div > div > a")
    CHECKBOX = (
    By.CSS_SELECTOR, "#form-product > div > table > tbody > tr:nth-child(1) > td:nth-child(1) > input[type=checkbox]")
    BUTTON_DELETE = (By.CSS_SELECTOR, "#content > div.page-header > div > div > button.btn.btn-danger")
    WARNING_ALERT = ((By.CSS_SELECTOR, ".alert-danger"))

    def go_to_main_page(self):
        self.browser.get(self.browser.url)

    def click_admin_login(self):
        admin_login = self._element(self.ADMIN_LOGIN)
        admin_login.click()
        return admin_login

    def click_admin_password_forget(self):
        admin_login = self._element(self.ADMIN_PASSWORD_FORGET)
        admin_login.click()
        return admin_login

    def click_catalog_admin(self):
        catalog_admin = self._element(self.CATALOG_ADMIN)
        catalog_admin.click()
        return catalog_admin

    def click_main_page(self):
        main_page = self._element(self.MAIN_PAGE)
        main_page.click()
        return main_page

    def click_admin_username(self):
        admin_username = self._element(self.ADMIN_USERNAME)
        admin_username.click()
        return admin_username

    def click_products_link(self):
        products_link = self._element(self.PRODUCTS_LINK)
        products_link.click()
        return products_link

    def click_button_plus(self):
        button_plus = self._element(self.BUTTON_PLUS)
        button_plus.click()
        return button_plus

    def fill_new_product_form(self, name, description, meta_title, meta_description, meta_keywords, tags):
        ProductsForm(self.browser).create_product(name=name,
                                                  description=description,
                                                  meta_title=meta_title,
                                                  meta_description=meta_description,
                                                  meta_keywords=meta_keywords,
                                                  tags=tags)

    def warning_alert(self):
        alert = self._element(self.WARNING_ALERT)
        return alert

    def check_product(self):
        check = self._element(self.CHECKBOX)
        check.click()
        return check

    def click_delete_button(self):
        delete_button = self._element(self.BUTTON_DELETE)
        delete_button.click()
        return delete_button

    def fill_register_user_form(self, firstname, lastname, email, telephone, password, password2):
        RegisterForm(self.browser).create_user(firstname=firstname,
                                               lastname=lastname,
                                               email=email,
                                               telephone=telephone,
                                               password=password,
                                               password2=password2)
