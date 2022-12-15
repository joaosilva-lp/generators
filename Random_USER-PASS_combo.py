

import random
import subprocess
subprocess.run(["clear", ""])

c = ["1","2","3","4","5","6","7","8","9","0","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," "]

print(" ")
print(" ")

n = int(input("""   \33[1;42m Random Character Generator
\33[1;41m (.txt) file is saved in qpython folder
\33[0m\n\nHow many should be created :   """))
m = int(input("""   \33\n\n[0m\33[1;41m Min:4 Max:10 
\33[0mEnter the combo length :  """))
print (" ")
print (" ")
print ("\t\t\33[1;100m (.txt) yazmayın \33[0m ")
filename = input("\ntype the filename     :  ")
filename = filename + ".txt"
print (" ")

f = open(filename, "w")
f.write("")
f.close()
i = 1

if m==10 :
   while i <= n:
         g1=random.randint(0,61)
         g2=random.randint(0,61)
         g3=random.randint(0,61)
         g4=random.randint(0,61)
         g5=random.randint(0,61)
         g6=random.randint(0,61)
         g7=random.randint(0,61)
         g8=random.randint(0,61)
         g9=random.randint(0,61)
         g10=random.randint(0,61)
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
         g1=random.randint(1,61)
         g2=random.randint(1,61)
         g3=random.randint(1,61)
         g4=random.randint(1,61)
         g5=random.randint(1,61)
         g6=random.randint(1,61)
         g7=random.randint(1,61)
         g8=random.randint(1,61)
         g9=random.randint(1,61)
         g10=random.randint(1,61)
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
         user=user+":"+pw 
         print(i," = ",user)
         f = open(filename, "a")
         f.write(user)
         f.write("\n")
         f.close()
         i += 1
elif m==9 :
   while i <= n:
         g1=random.randint(0,61)
         g2=random.randint(0,61)
         g3=random.randint(0,61)
         g4=random.randint(0,61)
         g5=random.randint(0,61)
         g6=random.randint(0,61)
         g7=random.randint(0,61)
         g8=random.randint(0,61)
         g9=random.randint(0,61)
         c1 = c[g1]
         c2 = c[g2]
         c3 = c[g3]
         c4 = c[g4]
         c5 = c[g5]
         c6 = c[g6]
         c7 = c[g7]
         c8 = c[g8]
         c9 = c[g9]
         user = c1+c2+c3+c4+c5+c6+c7+c8+c9
         g1=random.randint(1,61)
         g2=random.randint(1,61)
         g3=random.randint(1,61)
         g4=random.randint(1,61)
         g5=random.randint(1,61)
         g6=random.randint(1,61)
         g7=random.randint(1,61)
         g8=random.randint(1,61)
         g9=random.randint(1,61)
         c1 = c[g1]
         c2 = c[g2]
         c3 = c[g3]
         c4 = c[g4]
         c5 = c[g5]
         c6 = c[g6]
         c7 = c[g7]
         c8 = c[g8]
         c9 = c[g9]
         pw = c1+c2+c3+c4+c5+c6+c7+c8+c9
         user=user+":"+pw 
         print(i," = ",user)
         f = open(filename, "a")
         f.write(user)
         f.write("\n")
         f.close()
         i += 1
elif m==8 :
   while i <= n:
         g1=random.randint(0,61)
         g2=random.randint(0,61)
         g3=random.randint(0,61)
         g4=random.randint(0,61)
         g5=random.randint(0,61)
         g6=random.randint(0,61)
         g7=random.randint(0,61)
         g8=random.randint(0,61)
         c1 = c[g1]
         c2 = c[g2]
         c3 = c[g3]
         c4 = c[g4]
         c5 = c[g5]
         c6 = c[g6]
         c7 = c[g7]
         c8 = c[g8]
         user = c1+c2+c3+c4+c5+c6+c7+c8
         g1=random.randint(1,61)
         g2=random.randint(1,61)
         g3=random.randint(1,61)
         g4=random.randint(1,61)
         g5=random.randint(1,61)
         g6=random.randint(1,61)
         g7=random.randint(1,61)
         g8=random.randint(1,61)
         c1 = c[g1]
         c2 = c[g2]
         c3 = c[g3]
         c4 = c[g4]
         c5 = c[g5]
         c6 = c[g6]
         c7 = c[g7]
         c8 = c[g8]
         pw = c1+c2+c3+c4+c5+c6+c7+c8
         user=user+":"+pw 
         print(i," = ",user)
         f = open(filename, "a")
         f.write(user)
         f.write("\n")
         f.close()
         i += 1
elif m==7 :
   while i <= n:
         g1=random.randint(0,61)
         g2=random.randint(0,61)
         g3=random.randint(0,61)
         g4=random.randint(0,61)
         g5=random.randint(0,61)
         g6=random.randint(0,61)
         g7=random.randint(0,61)
         c1 = c[g1]
         c2 = c[g2]
         c3 = c[g3]
         c4 = c[g4]
         c5 = c[g5]
         c6 = c[g6]
         c7 = c[g7]
         user = c1+c2+c3+c4+c5+c6+c7
         g1=random.randint(1,61)
         g2=random.randint(1,61)
         g3=random.randint(1,61)
         g4=random.randint(1,61)
         g5=random.randint(1,61)
         g6=random.randint(1,61)
         g7=random.randint(1,61)
         c1 = c[g1]
         c2 = c[g2]
         c3 = c[g3]
         c4 = c[g4]
         c5 = c[g5]
         c6 = c[g6]
         c7 = c[g7]
         pw = c1+c2+c3+c4+c5+c6+c7
         user=user+":"+pw 
         print(i," = ",user)
         f = open(filename, "a")
         f.write(user)
         f.write("\n")
         f.close()
         i += 1

elif m==6 :
   while i <= n:
         g1=random.randint(0,61)
         g2=random.randint(0,61)
         g3=random.randint(0,61)
         g4=random.randint(0,61)
         g5=random.randint(0,61)
         g6=random.randint(0,61)
         c1 = c[g1]
         c2 = c[g2]
         c3 = c[g3]
         c4 = c[g4]
         c5 = c[g5]
         c6 = c[g6]
         user = c1+c2+c3+c4+c5+c6
         g1=random.randint(1,61)
         g2=random.randint(1,61)
         g3=random.randint(1,61)
         g4=random.randint(1,61)
         g5=random.randint(1,61)
         g6=random.randint(1,61)
         c1 = c[g1]
         c2 = c[g2]
         c3 = c[g3]
         c4 = c[g4]
         c5 = c[g5]
         c6 = c[g6]
         pw = c1+c2+c3+c4+c5+c6
         user=user+":"+pw 
         print(i," = ",user)
         f = open(filename, "a")
         f.write(user)
         f.write("\n")
         f.close()
         i += 1
elif m==5 :
   while i <= n:
         g1=random.randint(0,61)
         g2=random.randint(0,61)
         g3=random.randint(0,61)
         g4=random.randint(0,61)
         g5=random.randint(0,61)
         c1 = c[g1]
         c2 = c[g2]
         c3 = c[g3]
         c4 = c[g4]
         c5 = c[g5]
         user = c1+c2+c3+c4+c5
         g1=random.randint(1,61)
         g2=random.randint(1,61)
         g3=random.randint(1,61)
         g4=random.randint(1,61)
         g5=random.randint(1,61)
         c1 = c[g1]
         c2 = c[g2]
         c3 = c[g3]
         c4 = c[g4]
         c5 = c[g5]
         pw = c1+c2+c3+c4+c5
         user=user+":"+pw 
         print(i," = ",user)
         f = open(filename, "a")
         f.write(user)
         f.write("\n")
         f.close()
         i += 1
elif m==4 :
   while i <= n:
         g1=random.randint(0,61)
         g2=random.randint(0,61)
         g3=random.randint(0,61)
         g4=random.randint(0,61)
         c1 = c[g1]
         c2 = c[g2]
         c3 = c[g3]
         c4 = c[g4]
         user = c1+c2+c3+c4
         g1=random.randint(1,61)
         g2=random.randint(1,61)
         g3=random.randint(1,61)
         g4=random.randint(1,61)
         c1 = c[g1]
         c2 = c[g2]
         c3 = c[g3]
         c4 = c[g4]
         pw = c1+c2+c3+c4
         user=user+":"+pw 
         print(i," = ",user)
         f = open(filename, "a")
         f.write(user)
         f.write("\n")
         f.close()
         i += 1

print ("\33[1;37;42m")
print (n," records created successfully : ",filename,)
print ("\33[0m")
print (" 🇧​🇾​ ☛ 🆃🅰️🅿️🅸🅽🅰🅺🅲🅸 ☚")
print (" ")
print (" ")
