d=int(input('enter day:'))
m=int(input('enter month:'))
y=int(input('enter year:'))
days=int(input('enter days:'))
months={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
if m>12 or m<1 or d<1 or d>months[m]:
    print('error')
else:
    if days!=0:
        while days>=(months[m]-d):
            if (y%4==0 and y%100!=0) or y==400:
                months.update({2:29})
            else:
                months.update({2:28})
            m+=1
            if m>12:
                y+=1
                m=1
            days-=months[m]
        d+=days
    print(d,'/',m,'/',y)
