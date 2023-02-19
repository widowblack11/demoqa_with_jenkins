class CalendarMixin:
    def select_dates_on_the_calendar(self, selector, *, year, month, day):
        self.browser.element(selector).click()
        self.browser.element('.react-datepicker__month-select').click()
        self.browser.element(f'[value="{month}"]').click()
        self.browser.element('.react-datepicker__year-select').click()
        self.browser.element(f'[value="{year}"]').click()
        self.browser.element(f'.react-datepicker__day--0{day}').click()