import shutil
import os

# 普通读取数据
def read_file(path):
    if os.path.exists(path) == False or os.path.getsize(path) == 0:
        print("file is empty.........")
        return
    with open(path, "r") as file:
        print("file is open.........")

        # read()  readline()  readlines() 均为读取文件方式，下面for读取适合大文件
        # read = file.readline()
        for line in file:
            print(line.rstrip())
        file.close()

"""
    copy文件
    @:param path 文件对应文件夹路径
    @:param source_file 源文件
    @:param target_file copy后文件
    @:return 返回copy文件的文件路径
"""
def copy_file(path, source_file, target_file):
    if(os.path.exists(path) != True):
        os.mkdir(path)
    copy = shutil.copy2(source_file, target_file)
    print(copy)

read_file("../resource/test.txt")
# copy_file("D:/ukar/demo", "D:/ukar/常用命令/git.txt", "D:/ukar/demo/git.txt")




