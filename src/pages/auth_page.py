import os

import allure

from src.locators.auth_page_locators import AuthPageLocators
from src.pages.base_page import BasePage


class AuthPage(BasePage):
    """ Класс от старта до авторизации."""
    @allure.step('Ввод логина: {login}')
    def set_login(self, login):
        self.el_until_clickable(
            AuthPageLocators.LOGIN_FIELD_LOCATOR, 3).send_keys(login)

    @allure.step('Ввод пароля: {password}')
    def set_password(self, password):
        self.el_until_clickable(
            AuthPageLocators.PASSWORD_FIELD_LOCATOR, 3).send_keys(password)

    @allure.step('Залогиниться с введенными данными')
    def confirm_login(self):
        self.el_until_clickable(AuthPageLocators.DO_LOGIN_BTN, 2).click()

    @allure.step(f'Авторизация с логином: "{os.getenv('LOGIN')}"')
    def login(self):
        self.set_login(os.getenv('LOGIN'))
        self.set_password(os.getenv('PASSWORD'))
        self.confirm_login()
        return self

    @allure.step('Нажать кнопку "Skip" для пропуска онбоардинга.')
    def skip_onboarding_by_skip_btn(self):
        self.el_until_clickable(AuthPageLocators.SKIP_BTN, 2).click()
        return self

    @allure.step(
        'Пролистнуть две начальные страницы онбоардинга и нажать '
        '"Let\'s start" для пропуска онбоардинга.')
    def skip_onboarding_by_swipe_and_lets_start_btn(self):
        self.swipe_left()
        self.swipe_left()
        with allure.step('Нажать кнопку Lets start'):
            self.el_until_clickable(
                AuthPageLocators.LETS_START_BTN, 2).click()
        return self

    @allure.step('Нажать на кнопку "Register" для открытие формы регистрации.')
    def open_register_form(self):
        self.click(AuthPageLocators.OPEN_REGISTER_PAGE_BTN, 2)
        return self

    @allure.step('Нажать на кнопку "Login" для открытие формы авторизации.')
    def open_login_form(self):
        self.click(AuthPageLocators.OPEN_LOGIN_PAGE_BTN, 3)
        return self

    @allure.step(
        'Онбординг пропущен. '
        'Открыта страница выбора перехода к логину либо к регистрации')
    def check_start_page_is_open(self):
        assert all((
            self.check_element_displayed(
                AuthPageLocators.OPEN_LOGIN_PAGE_BTN, 4),
            self.check_element_displayed(
                AuthPageLocators.OPEN_REGISTER_PAGE_BTN, 4
            )))

    @allure.step('Форма регистрации открыта.')
    def check_register_form_is_open(self):
        assert self.check_element_displayed(
            AuthPageLocators.REGISTER_BTN_IN_REGISTER_FORM, 2)

    @allure.step('Форма авторизации открыта.')
    def check_login_form_is_open(self):
        assert all((
            self.check_element_displayed(
                AuthPageLocators.LOGIN_FIELD_LOCATOR, 4),
            self.check_element_displayed(
                AuthPageLocators.PASSWORD_FIELD_LOCATOR, 4
            )))

    @allure.step(f'Логин выполнен пользователем: {os.getenv('LOGIN')}')
    def check_login(self):
        assert os.getenv('LOGIN') == self.get_username_in_title()

    @allure.step('Получить login пользователя')
    def get_username_in_title(self):
        return self.get_element_s_text(AuthPageLocators.USER_NAME_IN_TITLE, 5)
