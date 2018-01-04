import glob
import tarfile
import re

print("This script used to collect required files for PR")

print("""Script options:
        1. Config session issue
        2. Specific process logs
        3. PM/CM data collection
        4. Exit""")
option = int(input("Please Enter your Option : "))

log_path = "F:/Sat/github/file-collect-master/"
temp_path = "/opt/nfs/sathish/scripts/tmp_s/"
# process = ['Transform', 'Load', 'Write', 'DIMgr']
process = ['Transform']
file_t = []
empt_list = []


def config_log():
        print("config related files will be collected")
        date_c = int(input("Enter date (Ex:YYYYMMDD) :"))
        time_s = input("Enter start time of config session (Ex:HH):")
        time_e = input("Enter End time of config session (Ex:HH):")
        for i in process:
                process_log(i, date_c, time_s, time_e)


def pm_cm():
        print("PM/CM files will be collected")


def append1(file1):
        for i in file1:
                file_t.append(i)


def tar_file(tar, date, proc):
        tar1 = tarfile.open("{0}_log_{1}.tar.bz2".format(proc, date), "w:bz2")
        for name in tar:
                tar1.add(name)
        tar1.close()


def print_t(list1):
        count = 0
        for i in sorted(list1):
                print(i)
                count += 1
        print("Total files : ", count)


def process_log(process_c, date, start_time, end_time):
    print(process_c, date, start_time, end_time)
    print(len(str(start_time)), len(str(end_time)))
    val_l = []
    file1 = []
    file_list_stack = []
    file_list_gc = []
    global file_t
    if len(str(start_time)) == 1 & len(str(end_time)) == 1:
        print("Collecting ", process_c, "logs... ")
        file1 = glob.glob("{0}{1}*{2}0[{3}-{4}]*".format(log_path, process_c, date, start_time, end_time))
        append1(file1)
        print(file1)
        for i in range(len(file1)):
                # This will remove all special char and split into words
                data = re.findall(r"[\w']+", file1[i])
                value1 = str("/{0}/{1}/{2}/{3}.{4}.{5}".format(data[0], data[1], data[2], data[3], data[4], data[5]))
                val_l.append(value1)
        append1(list(set(val_l)))
#        tar_file(file_t, date, process_c)
        print_t(file_t)
        file_t = list(empt_list)
        print("Collecting ", process_c, " Stack traces logs... ")
        file_list_stack = glob.glob("{0}mycom{1}.sh.*{2}0[{3}-{4}]*".format(log_path, process_c.lower(), date, start_time, end_time))
        print(file_list_stack)
        print("Collecting ", process_c, "GC logs... ")
        file_list_gc = glob.glob("{0}mycom{1}_gc.*{2}0[{3}-{4}]*".format(log_path, process_c.lower(), date, start_time, end_time))
        print(file_list_gc)
    elif (len(str(start_time)) == 1) & (len(str(end_time)) == 2):
        print("1st elIf statement")
        c = str(end_time)
        print(int(c[0]))
        file1 = glob.glob("{0}{1}*{2}0[{3}-9]*".format(log_path, process_c, date, start_time, end_time))
        append1(file1)
        if int(c[0]) == 1:
            file1 = glob.glob("{0}{1}*{2}1[0-{4}]*".format(log_path, process_c, date, start_time, int(c[1])))
            append1(file1)
        elif int(c[0]) == 2:
            file1 = glob.glob("{0}{1}*{2}1[0-9]*".format(log_path, process_c, date, start_time, int(c[1])))
            append1(file1)
            file1 = glob.glob("{0}{1}*{2}2[0-{4}]*".format(log_path, process_c, date, start_time, int(c[1])))
            append1(file1)
        for i in range(len(file1)):
                data = re.findall(r"[\w']+", file1[i])
                value1 = str("/{0}/{1}/{2}/{3}.{4}.{5}".format(data[0], data[1], data[2], data[3], data[4], data[5]))
                val_l.append(value1)
        append1(list(set(val_l)))
        tar_file(file_t, date, process_c)
        print_t(file_t)
        file_t = list(empt_list)
    elif (len(str(start_time)) == 2) & (len(str(end_time)) == 2):
        print("2nd elIf statement")
        c = str(end_time)
        s = str(start_time)
        print(int(c[0]))
        if (int(s[0]) == 1) & (int(c[0]) == 1):
            file1 = glob.glob("{0}{1}*{2}1[{3}-{4}]*".format(log_path, process_c, date, int(s[1]), int(c[1])))
            append1(file1)
        elif (int(s[0]) == 2) & (int(c[0]) == 2):
            file1 = glob.glob("{0}{1}*{2}2[{3}-{4}]*".format(log_path, process_c, date, int(s[1]), int(c[1])))
            append1(file1)
        elif (int(s[0]) == 1) & (int(c[0]) == 2):
            file1 = glob.glob("{0}{1}*{2}1[{3}-9]*".format(log_path, process_c, date, int(s[1]), int(c[1])))
            append1(file1)
            file1 = glob.glob("{0}{1}*{2}2[0-{4}]*".format(log_path, process_c, date, int(s[1]), int(c[1])))
            append1(file1)
        for i in range(len(file1)):
                data = re.findall(r"[\w']+", file1[i])
                value1 = str("/{0}/{1}/{2}/{3}.{4}.{5}".format(data[0], data[1], data[2], data[3], data[4], data[5]))
                val_l.append(value1)
        append1(list(set(val_l)))
        tar_file(file_t, date, process_c)
        print_t(file_t)
        file_t = list(empt_list)


def process_log1():
    print("logs")


if option == 1:
        config_log()
elif option == 2:
        process_log1()
elif option == 3:
        pm_cm()
else:
        exit()
