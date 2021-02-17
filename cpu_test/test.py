import time
i=0
t0=time.time()
while i<1000:
    f=open("100MB.bin","rb")
    x=f.read()
    f.close()
    i+=1

print ("WC:",time.time()-t0)
print("CPU:",time.process_time())
