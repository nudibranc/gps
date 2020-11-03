from datetime import datetime, timedelta

file1 = open('platform.txt','r')
lines1 = file1.readlines()
file2 = open('sample.txt','r')
lines2 = file2.readlines()
for i in lines2:
    line = i.split(':')
    if 'File Modification Date/Time' in line[0]:
        second = int(line[5].split('+')[0])
        minute = int(line[4])
        day = int(line[3].split()[0])
        hour = int(line[3].split()[1])
        source_time = datetime(int(line[1]),int(line[2]),day,hour,minute,second)
        for j in lines1:
            line1 = j.split()
            if (line1[0] == '1'):
                fms = float('0.'+ line1[1].split('.')[1])
                ms = int(fms * 1000)
                utc = datetime(1980, 1, 6) + timedelta(seconds=(int(line1[2]) * 604800 + int(line1[1].split('.')[0])))
                if utc == source_time: print(line1)
                