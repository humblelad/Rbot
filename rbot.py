
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager as CM
import time
import random
from random import randint

class RBot:


    def __init__(self, username, password):
      
        print("""
        __________ __________           __    
        \______   \\______   \  ____  _/  |_  
         |       _/ |    |  _/ /  _ \ \   __\ 
         |    |   \ |    |   \(  <_> ) |  |   
         |____|_  / |______  / \____/  |__|   by @CircleNinja
        \/         \/                 
        """)
              

        #edit the message according to your liking

        message = ["It’s that time of year! May your merry celebrations be filled with joy and laughter. Happy Christmas and new year! Let's hope the new year make us achieve more in life.", "Wishing you and those around you a very Merry Christmas and a wonderful New Year. May the holidays bring you happy moments that become forever memories."\
        ,"Wishing you the happiest and most memorable holiday. Merry Christmas and happy new year! May we count the good things we have achieved this year!", "Wishing you a Merry Christmas and a Happy New Year filled with blessings, good health, and prosperity!","Wishing you a very Happy Christmas and new year. May this time of the year make us count the blessings we have in life."\
        ,"Wishing you a very happy Christmas and happy new year. Let us look forward to a new year of hope and blessings."]


        driver = webdriver.Chrome(executable_path=CM().install())
        driver.set_window_position(0, 0)

        driver.set_window_size(900, 900)


        driver.get("https://instagram.com")
        time.sleep(getRandomTime())
        driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(password)
        time.sleep(getRandomTime())
        driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()



        #add to list the users whom you want to dm your custom message.
        folks = ["receiver1","receiver2"]

        time.sleep(getRandomTime())


        driver.get("https://www.instagram.com/")
        time.sleep(getRandomTime())

        driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]") \
            .click()
        time.sleep(getRandomTime())
        driver.find_element_by_xpath(
            "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[5]/div/a") \
            .click()
        time.sleep(getRandomTime())
        for i in range(len(folks)):
            print("Dm'ing "+folks[i])
            random_num = random.choice(message)
            edit = str(random_num) + " “Christmas isn’t a season. It’s a feeling.” – Edna Ferber. \n https://m.123greetings.com/events/christmas/merry_christmas/magical_xmas_wishes_for_friends.html \n [ This is an automated msg via Rbot :) ]"

            driver.get("https://www.instagram.com/direct/new/")

            time.sleep(getRandomTime())
            driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]")\
              .click()



            # this is where you choose who to dm, change the send keys if you want to message someone else
            driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/input")\
                .send_keys(folks[i])


            time.sleep(getRandomTime())
    #before next
            driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div[1]/div")\
              .click()
    #next code

            time.sleep(getRandomTime())
            driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[3]/div/button/div")\
              .click()


            time.sleep(getRandomTime())

            driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys(edit)
            time.sleep(getRandomTime())

            driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button").click()
            time.sleep(getRandomTime())
            time.sleep(getRandomTime())

            time.sleep(f())

        driver.quit()
#adjust this according to need. Keep this random so that instagram thinks it as genuine user interactions.
def getRandomTime():
        randTime = randint(5, 6)
        return randTime


def f():
    r = randint(10, 15)
    return r




RBot("yourusername", "yourpassword")


