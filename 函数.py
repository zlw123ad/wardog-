import math


def is_number(s):
    try:  # 如果能运行float(s)语句，返回True（字符串s是浮点数）
        float(s)
        return True
    except ValueError:  # ValueError为Python的一种标准异常，表示"传入无效的参数"
        pass  # 如果引发了ValueError这种异常，不做任何事情（pass：不做任何事情，一般用做占位语句）
    try:
        import unicodedata  # 处理ASCii码的包
        unicodedata.numeric(s)  # 把一个表示数字的字符串转换为浮点数返回的函数
        return True
    except (TypeError, ValueError):
        pass
    return False

def lenn(answer1,answer2):

    def dq(lb):

        for i in range(len(lb)):

            if lb[i] == 'x' or lb[i] == 'X':

                str1=''
                int1=i+1

                while lb[int1] != 'y' and lb[int1] != 'Y':

                    if lb[int1] != ',':
                        str1+=lb[int1]

                    int1+=1

                str2=''
                int1+=1

                while int1 != len(lb) and lb[int1] != ' ':

                    if lb[int1] != ',':
                        str2+=lb[int1]

                    int1+=1

                return [str1,str2]

            elif lb[i] != 'x' or lb[i] != 'X':

                if i == len(lb)-1:
                    print('error')

    def ftlb(lb):

        for i in range(len(lb)):
            lb[i] = float(lb[i])

        return lb

    dq1 = ftlb(dq(answer1))
    dq2 = ftlb(dq(answer2))

    return1 = [0,0]

    x = dq2[0] - dq1[0]
    y = dq2[1] - dq1[1]
    angle = math.degrees(math.atan2(x, y))
    if angle < 0:
        angle = angle + 360

    return1[0] = math.sqrt(math.pow(dq1[0]-dq2[0],2)+math.pow(dq1[1]-dq2[1],2))
    return1[1] = round(angle, 2)

    return  return1
#读取文本输入(文本,分割字符的列表) 输出分割后的文本列表
def wbfg(str1,list):

    list1 = []
    str2 = ''
    str3 = ''

    for i in range(len(str1)):

        if str3 in list:#多个字符分割符
            str2=str2[:-len(str3)]

            if str2 != '':
                list1.append(str2)

            str3 = ''

        if str1[i] in list:#单个字符分割符

            if str2 != '':
                list1.append(str2)
                str2 = ''
                str3 = ''

        str3+=str1[i]
        str2+=str1[i]

    if str2 != '':
        list1.append(str2)

    return list1

def swj(str,number,tw): #删文本(文本,数量,头尾(l,r))
    if len(str) - number <= 0:
        return None
    st = ''
    if tw == 'r':
        for i in range(len(str)-number):
            st+=str[i]
    elif tw == 'l':
        for i in range(len(str)-number):
            st+=str[i+number]
    return st