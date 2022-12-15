import os,pip
import random
from random import choice
import traceback
import subprocess,webbrowser
import sys
import time
import names
os.system('cls')

time.sleep(0.5)
feyzo=("""
\33[37m+========================+========================+
|            Coded by: AbdXSlayer                 |
|                      Naz - R               |
|                      oppaje                     |
+========================+========================+
                                                   \33[37m""")
print(feyzo)

time.sleep(0.5)
print ("""

Choose Which Type of Combo You Would Like to Make.

0)User:User Numbered
1)Mail:Pass.
2)User:Pass Names.
3)User:Pass Names Matching.
4)FirstLast:FirstLast
5)Mail.
6)Pass.
7)User.User Matching
8)User.
9)User:Pass Numbers.
10)Mac Combo Generating.
11)foreign:User numbered
12)foriegn:User matching
13)User:Birth year
14)User:Pass:Birth year
15)User:Pass:(2 Num)
16)User:Pass:(4 Num)
17)User:Pass:(123 User)


99)Exit.

""")
menu = input("Enter Option ")      
if menu=="14":
	hwm = int(input("Enter number of combos to generate : "))
	print (" ")
	print ("Enter the name of the file you want to save  ")
	print ("No need to enter the .txt ")
	filename = input("example combos     :  ")
	filename = filename + ".txt"
	print (" ")


	f = open(filename, "w")
	f.write("")
	f.close()
	
	for i in range (0,hwm):
		i = 1+1
		fname = names.get_first_name()
		flastname = names.get_last_name()
		num = random.randint(10,10)
		all1 = "%s%s"%(fname,num)
		alln = "%s%s%s%s"%(all1,":",fname,num)
		all2 = "%s%s"%(flastname,num)
		allf = "%s%s%s%s"%(all2,":",flastname,num)
		all=alln 
		print(i," = ",all)
		f = open(filename, "a")
		f.write(all)
		f.write("\n")
		f.close()
		i += 1
	x = input("\nPress Enter To Exit...")
	
	
if menu=="13":
	hwm = int(input("Enter number of combos to generate : "))
	print (" ")
	print ("Enter the name of the file you want to save  ")
	print ("No need to enter the .txt ")
	filename = input("example combos     :  ")
	filename = filename + ".txt"
	print (" ")


	f = open(filename, "w")
	f.write("")
	f.close()
	
	for i in range (0,hwm):
		i = 1+1
		fname = names.get_first_name()
		flastname = names.get_last_name()
		num = random.randint(1900,2023)
		alln = "%s%s"%(fname,num)
		all=alln 
		print(i," = ",all)
		f = open(filename, "a")
		f.write(all)
		f.write("\n")
		f.close()
		i += 1
	x = input("\nPress Enter To Exit...")
	

if menu=="12":
	hwm = int(input("Enter number of combos to generate : "))
	print (" ")
	print ("Enter the name of the file you want to save  ")
	print ("No need to enter the .txt ")
	filename = input("example combos     :  ")
	filename = filename + ".txt"
	print (" ")


	f = open(filename, "w")
	f.write("")
	f.close()
	
	for i in range (0,hwm):
		i = 1+1
		fname = names.get_first_name()
		flastname = names.get_last_name()
		num = random.randint(000,999)
		all1 = "%s"%(fname)
		alln = "%s%s%s"%(all1,":",fname)
		all2 = "%s"%(flastname)
		allf = "%s%s%s"%(all2,":",flastname)
		all=alln 
		print(i," = ",all)
		f = open(filename, "a")
		f.write(all)
		f.write("\n")
		f.close()
		i += 1
	x = input("\nPress Enter To Exit...")
	

