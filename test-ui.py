import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import WB
import requests



driver = webdriver.Chrome()
driver.maximize_window()




def test_search_product_pos():
    '''
                      Результаты поиска соответствуют запрашиваемому товару
    '''
    WB.WB(driver).market()
    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='searchInput']"))
        )
    request = 'носки'
    search_input.clear()
    search_input.send_keys(request)
    search_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='applySearchBtn']"))
        )
    search_button.click()
    results_header = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, "//h1[contains(@class, 'searching-results__title')]"))
        )

    assert request.lower() in results_header.text.lower()



def test_search_product_neg():
    WB.WB(driver).market()
    search_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='searchInput']"))
        )
    request = 'kfjksdjfklds'
    search_input.clear()
    search_input.send_keys(request)
    search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='applySearchBtn']"))
        )
    search_button.click()
    WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.XPATH,
                                              "//div[contains(@class, 'searching-results__empty')] | "
                                              "//h1[contains(text(), 'Ничего не нашлось')]"))
        )
    empty_result = driver.find_element(By.XPATH,
                                              "//div[contains(@class, 'searching-results__empty')] | "
                                              "//h1[contains(text(), 'Ничего не нашлось')]").text
    expected_text = f'Ничего не нашлось по запросу «{request}»'
    assert empty_result == expected_text



def test_directions():
    '''
                      Страница с результатами по запрашиваемому направлению отображается
    '''
    WB.WB(driver).wb_avia()
    driver.find_element(By.CSS_SELECTOR,'#__next > main > div:nth-child(1) > div > div:nth-child(3) > div > div:nth-child(1) > div').click()
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="__next"]/main/div[1]/div/div/div/div[3]/div[2]/div[1]/div[1]/span')))
    element = driver.find_element(By.XPATH,'//*[@id="__next"]/main/div[1]/div/div/div/div[3]/div[2]/div[1]/div[1]/span')
    assert element.is_displayed() == True







def test_content_page():
    '''
                      Страница с результатами по запрашиваемой теме контента отображается
    '''
    WB.WB(driver).wibes()
    WebDriverWait(driver,50).until(EC.visibility_of_element_located((By.XPATH,"//button[contains(., 'Поиск')]")))
    requests = 'еда'
    driver.find_element(By.XPATH, "//button[contains(text(), 'Поиск')]").click()
    driver.find_element(By.XPATH,"//input[@placeholder='Поиск']").send_keys(requests)
    driver.find_element(By.XPATH,"//input[@placeholder='Поиск']").send_keys(Keys.ENTER)
    driver.implicitly_wait(5)
    element = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div/a[1]")
    assert element.is_displayed() == True




def test_order_button_visibility():
    """
    Кнопка Заказать отображается после добавления товара в корзину
    """
    driver.get('https://www.wildberries.ru/catalog/263573724/detail.aspx')
    add_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,
                                    "//button[contains(@class, 'btn-main') and contains(., 'Добавить в корзину')]"))
    )
    add_button.click()
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH,
                                          "//span[contains(@class, 'navbar-pc__notify') and text()='1']"))
    )
    driver.get('https://www.wildberries.ru/lk/basket')
    order_button = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH,
                                          "//button[contains(@class, 'btn-main') and contains(., 'Заказать')]"))
    )

    assert order_button.is_displayed()


    driver.quit()








