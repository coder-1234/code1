import smtplib
import sys
print('Welcome to Thapar ATM')
restart=('Yes')
t = 3
s=smtplib.SMTP('smtp.gmail.com',587) 
balance = 2000
while t >= 0:
    pin = int(input('Please Enter You 4 Digit Pin: '))
    if pin == (1234):
        print('You entered you pin Correctly\n')
        while restart not in ('N'):
            print('1. Balance\n')
            print('2. Make a Withdrawl\n')
            print('3. Change Pin\n')
            print('4. exit')
            option = int(input('What do you want to choose?'))
            

            if option == 1:
                print('Your Balance is ',balance,'\n')
                restart = input('Want to go back? ')
                if restart in ('N'):
                    print('Thank You')
                    break

            elif option == 2:
                withdrawl = float(input('Please Enter Desired amount:')) 
                balance=balance-withdrawl
                print('collect your cash')   
                s=smtplib.SMTP('smtp.gmail.com',587) 
                s.starttls() 
                s.login("hitarthgandhi2708@gmail.com", "Ghitarth@2000") 
                message = "balance deducted"+str(balance)
                s.sendmail("hitarthgandhi2708@gmail.com", "hitarthgandhi2708@gmail.com", message) 
                s.quit()             
                restart = input('Would You you like to go back? ')
                if restart in ('N'):
                    break
        
            elif option == 3:
                print('Enter new pin\n')
                pin=int(input())
            elif option == 4:
                exit()
                    
            else:
                print('wrong choice\n')
                restart = ('y')
    elif pin != ('1234'):
        print('Incorrect Password')
        t = t - 1
        if t == 0:
            print('\nNo try left')
            break
       