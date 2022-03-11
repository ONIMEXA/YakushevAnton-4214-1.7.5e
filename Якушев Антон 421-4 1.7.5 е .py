def input_variables():
    mas=(input('Введите значения n и m: ')).split()
    if len(mas)!=2:
        print("Введено неправильное количество значений")
        mas=input_variables()
    if mas[0].isdigit()==False or mas[1].isdigit()==False:
        print("Введены не числа")
        mas=input_variables()
    for i in range(len(mas)):mas[i]=int(mas[i])
    if mas[0]<mas[1] or mas[0]<0 or mas[1]<0:
        print("Условия не выполняются")
        mas=input_variables()
    return mas
def C(n,m):
    if m==n or m==0:return 1
    
    return C(n-1,m)+C(n-1,m-1)

def output(C,n,m):
    print("C({},{}) = ".format(m,n),end='')
    while m>=0 and n>=0:
        n_count=n
        while n_count>0:
            n_count-=1
            if (m==n_count or m==0)==False:print("C({},{})".format(m,n_count),end='')
            if m==n_count or m==0:print("1",end='')
            if (m==0 and n_count==0)==False:print(" + ",end='')
        m-=1
        n-=1
        
    print(' =',C)

if __name__ == '__main__':
    mas=input_variables()
    value=C(mas[0],mas[1])
    output(value,mas[0],mas[1])
    
    
