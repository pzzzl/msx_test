class Website:
    URL: str = "https://careers.msxi.com/"
    EXPECTED_TITLE: str = "MSXI Careers"

class Xpath:
    JOB_SEARCH: str = '//*[@id="header"]/div[4]/div[3]/div/div[1]/div/div/div/div/ul/li[1]/a'
    SEARCH_JOBS: str = '//*[@id="search-wrapper"]/div[1]/form/div/div/div[2]/div[2]/div[1]/input'
    JOB_TITLES: str = '(//tr[@class="data-row"]/td/span/a)'
    JOB_LOCATIONS: str = '(//tr[@class="data-row"]/td[2]/span)'
    JOB_DATES: str = '(//tr[@class="data-row"]/td[3]/span)'