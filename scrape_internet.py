from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)
driver.get("http://the-internet.herokuapp.com/")

# トップページの見出しを取得
heading = driver.find_element("tag name", "h1").text
print(f"Heading: {heading}")

# ページ内のリンク一覧を取得
links = driver.find_elements("css selector", "ul li a")
for link in links:
    print(link.text, link.get_attribute("href"))

driver.quit()
