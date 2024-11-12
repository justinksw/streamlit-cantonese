import streamlit as st

with st.echo():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from webdriver_manager.core.os_manager import ChromeType

    @st.cache_resource
    def get_driver():
        return webdriver.Chrome(
            service=Service(
                ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
            ),
            options=options,
        )

    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--headless")

    driver = get_driver()
    driver.get("https://humanum.arts.cuhk.edu.hk/Lexis/lexi-can/")

    st.code(driver.page_source)


# from time import sleep

# import streamlit as st

# with st.echo():
#     from selenium.webdriver.common.by import By
#     from selenium import webdriver
#     from selenium.webdriver.chrome.options import Options
#     from selenium.webdriver.chrome.service import Service
#     from webdriver_manager.chrome import ChromeDriverManager
#     from webdriver_manager.core.os_manager import ChromeType


#     @st.cache_resource
#     def get_driver():
#         return webdriver.Chrome(
#             service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()),
#             options=options,
#         )


#     options = Options()
#     options.add_argument("--disable-gpu")
#     options.add_argument("--headless")

#     DRIVER = get_driver()

#     URL = "https://humanum.arts.cuhk.edu.hk/Lexis/lexi-can/"
#     # URL = "https://humanum.arts.cuhk.edu.hk/Lexis/lexi-mf/"


#     def get_syllables(inp):

#         st.write("enter function")

#         DRIVER.get(URL)
#         sleep(1)

#         st.write("drive get")

#         frame = DRIVER.find_element(By.XPATH, "//html/frameset/frameset/frameset/frame[1]")

#         DRIVER.switch_to.frame(frame)

#         input = DRIVER.find_element(By.XPATH, "//html/body/form[1]/input[1]")

#         input.send_keys(f"{inp}")

#         st.write("send")

#         submit = DRIVER.find_element(By.XPATH, "/html/body/form[1]/input[2]")

#         submit.click()

#         st.write("submit")

#         DRIVER.switch_to.default_content()

#         table_frame = DRIVER.find_element(By.XPATH, "//html/frameset/frameset/frame")

#         DRIVER.switch_to.frame(table_frame)

#         table = DRIVER.find_element(By.XPATH, "//html/body/form/table[1]")

#         rows = table.find_elements(By.TAG_NAME, "tr")

#         syllables = []

#         for r in rows[1:]:

#             td1 = r.find_elements(By.TAG_NAME, "td")[0]

#             syllable = ""

#             for font in td1.find_elements(By.TAG_NAME, "font"):
#                 syllable += font.text

#             syllables.append(syllable)

#         return syllables


#     st.header("粵語拼音檢索")

#     st.write("Reference: https://humanum.arts.cuhk.edu.hk/Lexis/lexi-can/")

#     text = st.text_input(label="Enter **One** character to search")

#     if text:
#         try:
#             syllables = get_syllables(text)

#             for s in syllables:

#                 st.subheader(s)

#         except Exception as e:

#             st.write(e)
