import allure

from demoqa_tests.model.pages.practice_form import FormPage


@allure.feature("Регистрация через форму сайта")
@allure.title("Успешная регистрация при заполнении всех обязательных полей")
@allure.story("Регистрация")
def test_practice_form(setup_browser):
    with allure.step("Настроить браузер"):
        form_page = FormPage(setup_browser)
    with allure.step("Открыть страницу заполнения формы"):
        form_page.open_page_practice_form()

    with allure.step("Заполнить форму"):
        form_page.data_fill(firstName='Оксана', lastName='Прокопенко',
                            userEmail='proyeillepebe-2165@yopmail.com', gender='Female', Number='1234567890',
                            file='resource/test_5.jpeg', year='1998', month='0', day='01',
                            Subjects='Arts', Hobbies='Sports', State='NCR', City='Noida', Address='Краснодарский край')

    with allure.step("Отправить форму регистрации"):
        form_page.send_form()

    with allure.step("Проверить корректность данных в заполненной форме"):
        form_page.check_get_form(firstName='Оксана', lastName='Прокопенко', userEmail='proyeillepebe-2165@yopmail.com', gender='Female',
                                 Number='1234567890', file='test_5.jpeg',
                                 date='01 January,1998', Subjects='Arts', Hobbies='Sports', State='NCR',
                                 City='Noida', Address='Краснодарский край')

    with allure.step("Закрыть форму"):
        form_page.close_form()
