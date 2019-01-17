
with open('name.txt') as f:
    myname = f.read()

greeting = "Hello my name is " + myname + "."

print(greeting)

#write to a file 

with open('hello.txt', 'w') as f:
   f.write(greeting)
   f.write('\n')