'''
file operator
    Read
    Write
    Append(read or write file one line at a time)
'''

'''
module and function
pickle
    #a simple and a module,pickle,that makes it easy to store program data

    # return an object refer to the file object,
    # if the file do not exist,out will create a new one,
    # warning: if the file exist,open it in write mode will clear out the old data and start fresh.

    fObject = out("path To file","w/r")

    # fObject.write() function will return how many character it write
    # the file object keep track of where where the current line of the file is,
    # so it can write new line to the end of the file

    returnAnInteger = fObject.write("string")

    # when the write function end 
    # should mannually close the file , or it will close at the end of program

    fObject.close()

os
    #meaning: operating system
    #cwd: current working directory
    # 返回一个字符串，代表当前程序运行的路径
    
    os.getcwd()

    # 返回文件的绝对路径

    os.path.abspath("fileName")

    # 检查文件是否存在，或者实参是否为文件，或者是否为路径

    os.path.exists("path")
    os.path.isdir("path")
    os.path.isfile("path")

    # 列出指定目录下的所有文件及文件夹

    os.listdir("Directory")
    os.listdir(os.getcwd())
'''

from sys import getsizeof
import typing
import os

# startPath = "C:/Users/cba/Documents/个人文档/language/pythonLearning"
startPath = "c:\language"

# iterate every item in path , if it is file ,print the name ,or iterate the subdirectory
def walkThroug(path : str):
    for item in os.listdir(path):
        # itemABSPath = path + "//" + item
        itemABSPath = os.path.join(path,item)
        if os.path.isfile(itemABSPath):
            print(os.path.abspath(itemABSPath))
        else:
            print("Dir:" + itemABSPath)
            walkThroug(os.path.abspath(itemABSPath))
            # print(os.path.abspath(item))
            
walkThroug(startPath)


'''
os.walk()
    os模组自带的函数，可以实现类似的功能，不过更加的versatile
'''

print("\n")
# print("os.walk() output: ".format(os.walk(startPath)))
print("files in {} are : ".format(startPath))
count = 0
for dirs in os.walk(startPath):
    for fileName in dirs[2]:
        count += 1
        fileABSPath = os.path.join(dirs[0],fileName)
        print(" {}: {} ".format( count, fileABSPath))
        # print("and the size is: {}".format(os.path.getsize(fileABSPath)))
        print("and the size is: {}".format(os.stat(fileABSPath).st_size))
