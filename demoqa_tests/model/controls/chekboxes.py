from selene import have


class CheckboxMixin:
    def select_checkbox(self, selector, value):
        self.browser.all(selector).element_by(have.exact_text(value)).click()