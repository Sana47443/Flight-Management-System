#import mysql.connector
#obj=mysql.connector.connect(host='localhost',database='school',user='root',password='Sana1234$')
import random,csv
import datetime
import calendar
import os
import ast
from prettytable import PrettyTable
l=[['Flight No.','Dep apt','Arr apt','Dep Time','Arr Time','Economy','Business','First class']]
l1=[['Flight No.','Dep apt','Arr apt','Dep Time','Arr Time','Economy','Business','First class']]
l3=[['Booking Number','Name','Phone number','Nationality','Departure airport','Arrival Airport','Date','Time','Class','Food','Seat number']]
l4=[['Flight No.','Dep apt','Arrival apt','Adult Economy','Adult Business','Adult First_class','Child Economy','Child Business','Child First_class','Infant Economy','Infant Business','Infant First_class']]
l5=[['Flight No.','Dep apt','Arrival apt','Adult Economy','Adult Business','Adult First_class','Child Economy','Child Business','Child First_class','Infant Economy','Infant Business','Infant First_class']]
with open('IntlFlights.csv','r',newline='') as c1:
    r=csv.reader(c1)
    for i in r:
        if i[0]!='Flight No.':
            l.append(i)
    c1.close()
with open('DomFlights.csv','r',newline='') as c2:
    r=csv.reader(c2)
    for i in r:
        if i[0]!='Flight No.':
            l1.append(i)
    c2.close()
#print(l1)
with open('IntlFlightFares.csv','r',newline='') as c8:
    r=csv.reader(c8)
    for i in r:
        if i[0]!='Flight No.':
                l4.append(i)
    c8.close()
#print(l4)
with open('DomFlightFares.csv','r',newline='') as c12:
    r=csv.reader(c12)
    for i in r:
        if i[0]!='Flight No.':
                l5.append(i)
    c12.close()
def INTL(n):
    global l3
    adult=0
    infant=0
    child=0
    for i in range(n):
        for i in l:
                if (i[1]==loc1 and i[2]==loc2) and i!=n:
                    if (c1=='E' and len(i[5])==0) or (c1=='B' and len(i[6])==0) or (c1=='F' and len(i[7])==0):
                        print('Sorry all seats are booked')
                        break
        else:
            bno=random.randint(10000,99999)
            name=input('Enter your name:')
            ph=input('Enter your Contact No.:')
            nation=input('Nationality:')
            dob1=input('Date of Birth (yyyy-mm-dd):')
            a2=dob1[0:4]
            a2=int(a2)
            a22=dob1[5:7]
            if a22[0]=='0':
                a22=int(a22[1])
            else:
                a22=int(a22)
            a222=dob1[8:10]
            if a222[0]=='0':
                a222=int(a222[1])
            else:
                a222=int(a222)
            k1=datetime.date.today()
            while True:
                a2=dob1[0:4]
                a2=int(a2)
                a22=dob1[5:7]
                if a22[0]=='0':
                    a22=int(a22[1])
                else:
                    a22=int(a22)
                a222=dob1[8:10]
                if a222[0]=='0':
                    a222=int(a222[1])
                else:
                    a222=int(a222)
                if k1.year>a2>=2019:
                    print('Verified INFANT')
                    infant+=1
                    break
                elif k1.year==a2:
                    if k1.month>a22:
                        print('Verified INFANT')
                        infant+=1
                        break
                    elif k1.month==a22:
                        if k1.day>a222:
                            print('Verified INFANT')
                            infant+=1
                            break
                        else:
                            print('Invalid DOB')
                            dob1=input('Date of Birth (yyyy-mm-dd):')
                    else:
                        print('Invalid DOB')
                        dob1=input('Date of Birth (yyyy-mm-dd):')
                elif k1.year>a2>=2009:
                    print('Verified CHILD')
                    child+=1
                    break
                elif k1.year==a2:
                    if k1.month>a22:
                        print('Verified CHILD')
                        child+=1
                        break
                    elif k1.month==a22:
                        if k1.day>a222:
                            print('Verified CHILD')
                            child+=1
                            break
                        else:
                            print('Invalid DOB')
                            dob1=input('Date of Birth (yyyy-mm-dd):')
                    else:
                        print('Invalid DOB')
                        dob1=input('Date of Birth (yyyy-mm-dd):')
                elif 2008>a2:
                    print('Verfied ADULT')
                    adult+=1
                    break
                elif 2008==a2:
                    if k1.month>a22:
                        print('Verfied ADULT')
                        adult+=1
                        break
                    elif k1.month==a22:
                        if k1.day>a222:
                            print('Verified ADULT')
                            adult+=1
                            break
                        else:
                            print('Invalid DOB')
                            dob1=input('Date of Birth (yyyy-mm-dd):')
                    else:
                        print('Invalid DOB')
                        dob1=input('Date of Birth (yyyy-mm-dd):')
                else:
                    print('Invalid DOB')
                    dob1=input('Date of Birth (yyyy-mm-dd):')
            pn=input('Enter your passport number:')
            while True:
                if len(pn)<8:
                    print('Invalid No')
                    pn=input('Enter pass No.:')
                else:
                    break
            pass1=input('Enter expiration date(yyyy-mm-dd):')
            a1=pass1[0:4]
            a1=int(a1)
            a11=pass1[5:7]
            if a11[0]=='0':
                a11=int(a11[1])
            else:
                a11=int(a11)
            a111=pass1[8:10]
            if a111[0]=='0':
                a111=int(a111[1])
            else:
                a111=int(a111)
            k=datetime.date.today()
            while True:
                a1=pass1[0:4]
                a1=int(a1)
                a11=pass1[5:7]
                if a11[0]=='0':
                    a11=int(a11[1])
                else:
                    a11=int(a11)
                a111=pass1[8:10]
                if a111[0]=='0':
                    a111=int(a111[1])
                else:
                    a111=int(a111)
                if k.year<a1:
                    print('Verified')
                    break
                elif k.year==a1:
                    if k.month>a11:
                        print('Invalid Passport')
                        pass1=input('Passport date of expiry(yyyy-mm-dd):')
                    elif k.month<a11:
                        print('Verified')
                        break
                    elif k.month==a11:
                        if k.day<a111:
                            print('Verified')
                            break
                        else:
                            print('Invalid Passport')
                            pass1=input('Passport date of expiry(yyyy-mm-dd):')
                else:
                    print('Invalid Passport')
                    pass1=input('Passport date of expiry(yyyy-mm-dd):')
            food=input('Enter V for veg and NV for non-veg:')
            tic=[bno,name,ph,nation,loc1,loc2,date,time,c1,food]
            for i in l:
                    if i[1]==loc1 and i[2]==loc2:
                        if c1=='E':
                            lp=ast.literal_eval(i[5])
                            E=PrettyTable(['Economy'])
                            E.add_row([lp])
                            print(E)
                            x1=input('Enter your seat:')
                            tic+=[x1]
                            lp.remove(x1)
                            i[5]=str(lp)
                        elif c1=='B':
                            lr=ast.literal_eval(i[6])
                            B=PrettyTable(['Business'])
                            B.add_row([lr])
                            print(B)
                            x2=input('Enter your seat:')
                            tic+=[x2]
                            lr.remove(x2)
                            i[6]=str(lr)
                        elif c1=='F':
                            ls=ast.literal_eval(i[7])
                            FC=PrettyTable(['First Class'])
                            FC.add_row([ls])
                            print(FC)
                            x3=input('Enter your seat:')
                            tic+=[x3]
                            ls.remove(x3)
                            i[7]=str(ls)
            l3+=[tic]
    tfare=0
    for i in range(len(l4)):
        if l4[i][1]==loc1 and l4[i][2]==loc2 and i!=0:
            if c1=='E':
                tfare=adult*(int(l4[i][3][1:].replace(',','')))+child*(int(l4[i][6][1:].replace(',','')))+ infant*(int(l4[i][9][1:].replace(',','')))
            elif c1=='B':
                tfare=adult*(int(l4[i][4][1:].replace(',','')))+child*(int(l4[i][7][1:].replace(',','')))+ infant*(int(l4[i][10][1:].replace(',','')))
            elif c1=='F':
                tfare=adult*(int(l4[i][5][1:].replace(',','')))+child*(int(l4[i][8][1:].replace(',','')))+ infant*(int(l4[i][11][1:].replace(',','')))
    print('Your total flight fare:','$'+str(tfare))
    bank=input('Enter your bank:')
    cd=input('Enter your credit card no:')
    cvv=input('Enter your cvv code:')
    while True:
        if len(cvv)!=3:
            print('Invalid Code')
            cvv=input('Enter your cvv code:')
        else:
            break
    exp=input('Enter expiration date(yy-mm):')
    exp1=int(exp[0:2])
    while True:
        if exp1<21:
            print('Invalid date')
            exp=input('Enter expiration date(yy-mm):')
            exp1=int(exp[0:2])
        else:
            break
    print()
    print('Payment made successfully!')
