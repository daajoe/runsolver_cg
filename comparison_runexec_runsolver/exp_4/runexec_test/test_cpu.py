import multiprocessing
import time

def do_something():
    global i
    while i<4500:
        f=open("100MB.bin","rb")
        while True: 
            line=f.readline()
            if not line:
                break
        f.close()
        i+=1
        print(i)


i=0
t0=time.time()
processes=[]

for _ in range(4):
    p=multiprocessing.Process(target=do_something)
    p.start()
    processes.append(p)

for process in processes:
    process.join()

#print ("WC:",time.time()-t0)
#print("CPU:",time.process_time())
