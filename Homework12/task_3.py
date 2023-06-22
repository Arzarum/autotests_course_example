from atf.ui import *
from selenium.webdriver.common.by import By
from time import sleep

#  driver = webdriver.Chrome()


class MainPage(Region):
    accordion = CustomList(By.CSS_SELECTOR, "span.NavigationPanels-Accordion__title")
    accordion_subtitle_head = Link(By.CSS_SELECTOR, ".NavigationPanels-SubMenu__headTitle")


class AuthOnline(Region):
    login_inp = TextField(By.CSS_SELECTOR, "[name='Login']", 'Логин')
    password_inp = TextField(By.CSS_SELECTOR, "[name='Password']", 'Пароль')


class TaskPage(Region):
    create_new_button = Button(By.CSS_SELECTOR, '.icon-RoundPlus', 'Создать')
    accept_button = Button(By.CSS_SELECTOR, ".controls-Popup .controls-BaseButton", 'Принять')
    send_button = Button(By.CSS_SELECTOR, ".icon-BtArrow", 'Отправить')
    delete_button = Button(By.CSS_SELECTOR, ".controls-icon_style-danger", 'Удалить')

    create_new_button_menu = CustomList(By.CSS_SELECTOR, ".controls-Menu__row", 'Меню "Создать"')
    sent_messages = CustomList(By.CSS_SELECTOR, '.msg-dialogs-item p', 'Сообщения в реестре')
    main_tabs = CustomList(By.CSS_SELECTOR, ".sabyPage-MainLayout__tabs-item", 'Вкладки')
    folders_list = CustomList(By.CSS_SELECTOR, ".controls-ListEditor__columns", 'Папки')
    current_folder = CustomList(By.CSS_SELECTOR, ".controls-Grid__row-cell_selected__first-master", 'Текущая папка')
    tasks_list = CustomList(By.CSS_SELECTOR, ".edws-MainColumn", 'Задачи')
    tasks_info = CustomList(By.CSS_SELECTOR, ".controls-EditableArea__Text__inner", 'Дата и номер')

    create_name_input = TextField(By.CSS_SELECTOR, ".controls-Popup .controls-InputBase__field", 'Название')
    top_area_search = TextField(By.CSS_SELECTOR, ".controls-StackTemplate__top-area-content "
                                                 ".controls-Search__nativeField_caretEmpty", 'Поиск')
    sending_message_textbox = TextField(By.CSS_SELECTOR, "[role='textbox']", 'Сообщение')

    top_area_search_result = Element(By.CSS_SELECTOR, ".person-BaseInfo__line span[data-qa='person-Information__fio']",
                                     'Результат')
    marker = Element(By.CSS_SELECTOR, ".controls-Grid__row-cell_selected__first-master>"
                                      ".controls-ListView__itemV_marker", 'Маркер')
    task_executor = Element(By.CSS_SELECTOR, ".edws-StaffChooser__itemTpl-name", 'Исполнитель')
    task_author = Element(By.CSS_SELECTOR, ".edo3-Sticker__active", 'Автор')
    task_description = Element(By.CSS_SELECTOR, ".richEditor_Base_textContainer p", 'Описание')

    current_tab = Link(By.CSS_SELECTOR, ".controls-Tabs__item_view_selected", 'Текущая вкладка')


class Test(TestCaseUI):

    def test(self):

        self.browser.open('https://fix-online.sbis.ru/doc/a31c6b62-1dd8-45fc-91f1-b6a6a5985340?client=6001777')

        auth = AuthOnline(self.driver)
        auth.login_inp.type_in('Lisa_alisa' + Keys.ENTER)
        auth.password_inp.type_in('qazwsx123' + Keys.ENTER)

        # Проверяем, что заголовок соответствует эталону
        task = TaskPage(self.driver)
        self.browser.should_be(TitleExact('Задача №2 от 16.06.23'))

        # Проверяем исполнителя, дату, номер, описание и автора
        task.task_executor.should_be(ExactText('Лисичкина А.А.'))
        task.tasks_info.item(1).should_be(ExactText('16 июн, пт'))
        task.tasks_info.item(2).should_be(ExactText('2'))
        task.task_description.should_be(ExactText('Задача'))
        task.task_author.should_be(ExactText('Лисичкина А.А.'))
