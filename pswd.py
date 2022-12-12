import random
# colors
yellow='\033[93m'
gren='\033[92m'
cyan='\033[96m'
pink='\033[95m'
red='\033[91m'
b='\033[1m'
# code
print (red+b+"""

İNSTAGRAM İÇİN ŞİFRE OLUŞTURUCU

                                                   v 1.0
"""+b+red)

print (gren+b+"              <===[[ coded by GHOST ]]===>"+b+gren)
print (" ")
print (yellow+b+"        <---( GİT-HUB https://github.com/Team0x02/ )--->"+b+yellow)
print (" ")

length=int(input(cyan+b+"Parola Uzunluğunu Girin: "+b+cyan))
print (" ")
print (yellow+b+"-----> şifre oluşturuldu <----"+b+yellow)
print (" ")
char="abcdefghijklmnopqrstuvwxyz1234567890@#$%&*^"
password= (gren+b+" "+b+gren)
for i in range(length):

     password+=random.choice(char)

print(password)
print (" ")
print (yellow+b+"-----> şifreni al <----"+b+yellow)
print (" ")
