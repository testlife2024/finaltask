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
    request = 'носки'
    driver.find_element(By.CSS_SELECTOR,'#searchInput').send_keys(request)
    driver.find_element(By.CSS_SELECTOR,'#applySearchBtn').click()
    WebDriverWait(driver,5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#catalog > div > div.catalog-page__searching-results.searching-results > div > h1'),request))
    assert driver.find_element(By.CSS_SELECTOR,'#catalog > div > div.catalog-page__searching-results.searching-results > div > h1').text == request
    driver.quit()


def test_search_product_neg():
    '''
                      Результаты поиска несуществующего товара уведомляют об его отсутствии на маркетплейсе
    '''
    WB.WB(driver).market()
    requests = 'kfjksdjfklds'
    result_txt = f'Ничего не нашлось по запросу «{requests}»'
    driver.find_element(By.CSS_SELECTOR, '#searchInput').send_keys(requests)
    driver.find_element(By.CSS_SELECTOR, '#applySearchBtn').click()
    WebDriverWait(driver,5).until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="appReactRoot"]/div/div[1]/div[1]/div/h1'), result_txt))
    assert driver.find_element(By.XPATH,'//*[@id="appReactRoot"]/div/div[1]/div[1]/div/h1').text == result_txt
    driver.quit()


def test_directions():
    '''
                      Страница с результатами по запрашиваемому направлению отображается
    '''
    WB.WB(driver).wb_avia()
    driver.find_element(By.CSS_SELECTOR,'#__next > main > div:nth-child(1) > div > div:nth-child(3) > div > div:nth-child(1) > div').click()
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="__next"]/main/div[1]/div/div/div/div[3]/div[2]/div[1]/div[1]/span')))
    element = driver.find_element(By.XPATH,'//*[@id="__next"]/main/div[1]/div/div/div/div[3]/div[2]/div[1]/div[1]/span')
    assert element.is_displayed() == True
    driver.quit()


def test_content_page():
    '''
                      Страница с результатами по запрашиваемой теме контента отображается
    '''
    WB.WB(driver).wibes()
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div[2]/aside/section/nav/ul/li[2]/button')))
    requests = 'еда'
    driver.find_element(By.XPATH,"//button[contains(., 'Поиск')]").click()
    driver.find_element(By.XPATH,"//input[@placeholder='Поиск']").send_keys(requests)
    driver.find_element(By.XPATH,"//input[@placeholder='Поиск']").send_keys(Keys.ENTER)
    driver.implicitly_wait(5)
    element = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[1]/div/a[1]")
    assert element.is_displayed() == True
    driver.quit()


def test_add_to_cart():
    '''
                      Добавленный в корзину товар отображается в ней
    '''
    WB.WB(driver).market()
    requests = '263573724'
    driver.find_element(By.CSS_SELECTOR, '#searchInput').send_keys(requests)
    driver.find_element(By.CSS_SELECTOR, '#applySearchBtn').click()
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="imageContainer"]/div/div/canvas')))
    element = driver.find_element(By.XPATH,'//*[@id="imageContainer"]/div/div/canvas')
    while element.is_displayed():
        body = driver.find_element(By.TAG_NAME, 'body')
        driver.find_element(By.XPATH,'/html/body/div[1]/main/div[2]/div[3]/div[3]/div/div[3]/div[11]/div[2]/div/button').click()
        driver.implicitly_wait(5)
        result = driver.find_element(By.XPATH,'/html/body/div[1]/main/div[2]/div[3]/div[4]/div/div[1]/form/div[1]/div[1]/div[2]/div/div[1]/div').text
        assert result == '1 товар'
    driver.quit()



















