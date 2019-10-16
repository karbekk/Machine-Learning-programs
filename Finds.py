import csv

with open("D:\\data set\\golf.csv") as find:
    reader = csv.reader(find)
    data = list(reader)
print(data)


h = ['0','0','0','0','0','0']
for row in data:
    if row[-1] == 'Yes':
        j=0
        for col in row:
            if col!='Yes':
                if col!=h[j] and h[j] =='0':
                    h[j] = col
                    #print(col)
                elif col!=h[j] and h[j]!='0':
                    h[j]='?'
                    print(col)
            j= j+1
print(h)
