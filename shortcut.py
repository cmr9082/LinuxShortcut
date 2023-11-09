#!/bin/python3
#Caleb Roberts
#6/30/2023
import subprocess as sp
import os
import sys

home = str(sp.check_output('echo $HOME', shell=True))
home = home[2:(len(home)-3)]

#Initial Menu Setup
def showMenu() :
 sp.run('clear', shell=True)
 curDir = str(sp.check_output('echo $PWD', shell=True))
 curDir = curDir[2:(len(curDir)-3)]
 print("\n")
 print("************************************")
 print("********* \033[32mShortcut Creator\033[0m *********")
 print("************************************")
 print("\n")
 print("Current Directory: " +curDir)
 print("Enter Selection:")
 print("\n")
 print("       1 - Create a shortcut in your home directory")
 print("       2 - Remove a shortcut from your home directory.")
 print("       3 - Run shortcut report.")
 print("\n")

#Creating a Shortcut
def showCase1():
 fileName = input ("Please enter the file name to create a shortcut: ")
 find = ["sudo","find","/","-name",fileName]
 temp = sp.Popen(find, stderr=sp.PIPE,stdout=sp.PIPE).communicate()[0]
 filePath = temp.decode()
 temp2 = os.path.basename(filePath)
 if(len(filePath)>1):
  if(input("\nFound \33[92m"+fileName+"\33[0m! Select Y/y to create shortcut: ").upper() == "Y"):
   sp.run('ln -s '+temp2+' '+home+"/"+fileName+" 2>/dev/null", shell=True)
   print("Shortcut Created. Please Return to Main Menu")
 else:
  print("\nCould Not Find \33[92m"+fileName+"\33[0m")
  print("Please Return to Main Menu")
 
#Removing a Shortcut
def showCase2():
 fileName = input("Please enter the shortcut/link to remove: ")
 os.chdir(home)
 path = home+"/"+fileName
 if os.path.islink(path):
  if(input("\nAre you sure you want to remove \33[92m"+fileName+"\33[0m! Select Y/y to confirm: ").upper() == "Y"):
   sp.run('rm '+fileName, shell=True)
   print("Shortcut Removed. Please Return to Main Menu")
 else:
    print("\nIt seems a shortcut for \33[92m"+fileName+"\33[0m does not exist")
    print("Please Return to Main Menu")

#Shortcut Report
def showCase3():
 sp.run('clear', shell=True)
 os.chdir(home)
 shortCutNum = 0
 homeFiles=os.listdir(home)
 for i in homeFiles:
  if os.path.islink(i):
   shortCutNum = shortCutNum + 1
 print("\n")
 print("***********************************")
 print("********* \033[32mShortcut Report\033[0m *********")
 print("***********************************")
 print("\n")
 print("Your current directory is \33[33m"+home+"\33[0m")
 print("\n")
 print("The number of shorcut links is \33[33m"+str(shortCutNum)+"\33[0m\n")
 print("\33[33mSymbolic Link \t\t Target Path\33[0m")
 for i in homeFiles:
  if os.path.islink(i):
   print (i+"\t\t"+os.readlink(i))
 resp = input("\nTo return to the \33[33mMain Menu\33[0m, press \33[33mEnter\33[0m. Or select \33[33mR/r\33[0m to remove a link.").lower()
 if(resp == "r"):
  showCase2()

 

#Main - combines them all together
while True:
 showMenu()
 res = input('Please enter a number \033[32m1-4\033[0m or press "\033[31mQ/q/quit\033[0m" to quit the program. ').lower()
 if(res == 'q' or res =='quit'):
  break
 if(res == str(1)):
  sp.run('clear', shell=True)
  showCase1()
  input()
  continue
 if(res == str(2)):
  sp.run('clear', shell=True)
  showCase2()
  input()
  continue
 if(res == str(3)):
  sp.run('clear', shell=True)
  showCase3()
  input()
  continue
 else:
  print("Error: \033[31mInvalid Input\033[0m")
  input()
print("Exiting...")
