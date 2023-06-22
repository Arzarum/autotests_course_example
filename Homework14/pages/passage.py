from controls import *


@templatename('EDO3/passage:Panel')
class Panel(DialogTemplate):

    confirm_holiday = Button(By.CSS_SELECTOR, '[title="Согласовать отгул"] .controls-BaseButton__text', 'Согласовать отгул')
    worker_list = CustomList(By.CSS_SELECTOR, '[data-qa="person-Information__fio"]', 'Выбор сотрудника')
    worker_search_agreement = ControlsLookupInput(SabyBy.DATA_QA, 'controls-Render__field', 'Сотрудник')

    def agreement(self, **kwargs):
        """Заполнить согласование"""

        self.check_open()
        if 'Сотрудник' in kwargs.keys():
            self.worker_search_agreement.autocomplete_search(kwargs['Сотрудник'])

    def run_agreement(self):
        """Запустить согласование"""

        self.confirm_holiday.click()