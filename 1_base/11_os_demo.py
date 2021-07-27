# 功能描述
# by Shawn
# 开发时间: 2021/7/27 15:10
import os
import os.path

print("============os===============")
#os.system('notepad.exe')
#os.system('calc.exe')

print(os.getcwd())
print(os.listdir('../1_base'))

# test1
path=os.getcwd()
lst=os.listdir(path)
for f in lst:
    if f.endswith("py"):
        print(f)

# test2
lstFiles = os.walk(path)
for dirpath,dirname,filename in lstFiles:
    print(dirpath)
    print(dirname)
    print(filename)

    for dir in dirname:
        print(os.path.join(dirpath.dir))

    for file in filename:
        print(os.path.join(file))
    print("-------------")


print("============os.path===============")
print(os.path.abspath("11_os_demo.py"))
print(os.path.exists("11_os_demo.py"))
print(os.path.join('E:\\python',"11_os_demo.py"))
print(os.path.split("E:\\python\\11_os_demo.py"))  #('E:\\python\', '11_os_demo.py')
print(os.path.splitext("11_os_demo.py"))  # ('11_os_demo', 'py')
print(os.path.basename("E:\\python\\11_os_demo.py")) #11_os_demo.py
print(os.path.dirname("E:\\python\\11_os_demo.py"))  #E:\\python\\

