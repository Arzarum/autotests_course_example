from atf import *
from atf.ui import *
from controls import *
from passage import Panel
from popupTemplate import Popup
from selection import Stack


@templatename('WorkTimeDocuments/timeoff:Dialog')
class Dialog(DocumentTemplate):

    worker_search = ControlsLookupInput(SabyBy.DATA_QA, 'staff-Lookup__input', 'Сотрудник')
    worker_suggest = Element(By.CSS_SELECTOR, '.person-Information__fio', 'Сотрудник из автодополнения')
    data_filter = Element(By.CSS_SELECTOR, '.wtd-dayTimeSelector--hover-cursor-pointer', 'Фильтр по дате')
    confirm_calendar = ControlsCalendarPeriodDialog(By.CSS_SELECTOR, '.icon-Yes', 'Сохранить')
    type_holiday = ControlsDropdownSelector(By.CSS_SELECTOR, '.wtd-TimeOff__type-text', 'Тип отгула')
    holiday_with_pay = ControlsPopup(By.CSS_SELECTOR, '[title="с оплатой"] .ws-ellipsis', 'С оплатой')
    possible_reason = Element(By.CSS_SELECTOR, '.mce-content-body', 'Возможная причина')
    phase = Button(By.CSS_SELECTOR, '.edo3-PassageButton__button', 'На выполнение')
    delete_button = Element(By.CSS_SELECTOR, '.i.icon-Erase', 'Удалить')
    confirm = Button(By.CSS_SELECTOR, '[data-qa="controls-ConfirmationDialog__button-true"]', 'Да')
    cause_in_card = RichEditorExtendedEditor(By.CSS_SELECTOR, '[data-qa="wtd-Base__comment"]', 'Причина в карточке')
    data_in_card = ControlsLookupInput(By.CSS_SELECTOR, '.wtd-dayTimeSelector--hover-cursor-pointer', 'Дата в карточке')
    type_in_card = Element(By.CSS_SELECTOR, '.wtd-TimeOff__type-text', 'Тип отгула в карточке')
    worker_in_card = ControlsDropdownSelector(By.CSS_SELECTOR, '[data-qa="SelectedCollection__item__caption"]', 'Сотрудник в карточке')
    time = Button(By.CSS_SELECTOR, '.icon-TimeSkinny', 'Время')
    start_time = ControlsInputMask(By.CSS_SELECTOR, '[data-qa="wtd-TimeIntervalMinutes__start"] input', 'Время с')
    end_time = ControlsInputMask(By.CSS_SELECTOR, '[data-qa="wtd-TimeIntervalMinutes__end"] input', 'Время по')
    save_button = Button(By.CSS_SELECTOR, '[title="Сохранить"] .controls-text-unaccented', 'Сохранить')
    close_autodop = Button(By.CSS_SELECTOR, '.controls-CloseButton__close__icon_external', 'Закрыть')

    def fill_work_card(self, **kwargs):
        """Заполнить сотрудника в карточке через автодополнение"""

        self.check_open()
        if 'Сотрудник' in kwargs.keys():
            self.worker_search.autocomplete_search(kwargs['Сотрудник'])

    def fill_work_card_for_panel(self):
        """Заполнить сотрудника в карточке через справочную панель"""
        self.stack = Stack(self.driver)

        self.worker_search.open_data_dictionary()
        delay(1)
        self.stack.choice_worker()

    def fill_cause(self):
        """Заполнить возможную причину"""

        delay(1)
        self.possible_reason.type_in('Тестовая причина')

    def open_calendar(self):
        """Открыть календарь"""

        self.data_filter.click()

    def fill_calendar(self, tommorow):
        """Заполнить календарь"""
        self.popup = Popup(self.driver)

        self.popup.calendar_table(tommorow)

    def fill_type_holiday(self):
        """Заполнить тип отгула"""

        self.type_holiday.click()
        self.holiday_with_pay.click()

    def run_holiday(self):
        """Отправить на выполнение"""
        self.phase.click()

    def fill_agreement(self, **kwargs):
        """Заполнить согласование"""
        panel = Panel(self.driver)

        panel.agreement(**kwargs)

    def opisanie_card(self):
        """Заполнить описание отдельно и сохранить"""

        self.possible_reason.type_in('Тестовая причина')
        self.save_button.click()

    def time_and_date(self, start_time, end_time):
        """Выставить время на завтра с 12:00 до 14:00"""

        self.time.click()
        self.start_time.send_keys(start_time)
        self.end_time.send_keys(end_time)

    def check_visible_info(self):
        """
        Проверить информацию в карточке
        """

        self.cause_in_card.should_be(Displayed)
        self.data_in_card.should_be(Displayed)
        self.type_in_card.should_be(Displayed)
        self.worker_in_card.should_be(Displayed)









