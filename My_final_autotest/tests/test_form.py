import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import settings

# EXP-001
def test_open_page_auth(browser):
    auth = browser.find_element(By.CLASS_NAME, 'card-container__title')
    assert auth.text == 'Авторизация', 'Fail'

# EXP-002
def test_change_tel_in_mail(browser):
    browser.find_element(By.ID, 'username').send_keys(settings.mail)
    browser.find_element(By.ID, 'password').click()
    assert browser.find_element(By.XPATH, '//div[contains(@class, "rt-tab--active")]').text == 'Почта'

# EXP-003
def test_change_tel_in_login(browser):
    browser.find_element(By.ID, 'username').send_keys(settings.login)
    browser.find_element(By.ID, 'password').click()
    assert browser.find_element(By.XPATH, '//div[contains(@class, "rt-tab--active")]').text == 'Логин'

# EXP-004
def test_change_tel_on_numberLK(browser):
    browser.find_element(By.ID, 'username').send_keys('12345769743')
    browser.find_element(By.ID, 'password').click()
    assert browser.find_element(By.XPATH, '//div[contains(@class, "rt-tab--active")]').text == 'Лицевой счёт', 'FAIL'

# EXP-005
def test_redirect_reset_credentials(browser):
    browser.find_element(By.ID, 'forgot_password').click()
    assert browser.find_element(By.CLASS_NAME, 'card-container__title').text == 'Восстановление пароля'

# EXP-006
def test_redirect_registration(browser):
    browser.find_element(By.ID, 'kc-register').click()
    assert browser.find_element(By.XPATH, '//h1[@class="card-container__title"]').text == 'Регистрация'

# EXP-007
def test_agreement(browser):
    browser.find_element(By.XPATH, '//div[@class="auth-policy"]/a').click()
    browser.switch_to.window(browser.window_handles[1])
    title = browser.find_element(By.XPATH, '//div[@id="title"]/h1').text
    assert title.startswith('Публичная оферта'), 'FAIL'

# EXP-008
def test_auth_vk(browser):
    browser.find_element(By.ID, 'oidc_vk').click()
    assert 'vk.com' in browser.find_element(By.XPATH, '//div[@class="oauth_head"]/a').get_attribute('href')
    assert 'vk' in browser.current_url

# EXP-009
def test_empty_form(browser):
    browser.find_element(By.ID, 'kc-register').click()
    browser.find_element(By.NAME, 'register').click()
    osh = browser.find_elements(By.XPATH, '//span[contains(@class, "rt-input-container__meta--error")]')
    assert len(osh) == 5

# EXP-010
def test_registration_valid_with_email(browser):
    browser.find_element(By.XPATH, "//input[@name='firstName']").send_keys('Мария')
    browser.find_element(By.XPATH, "//input[@name='lastName']").send_keys('Тихвенко')
    browser.find_element(By.ID, "address").send_keys('marsochka@gmail.com')
    browser.find_element(By.ID, "password").send_keys('Cataract1')
    browser.find_element(By.ID, "password-confirm").send_keys('Cataract1')
    browser.find_element(By.XPATH, 'kc-register').click()
    assert browser.find_element(By.ID, "rt-code-1")

# EXP-011
def test_registration_with_pass_21(browser):
    browser.find_element(By.XPATH, "//input[@name='firstName']").send_keys('Мария')
    browser.find_element(By.XPATH, "//input[@name='lastName']").send_keys('Тихвенко')
    browser.find_element(By.ID, "address").send_keys('marsochka@gmail.com')
    browser.find_element(By.ID, "password").send_keys('Qwerty1Qwerty2Qwerty3')
    browser.find_element(By.ID, "password-confirm").send_keys('Qwerty1Qwerty2Qwerty3')
    browser.find_element(By.XPATH, 'kc-register').click()
    assert browser.find_element(By.XPATH, "//span[@class='rt-input-container__meta rt-input-container__meta--error']")

# EXP-012
 def test_registration_with_pass_without_digit(browser):
     browser.find_element(By.XPATH, "//input[@name='firstName']").send_keys('Мария')
     browser.find_element(By.XPATH, "//input[@name='lastName']").send_keys('Тихвенко')
     browser.find_element(By.ID, "address").send_keys('marsochka@gmail.com')
     browser.find_element(By.ID, "password").send_keys('Qwertytre')
     browser.find_element(By.ID, "password-confirm").send_keys('Qwertytre')
     browser.find_element(By.XPATH, 'kc-register').click()
     assert browser.find_element(By.XPATH, "//span[@class='rt-input-container__meta rt-input-container__meta--error']")

