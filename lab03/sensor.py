porog = int(input())
n = int(input())
x1,xe,x3,mx,s,c = 0,0,0,-100,0,0
mx=0
for i in range(n):
    x1+=1
    x = input()
    if x=='error':
        xe+=1
    else:
        x = float(x)
        if x>porog:
            x3+=1
        if x>mx:
            mx=x
        s+=x
        c+=1
print(x1)
print(xe)
print(x3)
print(f'{mx:.1f}')
print(f'{s/c:.1f}')

    
    



