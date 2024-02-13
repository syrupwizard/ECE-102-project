#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 14:31:38 2024

@author: austin
"""
###Define dictionaries to hold individual compnents and their state
door_state = {"door1": False, "door2": False, "door3": False, "door4": False} #true->open false->closed
light_state = {"light1": False, "light2": False, "light3": False, "light4": False}
alarm_state = {"alarm": False, "passcode": "0451"}

def get_line(prompt):
    user_string = str(input(prompt))
    return user_string



###check code and arm/disarm based on code correctness and state
def arm_disarm(user_string):
    if user_string == "arm 0451":
        alarm_state["alarm"] = True
        print("alarm armed")
    
    elif user_string == "disarm 0451":            
        alarm_state["alarm"] = False
        print("alarm disarmed")
    return alarm_state

def open_close(user_string):  
    for key in door_state:
        if "open" in user_string and key in user_string:
            door_state[key] = True
            print(f"{key} has been opened.")
        elif "close" in user_string and key in user_string:
            door_state[key] = False
            print(f"{key} has been closed.")
        
        
def trigger_alarm(user_string):
    if door_state == True and alarm_state == True:
        while user_string != "0451":
            print("ALARM!")
            print("WEE WOO WEE WOO")
            print("ALARM!")
            print("WEE WOO WEE WOO")
            get_line("Enter alarm code: ")
            
            
            
        
        

