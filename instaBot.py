from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Firefox(executable_path='./drivers/geckodriver')
driver.get('https://www.instagram.com/')
driver.implicitly_wait(5)

############################### INPUT USER INFO ###############################

username = input("Please Enter Username: ")
password = input("Please Enter Password: ")
print("\t\t\t\t YOU MUSTN'T FOLLOWED TARGET!!")
target_username = input("Please Enter Target Username: ")
msg = input("Please enter message text: ")
print("Connecting to Account...")
############################### LOGIN ###############################
try:
    login = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.NAME, "username"))
    )

    passwrd = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.NAME, "password"))
    )

    login.send_keys(username)
    passwrd.send_keys(password)
    passwrd.send_keys(Keys.RETURN)
    print("Connecting...")
except:
    print("Couldn`t Connect. Try again")
sleep(2)

############################### FIRST NOTIFICATION ###############################

try:
    notnow = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[1]/section/main/div/div/div/div/button"))
    )
    notnow.click()
except:
    print("Something gone wrong... try again.")

############################### SECOND NOTIFICATION ###############################

try:
    notnow2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button.aOOlW:nth-child(2)"))
    )
    notnow2.click()
except:
    print("Can't Click Not Now")
    driver.quit()


sleep(2)

############################### GETTING TARGET PROFILE ###############################
try:
    driver.get(f"https://www.instagram.com/{target_username}/")
    print(f"We've got {target_username} profile.")
except:
    print("Sorry, Target username unavailable")

############################### GETTING TARGET INFO ###############################

followers_count = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span"))
        )
print(f"{target_username} has {followers_count.text} followers")
print("You should enter less followers numbers than target have. ex..( ex 1000, 5000, 10000")
followers_number = int(input("Input followers number: "))
followers_count.click()# go to followers
sleep(2)
############################### FIRST PERSON TO FOLLOW ###############################
followers = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[5]/div/div/div[2]/ul/div/li[1]/div/div[2]/div[1]/div/div/span"))
        )
# follow first person
followers.click()

############################### CHECKING FIRST PERSON ###############################

try:
    follow = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button"))
    )
    print("Following first person.")
    follow.click()
    print("Sending Message...")
    message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/div/button"))
    )
    message.click()
    sleep(2)
    message_text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea"))
    )
    message_text.send_keys(msg)
    sleep(1)
    message_text.send_keys(Keys.RETURN)
    driver.back()
    sleep(2)
    #### UNFOLLOW
    unfollow = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH,
                "/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button"))
        )
    unfollow.click()
    sleep(2)
    unfollow_wait = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "button.aOOlW:nth-child(1)"))
    )
    unfollow_wait.click()
    sleep(2)
    driver.back()
except:
    print("This Account is Private")
    driver.back()
    sleep(3)

############################### FOLLOWERS LOOP ###############################
sleep(2)

i=1
for follower in range(followers_number):
    i +=1
    # Followers box scroll down #
    if i % 10 == 0:
        followers_panel = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")  # to scroll
        driver.execute_script(
            "arguments[0].scrollTop = arguments[0].scrollHeight", followers_panel
        )
    else:
        pass
    sleep(5)
    followers_loop = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, f"/html/body/div[4]/div/div/div[2]/ul/div/li[{str(i)}]/div/div[2]/div[1]/div/div/span"))
    )
    print(f"Checking User {i}")
    followers_loop.click()
    sleep(2)
    try:
        follow = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button"))
        )
        print("We Should Follow him to message something. Following...")
        follow.click()
        print("Sending Message...")
        message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/div/button"))
        )
        message.click()
        sleep(3)
        message_text = driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
        message_text.send_keys(msg)
        sleep(1)
        message_text.send_keys(Keys.RETURN)
        sleep(1)
        driver.back()
        sleep(2)
        unfollow = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH,
                    "/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button"))
        )
        unfollow.click()
        sleep(2)
        unfollow_wait = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "button.aOOlW:nth-child(1)"))
        )
        unfollow_wait.click()
        driver.back()
        sleep(5)
    except:
        print("This Account is Private")
        sleep(3)
        driver.back()
        sleep(2)




