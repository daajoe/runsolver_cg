import time
def send_list(line):
    myList.append(line)

myList=[]
i=0

while i < 1000:
    f=open("input.txt")
    i+=1
    time.sleep(2)
    for line in f:
        send_list(line)
    f.close()
