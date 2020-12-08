import shutil
import os
import time

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

# 普通写入文件 w：写入文件，会将原文件内容覆盖，a：追加模式写入
def write_file(path, mode="w"):
    if os.path.exists(path) == False or os.path.getsize(path) == 0:
        print("file is empty.........")
        return
    with open(path, mode) as file:
        print("file is open ....")
        file.write("\n")
        file.writelines(str(time.time()))
        print("file write end ...")

"""
    copy文件
    @:param source_file 源文件
    @:param target_file copy后文件
    @:return 返回copy文件的文件路径
"""
def copy_file( source_file, target_file):
    # if(os.path.exists(path) != True):
    #     os.mkdir(path)
    copy = shutil.copy2(source_file, target_file)
    print(copy)



# 手撸copy文件
def copy_file2(source_file, target_file):

    with open(source_file, "rb") as fsrc:
        with open(target_file, 'wb') as fdst:
            while True:
                buf = fsrc.read(1024)
                if not buf:
                    break
                fdst.write(buf)
            fdst.close()
        fsrc.close()

# read_file("../../../docs/test.txt")
# copy_file("/Users/youjia/Desktop/file/aa.xlsx", "/Users/youjia/Desktop/bb.xlsx")
# write_file("../../docs/test.txt", "a")
# copy_file2("/Users/youjia/Desktop/file/汇付后台开放平台接口规范v1.0.3_20200609.xlsx", "/Users/youjia/Desktop/bb.xlsx")



