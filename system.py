#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 14:31:38 2024

@author: austin
"""
###Define dictionaries to hold individual compnents and their state
door_state = {"door1": False, "door2": False, "door3": False, "door4": False} #true->open false->closed

light_state = {"light1": False, "light2": False, "light3": False, "light4": False}

alarm_state = {"alarm": False, "passcode": "0451"} #true -> armed

###HELP
def help_function(user_string):
    if user_string == "help":
        print("Instructions: To open/close door type 'open door#' or 'close door#' for example 'open door1' will open door 1\n"
              "To check if sensors are on type 'check sensor'\n"
              "To turn light on type 'turn on light#', to turn off type 'turn off light#'. For example typing 'turn on light3 will turn on light 3\n"
              "To check lights type 'check lights'\n"
              "To arm alarm type 'arm ****', to disarm alarm type 'disarm ****' \n"
              "To turn off type 'exit'"
              "To change passcode type 'change passcode + pass#'. For example if passcode is 0000 type 'change passcode 0000'. Then type in new passcode.")

def get_line(prompt):
    user_string = str(input(prompt))
    return user_string

#light_state["light1"]


###ALARM
###check code and arm/disarm based on code correctness and state
def arm_disarm(user_string):
    if user_string == f"arm {alarm_state['passcode']}":
        alarm_state["alarm"] = True
        print("alarm armed")
    
    elif user_string == f"disarm {alarm_state['passcode']}":            
        alarm_state["alarm"] = False
        print("alarm disarmed")
    return alarm_state

def trigger_alarm(user_string):
    
    if (door_state["door1"] or door_state["door2"] or door_state["door3"]
        or door_state["door4"]) == True and alarm_state["alarm"] == True:
        
        print("ALARM")
        while user_string != "0451":
            print("ALARM is sounding! ")
            print("A red light is flashing above the door ")
            print("WEE WOO WEE WOO")
            print("ALARM!")
            print("WEE WOO\n" 
                  "WEE WOO\n")
            
            user_string = get_line("Enter alarm code: ")
        print("alarm disarmed")
        alarm_state["alarm"] = False

def change_stuff(user_string):
    if user_string == f"change passcode {alarm_state['passcode']}":#might not work
        temp_code = input("Enter a new passcode: ")
        
        alarm_state["passcode"] = temp_code
        print("alarm passcode has been changed")
    return alarm_state

###DOORS
def open_close(user_string):  
    for key in door_state:
        
        if "open" in user_string and key in user_string:
            door_state[key] = True
            print(f"{key} has been opened.")
            
            
        elif "close" in user_string and key in user_string:
            door_state[key] = False
            print(f"{key} has been closed.")

def check_sensor(user_string):
    if user_string == "check sensor":
        if door_state["door1"] == True:
            print("Sensor 1 is on")
        else:
            print("Sensor 1 is off")

        if door_state["door2"] == True:
            print("Sensor 2 is on")
        else:
             print("Sensor 2 is off")

        if door_state["door3"] == True:
            print("Sensor 3 is on")
        else:
            print("Sensor 3 is off")

        if door_state["door4"] == True:
            print("Sensor 4 is on")
        else:
            print("Sensor 4 is off")
        
###LIGHTS
def activate_lights(user_string):
    for key in light_state:
        if "turn on" in user_string and key in user_string:
            light_state[key] = True
            print(f"{key} light is on.")
            
        elif "turn off" in user_string and key in user_string:
            light_state[key] = False
            print(f"{key} light is off.")            

def check_lights(user_string):
    if user_string == "check lights":
        if light_state["light1"] == True:
            print("light 1 is on")
        else: 
            print("light 1 is off")
        if light_state["light2"] == True:
            print ("light 2 is on")
        else: 
            print("light 2 is off")
        if light_state["light3"] == True:
            print("light 3 is on")
        else: 
            print("light 3 is off")
        if light_state["light4"] == True:
            print("light 1 is on")
        else: 
            print("light 4 is off")        



        
        """
        #CECE
□ help command prints instructions for terminal
X exit command closes python script cleanly
X Able to check state of sensors

□ Able to trigger individual sensors
□ Triggering sensor activates alarm (only when armed)
□ Able to check state of lights
□ Able to turn lights off/on
□ Able to check if alarm is armed
□ Able to arm alarm with the passcode 0451
        
        
        """

