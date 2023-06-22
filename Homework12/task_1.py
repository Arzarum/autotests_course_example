# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
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
    top_area_search = TextField(By.CSS_SELECTOR, ".controls-StackTemplate__top-area-content "
                                                 ".controls-Search__nativeField_caretEmpty", 'Поиск')
    top_area_search_result = Element(By.CSS_SELECTOR, ".person-BaseInfo__line span[data-qa='person-Information__fio']",
                                     'Результат')
    sending_message_textbox = TextField(By.CSS_SELECTOR, "[role='textbox']", 'Сообщение')
    sent_messages = CustomList(By.CSS_SELECTOR, '.msg-dialogs-item p', 'Сообщения в реестре')


class Test(TestCaseUI):

    def test(self):
        self.browser.open('https://fix-online.sbis.ru/')

        auth = AuthOnline(self.driver)
        auth.login_inp.type_in('Lisa_alisa'+Keys.ENTER)
        auth.password_inp.type_in('qazwsx123'+Keys.ENTER)

        # Переходим в раздел Контакты
        contacts = MainPage(self.driver)
        contacts.accordion.item(with_text='Контакты').click()
        contacts.accordion_subtitle_head.click()

        # Отправляем сообщение
        sending_msg = TaskPage(self.driver)
        self.browser.should_be(UrlExact('https://fix-online.sbis.ru/page/dialogs'))
        sleep(3)
        sending_msg.create_new_button.click()
        sending_msg.top_area_search.type_in("Лисичкина Алиса")
        sending_msg.top_area_search_result.should_be(ContainsText("Лисичкина Алиса"))
        sending_msg.top_area_search_result.click()
        sending_msg.sending_message_textbox.send_keys('Привет')
        sending_msg.send_button.click()

        # Проверяем, что сообщение отправлено и присутствует в реестре
        sending_msg.sent_messages.item(1).should_be(ExactText('Привет'))

        # Удаляем сообщение
        sending_msg.sent_messages.item(with_text='Привет').mouse_over()
        sending_msg.delete_button.click()

        # Проверяем, что сообщение удалено и не отображается в реестре
        sending_msg.sent_messages.item(1).should_not_be(ExactText('Привет'))
