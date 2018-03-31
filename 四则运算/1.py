#coding:utf-8
import random


operatorDicts = ['+','-','*','/']

a = int(input("请输入题数："))

#生成四则运算式
def generate():
    num = random.randint(1,3)
    formular = [str(random.randint(1, 100)),random.choice(operatorDicts),str(random.randint(1, 100))]
    for i in range(num-1):
        formular.append(random.choice(operatorDicts))
        formular.append(str(random.randint(1,100)))
    length = len(formular)
    if num==1:
        pass
    else:
        n = int(random.randrange(0,length-2,2))
        formular.insert(n,'(')
        v = random.randrange(0,3,2)
        m = n+v+4
        formular.insert(m,')')
    return formular



#将中缀表达式转为后缀表达式
def exchange(formular):
    postfix = []
    stack = []

    def opOrder(op1, op2):
        order_dic = {'*': 4, '/': 4, '+': 3, '-': 3}
        if op1 == '(' or op2 == '(':
            return False
        elif op2 == ')':
            return True
        else:
            if order_dic[op1] < order_dic[op2]:
                return False
            else:
                return True

    for s in formular:
        if s.isdigit():
            postfix.append(s)
        else:
            while len(stack) != 0 and opOrder(stack[-1], s):
                op = stack.pop()
                postfix.append(op)
            if len(stack) == 0 or s != ')':
                stack.append(s)
            else:
                top_op = stack.pop()
    if len(stack):
        for i in range(len(stack)):
            postfix.append(stack[i])
    return postfix

#将后缀转为二叉树
