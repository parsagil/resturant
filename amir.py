def reserve():
    tedad_khol_sandali =200
    
    print('hi welcome to resturant ')
    aa =  int (input( "how many of you are there ?"))
    
    tedad_khol_sandali = tedad_khol_sandali - aa
    print(tedad_khol_sandali)
    
    if aa > tedad_khol_sandali:
        print('the place is full :',tedad_khol_sandali)
    elif aa < tedad_khol_sandali:
        print('there is still room :',tedad_khol_sandali)
    
    

def menu ():
    print('''
          ************************ restaurant menu************************
          
          edibel:
          
                  1. hamber  ....................... 250.000
                  2. pitza ........................ 350.00
                  3. potatoes with mushrooms .............. 120.000
                  
          drink:
            
                  4. soda .............................30.000. 
                  5. dough................................ 30.000
                  6. whiskey ............................ 120.000
          ''')
    
    qimat={'1':250.000, 
           '2':350.000,
           '3':120.000,
           '4':30.000,
           '5':30.000,
           '6':120.000
           }
    
    list_qaza=[]
    
    
    while 1:
        order=int(input(' food number :'))
        list_qaza.append(order)
        a=input("do you have an order again ? y/n")
        if a == 'y':
            continue
        elif a == 'n':
            break
        else:
            print('enter y or n')
            continue
     
     
     
    ghinmat_nahi = []
    for i in list_qaza:
        if i == 1:
            ghinmat_nahi.append(qimat['1'])
        elif i == 2:
            ghinmat_nahi.append(qimat['2'])
        elif i == 3:
            ghinmat_nahi.append(qimat['3'])
        elif i == 4:
            ghinmat_nahi.append(qimat['4'])
        elif i == 5:
            ghinmat_nahi.append(qimat['5'])
        elif i == 6:
            ghinmat_nahi.append(qimat['6'])
            
    #print(ghinmat_nahi)
    
    
    gh = []
    
    total = 0
    for j in ghinmat_nahi:
        total += j
    gh.append(total)
    
    print('the final price :',gh)

    
    
    
if __name__ == '__main__':
    reserve()

if __name__ == '__main__':
    menu()
