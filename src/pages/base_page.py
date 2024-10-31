from time import sleep

import allure
from appium.webdriver import Remote
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """ Общие методы страниц."""
    def __init__(self, driver: Remote):
        self.driver = driver
        self.window_size = driver.get_window_size()
        self.width = self.window_size['width']
        self.height = self.window_size['height']

    def take_exception_screenshot(self):
        """ Делает скриншот и прикрепляет в allure отчет."""
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name='exception_screenshot',
            attachment_type=allure.attachment_type.PNG)

    def wait(self, timeout=1):
        """ Метод таймаута ожидания"""
        return WebDriverWait(self.driver, timeout=timeout)

    def el_until_clickable(self, locator, timeout=2):
        """ Возвращает элемент + ожидание, что элемент clickable."""
        return self.wait(timeout).until(EC.element_to_be_clickable(locator))

    def el_until_visibility(self, locator, timeout=2):
        """ Возвращает элемент + ожидание, что элемент виден."""
        return self.wait(timeout).until(
            EC.visibility_of_element_located(locator))

    def fill_field(self, locator, value, timeout=2):
        """
        Заполнить поле значением.
        :locator - элемент, в который заполнять
        :value - значение, которым заполнить элемент
        :timeout - timeout ожидания элемента
        """
        self.el_until_clickable(locator, timeout).send_keys(value)

    def click(self, locator, timeout=2):
        """
        :locator - искомый элемент
        :timeout - timeout ожидания элемента
        """
        self.el_until_clickable(locator, timeout).click()

    def check_element_displayed(self, locator, timeout=2):
        """ Отображается ли элемент на странице. Return: True or False"""
        return self.el_until_visibility(locator, timeout).is_displayed()

    def get_element_s_text(self, locator, timeout=2):
        """ Возвращает текст элемента"""
        return self.el_until_visibility(
            locator, timeout).get_attribute('text')

    @allure.step('Свайп вправо')
    def swipe_right(self):
        width1 = self.width * 0.1
        height1 = self.height * 0.5
        width2 = self.width * 0.9
        t = 1000
        n = 2  # n indicates the number of swipes
        sleep(1)
        for i in range(n):
            self.driver.swipe(width1, height1, width2, height1, t)

    @allure.step('Свайп влево')
    def swipe_left(self):
        width1 = self.width * 0.9
        height1 = self.height * 0.5
        width2 = self.width * 0.1
        t = 1000
        n = 1  # n indicates the number of swipes
        sleep(1)
        for i in range(n):
            self.driver.swipe(width1, height1, width2, height1, t)
