from controls import *


@templatename('Controls/datePopup')
class Popup(DialogTemplate):

    calendar = ControlsCalendarPeriodDialog()
    calendar.set_absolute_position(True)

    def calendar_table(self, tommorow):
        """
        Выбор даты в календаре
        """
        self.calendar.set_period(date_str=tommorow, apply=True)