def DOM(n):
    global l3
    adult=0
    infant=0
    child=0
    for i in range(n):
        for i in l1:
                if (i[1]==loc1 and i[2]==loc2) and i!=n:
                    if (cl1=='E' and len(i[5])==0) or (cl1=='B' and len(i[6])==0) or (cl1=='F' and len(i[7])==0):
                        print('Sorry all seats are booked')
                        break
        else:
            bno=random.randint(10000,99999)
            name=input('Enter your name:')
            ph=input('Enter your phone number:')
            nation=input('Nationality:')
            dob1=input('Date of Birth(yyyy-mm-dd):')
            a2=dob1[0:4]
            a2=int(a2)
            a22=dob1[5:7]
            if a22[0]=='0':
                a22=int(a22[1])
            else:
                a22=int(a22)
            a222=dob1[8:10]
            if a222[0]=='0':
                a222=int(a222[1])
            else:
                a222=int(a222)
            k1=datetime.date.today()
            while True:
                a2=dob1[0:4]
                a2=int(a2)
                a22=dob1[5:7]
                if a22[0]=='0':
                    a22=int(a22[1])
                else:
                    a22=int(a22)
                a222=dob1[8:10]
                if a222[0]=='0':
                    a222=int(a222[1])
                else:
                    a222=int(a222)
                if k1.year>a2>=2019:
                    print('Verified INFANT')
                    infant+=1
                    break
                elif k1.year==a2:
                    if k1.month>a22:
                        print('Verified INFANT')
                        infant+=1
                        break
                    elif k1.month==a22:
                        if k1.day>a222:
                            print('Verified INFANT')
                            infant+=1
                            break
                        else:
                            print('Invalid DOB')
                            dob1=input('Date of Birth (yyyy-mm-dd):')
                    else:
                        print('Invalid DOB')
                        dob1=input('Date of Birth (yyyy-mm-dd):')
                elif k1.year>a2>=2009:
                    print('Verified CHILD')
                    child+=1
                    break
                elif k1.year==a2:
                    if k1.month>a22:
                        print('Verified CHILD')
                        child+=1
                        break
                    elif k1.month==a22:
                        if k1.day>a222:
                            print('Verified CHILD')
                            child+=1
                            break
                        else:
                            print('Invalid DOB')
                            dob1=input('Date of Birth (yyyy-mm-dd):')
                    else:
                        print('Invalid DOB')
                        dob1=input('Date of Birth (yyyy-mm-dd):')
                elif 2008>a2:
                    print('Verfiied ADULT')
                    adult+=1
                    break
                elif 2008==a2:
                    if k1.month>a22:
                        print('Verfiied ADULT')
                        adult+=1
                        break
                    elif k1.month==a22:
                        if k1.day>a222:
                            print('Verified ADULT')
                            adult+=1
                            break
                        else:
                            print('Invalid DOB')
                            dob1=input('Date of Birth (yyyy-mm-dd):')
                    else:
                        print('Invalid DOB')
                        dob1=input('Date of Birth (yyyy-mm-dd):')
                else:
                    print('Invalid DOB')
                    dob1=input('Date of Birth (yyyy-mm-dd):')
            pn=input('Enter your passport number:')
            while True:
                if len(pn)<8:
                    print('Invalid No')
                    pn=input('Enter pass No.:')
                else:
                    break
            pass1=input('Enter expiration date(yyyy-mm-dd):')
            a1=pass1[0:4]
            a1=int(a1)
            a11=pass1[5:7]
            if a11[0]=='0':
                a11=int(a11[1])
            else:
                a11=int(a11)
            a111=pass1[8:10]
            if a111[0]=='0':
                a111=int(a111[1])
            else:
                a111=int(a111)
            k=datetime.date.today()
            while True:
                a1=pass1[0:4]
                a1=int(a1)
                a11=pass1[5:7]
                if a11[0]=='0':
                    a11=int(a11[1])
                else:
                    a11=int(a11)
                a111=pass1[8:10]
                if a111[0]=='0':
                    a111=int(a111[1])
                else:
                    a111=int(a111)
                if k.year<a1:
                    print('Verified')
                    break
                elif k.year==a1:
                    if k.month>a11:
                        print('Invalid Passport')
                        pass1=input('Passport date of expiry(yyyy-mm-dd):')
                    elif k.month<a11:
                        print('Verified')
                        break
                    elif k.month==a11:
                        if k.day<a111:
                            print('Verified')
                            break
                        else:
                            print('Invalid Passport')
                            pass1=input('Passport date of expiry(yyyy-mm-dd):')
                else:
                    print('Invalid Passport')
                    pass1=input('Passport date of expiry(yyyy-mm-dd):')
            food=input('Enter V for veg and NV for non-veg:')
            tic=[bno,name,ph,nation,loc1,loc2,date,time,cl1,food]
            for i in l1:
                    if i[1]==loc1 and i[2]==loc2:
                        if cl1=='E':
                            lp1=ast.literal_eval(i[5])
                            E1=PrettyTable(['Economy'])
                            E1.add_row([lp1])
                            print(E1)
                            x1=input('Enter your seat:')
                            tic+=[x1]
                            lp1.remove(x1)
                            i[5]=str(lp1)
                        elif cl1=='B':
                            lr1=ast.literal_eval(i[6])
                            B1=PrettyTable(['Business'])
                            B1.add_row([lr1])
                            print(B1)
                            x2=input('Enter your seat:')
                            tic+=[x2]
                            lr1.remove(x2)
                            i[6]=str(lr1)
                        elif cl1=='F':
                            ls1=ast.literal_eval(i[7])
                            FC1=PrettyTable(['First Class'])
                            FC1.add_row([ls1])
                            print(FC1)
                            x3=input('Enter your seat:')
                            tic+=[x3]
                            ls1.remove(x3)
                            i[7]=str(ls1)
            l3+=[tic]
    tfare=0
    for i in range(len(l5)):
        if l5[i][1]==loc1 and l5[i][2]==loc2 and i!=0:
            if cl1=='E':
                tfare=adult*(int(l5[i][3][1:]))+child*(int(l5[i][6][1:]))+ infant*(int(l5[i][9][1:]))
            elif cl1=='B':
                tfare=adult*(int(l5[i][4][1:]))+child*(int(l5[i][7][1:]))+ infant*(int(l5[i][10][1:]))
            elif cl1=='F':
                tfare=adult*(int(l5[i][5][1:]))+child*(int(l5[i][8][1:]))+ infant*(int(l5[i][11][1:]))
            print('Your total flight fare:','$'+str(tfare))
    bank=input('Enter your bank:')
    cd=input('Enter your credit card no:')
    cvv=input('Enter your cvv code:')
    while True:
        if len(cvv)!=3:
            print('Invalid Code')
            cvv=input('Enter your cvv code:')
        else:
            break
    exp=input('Enter expiration date(yy-mm):')
    exp1=int(exp[0:2])
    while True:
        if exp1<21:
            print('Invalid date')
            exp=input('Enter expiration date(yy-mm):')
            exp1=int(exp[0:2])
        else:
            break
    print()
    print('Payment made successfully!')
