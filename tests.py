a=input("请输入起始日期：")
b=input("请输入终止日期：")
x='-'
x=a.split('-')
y=b.split('-')
yesr1=int(x[0])
yesr2=int(y[0])
m1=int(x[1])
m2=int(y[1])
d1=int(x[2])
d2=int(y[2])

sum=0



if yesr1%4==0 and yesr2%4==0:
    yesr=yesr2-yesr1
    run = int(yesr / 4)
    sum=yesr * 365+run+2
    print("全部")
    print(sum)
elif yesr1%4!=0 and yesr2%4!=0:
    yesr = yesr2 - yesr1
    run = int(yesr / 4)

    sum = yesr * 365 + run + 1
    print(yesr2)
    print(yesr1)
    print('全不是')
    print(sum)
else:
    yesr = yesr2 - yesr1
    run = int(yesr / 4)
    sum = yesr * 365 + run
    print('只有一个是')
    print(sum)
print(sum)

maxm={1,3,5,7,8,10,12}
minm=[4,6,9,11]
towm=[2]
day=0

if m2>m1:
   lit=list(range(m1,m2))
   lit.append(m2)
   print(lit)
   for ch in lit:
       if ch in maxm:
           day=day+31
       elif ch in minm:
           day=day+30
       elif ch in towm:
           day=day+28
       print(day)


elif m2<m1:
    lit=list(range(m1,m2))
    lit.append(m1)
    for ch in lit:
        if ch in maxm:
            day = day - 31
        elif ch in minm:
            day = day - 30
        elif ch in towm:
            day = day - 28
        print(day)
else:day = d2-d1
print(day)









