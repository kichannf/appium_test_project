import allure


class TestStartPage:
    @allure.feature('Habitica')
    @allure.story('Стартовая страница')
    @allure.title('Пропустить онбоардинг кнопкой "Skip"')
    def test_click_skip_onboarding(self, start_page):
        start_page.click_ok_for_browser_stack()
        start_page.skip_onboarding_by_skip_btn()
        start_page.check_start_page_is_open()

    @allure.feature('Habitica')
    @allure.story('Стартовая страница')
    @allure.title('Пропустить онбоардинг 2 свайпами и нажатием "Let\'s start"')
    def test_swipe_and_click_start_onboarding(self, start_page):
        start_page.skip_onboarding_by_skip_btn()
        start_page.check_start_page_is_open()

    @allure.feature('Habitica')
    @allure.story('Стартовая страница')
    @allure.title('Открыть страницу регистрации')
    def test_open_register_page(self, start_page):
        start_page \
            .skip_onboarding_by_skip_btn() \
            .open_register_form() \
            .check_register_form_is_open()

    @allure.feature('Habitica')
    @allure.story('Стартовая страница')
    @allure.title('Открыть страницу авторизации')
    def test_open_login_page(self, start_page):
        start_page \
            .skip_onboarding_by_skip_btn() \
            .open_login_form() \
            .check_login_form_is_open()

    @allure.feature('Habitica')
    @allure.story('Авторизация')
    @allure.title('Выполнить логин')
    def test_login(self, start_page):
        start_page \
            .skip_onboarding_by_skip_btn() \
            .open_login_form() \
            .login() \
            .check_login()
