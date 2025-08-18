f = open("poetm.txt")
content = f.read()
if("hlo "in content):
    print("The hlo word is presnt in ")
else:
    print("the hlo world is not presnt in this sentence ")

f.close()
