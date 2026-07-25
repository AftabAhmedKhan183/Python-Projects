# File Management System --> CRUD Operations
from pathlib import Path
import os

#This function lists all the files that are present in your folder
def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))

    for i,items in enumerate(items):
        print(f"{i+1} : {items}")


#Function to create a file
def createfile():
    try:
        readfileandfolder()
        name = input("Enter the name of the file that you want to create: ")
        p = Path(name)

        if not p.exists():
            with open(p,'w') as fs:
                data = input("Any data that you want to write into your file : ")
                fs.write(data)
            print("FILE CREATED SUCCESSFULLY!!")
        else:
            print("Requested file already exists !!")
    except Exception as err:
        print(f"An error occured as {err}")


#Function to read a file
def readfile():
    try:
        readfileandfolder()
        name = input("Enter the name of the file that you want to read: ")
        p = Path(name)

        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data = fs.read()
                print("FILE CONTENT: ")
                print(data)
        else:
            print("Requested file does not exist!!")

    except Exception as err:
        print(f"An error occured as {err}")


#Function to update a file
def updatefile():
    try:
        readfileandfolder()
        name = input("Enter the name of the file which you want to update: ")
        print("")
        p = Path(name)

        if p.exists() and p.is_file():
            print("UPDATION CHOICES:")
            print("Press 1 for Updating the file name")
            print("Press 2 for Overwriting the file content")
            print("Press 3 for Appending some data into the file")

            updatechoice = int(input("Enter the updation choice:"))

            if updatechoice==1:
                newName = input("Enter the new name to update the filename : ")
                p2 = Path(newName)
                p.rename(p2)

            if updatechoice==2:
                with open(p,'w') as fs:
                    data = input("Enter the data which will be overwriting the previous data : ")
                    fs.write(data)

            if updatechoice==3:
                with open(p,'a') as fs:
                    data = input("Enter the content that you want to append : ")
                    fs.write(" " + data)

        else:
            print("Requested file does not exist!!")

    except Exception as err:
        print(f"An error occured as {err}")


#Function to delete a file
def deletefile():
    try:
        readfileandfolder()
        name = input("Enter the name of the file that you want to delete: ")
        p = Path(name)

        if p.exists() and p.is_file():
            os.remove(p)
        else:
            print("Requested file does not exist !!")

    except Exception as err:
        print(f"An error occured as {err}")

print("Welcome to the Terminal:")
print("Press 1 for Creating a file:")
print("Press 2 for Reading a file:")
print("Press 3 for Updating a file:")
print("Press 4 for Deleting a file:")

#Input the choices out of four
choice = int(input("Tell me your response:"))

if choice==1:
    createfile()

if choice==2:
    readfile()

if choice==3:
    updatefile()

if choice==4:
    deletefile()