import multiprocessing

def do_something():
    global i
    while True:
        i+=1
i=0
processes=[]

for _ in range(4):
    p=multiprocessing.Process(target=do_something)
    p.start()
    processes.append(p)

for process in processes:
    process.join()


