#!/usr/bin/env python
#coding: utf8 
import os
from splinter import Browser
from sys import exit
import time

username = raw_input("Nombre de usuario: ")
pswd = raw_input("Contraseña: ")
alias = raw_input("Alias: ")

with Browser('chrome') as browser:
	browser.visit("https://www.corporativo.telcel.com/pcorporativo/login.iface")
	button = browser.find_by_name("j_id22:j_id24").click()
	browser.fill('j_spring_security_check:j_username', username)
	browser.find_by_id('j_password').fill(pswd)
	browser.fill('j_spring_security_check:j_alias', alias)
	btn2 = browser.find_by_name("j_spring_security_check:j_id38").click()
	time.sleep(5)
  btn3 = browser.find_by_name("corporativo:menu:0.1").click()
  btn4 = browser.find_by_id("corporativo:menu:0:menuBar:adendum:link").click()
  num = 0
  while True:
         if browser.is_element_present_by_id("corporativo:menu:0:tree:n-" + str(num) + ":j_id65"):
             btn5 = browser.find_by_id("corporativo:menu:0:tree:n-" + str(num) + ":j_id65").click()
             tn6 = browser.find_by_name("corporativo:menu:0:j_id1254").click()
             time.sleep(10)
             if browser.is_element_not_present_by_id("corporativo:menu:0:j_id1257"):
                  print "Se hizo el proceso1"
                  print num
                  num += 1
             else:
                  btn7 = browser.find_by_id("corporativo:menu:0:j_id1257").click()
                  print "Se hizo el proceso2"
                  print num
                  time.sleep(10)
                  num += 1
         else:
              exit(0)
