from time import sleep

import streamlit as st

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument("--headless=new")

DRIVER = webdriver.Chrome(options=chrome_options)

URL = "https://humanum.arts.cuhk.edu.hk/Lexis/lexi-can/"
# URL = "https://humanum.arts.cuhk.edu.hk/Lexis/lexi-mf/"


def get_syllables(inp):

    DRIVER.get(URL)
    sleep(1)

    frame = DRIVER.find_element(By.XPATH, "//html/frameset/frameset/frameset/frame[1]")

    DRIVER.switch_to.frame(frame)

    input = DRIVER.find_element(By.XPATH, "//html/body/form[1]/input[1]")

    input.send_keys(f"{inp}")

    submit = DRIVER.find_element(By.XPATH, "/html/body/form[1]/input[2]")

    submit.click()

    DRIVER.switch_to.default_content()

    table_frame = DRIVER.find_element(By.XPATH, "//html/frameset/frameset/frame")

    DRIVER.switch_to.frame(table_frame)

    table = DRIVER.find_element(By.XPATH, "//html/body/form/table[1]")

    rows = table.find_elements(By.TAG_NAME, "tr")

    syllables = []

    for r in rows[1:]:

        td1 = r.find_elements(By.TAG_NAME, "td")[0]

        syllable = ""

        for font in td1.find_elements(By.TAG_NAME, "font"):
            syllable += font.text

        syllables.append(syllable)

    return syllables


st.header("粵語拼音檢索")

st.write("Reference: https://humanum.arts.cuhk.edu.hk/Lexis/lexi-can/")

text = st.text_input(label="Enter **One** character to search")

if text:
    try:
        syllables = get_syllables(text)

        for s in syllables:

            st.subheader(s)

    except:

        st.subheader("No result.")