from atf.ui import *
from controls import *


class ContactsRegistry(Region):
    """Реестр 'Контакты'"""

    folders_list = ControlsTreeGridView(By.CSS_SELECTOR, '.controls-Grid', 'Таблица "Папки"')
    messages_list = ControlsListView(By.CSS_SELECTOR, '.Hint-ListWrapper_list', 'Таблица "Сообщения"')
    sent_messages = CustomList(By.CSS_SELECTOR, '.msg-dialogs-item p', 'Конкретные сообщения')
    controls_button = Button(By.CSS_SELECTOR, '[data-qa="controls-itemActions__action null"]',
                                                                                        'Кнопки настройки сообщений')
    menu_options_messages = CustomList(By.CSS_SELECTOR, '.controls-Menu__popup-content)', 'Меню опций сообщений')
    menu_button = CustomList(By.CSS_SELECTOR, '.controls-Menu__content_baseline', 'Кнопка в меню опций сообщений')
    move_in_folder = Button(By.CSS_SELECTOR, '[title="123"].controls-Grid__row-cell__content', 'Перемещение в папку')
    litle_folder = CustomList(By.CSS_SELECTOR, '[title="123"].tag-base', 'Маленькая папка в сообщении')
    count_folder = CustomList(By.CSS_SELECTOR, '[data-qa="msg-folders-counter_total"]', 'Счетчик в папке')
    folder_123 = ControlsListView(By.CSS_SELECTOR, '[title="123"].msg-entity-plain-text', 'Папка "123"')
    folder_all_messages = ControlsListView(By.CSS_SELECTOR, '[title="Все сообщения"].msg-entity-plain-text',
                                                                                                'Папка "Все сообщения')
    delete_litle_folder = Button(By.CSS_SELECTOR, '.tags-base__close', 'Удаление маленькой папки из сообщения')
    message_data_info = CustomList(By.CSS_SELECTOR, '[data-qa="msg-entity-date"]', 'Дата сообщения в разделе "Диалоги')
    tab_chats = Element(By.CSS_SELECTOR, '[title="Чаты"]', 'Раздел "Чаты"')
    tab_dialog = Element(By.CSS_SELECTOR, '[title="Диалоги"]', 'Раздел "Диалоги"')
    message_chats_data_info = CustomList(By.CSS_SELECTOR, '[data-qa="msg-entity-date"]', 'Дата сообщения в разделе "Чаты"')
    tag = CustomList(By.CSS_SELECTOR, '[title="Лисичкин тег"][style="max-width: 170px; min-width: 0px; cursor: pointer;"]',
                                                                                                            'Тег "Лисичкин тег"')
    litle_tag = CustomList(By.CSS_SELECTOR, '[title="Лисичкин тег"][style="max-width: 170px; min-width: 40px; cursor: pointer;"]',
                                                                                            'Маленький тег в сообщении')
    count_tag = CustomList(By.CSS_SELECTOR, '.tags-base__countEntities', 'Счетчик тегов')
    delete_litle_tag = CustomList(By.CSS_SELECTOR, '.tags-base__close', 'Удаление тега из сообщения')

    def check_load(self):
        """Проверка загрузки элементов"""
        self.folders_list.check_load()
        self.messages_list.check_load()
