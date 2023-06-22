from pages.workSchedules_page import *
from pages.auth_page import AuthPage
from datetime import datetime, timedelta
from pages.timeoff import Dialog
from pages.passage import Panel


class TestShedulesList(TestCaseUI):
    today = datetime.now()
    tommorow = today + timedelta(days=1)
    tommorow_txt = tommorow.strftime("%d.%m.%y")

    @classmethod
    def setUpClass(cls):
        """
        Авторизация на стенде fix-online
        """
        AuthPage(cls.driver).auth(cls.config.get('LOGIN'), cls.config.get('PASSWORD'), cls.config.get('WORK_SCHEDULES_PAGE'))
        cls.page = WorkSchedulesRegistry(cls.driver)
        cls.page.check_load()

    def setUp(self):
        self.browser.open(self.config.get('WORK_SCHEDULES_PAGE'))
        self.page.check_load()

    def test_01(self):
        """Создание отгула с оплатой"""
        self.dialog = Dialog(self.driver)
        self.panel = Panel(self.driver)

        log('Создать новую карточку отгула')
        self.page.open_card()

        log('Заполнить карточку')
        work_data = {'Сотрудник': 'Коржов Коржик'}
        self.dialog.fill_work_card(**work_data)

        self.dialog.fill_cause()
        self.dialog.open_calendar()
        self.dialog.fill_calendar(self.tommorow_txt)
        self.dialog.fill_type_holiday()

        log('Запустить отгул на выполнение')
        self.dialog.run_holiday()

        log('Согласовать отгул')
        agreement_work_data = {'Сотрудник': 'Коржов Коржик'}
        self.dialog.fill_agreement(**agreement_work_data)

        self.panel.run_agreement()

        log('Проверить карточку в реестре')
        self.page.check_card()

        log('Проверить сохранение содержимого в карточке')
        self.page.card_in_regitstry.click()
        self.dialog.check_visible_info()

        log('Удалить отгул')
        self.browser.refresh()
        self.page.delete_card()

    def test_02(self):
        """Создание отгула с выбором сотрудника через справочник"""
        self.dialog = Dialog(self.driver)

        log('Создать новую карточку отгула')
        self.page.open_card()

        log('Выбрать сотрудника через справочник')
        self.dialog.fill_work_card_for_panel()

        log('Выставить время на завтра')
        self.dialog.open_calendar()
        self.dialog.fill_calendar(self.tommorow_txt)

        log('Выставить время на завтра с 12:00 до 14:00')
        self.dialog.time_and_date('1200', '1400')

        log('Заполнить описание и сохранить')
        self.dialog.opisanie_card()

        log('Проверить карточку')
        self.page.check_card()

        log('Удалить отгул')
        self.browser.refresh()
        self.page.delete_card()



