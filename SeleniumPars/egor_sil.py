from selenium import webdriver
import time
import openpyxl as opx


work_book = opx.Workbook()
work_book.create_sheet("Контакты", 0)
active_sheet = work_book['Контакты']
result_info = {}
data = []

driver = webdriver.Chrome()
driver.get("https://agrobizneskarta.ru/catalog/manufacturers/rastenievodstvo/?area=67&point=&type=1&SECTION_CODE=rastenievodstvo&PAGEN_1=1")
# ищем кнопку "Войти"
driver.find_element_by_id("loginzone").click()
#Находим и вписываем логин с паролем
time.sleep(5)
driver.find_element_by_name("USER_LOGIN").send_keys("****")
driver.find_element_by_name("USER_PASSWORD").send_keys("***")
#Осуществляем вход
driver.find_element_by_name("Login").click()
time.sleep(10)

for i in range(1,17):
    driver.get(f"https://agrobizneskarta.ru/catalog/manufacturers/rastenievodstvo/?area=31&point=&type=1&SECTION_CODE=rastenievodstvo&PAGEN_1={i}")
    mas_buttons = driver.find_elements_by_class_name('catalog_element')

    for butt in mas_buttons:
        firm_name = butt.find_element_by_tag_name("h2")
        firm_name.click()
        time.sleep(2)
        description = butt.find_element_by_class_name("description").text
        direction = driver.find_element_by_class_name("contact_info_inner").text
        active_sheet.append([firm_name.text, description, direction])
work_book.save('contacts.xlsx')