#print(l5)
intl1=[]
dom1=[]
op1=len(l)
op2=len(l1)
for i in range(1,op1):
    a=l[i][0]
    b=l[i][1]
    c=l[i][2]
    intl1.extend([a,b,c])
for i in range(1,op2):
    a1=l1[i][0]
    b1=l1[i][1]
    c1=l1[i][2]
    dom1.extend([a1,b1,c1])
F=PrettyTable(['Flight No.','Dep apt','Arrival apt','Adult E','Adult B','Adult FC','Child E','Child B','Child FC','Infant E','Infant B','Infant FC'])
D=PrettyTable(['Flight No.','Dep apt','Arrival apt','Adult E','Adult B','Adult FC','Child E','Child B','Child FC','Infant E','Infant B','Infant FC'])
print('Welcome to Fly airlines!\n')
print('PRESS 1: To access admin server:')
print('PRESS 2: To access user server:')
ch=int(input('Enter your choice:'))
if ch==1:
    ut=input('\nUSERNAME:')
    ut1=input('PASSWORD:')
    if ut=='airline7' and ut1=='airline7':
        print('VERIFIED')
        print('\n***WELCOME TO ADMIN FLIGHT DATABASE MANAGEMENT SYSTEM***')
        while True:
            print('\nPRESS 1: To add flight')
            print('PRESS 2: To change destinations')
            print('PRESS 3: To modify timings')
            print('PRESS 4: To change fares')
            print('PRESS 5: To add seats')
            print('PRESS 6: To delete flight')
            print('PRESS 7: To view all flights')
            print('PRESS 8: To view all bookings')
            print('PRESS 9: To view feedbacks')
            cho1=int(input("Pls enter choice:"))
            if cho1==1:
                    while True:
                            print('\nPRESS 1: International Flights')
                            print('PRESS 2: Domestic Flights')
                            cho2=int(input('Pls enter choice:'))
                            if cho2==1:
                                lm=[]
                                gh=[]
                                le=[]
                                lb=[]
                                lf=[]
                                fl1=input('\nFlight No.:')
                                fl2=input('Departure Destination:')
                                fl3=input('Arrival Destination:')
                                fl4=input('Departure Timing:')
                                fl5=input('Arrival Timing:')
                                fl6=int(input('\nNo. of seats in Economy:'))
                                for i in range(fl6):
                                        a=input('Seat No.:')
                                        le.append(a)
                                fl7=int(input('\nNo. of seats in Business:'))
                                for i in range(fl7):
                                        b=input('Seat No.:')
                                        lb.append(b)
                                fl8=int(input('\nNo. of seats in First Class:'))
                                for i in range(fl8):
                                        c=input('Seat No.:')
                                        lf.append(c)
                                lm.extend([fl1,fl2,fl3,fl4,fl5,le,lb,lf])
                                mk=input('\nInfant Economy Fare:')
                                mk1=input('Infant Business Fare:')
                                mk2=input('Infant First Class Fare:')
                                mk3=input('Child Economy Fare:')
                                mk4=input('Child Business Fare:')
                                mk5=input('Child First Class Fare:')
                                mk6=input('Adult Economy Fare:')
                                mk7=input('Adult Business Fare:')
                                mk8=input('Adult First Class Fare:')
                                gh.extend([fl1,fl2,fl3,mk6,mk7,mk8,mk3,mk4,mk5,mk,mk1,mk2])
                                with open('IntlFlights.csv','a',newline='')as c50:
                                        a=csv.writer(c50,delimiter=',')
                                        a.writerow(lm)
                                        c50.close()
                                with open('IntlFlightFares.csv','a',newline='')as c100:
                                        a=csv.writer(c100,delimiter=',')
                                        a.writerow(gh)
                                        c100.close()
                            elif cho2==2:
                                lm1=[]
                                gh1=[]
                                le1=[]
                                lb1=[]
                                lf1=[]
                                fl11=input('\nFlight No.:')
                                fl21=input('Departure Destination:')
                                fl31=input('Arrival Destination:')
                                fl41=input('Departure Timing:')
                                fl51=input('Arrival Timing:')
                                fl61=int(input('\nNo. of seats in Economy:'))
                                for i in range(fl61):
                                        a=input('Seat No.:')
                                        le1.append(a)
                                fl71=int(input('\nNo. of seats in Business:'))
                                for i in range(fl71):
                                        b=input('Seat No.:')
                                        lb1.append(b)
                                fl81=int(input('\nNo. of seats in First Class:'))
                                for i in range(fl81):
                                        c=input('Seat No.:')
                                        lf1.append(c)
                                lm1.extend([fl11,fl21,fl31,fl41,fl51,le1,lb1,lf1])
                                mk1=input('\nInfant Economy Fare:')
                                mk11=input('Infant Business Fare:')
                                mk21=input('Infant First Class Fare:')
                                mk31=input('Child Economy Fare:')
                                mk41=input('Child Business Fare:')
                                mk51=input('Child First Class Fare:')
                                mk61=input('Adult Economy Fare:')
                                mk71=input('Adult Business Fare:')
                                mk81=input('Adult First Class Fare:')
                                gh1.extend([fl11,fl21,fl31,mk61,mk71,mk81,mk31,mk41,mk51,mk1,mk11,mk21])
                                with open('DomFlights.csv','a',newline='')as c51:
                                        a=csv.writer(c51,delimiter=',')
                                        a.writerow(lm1)
                                        c51.close()
                                with open('DomFlightFares.csv','a',newline='')as c101:
                                        a=csv.writer(c101,delimiter=',')
                                        a.writerow(gh1)
                                        c101.close()
                            else:
                                    break
            elif cho1==2:
                    while True:
                            print('\nPRESS 1: International Flights:')
                            print('PRESS 2: Domestic Flights')
                            cho3=int(input('Pls enter choice:'))
                            if cho3==1:
                                    ap=input('\nFlight No.:')
                                    z1=0
                                    with open('IntlFlights.csv','r',newline='') as c52:
                                        r=csv.reader(c52)
                                        for i in r:
                                            if i[0]==ap:
                                                z1+=1      
                                    if z1==1:
                                        with open('IntlFlightsN.csv','w',newline='') as c40:
                                            w=csv.writer(c40,delimiter=',')
                                            with open('IntlFlights.csv','r',newline='') as c500:
                                                r=csv.reader(c500)
                                                for i in r:
                                                    if i[0]==ap:
                                                        dt=input('Enter new departure destination:')
                                                        ar=input('Enter new arrival destination:')
                                                        i[1]=dt
                                                        i[2]=ar
                                                        w.writerow(i)
                                                    else:
                                                        w.writerow(i)
                                                c500.close()
                                            c40.close()
                                        os.remove('IntlFlights.csv')
                                        os.rename('IntlFlightsN.csv','IntlFlights.csv')
                                        with open('IntlFlightFaresN.csv','w',newline='') as c140:
                                            w=csv.writer(c140,delimiter=',')
                                            with open('IntlFlightFares.csv','r',newline='') as c1500:
                                                r=csv.reader(c1500)
                                                for i in r:
                                                    if i[0]==ap:
                                                        i[1]=dt
                                                        i[2]=ar
                                                        w.writerow(i)
                                                    else:
                                                        w.writerow(i)
                                                c1500.close()
                                            c140.close()
                                        os.remove('IntlFlightFares.csv')
                                        os.rename('IntlFlightFaresN.csv','IntlFlightFares.csv')
                                    else:
                                        print('Flight not found')
                                        break
                            elif cho3==2:
                                    ap1=input('\nFlight No.:')
                                    z2=0
                                    with open('DomFlights.csv','r',newline='') as c53:
                                        r=csv.reader(c53)
                                        for i in r:
                                            if i[0]==ap1:
                                                z2+=1
                                        c53.close()
                                    if z2==1:
                                        with open('DomFlightsN.csv','w',newline='') as c41:
                                            w=csv.writer(c41,delimiter=',')
                                            with open('DomFlights.csv','r',newline='') as c501:
                                                r=csv.reader(c501)
                                                for i in r:
                                                    if i[0]==ap1:
                                                        dt=input('Enter new departure destination:')
                                                        ar=input('Enter new arrival destination:')
                                                        i[1]=dt
                                                        i[2]=ar
                                                        w.writerow(i)
                                                    else:
                                                        w.writerow(i)
                                                c501.close()
                                            c41.close()
                                        os.remove('DomFlights.csv')
                                        os.rename('DomFlightsN.csv','DomFlights.csv')
                                        with open('DomFlightFaresN.csv','w',newline='') as c141:
                                            w=csv.writer(c141,delimiter=',')
                                            with open('DomFlightFares.csv','r',newline='') as c1501:
                                                r=csv.reader(c1501)
                                                for i in r:
                                                    if i[0]==ap1:
                                                        i[1]=dt
                                                        i[2]=ar
                                                        w.writerow(i)
                                                    else:
                                                        w.writerow(i)
                                                c1501.close()
                                            c141.close()
                                        os.remove('DomFlightFares.csv')
                                        os.rename('DomFlightFaresN.csv','DomFlightFares.csv')
                                    else:
                                        print('Flight not found')
                                        break
                            else:
                                    break
                    else:
                        break
            elif cho1==3:
                    while True:
                            print('\nPRESS 1: International Flights:')
                            print('PRESS 2: Domestic Flights')
                            cho4=int(input('Pls enter choice:'))
                            if cho4==1:
                                z3=0
                                ap2=input('\nFlight No.:')
                                with open('IntlFlights.csv','r',newline='') as c54:
                                    r=csv.reader(c54)
                                    for i in r:
                                        if i[0]==ap2:
                                            z3+=1
                                    c54.close()
                                if z3==1:
                                    with open('IntlFlightsNE.csv','w',newline='') as c43:
                                        w=csv.writer(c43)
                                        with open('IntlFlights.csv','r',newline='') as c502:
                                            r=csv.reader(c502)
                                            for i in r:
                                                if i[0]==ap2:
                                                    i[3]=input('Enter dept time:')
                                                    i[4]=input('Enter arr time:')
                                                    w.writerow(i)
                                                else:
                                                    w.writerow(i)
                                            c502.close()
                                        c43.close()
                                    os.remove('IntlFlights.csv')
                                    os.rename('IntlFlightsNE.csv','IntlFlights.csv')
                                else:
                                    print('Flight not found')
                                    break
                            elif cho4==2:
                                    ap3=input('\nFlight No.:')
                                    z4=0
                                    with open('DomFlights.csv','r',newline='') as c55:
                                        r=csv.reader(c55)
                                        for i in r:
                                            if i[0]==ap3:
                                                z4+=1
                                        c55.close()
                                    if z4==1:
                                        with open('DomFlightsNE.csv','w',newline='') as c44:
                                            w=csv.writer(c44)
                                            with open('DomFlights.csv','r',newline='') as c503:
                                                r=csv.reader(c503)
                                                for i in r:
                                                    if i[0]==ap3:
                                                        i[3]=input('Enter dept time:')
                                                        i[4]=input('Enter arr time:')
                                                        w.writerow(i)
                                                    else:
                                                        w.writerow(i)
                                                c503.close()
                                            c44.close()
                                        os.remove('DomFlights.csv')
                                        os.rename('DomFlightsNE.csv','DomFlights.csv')
                                    else:
                                        print('Flight not found')
                                        break
                            else:
                                    break
                    else:
                        break
            elif cho1==4:
                    while True:
                            print('\nPRESS 1: International Flights:')
                            print('PRESS 2: Domestic Flights')
                            cho5=int(input('Pls enter choice:'))
                            if cho5==1:
                                    ap4=input('\nFlight No.:')
                                    z5=0
                                    with open('IntlFlights.csv','r',newline='') as c56:
                                        r=csv.reader(c56)
                                        for i in r:
                                            if i[0]==ap4:
                                                z5+=1
                                        c56.close()
                                    if z5==1:
                                        print('\nPRESS 1: Change Infant Fares')
                                        print('PRESS 2: Change Child Fares')
                                        print('PRESS 3: Change Adult Fares')
                                        cho11=int(input('Pls enter Choice:'))
                                        if cho11==1:
                                            infe=input('\nInfant Economy:')
                                            infb=input('Infant Business:')
                                            inff=input('Infant First Class:')
                                            with open('IntlFlightFaresN.csv','w',newline='') as c700:
                                                w=csv.writer(c700,delimiter=',')
                                                with open('IntlFlightFares.csv','r',newline='') as c205:
                                                    r=csv.reader(c205)
                                                    for j in r:
                                                        if j[0]==ap4:
                                                            j[9]=infe
                                                            j[10]=infb
                                                            j[11]=inff
                                                            w.writerow(j)
                                                        else:
                                                            w.writerow(j)
                                                    c205close()
                                                c700.close()
                                            os.remove('IntlFlightFares.csv')
                                            os.rename('IntlFlightFaresN.csv','IntlFlightFares.csv')
                                        elif cho11==2:
                                            chie=input('\nChild Economy:')
                                            chib=input('Child Business:')
                                            chif=input('Child First Class:')
                                            with open('IntlFlightFaresN.csv','w',newline='') as c701:
                                                w=csv.writer(c701,delimiter=',')
                                                with open('IntlFlightFares.csv','r',newline='') as c206:
                                                    r=csv.reader(c206)
                                                    for j in r:
                                                        if j[0]==ap4:
                                                            j[6]=chie
                                                            j[7]=chib
                                                            j[8]=chif
                                                            w.writerow(j)
                                                        else:
                                                            w.writerow(j)
                                                    c206.close()
                                                c701.close()
                                            os.remove('IntlFlightFares.csv')
                                            os.rename('IntlFlightFaresN.csv','IntlFlightFares.csv')
                                        elif cho11==3:
                                            adue=input('\nAdult Economy:')
                                            adub=input('Adult Business:')
                                            aduf=input('Adult First Class:')
                                            with open('IntlFlightFaresN.csv','w',newline='') as c702:
                                                w=csv.writer(c702,delimiter=',')
                                                with open('IntlFlightFares.csv','r',newline='') as c207:
                                                    r=csv.reader(c207)
                                                    for j in r:
                                                        if j[0]==ap4:
                                                            j[3]=adue
                                                            j[4]=adub
                                                            j[5]=aduf
                                                            w.writerow(j)
                                                        else:
                                                            w.writerow(j)
                                                    c207.close()
                                                c702.close()
                                            os.remove('IntlFlightFares.csv')
                                            os.rename('IntlFlightFaresN.csv','IntlFlightFares.csv')
                                    else:
                                        print('Flight Not Found')
                                        break
                            elif cho5==2:
                                    ap10=input('\nFlight No.:')
                                    z6=0
                                    with open('DomFlights.csv','r',newline='') as c90:
                                        r=csv.reader(c90)
                                        for i in r:
                                            if i[0]==ap10:
                                                z6+=1
                                    if z6==1:
                                        print('\nPRESS 1: Change Infant Fares')
                                        print('PRESS 2: Change Child Fares')
                                        print('PRESS 3: Change Adult Fares')
                                        cho90=int(input('Pls enter Choice:'))
                                        if cho90==1:
                                            infe=input('\nInfant Economy:')
                                            infb=input('Infant Business:')
                                            inff=input('Infant First Class:')
                                            with open('DomFlightFaresN.csv','w',newline='') as c91:
                                                w=csv.writer(c91,delimiter=',')
                                                with open('DomFlightFares.csv','r',newline='') as c208:
                                                    r=csv.reader(c208)
                                                    for j in r:
                                                        if j[0]==ap10:
                                                            j[9]=infe
                                                            j[10]=infb
                                                            j[11]=inff
                                                            w.writerow(j)
                                                        else:
                                                            w.writerow(j)
                                                    c208.close()
                                                c91.close()
                                            os.remove('DomFlightFares.csv')
                                            os.rename('DomFlightFaresN.csv','DomFlightFares.csv')
                                        elif cho90==2:
                                            chie=input('\nChild Economy:')
                                            chib=input('Child Business:')
                                            chif=input('Child First Class:')
                                            with open('DomFlightFaresN.csv','w',newline='') as c92:
                                                w=csv.writer(c92,delimiter=',')
                                                with open('DomFlightFares.csv','r',newline='') as c209:
                                                    r=csv.reader(c209)
                                                    for j in r:
                                                        if j[0]==ap10:
                                                            j[9]=chie
                                                            j[10]=chib
                                                            j[11]=chif
                                                            w.writerow(j)
                                                        else:
                                                            w.writerow(j)
                                                    c209.close()
                                                c92.close()
                                            os.remove('DomFlightFares.csv')
                                            os.rename('DomFlightFaresN.csv','DomFlightFares.csv')
                                        elif cho90==3:
                                            adue=input('\nAdult Economy:')
                                            adub=input('Adult Business:')
                                            aduf=input('Adult First Class:')
                                            with open('DomFlightFaresN.csv','w',newline='') as c93:
                                                w=csv.writer(c93,delimiter=',')
                                                with open('DomFlightFares.csv','r',newline='') as c210:
                                                    r=csv.reader(c210)
                                                    for j in r:
                                                        if j[0]==ap10:
                                                            j[9]=adue
                                                            j[10]=adub
                                                            j[11]=aduf
                                                            w.writerow(j)
                                                        else:
                                                            w.writerow(j)
                                                    c210.close()
                                                c93.close()
                                            os.remove('DomFlightFares.csv')
                                            os.rename('DomFlightFaresN.csv','DomFlightFares.csv')
                                    else:
                                        print('Flight Not Found')
                                        break
                            else:
                                break
                    else:
                        break
            elif cho1==5:
                    while True:
                            print('\nPRESS 1: International Flights:')
                            print('PRESS 2: Domestic Flights')
                            cho6=int(input('Pls enter choice:'))
                            if cho6==1:
                                    ap5=input('\nFlight No.:')
                                    z7=0
                                    with open('IntlFlights.csv','r',newline='') as c57:
                                        r=csv.reader(c57)
                                        for i in r:
                                            if i[0]==ap5:
                                                z7+=1
                                    if z7==1:
                                        print('\nPRESS 1: To add seats in Economy')
                                        print('PRESS 2: To add seats in Business')
                                        print('PRESS 3: To add seats in First Class')
                                        cho7=int(input('Pls enter your choice:'))
                                        if cho7==1:
                                            nj=int(input('No. of seats:'))
                                            with open('IntlFlightsN.csv','w',newline='') as c58:
                                                w=csv.writer(c58,delimiter=',')
                                                with open('IntlFlights.csv','r',newline='') as c211:
                                                    r=csv.reader(c211)
                                                    for j in r:
                                                        if j[0]==ap5:
                                                            j[5]=ast.literal_eval(j[5])
                                                            if j[5]=='Fully Booked':
                                                                j[5]=[]
                                                                for k in range(nj):
                                                                    kj=input('Seat No.:')
                                                                    j[5].append(kj)
                                                                w.writerow(j)
                                                            else:
                                                                for k in range(nj):
                                                                    kj=input('Seat No.:')
                                                                    j[5].append(kj)
                                                                w.writerow(j)
                                                        else:
                                                            w.writerow(j)
                                                    c211.close()
                                                c58.close()
                                            os.remove('IntlFlights.csv')
                                            os.rename('IntlFlightsN.csv','IntlFlights.csv')
                                        elif cho7==2:
                                            nj1=int(input('No. of seats:'))
                                            with open('IntlFlightsN.csv','w',newline='') as c59:
                                                w=csv.writer(c59,delimiter=',')
                                                with open('IntlFlights.csv','r',newline='') as c212:
                                                    r=csv.reader(c212)
                                                    for j in r:
                                                        if j[0]==ap5:
                                                            j[6]=ast.literal_eval(j[6])
                                                            if j[6]=='Fully Booked':
                                                                j[6]=[]
                                                                for k in range(nj1):
                                                                    kj1=input('Seat No.:')
                                                                    j[6].append(kj1)
                                                                w.writerow(j)
                                                            else:
                                                                for k in range(nj):
                                                                    kj1=input('Seat No.:')
                                                                    j[6].append(kj1)
                                                                w.writerow(j)
                                                        else:
                                                            w.writerow(j)
                                                    c212.close()
                                                c59.close()
                                            os.remove('IntlFlights.csv')
                                            os.rename('IntlFlightsN.csv','IntlFlights.csv')
                                        elif cho7==3:
                                            nj2=int(input('No. of seats:'))
                                            with open('IntlFlightsN.csv','w',newline='') as c60:
                                                w=csv.writer(c60,delimiter=',')
                                                with open('IntlFlights.csv','r',newline='') as c213:
                                                    r=csv.reader(c213)
                                                    for j in r:
                                                        if j[0]==ap5:
                                                            j[7]=ast.literal_eval(j[7])
                                                            if j[7]=='Fully Booked':
                                                                j[7]=[]
                                                                for k in range(nj2):
                                                                    kj2=input('Seat No.:')
                                                                    j[7].append(kj2)
                                                                w.writerow(j)
                                                            else:
                                                                for k in range(nj):
                                                                    kj2=input('Seat No.:')
                                                                    j[7].append(kj2)
                                                                w.writerow(j)
                                                        else:
                                                            w.writerow(j)
                                                    c213.close()
                                                c60.close()
                                            os.remove('IntlFlights.csv')
                                            os.rename('IntlFlightsN.csv','IntlFlights.csv')

                                        else:
                                            break
                                    else:
                                        print('Flight Not Found')
                                        break
                            elif cho6==2:
                                    ap6=input('\nFlight No.:')
                                    z8=0
                                    with open('DomFlights.csv','r',newline='') as c70:
                                        r=csv.reader(c70)
                                        for i in r:
                                            if i[0]==ap6:
                                                z8+=1
                                    if z8==1:
                                        print('\nPRESS 1: To add seats in Economy')
                                        print('PRESS 2: To add seats in Business')
                                        print('PRESS 3: To add seats in First Class')
                                        cho7=int(input('Pls enter your choice:'))
                                        if cho7==1:
                                            nj4=int(input('No. of seats:'))
                                            with open('DomFlightsN.csv','w',newline='') as c71:
                                                    w=csv.writer(c71,delimiter=',')
                                                    with open('DomFlights.csv','r',newline='') as c214:
                                                        r=csv.writer(c214)
                                                        for j in r:
                                                            if j[0]==ap6:
                                                                j[5]=ast.literal_eval(j[5])
                                                                if j[5]=='Fully Booked':
                                                                    j[5]=[]
                                                                    for k in range(nj4):
                                                                        kj4=input('Seat No.:')
                                                                        j[5].append(kj4)
                                                                    w.writerow(j)
                                                                else:
                                                                    for k in range(nj4):
                                                                        kj4=input('Seat No.:')
                                                                        j[5].append(kj4)
                                                                    w.writerow(j)
                                                            else:
                                                                w.writerow(j)
                                                        c214.close()
                                                    c71.close()
                                            os.remove('DomFlights.csv')
                                            os.rename('DomFlightsN.csv','DomFlights.csv') 
                                        elif cho7==2:
                                            nj5=int(input('No. of seats:'))
                                            with open('DomFlightsN.csv','w',newline='') as c72:
                                                    w=csv.writer(c72,delimiter=',')
                                                    with open('DomFlights.csv','r',newline='') as c215:
                                                        r=csv.writer(c215)
                                                        for j in r:
                                                            if j[0]==ap6:
                                                                j[6]=ast.literal_eval(j[6])
                                                                if j[6]=='Fully Booked':
                                                                    j[6]=[]
                                                                    for k in range(nj5):
                                                                        kj5=input('Seat No.:')
                                                                        j[6].append(kj5)
                                                                    w.writerow(j)
                                                                else:
                                                                    for k in range(nj5):
                                                                        kj5=input('Seat No.:')
                                                                        j[6].append(kj5)
                                                                    w.writerow(j)
                                                            else:
                                                                w.writerow(j)
                                                        c215.close()
                                                    c72.close()
                                            os.remove('DomFlights.csv')
                                            os.rename('DomFlightsN.csv','DomFlights.csv')
                                        elif cho7==3:
                                            nj6=int(input('No. of seats:'))
                                            with open('DomFlightsN.csv','w',newline='') as c73:
                                                    w=csv.writer(c73,delimiter=',')
                                                    with open('DomFlights.csv','r',newline='') as c216:
                                                        r=csv.writer(c216)
                                                        for j in a:
                                                            if j[0]==ap6:
                                                                j[7]=ast.literal_eval(j[7])
                                                                if j[7]=='Fully Booked':
                                                                    j[7]=[]
                                                                    for k in range(nj6):
                                                                        kj6=input('Seat No.:')
                                                                        j[7].append(kj6)
                                                                    w.writerow(j)
                                                                else:
                                                                    for k in range(nj6):
                                                                        kj6=input('Seat No.:')
                                                                        j[7].append(kj6)
                                                                    w.writerow(j)
                                                            else:
                                                                w.writerow(j)
                                            os.remove('DomFlights.csv')
                                            os.rename('DomFlightsN.csv','DomFlights.csv')

                                        else:
                                            break
                                    else:
                                        print('Flight Not Found')
                                        break
                            else:
                                    break
                    else:
                        break
            elif cho1==6:
                print('\nPRESS 1: International Flights')
                print('PRESS 2: Domestic Flights')
                cho99=int(input('Pls enter your choice:'))
                if cho99==1:
                    ap90=input('Flight No.:')
                    z9=0
                    with open('IntlFlights.csv','r',newline='') as c200:
                        r=csv.reader(c200)
                        for j in r:
                            if j[0]==ap90:
                                z9+=1
                        c200.close()
                    if z9==1:
                        with open('IntlFlightsN.csv','w',newline='') as c201:
                            w=csv.writer(c201,delimiter=',')
                            with open('IntlFlights.csv','r',newline='') as c202:
                                r=csv.reader(c202)
                                for j in r:
                                    if j[0]!=ap90:
                                        w.writerow(j)
                                c202.close()
                            c201.close()
                        os.remove('IntlFlights.csv')
                        os.rename('IntlFlightsN.csv','IntlFlights.csv')
                        print('\nFlight has been removed')
                        break
                    else:
                        print('Flight Not Found')
                        break
                elif cho99==2:
                    ap91=input('Flight No.:')
                    z10=0
                    with open('IntlFlights.csv','r',newline='') as c203:
                        r=csv.reader(c203)
                        for j in r:
                            if j[0]==ap91:
                                z10+=1
                        c203.close()
                    if z10==1:
                        with open('DomFlightsN.csv','w',newline='') as c204:
                            w=csv.writer(c204,delimiter=',')
                            with open('DomFlights.csv','r',newline='') as c205:
                                r=csv.reader(c205)
                                for j in r:
                                    if j[0]!=ap91:
                                        w.writerow(j)
                                c205.close()
                            c204.close()
                        os.remove('DomFlights.csv')
                        os.rename('DomFlightsN.csv','DomFlights.csv')
                        print('\nFlight has been removed')
                        break
                    else:
                        print('Flight Not Found')
                        break
                else:
                    break
            elif cho1==7:
                    print('\nPRESS 1: International Flights')
                    print('PRESS 2: Domestic Flights')
                    cho9=int(input('Pls enter your choice:'))
                    if cho9==1:
                            M=PrettyTable(['Flight No.','Dep apt','Arr apt','Dep Time','Arr Time','Economy','Business','First class'])
                            with open('IntlFlights.csv','r',newline='') as c74:
                                    r=csv.reader(c74)
                                    for j in r:
                                            if j[0]!='Flight No.':
                                                    M.add_row(j)
                                    print(M)
                                    c74.close()
                    elif cho9==2:
                            N=PrettyTable(['Flight No.','Dep apt','Arr apt','Dep Time','Arr Time','Economy','Business','First class'])
                            with open('DomFlights.csv','r',newline='') as c75:
                                    r=csv.reader(c75)
                                    for j in r:
                                            if j[0]!='Flight No.':
                                                    N.add_row(j)
                                    print(N)
                                    c75.close()
                    else:
                            break
            elif cho1==8:
                    print('\nPRESS 1: View all passengers bookings')
                    print('\nPRESS 2: View a passenger booking')
                    cho99=int(input('Pls enter your choice:'))
                    if cho99==1:
                        C=PrettyTable(['Booking Number','Name','Phone number','Nationality','Departure airport','Arrival Airport','Date','Time','Class','Food','Seat number'])
                        with open('Tickets.csv','r',newline='') as c1000:
                            r=csv.reader(c1000)
                            for i in r:
                                if i[0]!='Booking Number':
                                    C.add_row(i)
                            print(C)
                            c1000.close()
                    elif cho99==2:
                        A=PrettyTable(['Booking Number','Name','Phone number','Nationality','Departure airport','Arrival Airport','Date','Time','Class','Food','Seat number'])
                        bm=input('\nEnter Booking No.:')
                        with open('Tickets.csv','r',newline='') as c1000:
                            r=csv.reader(c1000)
                            for i in r:
                                if i[0]==bm:
                                    A.add_row(i)
                            else:
                                print('Booking No. not found')
                            print(A)
                            c1000.close()
            elif cho1==9:
                while True:
                    print('PRESS 1: To display all the recieved feedbacks')
                    print('PRESS 2: To display the feedback of a particular passenger')
                    print('PRESS 3: To update the status of a passenger')
                    print('PRESS 4: To delete a feedback')
                    print('PRESS 5: To display all feedbacks of a particular month having ratings less than 5')
                    print('PRESS 6: To display all feedbacks ratings wise where the complaint has not been addressed since 3 months')
                    print('PRESS 7: To display the count of feedbacks ratings wise')
                    print('PRESS 8: To display all feedbacks from latest to oldest')
                    print('PRESS 9: Exit')
                    ch1=int(input('Enter your choice:'))
                    if ch1==1:
                        c111=obj.cursor()
                        c111.execute('select * from feedback')
                        l111=c111.fetchall()
                        print()
                        for i1 in l111:
                            print(i1)
                        print()
                        c111.close()
                    elif ch1==2:
                        c111=obj.cursor()
                        x11=int(input('Enter booking number:'))
                        c111.execute('select * from feedback where Booking_number=%s',(x11,))
                        l11=c111.fetchall()
                        print()
                        for i1 in l11:
                            print(i1)
                        print()
                        c111.close()
                    elif ch1==3:
                        c111=obj.cursor()
                        x11=int(input('Enter booking number to be updated:'))
                        y11=input('Enter updated status:')
                        c111.execute('update feedback set status=%s where Booking_number=%s',(y11,x11))
                        obj.commit()
                        c111.close()
                    elif ch1==4:
                        c111=obj.cursor()
                        x11=int(input('Enter booking number to be deleted:'))
                        c111.execute('delete from feedback where Booking_number=%s',(x11,))
                        obj.commit()
                        c111.close()
                    elif ch1==5:
                        c111=obj.cursor()
                        x11=input('Enter month(mm):')
                        c111.execute("select * from feedback  where Date like concat( '____-',%s,'-__' ) and Passenger_Satisfaction_rating<5",(x11,))
                        l111=c111.fetchall()
                        print()
                        for i1 in l111:
                            print(i1)
                        print()
                        c111.close()
                    elif ch1==6:
                        c111=obj.cursor()
                        c111.execute("select Passenger_Satisfaction_rating,count(*) from feedback where timestampdiff(month,date,curdate())=3 and status='Not Viewed' group by  Passenger_Satisfaction_rating")
                        l111=c111.fetchall()
                        print()
                        print('Passenger_Satisfaction_rating','count')
                        for i1 in l111:
                            print(i1)
                        print()
                        c111.close()
                    elif ch1==7:
                        c111=obj.cursor()
                        c111.execute('select  Passenger_Satisfaction_rating ,count(*) "No of feedbacks" from feedback group by Passenger_Satisfaction_rating')
                        l111=c111.fetchall()
                        print()
                        print('Passenger_Satisfaction_rating','count')
                        for i1 in l111:
                            print(i1)
                        print()
                        c111.close()
                    elif ch1==8:
                        c111=obj.cursor()
                        c111.execute('select * from feedback order by date desc')
                        l111=c111.fetchall()
                        print()
                        for i1 in l111:
                            print(i1)
                        print()
                        c111.close()
                    elif ch1==9:
                        break
            else:
                break
