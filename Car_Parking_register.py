


#### Create a list for number and model name ####

no=[4567,2345,5678]
model=['dfgg','sdfd','wert']


def car_add(a,b):
    no.append(a)
    model.append(b)
    print('The car no and model added')
    return no,model
def search(c,g,h):
    l=g.index(c)
    j=h[l]
    print('The car position is ', l+1)
    print('The car No is',c)
    print('The car model is ',j)
    
def remove():
    no.remove(k)
    model.remove(p)
    print(' The car num is removed from the list ',k)
    print(' The car model is removed from the list ',p)
    
    
def car_count():
    print('The total car count',len(no))

while True:
    x=int(input('''
              #####CAR PARKING REGISTER#####
              1. Add the cars
              2. search your car
              3. total count
              4. Remove
              5. Exit
              Enter the options: '''))
    if x==1:
        a=int(input('Enter the carno.'))
        b=input('Enter your car model')
        g,h=car_add(a,b)
        
    elif x==2:
        c=int(input('Enter your car no for search '))
        search(c,g,h)
        
    elif x==3:
        car_count()

    elif x==4:
        k = int(input('Enter the car no to remove '))
        p = input('Enter the model no to remove ')
        remove()
        
    
    elif x==5:
        break
    else:
        print('Invalid data')
