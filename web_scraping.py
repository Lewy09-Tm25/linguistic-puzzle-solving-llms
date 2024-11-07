import pandas as pd
from selenium import webdriver 
from selenium.webdriver.common.by import By 
# from webdriver_manager.chrome import ChromeDriverManager

URL_TO_SCRAPE = "https://www.uklo.org/past-exam-papers/"

def create_df(*data):
    df = pd.DataFrame({})
    for ind, d in enumerate(data[0]):
        df[ind] = d
    df.columns = df.iloc[0]
    df = df[1:].reset_index(drop=True)
    df.to_csv("scraped_data.csv",index = False)



def scrape(url):
    # set webdriver path here it may vary
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.get(url)
    levels = []
    qatexts = []
    qaurls = []
    subs = []
    tformats = []
    themes = []
    langs = []
    authors = []
    # level
    level = driver.find_elements(By.CLASS_NAME, "column-1")
    # qaurl
    qaurl = driver.find_elements(By.XPATH, '//td[@class="column-2"]')
    # subject
    sub = driver.find_elements(By.CLASS_NAME, "column-3")
    # format
    tformat = driver.find_elements(By.CLASS_NAME, "column-4")
    # theme
    theme = driver.find_elements(By.CLASS_NAME, "column-5")
    # lang_family
    lang_family = driver.find_elements(By.CLASS_NAME, "column-6")
    # author
    author = driver.find_elements(By.CLASS_NAME, "column-7")

    for i in range(222):
        levels.append(level[i].text)
        subs.append(sub[i].text)
        tformats.append(tformat[i].text)
        themes.append(theme[i].text)
        langs.append(lang_family[i].text)
        authors.append(author[i].text)

    # Handling URLs
    for i in range(220):
        a_tag = qaurl[i].find_element(By.TAG_NAME, 'a')
        text = a_tag.text
        link = a_tag.get_attribute('href')
        qatexts.append(text)
        qaurls.append(link)
    
    qaurls = ["URL",""] + qaurls
    qatexts = ["Year_round",""] + qatexts
    driver.close()

    cols = [levels,qaurls,qatexts,subs,tformats,themes,langs,authors]
    create_df(cols)


if __name__ == "__main__":
    scrape(URL_TO_SCRAPE)