from selenium import webdriver
from selenium.webdriver.common.by import By
from variables import Website, Xpath
import pandas as pd

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get(Website.URL)

    driver.maximize_window()
    driver.implicitly_wait(30)

    assert Website.EXPECTED_TITLE in driver.title

    job_search = driver.find_element(By.XPATH, Xpath.JOB_SEARCH)
    job_search.click()

    location_input = driver.find_element(By.NAME, 'locationsearch')
    location_input.send_keys('Brasil')

    search_jobs_button = driver.find_element(By.XPATH, Xpath.SEARCH_JOBS)
    search_jobs_button.click()

    titles = driver.find_elements(By.XPATH, Xpath.JOB_TITLES)
    amount = len(titles) + 1

    data = []

    for i in range(1, amount):
        title = driver.find_element(By.XPATH, f'{Xpath.JOB_TITLES}[{i}]').text
        location = driver.find_element(By.XPATH, f'{Xpath.JOB_LOCATIONS}[{i}]').text
        date = driver.find_element(By.XPATH, f'{Xpath.JOB_DATES}[{i}]').text
        print(title, location, date)
        data.append([title, location, date])

    df = pd.DataFrame(data, columns=['Title', 'Location', 'Date'])

    df.to_excel('output.xlsx', engine='openpyxl')