if menu=="15":
	hwm = int(input("Enter number of combos to generate : "))
	print (" ")
	print ("Enter the name of the file you want to save  ")
	print ("No need to enter the .txt ")
	filename = input("example combos     :  ")
	filename = filename + ".txt"
	print (" ")


	f = open(filename, "w")
	f.write("")
	f.close()
	
	for i in range (0,hwm):
		i = 1+1
		fname = names.get_first_name()
		flastname = names.get_last_name()
		num = random.randint(00,99)
		all1 = "%s%s"%(fname,num)
		alln = "%s%s%s%s"%(all1,":",fname,num)
		all2 = "%s%s"%(flastname,num)
		allf = "%s%s%s%s"%(all2,":",flastname,num)
		all=alln 
		print(i," = ",all)
		f = open(filename, "a")
		f.write(all)
		f.write("\n")
		f.close()
		i += 1
	x = input("\nPress Enter To Exit...")
	
if menu=="17":
	hwm = int(input("Enter number of combos to generate : "))
	print (" ")
	print ("Enter the name of the file you want to save  ")
	print ("No need to enter the .txt ")
	filename = input("example combos     :  ")
	filename = filename + ".txt"
	print (" ")


	f = open(filename, "w")
	f.write("")
	f.close()
	
	for i in range (0,hwm):
		i = 1+1
		fname = names.get_first_name()
		flastname = names.get_last_name()
		num = random.randint(123,123)
		all1 = "%s%s"%(fname,num)
		alln = "%s%s%s%s"%(all1,":",fname,num)
		all2 = "%s%s"%(flastname,num)
		allf = "%s%s%s%s"%(all2,":",flastname,num)
		all=alln 
		print(i," = ",all)
		f = open(filename, "a")
		f.write(all)
		f.write("\n")
		f.close()
		i += 1
	x = input("\nPress Enter To Exit...")
	
	
if menu=="16":
	hwm = int(input("Enter number of combos to generate : "))
	print (" ")
	print ("Enter the name of the file you want to save  ")
	print ("No need to enter the .txt ")
	filename = input("example combos     :  ")
	filename = filename + ".txt"
	print (" ")


	f = open(filename, "w")
	f.write("")
	f.close()
	
	for i in range (0,hwm):
		i = 1+1
		fname = names.get_first_name()
		flastname = names.get_last_name()
		num = random.randint(0000,9999)
		all1 = "%s%s"%(fname,num)
		alln = "%s%s%s%s"%(all1,":",fname,num)
		all2 = "%s%s"%(flastname,num)
		allf = "%s%s%s%s"%(all2,":",flastname,num)
		all=alln 
		print(i," = ",all)
		f = open(filename, "a")
		f.write(all)
		f.write("\n")
		f.close()
		i += 1
	x = input("\nPress Enter To Exit...")
	
	
if menu=="11":
	hwm = int(input("Enter number of combos to generate : "))
	print (" ")
	print ("Enter the name of the file you want to save  ")
	print ("No need to enter the .txt ")
	filename = input("example combos     :  ")
	filename = filename + ".txt"
	print (" ")


	f = open(filename, "w")
	f.write("")
	f.close()
	
	for i in range (0,hwm):
		i = 1+1
		fname = names.get_first_name()
		flastname = names.get_last_name()
		num = random.randint(000,999)
		all1 = "%s%s"%(fname,num)
		alln = "%s%s%s%s"%(all1,":",fname,num)
		all2 = "%s%s"%(flastname,num)
		allf = "%s%s%s%s"%(all2,":",flastname,num)
		all=alln 
		print(i," = ",all)
		f = open(filename, "a")
		f.write(all)
		f.write("\n")
		f.close()
		i += 1
	x = input("\nPress Enter To Exit...")
	
	
if menu=="0":
	hwm = int(input("Enter number of combos to generate : "))
	print (" ")
	print ("Enter the name of the file you want to save  ")
	print ("No need to enter the .txt ")
	filename = input("example combos     :  ")
	filename = filename + ".txt"
	print (" ")


	f = open(filename, "w")
	f.write("")
	f.close()
	
	for i in range (0,hwm):
		i = 1+1
		rname = names.get_first_name()
		rlastname = names.get_last_name()
		num = random.randint(3,3)
		all1 = "%s%s"%(rname,num)
		alln = "%s%s%s%s"%(all1,":",rname,num)
		all2 = "%s%s"%(rlastname,num)
		allf = "%s%s%s%s"%(all2,":",rlastname,num)
		all=alln 
		print(i," = ",all)
		f = open(filename, "a")
		f.write(all)
		f.write("\n")
		f.close()
		i += 1
	x = input("\nPress Enter To Exit...")
	
	
