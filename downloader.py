import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time

# set absolute paths and variables according to your OS
# LINKFILE = "/your/unix/path/downloadlinks.txt"
LINKFILE = r"C:\Users\USERNAME\Documents\aloscraper\downloadlinks.txt"
# BASEPATH = "/your/unix/path/content"
BASEPATH = r"C:\Users\USERNAME\Documents\aloscraper"
WINDOWS = True

# read config and prepare data
paths = []
lines = []
with open(LINKFILE) as f:
    lines = [line.rstrip() for line in f]
for line in lines:
    paths.append(BASEPATH +
                 line.split("series")[1].split("workouts")[0])
if WINDOWS:
    for path in paths:
        path.replace("/", "\\")


# download mp4 with urllib


def downloadmp4(url, filename, path):
    print("Downloading: " + filename)
    urllib.request.urlretrieve(
        url, path + filename + ".mp4")


# initialize webdriver and do a manual login
browser = webdriver.Chrome()
browser.get(
    "https://www.alomoves.com/signin")
time.sleep(25)

# run the download routine for all courses
for i in range(len(lines)):

    # grab all video links by searching the divs
    browser.get(lines[i])
    workoutLinks = browser.find_elements_by_xpath(
        "//div[contains(@class,'workout-title')]/a")
    reallinks = [link.get_attribute("href") for link in workoutLinks]

    # create directory for the course
    try:
        os.makedirs(paths[i])
    except OSError:
        pass

    # call download routine for every available link
    print("== Starting Course: " + paths[i] + " ==")
    for link in reallinks:
        browser.get(link)
        time.sleep(10)
        videolink = browser.find_element_by_tag_name(
            "video").get_attribute("currentSrc")
        videotitle = browser.find_element_by_tag_name(
            "h1").get_attribute("innerText").replace(":", "").replace(" ", "_").replace("/", "")
        downloadmp4(videolink, videotitle, paths[i])
browser.quit()
print("++ All downloads completed successfully, have fun! ++")
