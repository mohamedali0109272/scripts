import os

os.system("echo log.txt > log.txt")
file = []
sub_format = []
log = []
for f in os.listdir():
    
    f_name, f_ext = os.path.splitext(f)
    
    if f_ext == ".mkv":
        sub_format.append(f_name)
       
    if f_ext == ".srt" :
        filef = '{}{}'.format(f_name, f_ext)
        file.append(filef)
        
k=0

while 1==1:
    l= sub_format[k]
    j= file[k]
    lo =(j, l+".srt")
    log.append(lo)
    print(lo)
    output_write = open("log.txt","r+")
    output_write.write(str(log))
    #output_write.close()
    #os.rename(j, l+".srt")
    k = k+1
