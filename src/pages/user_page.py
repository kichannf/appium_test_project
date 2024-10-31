import allure

from src.data.data import HABIT
from src.locators.user_page_locators import UserPageLocators
from src.pages.base_page import BasePage


class UserPage(BasePage):
    TITLE = HABIT.get('title')
    NOTES = HABIT.get('notes')
    TITLE_EDIT = HABIT.get('title')
    NOTES_EDIT = HABIT.get('notes')

    @allure.step('Открыть форму создания привычки')
    def open_create_habit_form(self):
        self.click(UserPageLocators.OPEN_CREATE_HABIT_BTN, 4)
        return self

    @allure.step('Открыть первую привычку')
    def open_first_habit(self):
        self.click(UserPageLocators.OPEN_FIRST_HABIT, 4)
        return self

    @allure.step('Нажать удалить привычку в карточке привычки')
    def click_del_habit(self):
        self.click(UserPageLocators.DEL_HABIT_BTN, 4)
        return self

    @allure.step('Подтвердит удаление привычки')
    def confirm_del_habit(self):
        self.click(UserPageLocators.CONFIRM_DEL_HABIT_BTN, 3)
        return self

    @allure.step('Удалить привычку в карточке привычки')
    def del_habit(self):
        self.click_del_habit()
        self.confirm_del_habit()
        return self

    @allure.step('Заполнить Title привычки значением: {title}')
    def fill_habit_title(self, title):
        self.fill_field(UserPageLocators.TASK_TITLE_FIELD, title, 2)
        return self

    @allure.step('Заполнить Notes привычки значением: {notes}')
    def fill_habit_notes(self, notes):
        self.fill_field(UserPageLocators.NOTES_FIELD, notes, 2)
        return self

    @allure.step('Нажать "сохранить привычку"')
    def click_save_habit(self):
        self.click(UserPageLocators.SAVE_HABIT_BTN, 2)
        return self

    @allure.step(f'Создать привычку: Title={TITLE}, NOTES={NOTES}')
    def create_habit_with_title_and_notes(self):
        self.fill_habit_title(self.TITLE)
        self.fill_habit_notes(self.NOTES)
        self.click_save_habit()
        return self

    @allure.step(f'Изменить привычку: Title={TITLE_EDIT}, NOTES={NOTES_EDIT}')
    def edit_habit_with_title_and_notes(self):
        self.fill_habit_title(self.TITLE_EDIT)
        self.fill_habit_notes(self.NOTES_EDIT)
        self.click_save_habit()
        return self

    @allure.step('Форма создания привычки открыта')
    def check_create_habit_form_is_open(self):
        assert self.check_element_displayed(
            UserPageLocators.CREATE_HABIT_FORM_TITLE, 3)
