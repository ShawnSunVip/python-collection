# 功能描述 学生管理系统
# by Shawn
# 开发时间: 2021/7/27 15:54
import os

def menu():
    print('===================================学生管理系统=====================================')
    print('====================================功能菜单=======================================')
    print('\t\t\t\t\t\t\t\t\t1.增')
    print('\t\t\t\t\t\t\t\t\t2.查')
    print('\t\t\t\t\t\t\t\t\t3.删')
    print('\t\t\t\t\t\t\t\t\t4.改')
    print('\t\t\t\t\t\t\t\t\t5.排序')
    print('\t\t\t\t\t\t\t\t\t6.统计人数')
    print('\t\t\t\t\t\t\t\t\t7.显示所有')
    print('\t\t\t\t\t\t\t\t\t0.退出')
    print('==================================================================================')


def add():
    student_list=[]
    while True:
        id=input('entry student id:')
        if not id:
            break
        name = input('entry student name:')
        if not name:
            break

        try:
            english= int(input('English score:'))
            java =int(input('Java score:'))
            python =int(input('Python score:'))
        except:
            print('invalid! entry agin!')
            continue

        student ={'id':id,'name':name,'english':english,'java':java,'python':python}
        student_list.append(student)
        ans =input('is continue?y/n')
        if ans =='y' or ans =='Y':
            continue
        else:
            break

    save(student_list)
    print('entry success!')

filename='student.txt'
def save(lst):
    try:
        file = open(filename,'a',encoding='utf-8')
    except:
        file = open(filename,'w',encoding='utf-8')
    for item in lst:
        file.write(str(item)+'\n')
    file.close()

def search():
    pass
def delete():
    while True:
        id =input('entry student Id:')
        if id !='':
            if os.path.exists(filename):
                with open(filename,'r',encoding='utf-8') as file:
                    student_list =file.readlines()
            else:
                student_list =[]
            flag=False
            if student_list:
               with open(filename,'w',encoding='utf-8') as wfile:
                    d={}
                    for item in student_list:
                        d=dict(eval(item))
                        if d['id'] !=id:
                            wfile.write(str(d)+"\n")
                        else:
                            flag=True
                    if flag:
                        print(f'id={id} is deleted!')
                    else:
                        print(f'id={id} is not exist!')
            else:
                print('no student')
                break
            show()

            ans =input('is continue?y/n')
            if ans =='y' or ans =='Y':
                continue
            else:
                break


def modify():
    pass
def sort():
    pass
def total():
    pass
def show():
    pass


def main():
    while True:
        menu()
        choose =int(input('please choose:'))
        if choose in [0,1,2,3,4,5,6,7]:
            if choose ==0:
                ans =input('ensure exit？y/n')
                if ans =='y' or ans =='Y':
                    print('thank you！！！')
                    break
                else:
                    continue
            elif choose == 1:
                add()
            elif choose == 2:
                search()
            elif choose == 3:
                delete()
            elif choose == 4:
                modify()
            elif choose == 5:
                sort()
            elif choose == 6:
                total()
            elif choose == 7:
                show()

if __name__ == '__main__':
    main()