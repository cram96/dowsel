import time
import pyautogui
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
def main():
    user=sys.argv[1]
    pwd=sys.argv[2]

    driver=webdriver.Chrome()
    driver.get("http://intranet.ceu.es")

    elem=driver.find_element_by_id("ctl00_PlaceHolderMain_UserName")
    elem.send_keys(user)
    elem=driver.find_element_by_id("ctl00_PlaceHolderMain_Password")
    elem.send_keys(pwd)
    elem.send_keys(Keys.RETURN)
    elem=driver.find_element_by_xpath('//*[@id="ctl00_ctl44_g_0153459f_8a2e_4df3_80be_ce7bdcc2242e_csr"]/section/div/article[3]/a/div[1]/i')
    elem.click()
    time.sleep(2)
    elem=driver.find_element_by_css_selector('#_3_1termCourses_noterm > ul > li:nth-child(5) > a')
    elem.click()
    time.sleep(1)
    elem=driver.find_element_by_xpath('//*[@id="paletteItem:_1094553_1"]/a')
    elem.click()
    time.sleep(3)
    elem=driver.find_element_by_xpath('//*[@id="contentListItem:_670950_1"]/div[2]/div/div[2]/ul/li/a')
    elem.click()
    time.sleep(4)
    tabs = driver.window_handles

    driver.switch_to.window(tabs[1])
    time.sleep(2)
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 's')
    pyautogui.press("ENTER")

    time.sleep(10)
main()




