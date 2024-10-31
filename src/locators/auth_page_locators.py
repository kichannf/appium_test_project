from dataclasses import dataclass


@dataclass
class AuthPageLocators:
    SKIP_BTN = ('id', 'com.habitrpg.android.habitica:id/skipButton')
    LETS_START_BTN = ('id', 'com.habitrpg.android.habitica:id/finishButton')
    OPEN_LOGIN_PAGE_BTN = (
        'id', 'com.habitrpg.android.habitica:id/show_login_button')
    OPEN_REGISTER_PAGE_BTN = (
        'id', 'com.habitrpg.android.habitica:id/new_game_button')
    REGISTER_BTN_IN_REGISTER_FORM = (
        'id', 'com.habitrpg.android.habitica:id/login_btn')
    LOGIN_FIELD_LOCATOR = ('id', 'com.habitrpg.android.habitica:id/username')
    PASSWORD_FIELD_LOCATOR = (
        'id', 'com.habitrpg.android.habitica:id/password')
    DO_LOGIN_BTN = ('id', 'com.habitrpg.android.habitica:id/login_btn')
    USER_NAME_IN_TITLE = (
        'id', 'com.habitrpg.android.habitica:id/toolbar_title')
