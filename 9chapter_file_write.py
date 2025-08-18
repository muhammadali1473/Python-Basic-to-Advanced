st = "hlo I am Ali nic to meet you "

f = open("myfile.txt","a")
f.write(st)
f.close()



f = open("myfile.txt")
print(f.read)
f.close()
with open("myfile.txt") as f:
    print(f.read()) 