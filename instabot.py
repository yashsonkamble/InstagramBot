from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
import random


ibot = webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")
ibot.implicitly_wait(2)


def login():
    ibot.get('https://www.instagram.com/accounts/login/')
    sleep(3)
    username = open("usernm.txt", "r")
    unm = str(username.read())
    password = open("pass.txt", "r")
    passw = str(password.read())
    ibot.find_element_by_xpath(
        "/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input").send_keys(unm)
    sleep(2)
    ibot.find_element_by_xpath(
        "/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input").send_keys(passw + Keys.RETURN)
    sleep(1)

    # save login info not now button
    try:
        ibot.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/div/div/div/button').click()
    except:
        pass

    sleep(4)
    # info about notifications(to select not now)

    try:
        deny_msg = ibot.find_element_by_xpath(
            '/html/body/div[4]/div/div/div/div[3]/button[2]').click()
    except:
        pass



def Dir_msg():
    msg = ["Kasa kai Bhava", "Hey Buddy", "Hello Man",
           "Hi from studybot", "Hope you are doing well", "Have a good day"]
    y = len(msg) - 1
    x  = int(y)
    #num = int(random.randint(0, x))
    usernames_list = list()

    with open("usernames.txt") as f:
        for line in f:
            x=line.strip("\n")
            usernames_list.append(x)

    # go to DM section

    msg_list = ibot.find_element_by_xpath(
            '/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
    
    
    for usernm in usernames_list:
        num = int(random.randint(0, len(msg) - 1))
        
        sleep(2)
        # click on search user icon
        search_user_icon = ibot.find_element_by_xpath(
            '/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button/div').click()
        sleep(2)
        # Enter username of user in text field
        search_ser = ibot.find_element_by_xpath(
            '/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(usernm + Keys.RETURN)
        sleep(2)
        
        #Select the username from list of usernames you see(First one selected)
        select_user = ibot.find_element_by_xpath(
            '/html/body/div[5]/div/div/div[2]/div[2]/div[1]/div/div[3]/button').click()
        sleep(2)

        # click next button
        next_button = ibot.find_element_by_xpath(
            '/html/body/div[5]/div/div/div[1]/div/div[2]/div/button/div').click()
        sleep(2)
    
        #send messgeage
        send_msg = ibot.find_element_by_xpath(
            "//textarea[@placeholder='Message...']").send_keys(msg[num] + Keys.RETURN)



def Follow(usernm):
    url = 'https://www.instagram.com/' + usernm + '/'
    ibot.get(url)
    sleep(1)
    try:
        #follow = ibot.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div[2]/div/div/div/span/span[1]/button').click()
        follow = ibot.find_element_by_class_name('_5f5mN').click()
        sleep(1)
    except:
        pass
    sleep(2)



def Unfollow(usernm):
    url = 'https://www.instagram.com/' + usernm + '/'
    ibot.get(url)
    sleep(2)
    try:
        unfollow = ibot.find_element_by_class_name('_5f5mN').click()
        sleep(1)
        y = ibot.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[1]').click()
        sleep(1)
    except:
        pass
    sleep(2)



def comment(usernm, amount):
    cmt = ["Nice post man", "Keep it up", "Keep posting", "You are awesome", "I am amazed", "Good work"]
    x = len(cmt) - 1
    url = 'https://www.instagram.com/' + usernm + '/'
    ibot.get(url)
    sleep(2)
    ibot.find_element_by_class_name('v1Nh3').click()
    sleep(1)
    i = 1
    while i <= amount:
        num = random.randint(0, len(cmt) - 1)
        #print(num)
        sleep(2)
        addcmt = ibot.find_element_by_class_name('RxpZH').click()
        sleep(2)
        ibot.find_element_by_xpath(
            "//textarea[@placeholder='Add a comment…']").send_keys(cmt[num])
        sleep(2)
        ibot.find_element_by_xpath("//button[@type='submit']").click()
        sleep(2)
        ibot.find_element_by_class_name(
            'coreSpriteRightPaginationArrow').click()
        sleep(2)
        i += 1


def like_hashtag(hashT, amount):
    ibot.get('https://www.instagram.com/explore/tags/' + hashT)
    ibot.find_element_by_class_name('v1Nh3').click()
    i = 1
    while i <= amount:
        sleep(1)
        ibot.find_element_by_class_name('fr66n').click()
        sleep(2)
        ibot.find_element_by_class_name(
            'coreSpriteRightPaginationArrow').click()
        sleep(1)
        i += 1


def like_username(usernm, amount):
    url = 'https://www.instagram.com/' + usernm + '/'
    ibot.get(url)
    ibot.find_element_by_class_name('v1Nh3').click()
    i = 1
    while i <= amount:
        sleep(1)
        ibot.find_element_by_class_name('fr66n').click()
        sleep(2)
        ibot.find_element_by_class_name(
            'coreSpriteRightPaginationArrow').click()
        sleep(1)
        i += 1

def homepage():
    ibot.get('https://www.instagram.com/')                                   
    sleep(2) 

def LogOut():
    log = ibot.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img').click()
    sleep(1)
    logout = ibot.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/div[2]/div/div/div/div').click()


"""   
login()
Dir_msg()
comment("chappri_memer", 3)
Follow("therock")
Unfollow("therock")
like_hashtag("pune", 3)
like_username("chappri_memer", 3)
"""



print("\n_________________________________________________________________")
print("\n____________________SDL MINIPROJECT DYP__________________________")
login()
while(1):
    print("""\n\t\tSELECT FROM GIVEN CHOISES
            \t\t1 -->Like by Hastag
            \t\t2 -->Like by Username
            \t\t3 -->Follow
            \t\t4 -->Unfollow
            \t\t5 -->comment
            \t\t6 -->Dir_msg
            \t\t7 -->Exit
            """)
    ch =int(input("\nEnter Choice : "))
    if ch == 1:
        hashT = input("Enter hashtag : ")
        amount = int(input("Enter no of posts to like : "))
        homepage()
        like_hashtag(hashT, amount)

    elif ch ==2:
        usernm = input("Enter Username of A/C for liking pictures: ")
        amount = int(input("Enter no of posts to like : "))
        homepage()
        like_username(usernm, amount)

    elif ch ==3:
        usernm = input("Enter Username of A/C to follow : ")
        homepage()
        Follow(usernm)

    elif ch ==4:
        usernm = input("Enter Username of A/C to unfollow : ")
        homepage()
        Unfollow(usernm)

    elif ch ==5:
        usernm = input("Enter Username of A/C for commenting: ")
        amount = int(input("Enter no of posts to add comment : "))
        homepage()
        comment(usernm, amount)

    elif ch ==6:
        
        homepage()
        Dir_msg()

    elif ch ==7:
        homepage()
        LogOut()
        sleep(2)
        break

    else:
        print("WRONG CHOICE")
