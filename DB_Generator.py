import random
import time
import colorama
import os 
import sys
from colorama import Fore 
from colorama import init 

os.system('title made by exemaster')
time.sleep(1)

file = open ("DB.txt", "w", encoding="utf-8")

print(Fore.YELLOW)



print('''


     //    ) ) //   ) ) 
    //    / / //___/ /  
   //    / / / __  (    
  //    / / //    ) )   
 //____/ / //____/ /    
                                                        
                                                        
     //   ) )                                            
    //         ___       __      ___      __      ___    
   //  ____  //___) ) //   ) ) //___) ) //  ) ) //   ) ) 
  //    / / //       //   / / //       //      //   / /  
 ((____/ / ((____   //   / / ((____   //      ((___( (   
                         
                         
                         
  __  ___  ___      __    
   / /   //   ) ) //  ) ) 
  / /   //   / / //       
 / /   ((___/ / //        

 '''

 )

print('press Enter')
input()

print(Fore.GREEN)
print('загрузка')
print('-')
time.sleep(1)
os.system('CLS')
print('----')
time.sleep(1)
os.system('CLS')
print('--------')
time.sleep(1)
os.system('CLS')
print('------------')
time.sleep(1)
os.system('CLS')
print('------------------')
time.sleep(1)
os.system('CLS')
print('---------------------')
time.sleep(1)
os.system('CLS')
print('--------------------------')
time.sleep(1)
os.system('CLS')
print('готово!')
time.sleep(1)
os.system('CLS')

print(Fore.BLUE)

answer = input("хотите ли вы использовать шаблон?:yes/no:")

def gen_var_1():
    pet = input('pet:')
    year = input('year:')
    name = input('name:')
    country = input('country:')
    sport = input('sport:')
    friend = input('friend:')
    phone_num  = input('prhone num:')
    lis = [pet ,year ,name ,country ,sport ,friend ,phone_num ]
    ammount = int(input('количество паролей:'))
    lenght = int(input('длина паролей:'))
    print(lis)

    for x in range( ammount ):
	    password = ''

	    for i in range( lenght ):
	        password += random.choice(lis)

	    print(password)

	    file.write(  password + '\n')
    print(Fore.RED)
    print('Дело сделано! Нажмите enter!')

def gen_var_2():
    print("Для создания брут листа впишыте все данные через ; после каждого слова")
    time.sleep(1)
    print("например(flipper;jhon;jacket)")
    time.sleep(1)
    list_one = input("Ввод:")
    lis = list_one.split(";")
    print(lis)
    ammount = int(input('количество паролей:'))
    lenght = int(input('длина паролей:'))
    for x in range( ammount ):
        password = ''
    
        for i in range( lenght ):
            password += random.choice(lis)
    
        print(password)
    
        file.write(  password + '\n')
    print(Fore.RED)
    print('Дело сделано! Нажмите enter!')
       

if answer ==("yes"):
    gen_var_1() 
      
elif answer ==("no"):
    gen_var_2()

else:
    print("ошибка , неизвестная комманда!")

input()



