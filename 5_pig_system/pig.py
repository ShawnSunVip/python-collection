# 功能描述
# by Shawn
# 开发时间: 2021/8/4 9:39
import os
import xlwt
from decimal import Decimal

def menu():
    print("****************************************穆三姐猪肉系统*******************************************")
    print("*****************************************╭︿︿︿︿︿╮********************************************")
    print("*****************************************{/ o  o /}**********************************************")
    print("***************************************** ( (oo) )***********************************************")
    print("*******************************************︶︶︶************************************************")
    print("*******************************************功能菜单**********************************************")
    print('\t\t\t\t\t1.增加品类')
    print('\t\t\t\t\t2.显示所有')
    print('\t\t\t\t\t3.删除品类')
    print('\t\t\t\t\t4.修改品类')
    print('\t\t\t\t\t5.导出品类')
    print('\t\t\t\t\t0.退出系统')
    print("************************************************************************************************")

filename='pig.txt'

def add():
    pig_list=[]
    while True:
        name =input('请输入猪肉品类：')
        if not name:
            print("不允许输入空，请重新输入！！！")
            continue
        flag =False
        if os.path.exists(filename):
            with open(filename,'r',encoding='utf-8') as file:
                file_list =file.readlines()
                for item in file_list:
                    d =dict(eval(item))
                    if d['name'] == name:
                        flag =True
        if flag:
            print("该品类已存在，请重新输入！！！")
            continue

        try:
            price =float(input('请输入单价：'))
            quantity =int(input('请输入数量：'))
        except:
            print('输入有误，请重新输入！！！')
            continue

        pig = {'name':name,'price':price,'quantity':quantity}
        pig_list.append(pig)

        ans =input('是否继续录入？y/n:')
        if ans == 'y' or ans == 'Y':
            continue
        else:
            break

    save(pig_list)
    print('保存成功！！！')

def save(pig_list):
    try:
        file =open(filename,'a',encoding='utf-8')
    except:
        file =open(filename,'w',encoding='utf-8')
    for pig in pig_list:
        file.write(str(pig)+"\n")
    file.close()

def delete():
    while True:
        name= input('请输入你需要删除的品类：')
        if name !='':
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as file:
                    pig_list = file.readlines()
            else:
                pig_list = []
            flag =False
            if pig_list:
                with open(filename,'w',encoding='utf-8') as wfile:
                    for item in pig_list:
                        d =dict(eval(item))
                        if d['name'] != name:
                            wfile.write(str(d)+"\n")
                        else:
                            flag=True

                    if flag:
                        print(f'{name}删除成功！！！')
                    else:
                        print(f'{name}不存在！！！')
                        ans = input('是否继续删除？y/n:')
                        if ans == 'y' or ans == 'Y':
                            continue
                        else:
                            break
            else:
                print('暂无数据！！！')
                break

            ans = input('是否继续删除？y/n:')
            if ans == 'y' or ans == 'Y':
                continue
            else:
                break

        else:
            print('输入有误，请重新输入！！！')
            continue

def modify():
    while True:
        name = input('请输入你需要修改的品类：')
        if name != '':
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as file:
                    pig_list = file.readlines()
            else:
                pig_list = []
            flag = False
            pig_update_list =[]
            if pig_list:
                with open(filename, 'w', encoding='utf-8') as wfile:
                    for item in pig_list:
                        d = dict(eval(item))
                        if d['name'] != name:
                            wfile.write(str(d) + "\n")
                        else:
                            print(f'发现{name},请修改!')
                            while True:
                                try:
                                    d['price'] = float(input('请输入单价：'))
                                    d['quantity'] = int(input('请输入数量：'))
                                except:
                                    print("输入信息有误，请重新输入！！！")
                                else:
                                    break
                            wfile.write(str(d) + "\n")
                            flag = True
                            pig_update_list.append(d)
                    if flag:
                        print(f'{name}修改成功！！！')
                    else:
                        print(f'{name}不存在！！！')
                        continue
            else:
                print('暂无数据！！！')
                break

            ans = input('是否继续修改？y/n:')
            if ans == 'y' or ans == 'Y':
                continue
            else:
                if pig_update_list:
                    showPig(pig_update_list)
                break

        else:
            print('输入有误，请重新输入！！！')
            continue

