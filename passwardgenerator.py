import random
letters = ['a','b','c','d','e','f','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','E','F','I',
           'F','J','K','L','M','O','P','Q','R','S','T','U','V','W','X','Y','Z']
number =[1,2,3,4,5,6,7,8,9,0]
symbol = ['@','#','$','%','^','&','(','}']
print("Welcome to passward generator!!")
x =int(input("how many letters you want in your passward : "))
z =int(input("how many symbols you want in your passward : "))
y =int(input("how many numbers you want in your passward : "))
passward_list = []
for l in range(1,x+1):
    char = random.choice(letters)
    passward_list.append(char)

for s in range(1 ,z+1):
    sym = random.choice(symbol)
    passward_list.append(sym)

for n in range(1 ,y+1):
    num = random.choice(number)
    #passward = passward + str(num)
    passward_list.append(num)
print(passward_list)
random.shuffle(passward_list)
passward = ""
for p in passward_list:
    passward = passward +str(p)
print(passward)