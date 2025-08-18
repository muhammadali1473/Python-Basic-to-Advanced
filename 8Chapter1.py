'''
a = 12
b = 45
c = 56

average = (a + b + c)/3
print(average)

'''
'''
#Function
def avg():
    a = int(input("Entrer your first Name:"))
    b= int(input("Entrer your second Name:"))
    c = int(input("Entrer your third Name:"))
    d = int(input("Entrer your ffour Name:"))
    
    average =(a+ b + c)/3
    print(average)
    
avg()
'''
'''
def goodday(name, ending):
    print("Ali,"+name)
    print(ending)
    return "Done"

a = goodday("Muhammad: ","thank you")
print(a)
'''
#defasult argument 
'''
def goodday(name, ending = "thank you"):
  print(f"Good day, {name}")
  print(ending )

goodday("harry")
'''
def Goodboy(name,ending = "thankx Ali"):
    print(f" i am  good,{name}")
    print(ending)

Goodboy("Muhammad Ali","Thanks")
Goodboy("Asim")
