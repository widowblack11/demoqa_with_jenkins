from selene import be, have
# from selene.support.shared import browser

from demoqa_tests.model.controls.chekboxes import CheckboxMixin
from demoqa_tests.model.controls.select_dates_on_the_calendar import CalendarMixin
from demoqa_tests.model.controls.dropdown import DropdownMixin
from demoqa_tests.model.controls.radio_button import RadioMixin

# Открытие формы регистрации
from demoqa_tests.utils.resource import path_file


class FormPage(RadioMixin, CalendarMixin, CheckboxMixin, DropdownMixin):
    def __init__(self, browser):
        self.browser = browser
        
    def open_page_practice_form(self):
        self.browser.open(f'/automation-practice-form')

    # Заполнение формы регистрации
    def data_fill(self, firstName, lastName, userEmail, gender, Number,  file, year, month,
                  day, Subjects, Hobbies, State, City, Address ):
        self.browser.element('[id="firstName"]').should(be.blank).type(firstName)
        self.browser.element('[id="lastName"]').should(be.blank).type(lastName)
        self.browser.element('[id="userEmail"]').should(be.blank).type(userEmail)
    
        self.select_radio('[name=gender]', gender)
        self.browser.element('[id="userNumber"]').should(be.blank).type(Number)
    
        self.browser.element('#uploadPicture').set_value(path_file(file))
    
        self.select_dates_on_the_calendar('#dateOfBirthInput', year=year, month=month, day=day)
    
        self.browser.element('#subjectsInput').type(Subjects).press_enter()
    
        self.select_checkbox('.custom-checkbox', Hobbies)
    
        self.dropdown_react('3', State)
        self.dropdown_react('4', City)
        self.browser.element('#currentAddress').type(Address)

    # Отправка формы регистрации
    def send_form(self):
        self.browser.element('#submit').press_enter()

    def check_get_form(self, firstName, lastName, userEmail, gender, Number,  file, date, Subjects, Hobbies, State, City, Address):
        self.browser.all('.table-responsive').all('tr').element(2).should(have.text(userEmail))
        self.browser.all('.table-responsive').all('tr').element(3).should(have.text(gender))
        self.browser.all('.table-responsive').all('tr').element(4).should(have.text(Number))
        self.browser.all('.table-responsive').all('tr').element(5).should(have.text(date))
        self.browser.all('.table-responsive').all('tr').element(6).should(have.text(Subjects))
        self.browser.all('.table-responsive').all('tr').element(7).should(have.text(Hobbies))
        self.browser.all('.table-responsive').all('tr').element(8).should(have.text(file))
        self.browser.all('.table-responsive').all('tr').element(9).should(have.text(Address))

    def close_form(self):
        self.browser.element('#closeLargeModal').press_enter()