if menu=="1":
	#os.system('clear')
	gmail = input("Which Mail Type ? (Ex:@gmail.com): ")
	hwm = int(input("Enter number of combos to generate : "))
	print (" ")
	print ("Enter the name of the file you want to save  ")
	print ("No need to enter the .txt ")
	filename = input("example combos     :  ")
	filename = filename + ".txt"
	print (" ")


	f = open(filename, "w")
	f.write("")
	f.close()

	for i in range (0,hwm):
		i = 1+1
		rname = names.get_first_name()
		rlastname = names.get_last_name()
		num = random.randint(0,2023)
		all1 = "%s%s%s"%(rname,num,gmail)
		alln = "%s%s%s%s"%(all1,":",rname,num)
		all2 = "%s%s%s"%(rlastname,num,gmail)
		allf = "%s%s%s%s"%(all2,":",rlastname,num) 
		all=alln 
		print(i," = ",all)
		f = open(filename, "a")
		f.write(all)
		f.write("\n")
		f.close()
		i += 1
	x = input("\nPress Enter To Exit...")

if menu=="2":
	hwm = int(input("Enter number of combos to generate : "))
	print (" ")
	print ("Enter the name of the file you want to save  ")
	print ("No need to enter the .txt ")
	filename = input("example combos     :  ")
	filename = filename + ".txt"
	print (" ")


	f = open(filename, "w")
	f.write("")
	f.close()

	for i in range (0,hwm):
		i = 1+1
		rname = names.get_first_name()
		rlastname = names.get_last_name()
		num = random.randint(1900,2023)
		all1 = "%s%s"%(rname,num)
		alln = "%s%s%s%s"%(all1,":",rlastname,num)
		all2 = "%s%s"%(rlastname,num)
		allf = "%s%s%s%s"%(all2,":",rname,num) 
		all=alln 
		print(i," = ",all)
		f = open(filename, "a")
		f.write(all)
		f.write("\n")
		f.close()
		i += 1
	x = input("\nPress Enter To Exit...")
	

if menu=="3":
	hwm = int(input("Enter number of combos to generate : "))
	print (" ")
	print ("Enter the name of the file you want to save  ")
	print ("No need to enter the .txt ")
	filename = input("example combos     :  ")
	filename = filename + ".txt"
	print (" ")


	f = open(filename, "w")
	f.write("")
	f.close()
	
	for i in range (0,hwm):
		i = 1+1
		rname = names.get_first_name()
		rlastname = names.get_last_name()
		num = random.randint(0,0)
		all1 = "%s%s"%(rname,num)
		alln = "%s%s%s%s"%(all1,":",rname,num)
		all2 = "%s%s"%(rlastname,num)
		allf = "%s%s%s%s"%(all2,":",rlastname,num)
		all=alln 
		print(i," = ",all)
		f = open(filename, "a")
		f.write(all)
		f.write("\n")
		f.close()
		i += 1
	x = input("\nPress Enter To Exit...")


if menu=="4":
	hwm = int(input("Enter number of combos to generate : "))
	print (" ")
	print ("Enter the name of the file you want to save  ")
	print ("No need to enter the .txt ")
	filename = input("example combos     :  ")
	filename = filename + ".txt"
	print (" ")


	f = open(filename, "w")
	f.write("")
	f.close()

	for i in range (0,hwm):
		i = 1+1
		rname = names.get_first_name()
		rlastname = names.get_last_name()
		#num = random.randint(1900,2020)
		all1 = "%s%s"%(rname,rlastname)
		alln = "%s%s%s%s"%(all1,":",rname,rlastname)
		all2 = "%s%s"%(rname,rlastname)
		allf = "%s%s%s%s"%(all2,":",rname,rlastname) 
		all=(alln)
		print(i," = ",all)
		f = open(filename, "a")
		f.write(all)
		f.write("\n")
		f.close()
		i += 1
	x = input("\nPress Enter To Exit...")


