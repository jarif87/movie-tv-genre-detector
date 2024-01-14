from selenium.webdriver.common.by import By
from selenium import webdriver
from tqdm import tqdm
import pandas as pd
import time

if __name__ == "__main__":
    # webdriver_path = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome()

    df = pd.read_csv("movie_urls_part1.csv",encoding='latin-1')
    movie_urls = df.url.to_list()

    movie_data = []
    for movie_url in tqdm(movie_urls):
        try:
            driver.get(movie_url)
            time.sleep(3)

            summary_element = driver.find_element(By.CLASS_NAME, "c-productDetails_summary")
            description = summary_element.find_element(By.CLASS_NAME, "c-productDetails_description").text

            genres_elements = driver.find_elements(By.CLASS_NAME, "c-genreList_item")
            genres = [genre.find_element(By.CLASS_NAME, "c-globalButton_label").text for genre in genres_elements]

            movie_data.append({
                "url": movie_url,
                "description": description,
                "genres": genres
            })
            time.sleep(3)

            df = pd.DataFrame(data=movie_data, columns=movie_data[0].keys())
            df.to_csv("movie_details_part1.csv", index=False)

        except Exception as e:
            print(f"Error processing {movie_url}: {str(e)}")
            time.sleep(3)

    driver.quit()
