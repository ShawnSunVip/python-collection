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
        flag = False
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as file:
                file_list = file.readlines()
                for item in file_list:
                    d = dict(eval(item))
                    if d['id'] == id:
                        flag = True
        if flag:
            print('this student id is exist,please entry agin!')
            continue

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
    while True:
        id =''
        name =''
        if os.path.exists(filename):
            type = input('if id entry 1,if name entry 2:')
            if type =='1':
                id = input('please entry student id:')
            elif type =='2':
                name = input('please entry student name:')
            else:
                print('info error,please entry agin!')
                search()

            with open(filename, 'r', encoding='utf-8') as file:
                file_list = file.readlines()
                if file_list:
                    flag = True
                    for item in file_list:
                        d = dict(eval(item))
                        if id !='':
                            if d['id'] == id:
                                flag = False
                                print('id:{0},name:{1},english:{2},java:{3},python:{4} \t'.format(d['id'], d['name'],
                                                                                                  d['english'],
                                                                                                  d['java'],
                                                                                                  d['python']))
                        elif name !='':
                            if d['name'] == name:
                                flag = False
                                print('id:{0},name:{1},english:{2},java:{3},python:{4} \t'.format(d['id'], d['name'],
                                                                                                  d['english'],
                                                                                                  d['java'],
                                                                                                  d['python']))
                    if flag:
                        print('not found student')
                else:
                    print('no student')

        else:
            print('no student')

        ans = input('is continue?y/n')
        if ans == 'y' or ans == 'Y':
            continue
        else:
            break

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
    while True:
        id = input('entry student Id:')
        if id != '':
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as file:
                    student_list = file.readlines()
            else:
                student_list = []
        if student_list:
            with open(filename, 'w', encoding='utf-8') as wfile:
                d = {}
                flag =False
                for item in student_list:
                    d = dict(eval(item))
                    if d['id'] != id:
                        wfile.write(str(d) + "\n")
                    else:
                        print(f'find this student={id},please modify!')
                        while True:
                            try:
                                d['name'] = input('entry student name:')
                                d['english'] = int(input('English score:'))
                                d['java'] = int(input('Java score:'))
                                d['python'] = int(input('Python score:'))
                            except:
                                print("info error")
                            else:
                                break
                        wfile.write(str(d)+"\n")
                        flag =True
                if flag:
                    print(f'id={id} is updated!')
                else:
                    print(f'not find this student={id}')
        else:
            print('no student')
            break

        show()

        ans = input('is continue?y/n')
        if ans == 'y' or ans == 'Y':
            continue
        else:
            break
def sort():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            file_list = file.readlines()
        student_list=[]
        for item in file_list:
            d = dict(eval(item))
            student_list.append(d)
    else:
        return

    asc_or_desc = input('请选择排序方式 0：升序，1：降序:')
    if asc_or_desc =='0':
        asc_or_desc_bool =False
    elif asc_or_desc =='1':
        asc_or_desc_bool =True
    else:
        print('error,please agin')
        sort()

    model =input('请选择排序方式 0：总成绩，1：英语，2：python，3：java：')
    if model =='0':
        student_list.sort(key=lambda x: x['english']+x['python']+x['java'],reverse=asc_or_desc_bool)
    elif model =='1':
        student_list.sort(key=lambda x: x['english'],reverse=asc_or_desc_bool)
    elif model =='2':
        student_list.sort(key=lambda x: x['python'],reverse=asc_or_desc_bool)
    elif model =='3':
        student_list.sort(key=lambda x: x['java'],reverse=asc_or_desc_bool)
    else:
        print('error,please agin')
        sort()
    showStudent(student_list)

def total():
    pass

def show():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            file_list = file.readlines()
            student_list =[]
            for item in file_list:
                d = dict(eval(item))
                student_list.append(d)
            showStudent(student_list)

def showStudent(student_list):
    for item in student_list:
        print('id:{0},name:{1},english:{2},java:{3},python:{4} \t'.format(item['id'], item['name'], item['english'], item['java'],
                                                                          item['python']))

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