# EXP-013
def test_registration_with_tel_firstname_31char(browser):
    browser.find_element(By.XPATH, "//input[@name='firstName']").send_keys('МашаМашаМарияМашаМарияМашаМария')
    browser.find_element(By.XPATH, "//input[@name='lastName']").send_keys('Тихвенко')
    browser.find_element(By.ID, "address").send_keys('+79994567890')
    browser.find_element(By.ID, "password").send_keys('Qwerty123')
    browser.find_element(By.ID, "password-confirm").send_keys('Qwerty123')
    browser.find_element(By.XPATH, 'kc-register').click()
    assert browser.find_element(By.XPATH, "//span[@class='rt-input-container__meta rt-input-container__meta--error']")

# EXP-014
def test_registration_with_tel_firstname_1char(browser):
    browser.find_element(By.XPATH, "//input[@name='firstName']").send_keys('М')
    browser.find_element(By.XPATH, "//input[@name='lastName']").send_keys('Тихвенко')
    browser.find_element(By.ID, "address").send_keys('+79994567890')
    browser.find_element(By.ID, "password").send_keys('Qwerty123')
    browser.find_element(By.ID, "password-confirm").send_keys('Qwerty123')
    browser.find_element(By.XPATH, 'kc-register').click()
    assert browser.find_element(By.XPATH, "//span[@class='rt-input-container__meta rt-input-container__meta--error']")

# EXP-015
def test_registration_with_tel_non_equals_pass(browser):
    browser.find_element(By.XPATH, "//input[@name='firstName']").send_keys('Мария')
    browser.find_element(By.XPATH, "//input[@name='lastName']").send_keys('Тихвенко')
    browser.find_element(By.ID, "address").send_keys('+79994567890')
    browser.find_element(By.ID, "password").send_keys('Qwerty123')
    browser.find_element(By.ID, "password-confirm").send_keys('Qwerty1234')
    browser.find_element(By.XPATH, 'kc-register').click()
    assert browser.find_element(By.XPATH, "//span[@class='rt-input-container__meta rt-input-container__meta--error']")


# EXP-016
@pytest.mark.xfail(reason='Капча не верна')
def test_recovery_pass_with_mail(browser):
    browser.find_element(By.ID, 'forgot_password').click()
    browser.find_element(By.ID, 'username').send_keys(settings.mail)
    # пароль восстанавливается по капче
    browser.find_element(By.ID, 'captcha').send_keys() # ввести капчу
    browser.find_element(By.ID, 'reset')
    assert browser.find_element(By.XPATH, '//h1[@class="card-container__title"]').text == 'Восстановление пароля'


# EXP-017
def test_auth_with_tel(browser):
    browser.find_element(By.ID, 'username').send_keys(settings.mtel)
    browser.find_element(By.ID, 'password').send_keys(settings.password)
    browser.find_element(By.ID, 'kc-login').click()
    assert browser.find_element(By.ID, 'logout-btn')


# EXP-018
def test_auth_with_mail(browser):
    browser.find_element(By.ID, 'username').send_keys(settings.mail)
    browser.find_element(By.ID, 'password').send_keys(settings.password)
    browser.find_element(By.ID, 'kc-login').click()
    assert browser.find_element(By.ID, 'logout-btn')

# EXP-019
def test_auth_invalid_email(browser):
    browser.find_element(By.ID, 'username').send_keys('marsa73@gmail.com')
    browser.find_element(By.ID, "password").send_keys('Qwerty11!')
    browser.find_element(By.ID, 'kc-login').click()
    assert browser.find_element(By.XPATH, '//*[@id="form-error-message"]')
    assert browser.find_element(By.XPATH, "//span[contains(text(), 'Неверный логин или пароль')]")


# EXP-020
def test_auth_invalid_password(browser):
    browser.find_element(By.ID, 'username').send_keys(settings.mtel)
    browser.find_element(By.ID, 'password').send_keys('')
    browser.find_element(By.ID, 'kc-login').click()
    assert browser.find_element(By.XPATH, '//*[@id="form-error-message"]')
    assert browser.find_element(By.XPATH, "//span[contains(text(), 'Неверный логин или пароль')]")

