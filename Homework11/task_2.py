# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:

    driver.get("https://fix-online.sbis.ru/")
    driver.maximize_window()
    sleep(2)
    user_login, user_password = "Lisa_alisa", "qazwsx123"
    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.send_keys(user_login + Keys.ENTER)
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.send_keys(user_password + Keys.ENTER)
    sleep(2)

    assert driver.current_url == "https://fix-online.sbis.ru/", 'Неверный адрес сайта'

    sleep(1)

    driver.get('https://fix-online.sbis.ru/page/dialogs')

    sleep(2)

    add_btn = driver.find_element(By.CSS_SELECTOR, '[data-name="sabyPage-addButton"] .controls-icon')
    add_btn.click()
    sleep(2)

    my_name = "Лисичкина Алиса"
    search_input = driver.find_element(By.CSS_SELECTOR, '[templatename="Addressee/popup:Stack"] input')
    search_input.send_keys(my_name)
    search_input.send_keys(Keys.ENTER)

    sleep(2)

    myself = driver.find_element(By.CSS_SELECTOR, 'span[data-qa="person-Information__fio"]')
    myself.click()

    sleep(2)

    text_input = driver.find_element(By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field"]')
    sleep(1)
    text_input.send_keys('Привет' + Keys.ENTER)

    driver.find_element(By.CSS_SELECTOR, '[title="Отправить"]').click()
    sleep(2)

    message_text = driver.find_element(By.CSS_SELECTOR, '.msg-entity-content_outgoing p')
    assert message_text.text == "Привет"
    assert message_text.is_displayed()

    messages_count = len(driver.find_elements(By.CSS_SELECTOR, '.msg-entity-content_outgoing p'))

    sleep(2)
    actions = ActionChains(driver)
    actions.context_click(message_text)
    actions.perform()
    sleep(1)
    driver.find_element(By.CSS_SELECTOR, '[title="Перенести в удаленные"]').click()
    sleep(2)

    elements = driver.find_elements(By.CSS_SELECTOR, '.my-element')

    assert messages_count != len(driver.find_elements(By.CSS_SELECTOR, '.msg-entity-content_outgoing p'))

except Exception as e:
    raise e
finally:
    driver.quit()
