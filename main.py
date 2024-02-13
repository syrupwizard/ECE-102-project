#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 13:55:03 2024

@author: austin
"""

"""Initialization:
Initialize the sensor_states dictionary with keys representing each intrusion sensor (door1, door2, door3, door4) and set their initial state to False (not triggered).
Initialize the light_states dictionary with keys representing each room (room1, room2, room3, room4) and set their initial state to False (lights off).
Initialize the alarm_status dictionary with keys "armed" and "passcode", setting the initial alarm state to False (disarmed) and the passcode to "0451".
Define the state_file variable indicating the path to the file for saving and loading the state.
"""
import system as sys #file containing

def menu():
   prompt = "Enter a command: "
   user_string = sys.get_line(prompt)
   
   while user_string != "exit":
       sys.arm_disarm(user_string)#operate alarm
       sys.open_close(user_string)#operate doors
       
       
       print("States: ")
       print(sys.alarm_state)#testing
       print(sys.door_state)
       #check door state for alarm
       
       

       user_string = sys.get_line(prompt)#get input at end of loop  

menu()



    

















