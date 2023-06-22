from atf.ui import *
from atf import *
from controls import *
from timeoff import Dialog
from popupTemplate import Popup


class WorkSchedulesRegistry(Region):
    """Реестр 'Графики работ'"""

    content_table = HintTemplateEmptyView(By.CSS_SELECTOR, '.hint-EmptyView', 'Таблица контента')
    button_plus = ExtControlsDropdownAddButton(By.CSS_SELECTOR, '.icon-RoundPlus', 'Кнопка создания')
    menu_button_plus = CustomList(By.CSS_SELECTOR, '.controls-margin_bottom-3xs .ws-flex-row div', 'Меню кнопки плюс')
    holiday_list_cs = ControlsScroll(By.CSS_SELECTOR, '.wtd-List__mainInfo-wrap-content-type', 'Запись в таблице отгулов')
    card_in_regitstry = ControlsScroll(By.CSS_SELECTOR, '.wtd-List__mainInfo-wrap-content-type', 'Карточка в реестре')
    delete_button = ControlsScroll(By.CSS_SELECTOR, 'i.icon-Erase', 'Удалить запись')
    confirm_delete = Button(By.CSS_SELECTOR, '[data-qa="controls-ConfirmationDialog__button-true"]', 'Да')

    def check_load(self):
        """Проверка загрузки элементов"""
        self.content_table.check_load()

    def open_card(self):
        """
        Создать новую карточку отгула
        """

        self.button_plus.click()
        self.menu_button_plus.item(contains_text='Отгул').click()
        delay(2)

    def work_in_card(self, date):
        """
        Заполнить карточку
        """
        self.popup = Popup(self.driver)
        self.dialog = Dialog(self.driver)
        work_data = {'Сотрудник': 'Коржов Коржик'}

        self.dialog.fill_work_card(**work_data)
        self.dialog.fill_cause()
        self.dialog.open_calendar()
        self.dialog.fill_calendar(date)
        self.dialog.fill_type_holiday()

    def check_card(self):
        """Проверить наличие карточки в реестре"""
        self.card_in_regitstry.should_be(Displayed)
        delay(1)

    def delete_card(self):
        """Удалить карточку из реестра"""

        self.card_in_regitstry.mouse_over()
        self.delete_button.click()
        self.confirm_delete.click()


