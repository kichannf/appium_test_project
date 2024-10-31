import allure


class TestHabit:
    @allure.feature('Habitica')
    @allure.story('Привычка')
    @allure.title('Открыть форму создания привычки')
    def test_open_create_form_habit(self, user_page):
        user_page.open_create_habit_form()
        user_page.check_create_habit_form_is_open()

    @allure.feature('Habitica')
    @allure.story('Привычка')
    @allure.title('Создать привычку с Title и Notes')
    def test_create_habit_with_title_and_notes(self, user_page):
        user_page \
            .open_create_habit_form() \
            .create_habit_with_title_and_notes()

    @allure.feature('Habitica')
    @allure.story('Привычка')
    @allure.title('Открыть созданную привычку')
    def test_open_created_habit(self, user_page):
        user_page.open_first_habit()

    @allure.feature('Habitica')
    @allure.story('Привычка')
    @allure.title('Удалить привычку')
    def test_del_habit(self, user_page):
        user_page \
            .open_create_habit_form() \
            .create_habit_with_title_and_notes() \
            .open_first_habit() \
            .del_habit()

    @allure.feature('Habitica')
    @allure.story('Привычка')
    @allure.title('Обновить созданную привычку (Title и Notes)')
    def test_update_created_habit_title_and_notes(self, user_page):
        user_page \
            .open_create_habit_form() \
            .edit_habit_with_title_and_notes()
