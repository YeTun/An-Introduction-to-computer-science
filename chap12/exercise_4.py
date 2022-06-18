# Me Computer, Mandalay.
# June 23, 2022
# exercise_4.py

from atmmanager import ATMApp, User
from textatm import TextInterface

def main():
    interface = TextInterface()
    app = ATMApp("new_atmusers.json", interface) 

main()
 