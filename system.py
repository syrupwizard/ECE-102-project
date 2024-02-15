#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 14:31:38 2024

@author: Austin, Cece, and Chris
"""
import json
import os
###Define dictionaries to hold individual components and their state
door_state = {"door1": False, "door2": False, "door3": False, "door4": False} #true->open false->closed

light_state = {"light1": False, "light2": False, "light3": False, "light4": False}

alarm_state = {"alarm": False, "passcode": "0451"} #true -> armed
###File names of dictionaries
DOOR_STATE_FILE = "door_state.json"
LIGHT_STATE_FILE = "light_state.json"
ALARM_STATE_FILE = "alarm_state.json"

###HELP
def help_function(user_string):
    if user_string == "help":
        print("Instructions: \n"
              "To open/close door type 'open door#' or 'close door#' for example 'open door1' will open door 1\n\n"
              "To check if sensors are on type 'check sensors' (sensors are based on door state and are manipulated by opening and closing door\n\n"
              "To turn light on type 'turn on light#', to turn off type 'turn off light#'. For example typing 'turn on light3 will turn on light 3\n\n"
              "To check lights type 'check lights'\n"
              "To arm alarm type 'arm ****', to disarm alarm type 'disarm ****' \n\n"
              "To change passcode type 'change passcode + pass#'. \nFor example if passcode is 0000 type 'change passcode 0000'. Then type in new passcode.\n\n"
                "To exit program type 'exit'\n\n")
###INPUT
def get_line(prompt):
    user_string = str(input(prompt))
    return user_string

#light_state["light1"]

###LOAD
def load_file():    
    # Load door state
    if os.path.exists(DOOR_STATE_FILE):
        with open(DOOR_STATE_FILE, 'r') as file:
            door_state = json.load(file)
    
    # Load light state
    if os.path.exists(LIGHT_STATE_FILE):
        with open(LIGHT_STATE_FILE, 'r') as file:
            light_state = json.load(file)
    
    # Load alarm state
    if os.path.exists(ALARM_STATE_FILE):
        with open(ALARM_STATE_FILE, 'r') as file:
            alarm_state = json.load(file)
    
    print("Data loaded successfully.")

def save_file():
    # Save door state
    with open(DOOR_STATE_FILE, 'w') as file:
        json.dump(door_state, file, indent=4)
    
    # Save light state
    with open(LIGHT_STATE_FILE, 'w') as file:
        json.dump(light_state, file, indent=4)
    
    # Save alarm state
    with open(ALARM_STATE_FILE, 'w') as file:
        json.dump(alarm_state, file, indent=4)
    
    print("Data saved successfully.")


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
        
        print("...An alarm is suddenly triggered. What will you do?!")
        while user_string != alarm_state['passcode']:
            print("WEE WOO WEE WOO")
            print("A red light is flashing above the door.")
            print("WEE WOO WEE WOO")
            
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
    if user_string == "check sensors":
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
            print(f"{key} is on.")
            
        elif "turn off" in user_string and key in user_string:
            light_state[key] = False
            print(f"{key} is off.")            

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

