#open browser
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
try:
    driver.get("https://telranedu.web.app/login")
    #driver.get("https://icarro-v1.netlify.app/search?page=0&size=10"
    #driver.get("https://www.w3schools.com/css/css_table.asp")

    # #by TAG_NAME
    div = driver.find_elements(By.TAG_NAME,"div")
    div2 = driver.find_element(By.CSS_SELECTOR,"div")
    div3 = driver.find_element(By.XPATH, "//div")
    # print(len(div))

    h1 = driver.find_element(By.TAG_NAME,"h1")
    h1_2 = driver.find_element(By.CSS_SELECTOR,"h1")
    h1_3 = driver.find_element(By.XPATH, "//h1")

    input = driver.find_element(By.TAG_NAME,"input")
    input1 = driver.find_element(By.CSS_SELECTOR, "input")
    input1_1 = driver.find_element(By.XPATH, "//input")

    a_list = driver.find_elements(By.TAG_NAME,"a")
    #find_element returning .web
    a_list_1 = driver.find_elements(By.CSS_SELECTOR, "a")
    a_list_2 = driver.find_elements(By.XPATH, "//a")
    print(len(a_list)) #find_elements returning list

    # # by class
    container = driver.find_element(By.CLASS_NAME,"container")
    container_1 = driver.find_element(By.CSS_SELECTOR,".container")
    container_2 = driver.find_element(By.XPATH,"//*[@class = 'container']")

    nav_bar = driver.find_elements(By.CLASS_NAME,"active")
    nav_bar_1 = driver.find_elements(By.CSS_SELECTOR, ".active")
    nav_bar_2 = driver.find_elements(By.XPATH, "//*[@class = 'active']")
    # print(len(nav_bar))
    # print(len(nav_bar_1))

    login_1 = driver.find_element(By.CLASS_NAME,"login_login__3EHKB")
    login_1_1 = driver.find_element(By.CSS_SELECTOR, ".login_login__3EHKB")
    login_1_1_1 = driver.find_element(By.XPATH, "//*[@class = 'login_login__3EHKB']")

    # # by ID
    root = driver.find_element(By.ID,"root")
    root1 = driver.find_element(By.CSS_SELECTOR,"#root")
    root2 = driver.find_elements(By.ID,"root")
    root3 = driver.find_element(By.XPATH, "//*[@id = 'root']")
    # print(len(root2))

    # # by attribute
    name = driver.find_element(By.CSS_SELECTOR,'input[name="email"]')
    email = driver.find_element(By.CSS_SELECTOR,"input[name=\"email\"]")
    email_xpath = driver.find_element(By.XPATH, "//input[@name = 'email']")

    subtitle = driver.find_element(By.CSS_SELECTOR,'[Type your data and hit Yalla!"]')
    start_sub = driver.find_element(By.CSS_SELECTOR,"")

    #by text xPath
    login_button = driver.find_element(By.XPATH,"//button[text() = 'Login']")
    login_1_button = driver.find_element(By.XPATH, "//*[contains(text(),'Login')]")

    #by attribute
    input2 = driver.find_element(By.XPATH,"//input[@placeholder = 'Email']")
    #css
    input3 = driver.find_element(By.CSS_SELECTOR, "[placeholder^='Em']")
    #start xPath
    input3_1 = driver.find_element(By.XPATH,"//*[starts-with(@placeholder,'Em')]")
    #end CSS
    input4 = driver.find_element(By.CSS_SELECTOR,"[placeholder$='il']")
    #end xPath
    input5 = driver.find_element(By.XPATH,"//*[contains(@placeholder,'il')]")
    #middle CSS
    input6 = driver.find_element(By.CSS_SELECTOR,"[placeholder *= 'ai']")
    #middle xPath
    input7 = driver.find_element(By.CSS_SELECTOR, "//*[contains(@placeholder,'ai')]")


    #LinkText & partialLinkText
    home = driver.find_element(By.LINK_TEXT, "HOME")
    home1 = driver.find_element(By.PARTIAL_LINK_TEXT, "  ....")  # часть слова в предложении

#css in table
#row
   # mexico = driver.find_element(By.CSS_SELECTOR,"#customers tr:nth-child(3)")
#column
   # mexico1 = driver.find_element(By.CSS_SELECTOR,"#customers tr:nth-child(4)>td:nth-child(3)")
   # assert mexico1.text == "Mexico"
#first row
    #item = driver.find_element(By.CSS_SELECTOR,"#customers tr:first-child")
#last row
    #italy = driver.find_element(By.CSS_SELECTOR,"#customers tr:last-child")



finally:
    driver.quit()