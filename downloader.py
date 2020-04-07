import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
import getpass

browser = webdriver.Chrome()
paths = []
lines = []
LINKFILE = ""
BASEPATH = ""
SYSTEM = os.name

if SYSTEM == "nt":
    LINKFILE = os.getcwd() + "\\downloadlinks.txt"
    with open(LINKFILE) as f:
        lines = [line.rstrip() for line in f]
    BASEPATH = os.getcwd() + "\\content"
    for line in lines:
        line = line.split("series")[1].split("workouts")[0]
        paths.append(BASEPATH + "\\" + line[1:-1]
                     + "\\")
    for path in paths:
        path.replace("/", "\\")
elif SYSTEM == "posix":
    LINKFILE = os.getcwd() + "/downloadlinks.txt"
    with open(LINKFILE) as f:
        lines = [line.rstrip() for line in f]
    BASEPATH = os.getcwd() + "/content"
    for line in lines:
        line = line.split("series")[1].split("workouts")[0]
        paths.append(BASEPATH + line)
else:
    print("OS not supported, please open an issue on Github.")


def downloadmp4(url, filename, path):
    fullname = path + filename + ".mp4"
    if os.path.isfile(fullname):
        print(filename + " already exists, skipping...")
        return()
    else:
        print("Downloading: " + filename)
        urllib.request.urlretrieve(
            url, fullname)


def doLogin(email, password):
    browser.get(
        "https://www.alomoves.com/signin")
    time.sleep(5)
    mailfield = browser.find_elements_by_xpath(
        "//input[contains(@name,'email')]")[1]
    pwfield = browser.find_elements_by_xpath(
        "//input[contains(@name,'password')]")[2]
    mailfield.send_keys(email)
    mailfield.send_keys(Keys.TAB)
    time.sleep(1)
    pwfield.send_keys(password)
    pwfield.send_keys(Keys.ENTER)


def collectClasses(courselink):
    print(f"== Grabbing links for {courselink} ==")
    browser.get(courselink)
    workoutLinks = browser.find_elements_by_xpath(
        "//div[contains(@class,'workout-title')]/a")
    reallinks = [link.get_attribute("href") for link in workoutLinks]
    return reallinks


def grabLesson(lessonlink, path):
    browser.get(lessonlink)
    time.sleep(5)
    videolink = browser.find_element_by_tag_name(
        "video").get_attribute("currentSrc")
    videotitle = browser.find_element_by_tag_name(
        "h1").get_attribute("innerText").replace(":", "").replace(" ", "_").replace("/", "")
    downloadmp4(videolink, videotitle, path)


def makeDir(dirr):
    try:
        os.makedirs(dirr)
    except OSError:
        pass


def main():
    email = input('Enter Email:')
    password = getpass.getpass(prompt='Enter Password:')
    doLogin(email, password)
    for i in range(len(lines)):
        lessonlinks = collectClasses(lines[i])
        makeDir(paths[i])
        for link in lessonlinks:
            grabLesson(link, paths[i])
    browser.quit()
    print("++ All downloads completed successfully, have fun! ++")


main()
