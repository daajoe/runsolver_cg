import multiprocessing
import time

#start=time.perf_counter()

i=0

def do_something(seconds):
    while i<1000:
        f=open("100MB.bin","rb")
        x=f.read()
        f.close()
        i+=1

processes=[]

for _ in range(2):
    p=multiprocessing.Process(target=do_something, args=[1.5])
    p.start()
    processes.append(p)

for process in processes:
    process.join()


#do_something()
#do_something()

f#inish=time.perf_counter()

#print(f'Finished in {round(finish-start,2)} second(s)')
