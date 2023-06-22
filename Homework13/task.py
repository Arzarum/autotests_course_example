# Переместить запись в другую папку и проверить перемещение (убедиться в: наличии в папке и увеличении счётчика).
# И вернуть обратно.
# Проверить, что дата сообщения в реестре Диалоги совпадает с датой в Чатах
# Пометить сообщение эталонным тегом. Убедиться, что тег появился на сообщении, а счётчик тегов увеличился.
# Снять тег и проверить.

from atf import *
from pages.contacts_page import *
from pages.auth_page import *


class TestContactsList(TestCaseUI):

    @classmethod
    def setUpClass(cls):
        AuthPage(cls.driver).auth(cls.config.get('LOGIN'), cls.config.get('PASSWORD'), cls.config.get('CONTACTS_PAGE'))
        cls.page = ContactsRegistry(cls.driver)
        cls.page.check_load()

    def setUp(self):
        self.browser.open(self.config.get('CONTACTS_PAGE'))
        self.page.check_load()

    def test_move_record(self):
        log('Переместить сообщение в другую папку')
        self.page.sent_messages.mouse_over()
        self.page.controls_button.click()
        self.page.menu_button.item(with_text='Переместить').click()
        self.page.move_in_folder.click()

        log('Убедиться, что сообщение находится в другой папке, а также изменился счетчик')
        self.page.litle_folder.should_be(ExactText('123'))
        self.page.count_folder.should_be(ExactText('1'))
        self.page.folder_123.click()
        self.page.sent_messages.should_be(ExactText('Привет'))

        log('Удалить сообщение из папки')
        self.page.folder_all_messages.click()
        delay(3)
        self.page.delete_litle_folder.click()

    def test_comparison(self):
        log('Проверить на совпадение даты в "Диалоги" и в "Чаты')
        delay(5)
        self.page.message_data_info.item(contains_text='20 июн 16:21').should_be(Displayed)
        self.page.tab_chats.click()
        self.page.message_chats_data_info.item(contains_text='20 июн 16:21').should_be(Displayed)
        self.page.tab_dialog.click()

    def test_tagging(self):
        log('Создаем пометку тегом для сообщения')
        delay(5)
        self.page.folder_all_messages.click()
        self.page.sent_messages.mouse_over()
        self.page.controls_button.click()
        self.page.menu_button.item(with_text='Пометить').click()
        self.page.tag.click()

        log('Проверить отметку тегом и увеличение счетчика тега')
        self.page.litle_tag.should_be(ExactText('Лисичкин тег'))
        self.page.count_tag.should_be(ExactText('1'))

        log('Удалить тег и проверить, что он удалился')
        self.page.delete_litle_tag.click()
        self.page.litle_tag.should_not_be(Visible)

    def tearDown(self):
        self.browser.close_windows_and_alert()
