from selene.support.conditions import have


class RadioMixin:
    def select_radio(self, selector, value):
        self.browser.all(selector).element_by(have.value(value)).element('..').click()