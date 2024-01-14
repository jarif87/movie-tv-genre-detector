from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from tqdm import tqdm
import time

if __name__ == "__main__":
    driver = webdriver.Chrome()

    df = pd.read_csv("tv_show_data.csv")
    tv_show_urls = df.url.to_list()

    tv_show_data = []

    for tv_show_url in tqdm(tv_show_urls, desc="Scraping TV Shows", unit="TV Show"):
        try:
            driver.get(tv_show_url)

            # Wait for the title element to be present
            title_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "c-productDetails_summary_title"))
            )
            title = title_element.text

            # Wait for the description element to be present
            description_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "c-productDetails_description"))
            )
            description = description_element.text

            # Wait for the genres elements to be present
            genres_elements = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "c-genreList_item"))
            )
            genres = [genre.text for genre in genres_elements]

            tv_show_data.append({
                "title": title,
                "url": tv_show_url,
                "description": description,
                "genres": genres
            })

        except Exception as e:
            print(f"An error occurred for {tv_show_url}: {str(e)}")

        time.sleep(3)

    driver.quit()

    df_tv_show = pd.DataFrame(data=tv_show_data, columns=tv_show_data[0].keys())
    df_tv_show.to_csv("tv_show_details.csv", index=False)
