from selenium.webdriver.common.by import By
from selenium import webdriver
from tqdm import tqdm
import pandas as pd
import time

if __name__ == "__main__":
    driver = webdriver.Chrome()
    base_url = "https://www.metacritic.com/browse/movie/"
    movie_urls = []

    for idx in tqdm(range(660)):
        page_no = idx + 1
        page_url = f"{base_url}?page={page_no}"
        driver.get(page_url)
        
     
        rows = driver.find_elements(By.CLASS_NAME, "c-finderProductCard")

        for row in rows:
           
            url_tag = row.find_element(By.CLASS_NAME, "c-finderProductCard_container")
            title = row.text  
            movie_url = url_tag.get_attribute('href')
            movie_urls.append({"title": title, "url": movie_url})

        time.sleep(1)

    df = pd.DataFrame(data=movie_urls, columns=movie_urls[0].keys())
    df.to_csv("movie_urls.csv", index=False)

    driver.quit()
