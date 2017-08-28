import os
#import win32print 
import sys
from Bill import *

def CreateItemFromUserInput():
    correct = False
    while correct is False:
        name = input("Enter name of the item you wish to add to the bill: ")
        price = float(input("Enter the per unit price of the item: "))
        quantity = int(input("Enter the quantity of this item: "))
        newItem = BillItem(name,price,quantity)
        correct = (input("Is this correct?(y/n)\n{}\n".format(newItem)) == "y")
    return(newItem)
    
def Add():
    item = CreateItemFromUserInput()
    bill.Add(item)

def Remove():
    if(len(bill) > 0):
        pos = int(input("Enter the position of the item you wish to remove: "))
        bill.Remove(pos)
    else:
        print("No items to remove")

#def Export():

def Print():
    p = win32print.OpenPrinter(printer_name)
    job = win32print.StartDocPrinter(p, 1, ("test of raw data", None, "RAW")) 
    
    win32print.StartPagePrinter(p) 
    win32print.WritePrinter(p, "data to print") 
    win32print.EndPagePrinter(p)

def View():
    print(bill)

def Help():
    keys = sorted(commands.keys())
    #print(keys)
    for key in keys:
        print('{} {:>10}\n'.format(key,commands[key]["help"]))
        
def Invalid():
    print("Command was invalid")
    
commands = {
    'a' : {"method":Add,"help":"Add an item to the bill"},
    'r' : {"method":Remove,"help":"Remove an item from the bill"},
#    'e' : Export,
#    'p' : Print,
    'v' : {"method":View,"help":"Displays the bill"},
    'h' : {"method":Help,"help":"Displays list of commands"}
}

def ProcessCommand(cmd):
    #action = .get(cmd,Invalid)()
    if(cmd in commands):
        commands[cmd]["method"]()
    else:
        Invalid()
        
customerName = input("Enter the name of the customer: ")
bill = Bill(customerName)

run = True
#Add()

while run is True:
    cmd = input("Enter Command: ")
    if(cmd != "x"):
        ProcessCommand(cmd)
        #print(bill)
    else:
        run = False
