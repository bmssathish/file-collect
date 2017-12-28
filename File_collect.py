#!/usr/bin/python
import os
import commands
import glob
import tarfile
import re

print("This script used to collect required files for PR")

print("""Script options:
        1. Config session issue
        2. Speific process logs
        3. PM/CM data collectioni
        4. Exit""")
option=int(input("Please Enter your Option : "))

log_path="/opt/mycom/logs/"
temp_path="/opt/nfs/sathish/scripts/tmp_s/"
#process=['Transform','Load','Write','DIMgr']
process=['Transform']
def config_log():
        print("config related files will be collected")
        date_c=int(input("Enter date (Ex:YYYYMMDD) :"))
        time_s=input("Enter start time of config session (Ex:HH):")
        time_e=input("Enter End time of config session (Ex:HH):")
        for i in process:
                process_log(i,date_c,time_s,time_e)

def pm_cm():
        print("PM/CM files will be collected")

file_t=[]
def append1(file1):
        for i in file1:
                file_t.append(i)
def tar_file(tar):
        tar1 = tarfile.open("Transform_log.tar", "w")
        for name in (tar):
                tar1.add(name)
                tar1.close()

def process_log(process_c,date,start_time,end_time):
    print(process_c,date,start_time,end_time)
    print(len(str(start_time)),len(str(end_time)))
    val_l=[]
    if len(str(start_time)) == 1 & len(str(end_time)) ==1:
        print("If statement")
        file1=glob.glob("{0}{1}*{2}0[{3}-{4}]*".format(log_path,process_c,date,start_time,end_time))
        append1(file1)
        for i in range(len(file1)):
                data=re.findall(r"[\w']+", file1[i])
                value1=str("/{0}/{1}/{2}/{3}.{4}.{5}".format(data[0],data[1],data[2],data[3],data[4],data[5]))
                val_l.append(value1)
        append1(list(set(val_l)))
        print_t(file_t)
        tar_file(file_t)
    elif (len(str(start_time)) == 1) & (len(str(end_time)) == 2):
        print("1st elIf statement")
        c=str(end_time)
        print(int(c[0]))
        file1=glob.glob("{0}{1}*{2}0[{3}-9]*".format(log_path,process_c,date,start_time,end_time))
        append1(file1)
        if int(c[0]) == 1:
            file1=glob.glob("{0}{1}*{2}1[0-{4}]*".format(log_path,process_c,date,start_time,int(c[1])))
            append1(file1)
        elif int(c[0]) == 2:
            file1=glob.glob("{0}{1}*{2}1[0-9]*".format(log_path,process_c,date,start_time,int(c[1])))
            append1(file1)
            file1=glob.glob("{0}{1}*{2}2[0-{4}]*".format(log_path,process_c,date,start_time,int(c[1])))
            append1(file1)
        for i in range(len(file1)):
                data=re.findall(r"[\w']+", file1[i])
                value1=str("/{0}/{1}/{2}/{3}.{4}.{5}".format(data[0],data[1],data[2],data[3],data[4],data[5]))
                val_l.append(value1)
        append1(list(set(val_l)))
        print_t(file_t)
    elif (len(str(start_time)) == 2) & (len(str(end_time)) == 2):
        print("2nd elIf statement")
        c=str(end_time)
        s=str(start_time)
        print(int(c[0]))
        if (int(s[0]) == 1) & (int(c[0]) == 1):
            file1=glob.glob("{0}{1}*{2}1[{3}-{4}]*".format(log_path,process_c,date,int(s[1]),int(c[1])))
            append1(file1)
        elif (int(s[0]) == 2) & (int(c[0]) == 2):
            file1=glob.glob("{0}{1}*{2}2[{3}-{4}]*".format(log_path,process_c,date,int(s[1]),int(c[1])))
            append1(file1)
        elif (int(s[0]) == 1) & (int(c[0]) == 2):
            file1=glob.glob("{0}{1}*{2}1[{3}-9]*".format(log_path,process_c,date,int(s[1]),int(c[1])))
            append1(file1)
            file1=glob.glob("{0}{1}*{2}2[{3}-{4}]*".format(log_path,process_c,date,int(s[1]),int(c[1])))
            append1(file1)
        for i in range(len(file1)):
                data=re.findall(r"[\w']+", file1[i])
                value1=str("/{0}/{1}/{2}/{3}.{4}.{5}".format(data[0],data[1],data[2],data[3],data[4],data[5]))
                val_l.append(value1)
        append1(list(set(val_l)))
        print_t(file_t)

def print_t(list1):
        count=0
        for i in sorted(list1):
                print(i)
                count +=1
        print("Total files : ",count)

if option == 1:
        config_log()
elif option == 2:
        process_log()
elif option == 3:
        pm_cm()
else:
        exit()