if menu=="5":
	#os.system('clear')
	gmail = input("Which Mail Type ? (Ex:@gmail.com): ")
	hwm = int(input("Enter number of combos to generate : "))
	print (" ")
	print ("Enter the name of the file you want to save  ")
	print ("No need to enter the .txt ")
	filename = input("example combos     :  ")
	filename = filename + ".txt"
	print (" ")


	f = open(filename, "w")
	f.write("")
	f.close()
	
	for i in range (0,hwm):
		i = 1+1
		rname = names.get_first_name()
		rlastname = names.get_last_name()
		num = random.randint(1500,2023)
		all1 = "%s%s%s"%(rname,num,gmail)
		all2 = "%s%s%s"%(rlastname,num,gmail)
		all=all1 
		print(i," = ",all)
		f = open(filename, "a")
		f.write(all)
		f.write("\n")
		f.close()
		i += 1
	x = input("\nPress Enter To Exit...")
	
	
if menu=="6":
	#os.system('clear')
	hwm = int(input("Enter number of combos to generate : "))
	print (" ")
	print ("Enter the name of the file you want to save  ")
	print ("No need to enter the .txt ")
	filename = input("example combos     :  ")
	filename = filename + ".txt"
	print (" ")


	f = open(filename, "w")
	f.write("")
	f.close()
	
	for i in range (0,hwm):
		i = 1+1
		rname = names.get_first_name()
		rlastname = names.get_last_name()
		num = random.randint(0,2023)
		alln = "%s%s"%(rname,num)
		all=alln 
		print(i," = ",all)
		f = open(filename, "a")
		f.write(all)
		f.write("\n")
		f.close()
		i += 1
	x = input("\nPress Enter To Exit...")
	
if menu=="7":
	hwm = int(input("Enter number of combos to generate : "))
	print (" ")
	print ("Enter the name of the file you want to save  ")
	print ("No need to enter the .txt ")
	filename = input("example combos     :  ")
	filename = filename + ".txt"
	print (" ")


	f = open(filename, "w")
	f.write("")
	f.close()
	
	for i in range (0,hwm):
		i = 1+1
		rname = names.get_first_name()
		rlastname = names.get_last_name()
		num = random.randint(000,999)
		all1 = "%s"%(rname)
		alln = "%s%s%s"%(all1,":",rname)
		all2 = "%s"%(rlastname)
		allf = "%s%s%s"%(all2,":",rlastname)
		all=alln 
		print(i," = ",all)
		f = open(filename, "a")
		f.write(all)
		f.write("\n")
		f.close()
		i += 1
	x = input("\nPress Enter To Exit...")


if menu=="8":
	hwm = int(input("Enter number of combos to generate : "))
	print (" ")
	print ("Enter the name of the file you want to save  ")
	print ("No need to enter the .txt ")
	filename = input("example combos     :  ")
	filename = filename + ".txt"
	print (" ")


	f = open(filename, "w")
	f.write("")
	f.close()
	
	for i in range (0,hwm):
		i = 1+1
		rname = names.get_first_name()
		rlastname = names.get_last_name()
		num = random.randint(1900,2023)
		all1 = "%s%s"%(rname,num)
		all2 = "%s%s"%(rlastname,num)
		all=all1 
		print(i," = ",all)
		f = open(filename, "a")
		f.write(all)
		f.write("\n")
		f.close()
		i += 1
	x = input("\nPress Enter To Exit...")

