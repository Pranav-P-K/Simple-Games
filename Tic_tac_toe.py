print('\n\tHello users! Welcome to TIC-TAC-TOE !!\n')
a = input('User 1: ')
b = input('User 2: ')
print('\n')
for i in range(1,10,3):
    print('|',i,'|',i+1,'|',i+2,'|')
print('\nUser 1:',a,'==> X')
print('User 2:',b,'==> O')
c1 = [' ',' ',' ',' ']
c2 = [' ',' ',' ',' ']
c3 = [' ',' ',' ',' ']
c4 = [1,2,3,4,5,6,7,8,9]
c5 = [1,2,3,4,5,6,7,8,9]
for turn in range(5):    
    f = int(input('\nEnter the position of X (1-9): '))
    if f in c4:
        print('\n',a,"'s turn:")
        if f == 1 or f == 2 or f == 3:
            c1[f-1] = 'X'
            print('','|'+'|'.join(c1),'\n','|'+'|'.join(c2),'\n','|'+'|'.join(c3))
        if f == 4 or f == 5 or f == 6:
            c2[f-4] = 'X'
            print('','|'+'|'.join(c1),'\n','|'+'|'.join(c2),'\n','|'+'|'.join(c3))
        if f == 7 or f == 8 or f == 9:
            c3[f-7] = 'X'
            print('','|'+'|'.join(c1),'\n','|'+'|'.join(c2),'\n','|'+'|'.join(c3))
        c4.remove(f)
    if c1 == ['X','X','X',' '] or c2 == ['X','X','X',' '] or c3 == ['X','X','X',' ']:
        print('\n',a,'is the Winner')
        break  
    if (c1[0]=='X' and c2[0]=='X' and c3[0]=='X') or (c1[1]=='X' and c2[1]=='X' and c3[1]=='X') or (c1[2]=='X' and c2[2]=='X' and c3[2]=='X'):
        print('\n',a,'is the Winner')
        break    
    if (c1[0]=='X' and c2[1]=='X' and c3[2]=='X') or (c1[2]=='X' and c2[1]=='X' and c3[0]=='X'):
        print('\n',a,'is the Winner')
        break
    g = int(input('\nEnter the position of O (1-9): '))
    if g in c5:
        print('\n',b,"'s turn:")
        if g == 1 or g == 2 or g == 3:
            c1[g-1] = 'O'
            print('','|'+'|'.join(c1),'\n','|'+'|'.join(c2),'\n','|'+'|'.join(c3))
        if g == 4 or g == 5 or g == 6:
            c2[g-4] = 'O'
            print('','|'+'|'.join(c1),'\n','|'+'|'.join(c2),'\n','|'+'|'.join(c3))
        if g == 7 or g == 8 or g == 9:
            c3[g-7] = 'O'
            print('','|'+'|'.join(c1),'\n','|'+'|'.join(c2),'\n','|'+'|'.join(c3))
        c5.remove(g)
    if c1 == ['O','O','O',' '] or c2 == ['O','O','O',' '] or c3 == ['O','O','O',' ']:
        print('\n',b,'is the Winner')
        break
    if (c1[0]=='O' and c2[0]=='O' and c3[0]=='O') or (c1[1]=='O' and c2[1]=='O' and c3[1]=='O') or (c1[2]=='O' and c2[2]=='O' and c3[2]=='O'):
        print('\n',b,'is the Winner')
        break
    if (c1[0]=='O' and c2[1]=='O' and c3[2]=='O') or (c1[2]=='O' and c2[1]=='O' and c3[0]=='O'):
        print('\n',b,'is the Winner')
        break
    if f == g or f > 9 or g > 9 or f < 0 or g < 0:
        print("Enter valid position!!")