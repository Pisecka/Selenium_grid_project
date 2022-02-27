from selenium.webdriver.common.by import By

from .BasePage import BasePage


class MainPage(BasePage):
    SLIDESHOW = (By.ID, "slideshow0")
    BUTTON_SEARCH = (By.CSS_SELECTOR, "#search > span > button")
    BUTTON_CART = (By.CSS_SELECTOR, "#cart > button")
    SITE_MAP = (By.CSS_SELECTOR, "body > footer > div > div > div:nth-child(2) > ul > li:nth-child(3) > a")
    CURRENCY = (By.CSS_SELECTOR, "#form-currency > div > button")
    BUTTON_DOLLAR = (By.CSS_SELECTOR, "#form-currency > div > ul > li:nth-child(3) > button")

    def click_slideshow(self):
        slideshow = self._element(self.SLIDESHOW)
        slideshow.click()
        return slideshow

    def click_button_search(self):
        button_search = self._element(self.BUTTON_SEARCH)
        button_search.click()
        return button_search

    def click_button_cart(self):
        button_cart = self._element(self.BUTTON_CART)
        button_cart.click()
        return button_cart

    def click_site_map(self):
        site_map = self._element(self.SITE_MAP)
        site_map.click()
        return site_map

    def click_currency(self):
        currency = self._element(self.CURRENCY)
        currency.click()
        return currency

    def go_to_catalog_page(self):
        catalog_url = "index.php?route=product/category&path=20"
        self.browser.get(self.browser.url + catalog_url)

    def go_to_product_page(self):
        product_url = "index.php?route=product/product&product_id=43"
        self.browser.get(self.browser.url + product_url)

    def go_to_register_page(self):
        register_url = "index.php?route=account/register"
        self.browser.get(self.browser.url + register_url)

    def go_to_admin_page(self):
        admin_page = "admin"
        self.browser.get(self.browser.url + admin_page)

    def click_button_dollar(self):
        button_dollar = self._element(self.BUTTON_DOLLAR)
        button_dollar.click()
        return button_dollar
