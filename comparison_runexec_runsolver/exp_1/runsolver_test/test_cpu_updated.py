import multiprocessing
import time

start=time.perf_counter()

def do_something():
    global i
    while True:
        i+=1
i=0
processes=[]

for _ in range(3):
    p=multiprocessing.Process(target=do_something)
    p.start()
    processes.append(p)

for process in processes:
    process.join()


finish=time.perf_counter()

print(f'Finished in {round(finish-start,2)} second(s)') #will not print if tool limits at 1 hour
