import multiprocessing

def do_something():
    global i
    while True:
        i+=1
        if i == 500000:
            print(i,"iterations have been reached")
        elif i == 5000000:
            print(i,"iterations have been reached")
i=0
processes=[]

for _ in range(8):
    p=multiprocessing.Process(target=do_something)
    p.start()
    processes.append(p)

for process in processes:
    process.join()


