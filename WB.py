class WB():
    def __init__(self, driver):
        self._driver = driver

    def market(self):
        '''
                Функция, переходящая на главную страницу маркетплейса
        '''
        self._driver.get('https://www.wildberries.ru/')
        self._driver.maximize_window()

    def wb_avia(self):
        '''
                        Функция, переходящая на страницу с авиабилетами
        '''
        self._driver.get('https://www.wildberries.ru/travel?entry_point=tab_header')
        self._driver.maximize_window()

    def wibes(self):
        '''
                        Функция, переходящая на страницу контентплейса
        '''
        self._driver.get('https://wibes.ru/')
        self._driver.maximize_window()

