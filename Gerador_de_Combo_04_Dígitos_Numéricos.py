

import random
import subprocess
subprocess.run(["clear", ""])


c = ["1","2","3","4","5","6","7","8","9","0","9","8","7","6","5","4","3","2","1"]

print(" ")
print(" ")


n = int(input("""   \33[0m\33[1;41m Gerador de Combo 04 Dígitos Numéricos! 
\33[0m\n\nDigite a Quantidade que deseja: """))
print (" ")
print (" ")
print ("\t\t\33[1;100m Não coloque (.txt) \33[0m ")
filename = input("\nDê um Nome ao Combo: ")
filename = filename + ".txt"
print (" ")



f = open(filename, "w")
f.write("")
f.close()



i = 1

while i <= n:
   g1=random.randint(0,10)
   g2=random.randint(0,10)
   g3=random.randint(0,10)
   g4=random.randint(0,10)
   g5=random.randint(0,10)
   g6=random.randint(0,10)
   g7=random.randint(0,10)
   g8=random.randint(0,10)
   g9=random.randint(0,10)
   g10=random.randint(0,10)
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
   user = c1+c2+c3+c4
   g1=random.randint(1,10)
   g2=random.randint(1,10)
   g3=random.randint(1,10)
   g4=random.randint(1,10)
   g5=random.randint(1,10)
   g6=random.randint(1,10)
   g7=random.randint(1,10)
   g8=random.randint(1,10)
   g9=random.randint(1,10)
   g10=random.randint(1,10)
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
   pw = c1+c2+c3+c4
   user=user+":"+pw 
   print(i," = ",user)
   f = open(filename, "a")
   f.write(user)
   f.write("\n")
   f.close()
   i += 1
   


print ("\33[1;37;42m")
print (n," Arquivo Salvo com sucesso: ",filename,)
print ("\33[0m")
print ("🇬 🇦 🇧 🇷 🇮 🇪 🇱   🇦 🇵 🇰 🇸 ")
print (" ")
print (" ")

