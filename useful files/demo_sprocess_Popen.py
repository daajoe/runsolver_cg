
import subprocess

#to read
process = subprocess.Popen(['echo', 'Something random'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
stdout, stderr = process.communicate()
print (stdout.strip('\n'), stderr)

#to take as input
process3 = subprocess.Popen(["cat"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
output, errors = process3.communicate(input="Hello from the other side!")
#process3.wait()
print(output)
#print(errors)

#doing something else while waiting for the process to finish
process1 = subprocess.Popen(['ping', '-c 4', 'python.org'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
while True:
    output = process1.stdout.readline()
    print (output.strip())
    #sth else can be done
    for i in range(3):
        print(i)
    return_code = process1.poll()
    if return_code is not None:
        print("Return Code", return_code)
        for output in process1.stdout.readlines():
            print(output.strip())
        break

#to write to a file
with open('output1.txt', 'w') as f:
    process2 = subprocess.Popen(['ls', '-l'], stdout=f)
