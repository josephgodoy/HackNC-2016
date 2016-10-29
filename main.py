#'''
#HackNC 2016
#Automation script setup for RPi:
#Requires 'pwnie express' libraries.
#'''
import subprocess
from subprocess import call
import os

print("Select a task to perform:\n")
print("Task | Description\n")

task = raw_input()
script1 = "bash task1.sh"
script2 = "bash task2.sh"
script3 = "bash task3.sh"

if task == 'task1':
   os.system(script1)
elif task == 'task2':
   os.system(script2)
elif task == 'task3':
   os.system(script3)

# Rinse and repeat to add more tasks.
#NOTE: Make sure to keep the bash scripts in the same directory.
