'''
HackNC-2016: main.py
Automation script setup for RPi:
Requires 'pwnie express' libraries.
'''
import subprocess

print("Select a task to perform:\n")
print("Task | Description\n")

task = input("> ")

if task == 'task1':
   subprocess.call("./task1.sh", shell = True)
elif task == 'task2':
   subprocess.call("./task1.sh", shell = True)
elif task == 'task3':
   subprocess.call("./task3.sh", shell = True)

# Rinse and repeat to add more tasks.
#NOTE: Make sure to keep the bash scripts in the same directory.
