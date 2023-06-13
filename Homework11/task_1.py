# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

try:
    site = "https://sbis.ru/"
    driver.maximize_window()
    driver.get(site)
    sleep(1)

    contacts_lnk = driver.find_element(By.LINK_TEXT, "Контакты")
    contacts_lnk.click()
    sleep(1)

    logo_lnk = driver.find_element(By.CSS_SELECTOR, '[title="tensor.ru"]')
    logo_lnk.click()
    driver.switch_to.window(driver.window_handles[-1])
    sleep(1)

    news_block = driver.find_element(By.CSS_SELECTOR, ".tensor_ru-Index__block4-content > .tensor_ru-Index__card-title")
    driver.execute_script("return arguments[0].scrollIntoView(true);", news_block)
    assert news_block.is_displayed(), 'Блока нет на странице'
    assert news_block.text == "Сила в людях"
    sleep(1)

    about_lnk = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-bg .tensor_ru-link')
    about_lnk.click()
    sleep(1)
    assert driver.current_url == "https://tensor.ru/about"

except AssertionError as e:
    raise e
except Exception as e:
    print(e)
finally:
    driver.quit()
