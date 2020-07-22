import subprocess

#if shell=true used then no need of using lists but not reommended if user gives input
subprocess.run('ls -la', shell=True) 

#to print args and return code
p1=subprocess.run(['ls', '-la'])
print(p1)
print(p1.args)
print(p1.returncode)

#both give same results, and the output is captured in stdout. So running just the first line will not give the output
p2=subprocess.run(['ls', '-la'], capture_output=True, text=True)
#p2=subprocess.run(['ls', '-la'], stdout=subprocess.PIPE, text=True)
print(p2.stdout)

#sending output to file. Useful for logging
with open('output.txt', 'w') as f:
    p3=subprocess.run(['ls', '-la'], stdout=f, text=True)

#showing errors
p4=subprocess.run(['ls', '-la', 'habijabi'], capture_output=True, text=True)
#p4=subprocess.run(['ls', '-la', 'habijabi'], capture_output=True, text=True, check=True) #to let Python throw exception
print(p4.returncode)
print(p4.stdout)
print(p4.stderr)
#print(p4)

#ignore errors by redirecting them to DEVNULL
p5=subprocess.run(['ls', '-la', 'habijabi'], stderr=subprocess.DEVNULL)
print(p5.stderr)

#take output from one command and give it as input to another
p6=subprocess.run(['cat', 'input.txt'], capture_output=True, text=True)
print(p6.stdout)

p7=subprocess.run(['grep', '-n', 'show something'], capture_output=True, text=True, input=p6.stdout)
print(p7.stdout)

#doing it with shell=True
p1=subprocess.run('cat prac.txt | grep -n "show something"', capture_output=True, text=True, shell=True)
print(p1.stdout)
