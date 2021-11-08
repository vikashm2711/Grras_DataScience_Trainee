from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

input('Press Enter After Scanning QR code and ur ready')
filepath = "C://Users/Kiki/Pictures/Illustrator/4x/1.jpg"
contact=["Vikash Maurya","Kiki","Vikash Maurya"]
NF_contact=[]

for i in contact:
    sleep(1)
    search = driver.find_element_by_xpath('//span[@data-icon="chat"]')
    search.click()
    
    inputElement=driver.find_element_by_xpath('//div[@class="_13NKt copyable-text selectable-text"]')
    inputElement.send_keys(f"{i}")
    sleep(1)
    try:
        print(i)
        selectname=driver.find_element_by_xpath('//span[@title="{}"]'.format(i))
        selectname.click()
    except:
        print("Contact Not Found:",i)
        NF_contact.append(i)
        sleep(1)
        pass
    else:
        attachment_box = driver.find_element_by_xpath('//div[@title = "Attach"]')
        attachment_box.click()
        sleep(2)
        attachment_doc= driver.find_element_by_xpath('//span[@data-icon="attach-image"]')
        attachment_doc.click()

        image_box = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
        sleep(1)

        image_box.send_keys(filepath)

        sleep(3)

        send_button = driver.find_element_by_xpath('//span[@data-icon="send"]')
        send_button.click()
        sleep(1)
        
        inputElement=driver.find_element_by_xpath('//div[@class="_13NKt copyable-text selectable-text"][@contenteditable="true"][@data-tab="9"]')
        for msgline in msg:
            inputElement.send_keys(msgline + Keys.SHIFT+Keys.ENTER)
        sleep(1)
        send_button = driver.find_element_by_xpath('//span[@data-icon="send"]')
        send_button.click()