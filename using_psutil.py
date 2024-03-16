import psutil

p=psutil.virtual_memory()

a=p.total
b=p.available
c=p.free
e=p.used
d=p.percent

print('Total Memory',a)
print('Available Memory',b)
print('Used Memory',c)
print('Memory free',e)
print('Memory Percent',d)


#CPU count -the number of processing cores available in the computer
cpu_count=psutil.cpu_count()
cpu_percent=psutil.cpu_percent()

print('\n\nCPU count',cpu_count)
print('CPU Percent',cpu_percent,'\n\n')


#listing running process
#for process in psutil.process_iter():
   # print(process.pid,process.name())

#getting disk usage
d=psutil.disk_usage('/')

a=d.total
b=d.used
c=d.free
e=d.percent

print('Total disk',a)
print('Used disk',b)
print('Free disk',c)
print('Memory Percent',e)