if menu=="10":
	string = '0123456789ABCDEF'
	file = 'MacAddresses.txt'

	def duplicate(path):
	  f = open(path, 'r', errors='ignnore').readlines()
	  old = len(f)
	  new_f = set(f)
	  new = len(new_f)
	  o = open(path, 'w')
	  for line in new_f:
	    o.write(line)
	  print(f"{old - new} duplicate(s) have been removed!")
	  print(f"\nFinished! Results have been saved in {path}")


	def mode1():
	  mac = ''.join(choice(string) for _ in range(6))
	  return f"00:1A:79:{mac[0:2]}:{mac[2:4]}:{mac[4:6]}\n"


	def mode2(custom):
	  list1 = []
	  for letter in custom:
	    if letter == '*':
	      letter = letter.replace('*', ''.join(choice(string)))
	    list1.append(letter)
	  return ''.join(list1) + "\n"


	def generator(mode, custom):
	  with open(file, 'w') as o:
	    for x in range(number):
	      if mode == '1':
	        o.write(mode1())
	      elif mode == '2':
	        o.write(mode2(custom))
	      print(f"Generated: {x + 1} MAC addresses", end='\r')
	  print("\nRemoving duplicates...", end='\r')
	  duplicate(file)


	if __name__ == '__main__':
	  try:
	    print("""
                             __  __    _    ____    ____                           _             
                            |  \/  |  / \  / ___|  / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
                            | |\/| | / _ \| |     | |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
                            | |  | |/ ___ \ |___  | |_| |  __/ | | |  __/ | | (_| | || (_) | |   
                            |_|  |_/_/   \_\____|  \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|  
                            
                                            Coded by: oppaje For NeThinGoez.com
                                      """)
	    mode = input("""Select Mode:
	    1. Default: 00:1A:79:**:**:**
	    2. Custom (Example: 00:1A:79:*8:1B:**)
	    > """)
	    custom = input("Enter custom mode: ") if mode == '2' else None
	    number = int(input("Enter the amount of Macs to generate: "))
	    generator(mode, custom)
	  except:
	    print(traceback.format_exc())
	    print('Something went wrong, please try again. If the same error keeps happening contact oppaje.')
	  input("Press enter to close: ")

if menu=="9":
	c = 	["1","2","3","4","5","6","7","8","9","0","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," "]


print(" ")
print(" ")

# To take input from the user,
n = int(input("Enter number of combos to generate :   "))
print (" ")
print ("Enter the name of the file you want to save  ")
print ("No need to enter the .txt ")
filename = input("example combos     :  ")
filename = filename + ".txt"
print (" ")

# reset filename

f = open(filename, "w")
f.write("")
f.close()

i = 1

while i <= n:
   g1=random.randint(0,9)
   g2=random.randint(0,9)
   g3=random.randint(0,9)
   g4=random.randint(0,9)
   g5=random.randint(0,9)
   g6=random.randint(0,9)
   g7=random.randint(0,9)
   g8=random.randint(0,9)
   g9=random.randint(0,9)
   g10=random.randint(0,9)
   c1 = c[g1]
   c2 = c[g2]
   c3 = c[g3]
   c4 = c[g4]
   c5 = c[g5]
   c6 = c[g6]
   c7 = c[g7]
   c8 = c[g8]
   c9 = c[g9]
   c10 = c[g10]
   user = c1+c2+c3+c4+c5+c6+c7+c8+c9+c10
   g1=random.randint(1,9)
   g2=random.randint(1,9)
   g3=random.randint(1,9)
   g4=random.randint(1,9)
   g5=random.randint(1,9)
   g6=random.randint(1,9)
   g7=random.randint(1,9)
   g8=random.randint(1,9)
   g9=random.randint(1,9)
   g10=random.randint(1,9)
   c1 = c[g1]
   c2 = c[g2]
   c3 = c[g3]
   c4 = c[g4]
   c5 = c[g5]
   c6 = c[g6]
   c7 = c[g7]
   c8 = c[g8]
   c9 = c[g9]
   c10 = c[g10]
   pw = c1+c2+c3+c4+c5+c6+c7+c8+c9+c10
   #user=user+":"+pw
   user=user+":"+user 
   print(i," = ",user)
   f = open(filename, "a")
   f.write(user)
   f.write("\n")
   f.close()
   i += 1
   
   
print (" ")
print (n," COMBOS SAVED TO : ",filename,)
print (" ")
print ("SCRIPT WRITTEN BY <= Naz R =>")
print (" ")
print ("PRESS ENTER TO EXIT")
input()



if menu=="99":
	quit()

	