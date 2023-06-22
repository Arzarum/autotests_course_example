# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Задачи на вкладку "В работе"
# Убедиться, что выделена папка "Входящие" и стоит маркер.
# Убедиться, что папка не пустая (в реестре есть задачи)
# Перейти в другую папку, убедиться, что теперь она выделена, а со "Входящие" выделение снято
# Создать новую папку и перейти в неё
# Убедиться, что она пустая
# Удалить новую папку, проверить, что её нет в списке папок
# Для сдачи задания пришлите код и запись с экрана прохождения теста

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

        self.browser.open('https://fix-online.sbis.ru/')

        auth = AuthOnline(self.driver)
        auth.login_inp.type_in('Lisa_alisa'+Keys.ENTER)
        auth.password_inp.type_in('qazwsx123'+Keys.ENTER)

        # Переходим в задачи
        tasks = MainPage(self.driver)
        tasks.accordion.item(with_text='Задачи').click()
        tasks.accordion_subtitle_head.click()

        # Переходим на вкладку "В работе"
        tasks = TaskPage(self.driver)
        tasks.main_tabs.item(with_text='В работе').click()

        # Проверяем, что находимся в папке "Входящие"
        tasks.current_folder.should_be(ContainsText('Входящие'))
        tasks.marker.should_be(Visible)

        # Проверяем, что папка не пуста
        tasks.tasks_list.should_not_be(CountElements(0))

        # Переходим в другую папку
        tasks.folders_list.item(with_text='Другая папка').click()

        # Проверяем, что папка "Входящие" не выделена
        tasks.current_folder.should_be(CountElements(1))

        # Создаем новую папку
        tasks.create_new_button.click()
        tasks.create_new_button_menu.item(with_text='Папка').click()
        sleep(1)
        tasks.create_name_input.send_keys('Папка1')
        tasks.accept_button.click()

        # Проверяем, что папка пустая
        tasks.folders_list.item(with_text='Папка1').click()
        tasks.tasks_list.should_be(CountElements(0))

        # Удаляем созданную папку
        tasks.folders_list.item(with_text='Папка1').context_click()
        tasks.delete_button.click()
        tasks.accept_button.click()
        tasks.folders_list.should_not_be(ContainsText('Папка1'))
