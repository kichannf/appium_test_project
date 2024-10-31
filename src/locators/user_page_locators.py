from dataclasses import dataclass


@dataclass
class UserPageLocators:
    OPEN_CREATE_HABIT_BTN = (
        'id', 'com.habitrpg.android.habitica:id/add_button')
    CREATE_HABIT_FORM_TITLE = (
        'xpath', '//android.widget.TextView[@text="Create Habit"]')
    TASK_TITLE_FIELD = (
        'id', 'com.habitrpg.android.habitica:id/text_edit_text')
    NOTES_FIELD = ('id', 'com.habitrpg.android.habitica:id/notes_edit_text')
    SAVE_HABIT_BTN = (
        'id', 'com.habitrpg.android.habitica:id/action_save')
    OPEN_FIRST_HABIT = (
        'xpath',
        '(//android.widget.LinearLayout[@resource-id='
        '"com.habitrpg.android.habitica:id/main_task_wrapper"])[1]')
    DEL_HABIT_BTN = ('id', 'com.habitrpg.android.habitica:id/action_delete')
    CONFIRM_DEL_HABIT_BTN = (
        'xpath', '//android.widget.Button[@text="Delete Task"]')
