from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd
from tqdm import tqdm
import time

if __name__ == "__main__":
    driver = webdriver.Chrome()
    base_url = "https://www.metacritic.com/browse/tv/all/all/all-time/new/?releaseYearMin=1910&releaseYearMax=2024&page="
    tv_show_data = []

    # Adjust the range based on the number of pages you want to scrape
    total_pages = 282
    for idx in tqdm(range(1, total_pages + 1), desc="Scraping Pages"):
        page_url = f"{base_url}{idx}"
        driver.get(page_url)
        
        # Adjust the class name based on the structure of the website
        tv_show_elements = driver.find_elements(By.CLASS_NAME, "c-finderProductCard")

        for tv_show_element in tv_show_elements:
            # Extract relevant information based on the HTML structure
            title_element = tv_show_element.find_element(By.CLASS_NAME, "c-finderProductCard_titleHeading")
            title = title_element.find_element(By.TAG_NAME, "span").text
            url_element = tv_show_element.find_element(By.CLASS_NAME, "c-finderProductCard_container")
            url = url_element.get_attribute("href")

            tv_show_data.append({"title": title, "url": url})

        time.sleep(1)

    df = pd.DataFrame(data=tv_show_data, columns=tv_show_data[0].keys())
    df.to_csv("tv_show_data.csv", index=False)

    driver.quit()
