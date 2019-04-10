
"""
https://blog.csdn.net/gusui7202/article/details/83239142
qhy。
"""
import sys
import os
data_dir = "C:/Users/19482/Desktop/wrr/HOG_SVM-master/image128"
file_list = []
write_file_name = 'C:/Users/19482/Desktop/wrr/HOG_SVM-master/image128/train.txt'
write_file = open(write_file_name, "w")
tt=os.listdir(data_dir)
for file in tt:
    if file.endswith(".jpg"):
        write_name = file
        # print(type(write_name))
        # print(write_name[0])
        # print(type(write_name[0]))

        if write_name[0]=='f':
            file_list.append(write_name + " "+'1')
        if write_name[0]=='s':
            file_list.append(write_name + " "+'2')


print(file_list)
for current_line in range(len(file_list)):
     write_file.write(file_list[current_line] + '\n')
write_file.close()
