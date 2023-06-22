from controls import *
from atf.ui import *
from atf import *


@templatename('Staff/selection:Stack')
class Stack(CatalogTemplate):

    search = ControlsSearchInput(By.CSS_SELECTOR, '[data-qa="controls-Render__field"]', 'Поиск')
    worker = Element(By.CSS_SELECTOR, '[title="Тестировщик"]', 'Сотрудник')

    def choice_worker(self):
        """Выбор сотрудника через справочную панель"""

        self.search.type_in('Коржов Коржик')
        delay(1)
        self.worker.click()

