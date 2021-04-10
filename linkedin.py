
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

LinkedInUsername = "Email"

chrome_options = Options()
chrome_options.add_argument("--headless")           # This is done to NOT display a Google Chrome window in our monitor while the data is being collected.
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/")
driver.find_element_by_xpath("/html/body/main/section[1]/div[2]/form/div[2]/div[1]/input")\
            .send_keys(LinkedInUsername)

driver.find_element_by_xpath("/html/body/main/section[1]/div[2]/form/div[2]/div[2]/input")\
            .send_keys("password")
driver.find_element_by_xpath("/html/body/main/section[1]/div[2]/form/button")\
            .click()
sleep(6)


data="flutter"
# Put the URL of the Linkedin Jobs Search you want. Example (Keyworkd=Cloud , Location=Worldwide)
driver.get(f"https://www.linkedin.com/search/results/content/?datePosted=%22past-24h%22&keywords={data}&origin=FACETED_SEARCH")
sleep(4)

mylist=[]
start1 = driver.find_element_by_xpath("/html/body/div[8]/div[3]/div/div[1]/div/div[1]/main/div/div/div[2]/ul/li[2]/div/div/div[2]/div[1]/div/div/div/p").text

mylist.append(start1)

for x in mylist:
	print(x)