def show():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            file_list = file.readlines()
            pig_list =[]
            for item in file_list:
                d = dict(eval(item))
                pig_list.append(d)
            showPig(pig_list)
    else:
        print('暂无数据！！！')

def showPig(pig_list):
    print("品类\t\t\t单价\t\t\t数量\t\t总价")
    for pig in pig_list:
        if len(pig['name']) ==2:
            print(
                '{0}\t\t\t{1}\t\t\t{2}\t\t{3}'.format(pig['name'], str(pig['price']), str(pig['quantity']),
                                                                  str((Decimal(pig['price']) * Decimal(pig['quantity'])).quantize(Decimal('0.00')))))
        elif len(pig['name']) ==3:
            print(
                '{0}\t\t\t{1}\t\t\t{2}\t\t{3}'.format(pig['name'], str(pig['price']), str(pig['quantity']),
                                                                  str((Decimal(pig['price']) * Decimal(pig['quantity'])).quantize(Decimal('0.00')))))
        elif len(pig['name']) ==4:
            print(
                '{0}\t\t{1}\t\t\t{2}\t\t\t{3}'.format(pig['name'], str(pig['price']), str(pig['quantity']),
                                                                str((Decimal(pig['price']) * Decimal(pig['quantity'])).quantize(Decimal('0.00')))))

def export():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            file_list = file.readlines()
            pig_list = []
            for item in file_list:
                d = dict(eval(item))
                d['total'] = (Decimal(d['price'])*int(d['quantity'])).quantize(Decimal('0.00'))
                pig_list.append(d)
            write_data_excel(pig_list)
        print('导出成功！！！')
    else:
        print('暂无数据！！！')

def write_data_excel(list):
    wbk =xlwt.Workbook(encoding='utf-8')

    sheet = wbk.add_sheet('Sheet1',cell_overwrite_ok=True)

    title_list = ['\t品类','单价','数量','总价']

    font =xlwt.Font()
    font.name = u"微软雅黑"
    font.color = "black"
    font.height = 220
    font.bold = True

    border = xlwt.Borders()  # 给单元格加框线
    border.left = xlwt.Borders.THIN  # 左
    border.top = xlwt.Borders.THIN  # 上
    border.right = xlwt.Borders.THIN  # 右
    border.bottom = xlwt.Borders.THIN  # 下

    alignment = xlwt.Alignment()  # 设置字体在单元格的位置
    alignment.horz = xlwt.Alignment.HORZ_CENTER  # 水平方向
    alignment.vert = xlwt.Alignment.VERT_CENTER  # 竖直方向

    pattern = xlwt.Pattern()
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    pattern.pattern_fore_colour = xlwt.Style.colour_map['ice_blue']

    title_stype = xlwt.XFStyle()
    title_stype.font = font
    title_stype.alignment = alignment
    title_stype.borders=border
    title_stype.pattern=pattern

    content_stype = xlwt.XFStyle()
    content_stype.borders = border

    tail_stype = xlwt.XFStyle()
    tail_stype.borders =border
    tail_stype.font=font
    tail_stype.alignment=alignment
    tail_stype.pattern=pattern

    y = 0
    sum =0
    for i in range(len(list)):
        if i ==0:
            for x in range(len(title_list)):
                sheet.write(0,x,title_list[x],title_stype)
        j=0
        for item in list[i]:
            y = i + 1
            sheet.write(y,j,list[i][item],content_stype)
            if item =='total':
                sum += list[i][item]
            j+=1

    sheet.write_merge(y+1,y+1,0,2,'合计',tail_stype)
    sheet.write(y+1, 3, sum,content_stype)

    wbk.save('pig.xls')

def main():
    while True:
        menu()
        choose = int(input('请选择功能:'))
        if choose in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choose == 0:
                ans = input('确认退出吗？y/n：')
                if ans == 'y' or ans == 'Y':
                    print('感谢使用！！！')
                    break
                else:
                    continue
            elif choose == 1:
                add()
            elif choose == 2:
                show()
            elif choose == 3:
                delete()
            elif choose == 4:
                modify()
            elif choose == 5:
                export()
        else:
            print("选择有误，请重新选择！！！")

if __name__ == '__main__':
    main()