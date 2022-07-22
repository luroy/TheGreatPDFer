import time
from io import BytesIO

from PIL import Image
from fpdf import FPDF
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

x = 1300
y = 1200
off = 160
try:
    print("Drivers initialization")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument('--disable-logging')
    chrome_options.add_argument("--headless")
    chrome_options.add_argument(F"--window-size={x},{y}")
    s = Service('C:/Users/lea.uroy/TheGreatPDFer/Driver/chromedriver.exe')
    driver = webdriver.Chrome(service=s,
                              options=chrome_options)
except:
    exit("Driver Error")
print("Done !")
URL = 'https://international.scholarvox.com/reader/docid/88865376/page/'
pdf = FPDF(unit="pt", format=(x - 2 * off + 20, y + 50))
pdf.set_auto_page_break(0)
try:
    for i in range(1, 10):
        name = F"page{i}"
        print("Starting " + name)
        driver.get(URL + str(i))
        time.sleep(1.5)
        png = driver.get_screenshot_as_png()
        im = Image.open(BytesIO(png))
        output_img = im.crop((off, 0, x - off - 40, y))
        output_img.save(name + ".png")
        pdf.add_page()
        pdf.image(name + ".png")
        print(name.split(".")[0], "done !")
    pdf.output("yourfile.pdf", "F")
    driver.quit()
except Exception as ignored:
    driver.close()
    driver.quit()