elif ch==2:
    while True:
        print('\nPRESS 1: To book flights')
        print('PRESS 2: To modify bookings')
        print('PRESS 3: To view bookings')
        print('PRESS 4: To give feedbacks')
        choice=int(input('\nEnter your choice:'))
        if choice==1:
            print('\nWELCOME TO FLY AIRLINES')
            p=int(input('\nIf international,press 3 or if domestic,press 4:'))
            if p==3:
                with open('tn.csv','w',newline='') as c2:
                    w=csv.writer(c2,delimiter=',')
                    with open('IntlFlights.csv','r',newline='') as c1:
                        r=csv.reader(c1,delimiter=',')
                        for i in r:
                            if i[0]!='Flight No.':
                                if i[5]=='Fully Booked' or len(ast.literal_eval(i[5]))==0:
                                    i[5]='Fully Booked'
                                if i[6]=='Fully Booked' or len(ast.literal_eval(i[6]))==0:
                                    i[6]='Fully Booked'
                                if i[7]=='Fully Booked' or len(ast.literal_eval(i[7]))==0:
                                    i[7]='Fully Booked'
                                w.writerow(i)
                            else:
                                w.writerow(i)
                        c2.close()
                        c1.close()
                os.remove('IntlFlights.csv')
                os.rename('tn.csv','IntlFlights.csv')
                T=PrettyTable(['Flight No.','Dep apt','Arr apt','Dep Time','Arr Time'])
                for i in l:
                    lk=[]
                    if i[0]!='Flight No.':
                        lk.extend([i[0],i[1],i[2],i[3],i[4]])
                        T.add_row(lk)
                print(T)
                loc1=input('\nEnter your departure airport:')
                loc2=input('Enter your arrival airport:')
                o=0
                p=[]
                for i in l:
                    if i[1]==loc1 and i[2]==loc2:
                        o=1
                        p.append(i)
                        break
                if o==0:
                    print('Invalid')
                    break
                else:
                    dat=datetime.date.today()
                    dat1=str(dat)
                    tad=''
                    km=0
                    km=int(dat1[8:10])+1
                    tad=dat1[0:8]+str(km)
                    date=input('\nEnter departure date (yyyy-mm-dd):')
                    while True:
                        if date!=tad:
                            print('Invalid Date')
                            date=input('\nEnter departure date (yyyy-mm-dd):')
                        else:
                            break
                    time=input('Enter time:')
                    while True:
                        if time not in p[0]:
                            print('Invalid time')
                            time=input('Enter time:')
                        else:
                            break
                    for i in l4:
                        if i[0]!='Flight No.':
                            if i[1]==loc1 and i[2]==loc2:
                                F.add_row(i)
                    print(F)
                    c1=input('Enter your preffered class(E/B/F):')
                    if c1=='E':
                        for i in l:
                            if i[1]==loc1 and i[2]==loc2:
                                if len(ast.literal_eval(i[5]))==0:
                                    i[5]=='Fully Booked'
                                    print('Sorry all the seats are booked')
                                    break
                                else:
                                    n=int(input('Enter number of passengers:'))
                                    INTL(n)
                    elif c1=='B':
                        for i in l:
                            if i[1]==loc1 and i[2]==loc2:
                                if len(ast.literal_eval(i[6]))==0:
                                    i[6]=='Fully Booked'
                                    print('Sorry all the seats are booked')
                                    break
                                else:
                                    n=int(input('Enter number of passengers:'))
                                    INTL(n)
                    elif c1=='F':
                        for i in l:
                            if i[1]==loc1 and i[2]==loc2:
                                if len(ast.literal_eval(i[7]))==0:
                                    i[7]=='Fully Booked'
                                    print('Sorry all the seats are booked')
                                    break
                                else:
                                    n=int(input('Enter number of passengers:'))
                                    INTL(n)
            elif p==4:
                with open('tn1.csv','w',newline='') as c2:
                    w=csv.writer(c2,delimiter=',')
                    with open('DomFlights.csv','r',newline='') as c1:
                        r=csv.reader(c1,delimiter=',')
                        for i in r:
                            if i[0]!='Flight No.':
                                if i[5]=='Fully Booked' or len(ast.literal_eval(i[5]))==0:
                                    i[5]='Fully Booked'
                                if i[6]=='Fully Booked' or len(ast.literal_eval(i[6]))==0:
                                    i[6]='Fully Booked'
                                if i[7]=='Fully Booked' or  len(ast.literal_eval(i[7]))==0:
                                    i[7]='Fully Booked'
                                w.writerow(i)
                            else:
                                w.writerow(i)
                        c2.close()
                        c1.close()
                os.remove('DomFlights.csv')
                os.rename('tn1.csv','DomFlights.csv')
                L=PrettyTable(['Flight No.','Dep apt','Arr apt','Dep Time','Arr Time'])
                for i in l1:
                    lk1=[]
                    if i[0]!='Flight No.':
                        lk1.extend([i[0],i[1],i[2],i[3],i[4]])
                        L.add_row(lk1)
                print(L)
                loc1=input('Enter your departure airport:')
                loc2=input('Enter your arrival airport:')
                o=0
                p1=[]
                for i in l1:
                    if i[1]==loc1 and i[2]==loc2:
                        o=1
                        p1.append(i)
                        break
                if o==0:
                    print('Invalid')
                else:
                    dat=datetime.date.today()
                    dat1=str(dat)
                    tad=''
                    km=0
                    km=int(dat1[8:10])+1
                    tad=dat1[0:8]+str(km)
                    date=input('\nEnter departure date (yyyy-mm-dd):')
                    while True:
                        if date!=tad:
                            print('Invalid Date')
                            date=input('\nEnter departure date (yyyy-mm-dd):')
                        else:
                            break
                    time=input('Enter time:')
                    while True:
                        if time not in p1[0]:
                            print('Invalid Time')
                            time=input('Enter time:')
                        else:
                            break
                    for i in range(len(l5)):
                        if l5[i][1]==loc1 and l5[i][2]==loc2 and i!=0:
                            D.add_row(l5[i])
                    print(D)
                    cl1=input('Enter your preffered class(E/B/F):')
                    
                    if cl1=='E':
                        print(l1)
                        for i in l1:
                            if i[1]==loc1 and i[2]==loc2:
                                print(i[1],i[2])
                                if len(ast.literal_eval(i[5]))==0:
                                    i[5]=='Fully Booked'
                                    print('Sorry all the seats are booked')
                                    break
                                else:
                                    print('xxxx')
                                    n=int(input('Enter number of passengers:'))
                                    DOM(n)
                        print(n)
                    elif cl1=='B':
                        for i in l1:
                            if i[1]==loc1 and i[2]==loc2:
                                if len(ast.literal_eval(i[6]))==0:
                                    i[6]=='Fully Booked'
                                    print('Sorry all the seats are booked')
                                    break
                                else:
                                    n=int(input('Enter number of passengers:'))
                                    DOM(n)
                    elif cl1=='F':
                        for i in l1:
                            if i[1]==loc1 and i[2]==loc2:
                                if len(ast.literal_eval(i[7]))==0:
                                    i[7]=='Fully Booked'
                                    print('Sorry all the seats are booked')
                                    break
                                else:
                                    n=int(input('Enter number of passengers:'))
                                    DOM(n)
            print('\nThank you for choosing Fly Airlines!')
            with open('TicketsN.csv','w',newline='') as c10:
                w=csv.writer(c10,delimiter=',')
                with open('Tickets.csv','r') as c999:
                    r=csv.reader(c999)
                    for i in r:
                        if i[0]!='Booking Number':
                            w.writerow(i)
                    w.writerows(l3)
                    c999.close()
                c10.close()
            os.remove('Tickets.csv')
            os.rename('TicketsN.csv','Tickets.csv')
            if o==1:
                Tic=PrettyTable(['BNo','Name','Phone No','Nationality','Dep apt','Arrival Apt','Date','Time','Class','Food','SNo'])
                print(n)
                for ti in range(1,n+1):
                    Tic.add_row(l3[ti])
                print(Tic)
                print()
                print('\nThank you for choosing Fly Airlines!')
                
        elif choice==2:
            en=input('Pls enter Booking No.:')
            g=0
            with open('Tickets.csv','r',newline='') as c20:
                r=csv.reader(c20)
                for i in r:
                    if i[0]==en:
                        g+=1
                c20.close()
            if g>=1:
                V=PrettyTable(['Booking no','Name','Contact','Nationality','Dept Apt','Arr Apt','Date','Time','Class','Food','Seat'])
                with open('Tickets.csv','r',newline='') as c21:
                    r=csv.reader(c21)
                    for i in r:
                        if i[0]==en:
                            V.add_row(i)
                    print(V)
                    c21.close()
                while True:
                    print('\nPRESS 1: To delete booking')
                    ch1=int(input('Pls enter your choice:'))
                    if ch1==1:
                        vh=input('Do you want to delete the booking?:')
                        if vh=='yes' or vh=='Yes':
                            with open('TicketsN.csv','w',newline='') as c22:
                                w=csv.writer(c22,delimiter=',')
                                with open('Tickets.csv','r',newline='') as c35:
                                    r=csv.reader(c35)
                                    for i in r:
                                        if i[0]!=en:
                                            w.writerow(i)
                                    c35.close()
                                c22.close()
                            print('Your booking had been deleted')
                            os.remove('Tickets.csv')
                            os.rename('TicketsN.csv','Tickets.csv')
                        elif vh=='no' or vh=='No':
                            break
            else:
                print('Booking no. not found')
                break
        elif choice==3:
            en1=input('Pls enter booking no.:')
            g1=0
            with open('Tickets.csv','r',newline='') as c30:
                r=csv.reader(c30)
                for i in r:
                    if i[0]==en1:
                        g1+=1
                c30.close()
            if g1>=1:
                X=PrettyTable(['Booking no','Name','Contact','Nationality','Dept Apt','Arr Apt','Date','Time','Class','Food','Seat'])
                with open('Tickets.csv','r',newline='') as c24:
                    r=csv.reader(c24)
                    for i in r:
                        if i[0]==en1:
                            X.add_row(i)
                    print(X)
                    c24.close()
                break
            else:
                print('Booking no. not found')
                break
        elif choice==4:
            c2=obj.cursor()
            hs=eval(input('Booking No.:'))
            hs1=input('Name:')
            hs2=input('Please enter your feedback:')
            hs3=int(input('Passenger satisfaction rating(/10):'))
            hs4=input('Email address:')
            hs5='Not viewed'
            tw=datetime.date.today()
            c2.execute('insert into feedback values(%s,%s,%s,%s,%s,%s,%s)',(tw,hs,hs1,hs2,hs3,hs4,hs5))
            obj.commit()
            c2.close()
        else:
            break
                        
                        
                        
                    
                            
                
                
                
                














                
                

