# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.select import  Select
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

bs=webdriver.Firefox()

bs.get("http://192.168.0.1")
bs.find_element_by_id("login_pwd").send_keys("12345678")
bs.find_element_by_class_name("btn_login").click()
try:
    sleep(2)
    bs.find_element_by_id("nav_addon_b").click()
    sleep(3)
    bs.find_element_by_xpath("//div[@id='tab_wrapper']/div[2]/h3").click()
    sleep(1)
    bs.find_element_by_xpath("//div[@id='policy_routing']/div[2]").click()
    bs.implicitly_wait(3)
    for i in range(2,8):
        sleep(2)
        # 切换到内嵌frame才能够定位id和name
        bs.switch_to.frame("config_page")
        # bs.find_element_by_id("check_prio").send_keys(str(i))
        bs.find_element_by_id("routing_id").send_keys("item_"+str(i))
        s_lan=Select(bs.find_element_by_id("clrouting_lan_mode"))
        s_lan.select_by_value("sub_host")
        bs.find_element_by_id("clrouting_set_filter_ip").send_keys("192.168.0."+str(i))
        bs.find_element_by_id("clrouting_set_filter_mask").send_keys("255.255.255.255")
        s_wan=Select(bs.find_element_by_id("clrouting_wan_mode"))
        s_wan.select_by_value("sub_host")
        bs.find_element_by_id("clrouting_set_filter_ip_wan").send_keys("10.10.10." + str(i))
        bs.find_element_by_id("clrouting_set_filter_mask_wan").send_keys("255.255.255.255")
        bs.find_element_by_id("ifdev1").click()
        bs.find_element_by_id("save_button").click()
        # 切换回主界面
        bs.switch_to.default_content()
        WebDriverWait(bs,10).until(EC.visibility_of_element_located((By.CLASS_NAME,"success")))
        print bs.find_element_by_id('msg').text
        sleep(3)
        bs.switch_to.frame("config_page")
        # bs.find_element_by_id("check_prio").send_keys(str(i))
        bs.find_element_by_id("routing_id").send_keys("item_1_"+str(i))
        s_lan=Select(bs.find_element_by_id("clrouting_lan_mode"))
        s_lan.select_by_value("sub_host")
        bs.find_element_by_id("clrouting_set_filter_ip").send_keys("192.168.0."+str(i))
        bs.find_element_by_id("clrouting_set_filter_mask").send_keys("255.255.255.255")
        s_wan=Select(bs.find_element_by_id("clrouting_wan_mode"))
        s_wan.select_by_value("sub_host")
        bs.find_element_by_id("clrouting_set_filter_ip_wan").send_keys("10.10.111." + str(i))
        bs.find_element_by_id("clrouting_set_filter_mask_wan").send_keys("255.255.255.255")
        bs.find_element_by_id("ifdev0").click()
        bs.find_element_by_id("save_button").click()
        bs.switch_to.default_content()
        WebDriverWait(bs,10).until(EC.visibility_of_element_located((By.CLASS_NAME,"success")))
        print bs.find_element_by_id('msg').text
        sleep(3)

finally:
    bs.close()
    print "close Firefox!"