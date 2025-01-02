import pandas as pd
import matplotlib.pyplot as plt
while True:
    print("1.ADD PROPERTY\n2.ADD TENANT\n3.SHOW PROPERTY\n4.SHOW TENANT\n5.FIND PROPERTY\n6.ON RENT\n7.SHOW RENTAL PROPERTY\n8. DELETE PROPERTY\n9. GRAPH\n10 EXIT")
    ch=int(input('enter choice'))
    if ch==1:
        
        try:
            df=pd.read_csv('property1.csv')
        except FileNotFoundError:
            df=pd.DataFrame(columns= ['houseno','PINCODE','AREA','ADDRESS','RENT'])
        if df.empty:
            next_houseno=1
        else:
            f=len(df)
            next_houseno = f+1
        a= int(input('ENTER PINCODE='))
        b= input('ENTER AREA=')
        c=input('ENTER ADDRESS=')
        d=int(input('ENTER RENT OF HOUSE'))
        df.loc[len(df.index)]=[next_houseno,a,b,c,d]
        df.to_csv('property1.csv',index =False)
        
    elif ch==2:
        try:
            tf=pd.read_csv('tenant.csv')
        except FileNotFoundError :
            tf=pd.DataFrame(columns=['SNO','NAME','PERMANENT ADDRESS','MOBILE NO.','EMERGENCY MOBILE NO.'])
        if tf.empty:
            next_SNO=1
        else :
            e= len(tf)
            next_SNO = e+1
        g= input('ENTER NAME=')
        h=input ('ENTER PERMANENT ADDRESS=')
        i=int(input('ENTER MOBILE NO.='))
        k=int(input('ENTER EMERGENCY MOBILE NO.='))
        tf.loc[len(tf.index)]=[next_SNO,g,h,i,k]
        tf.to_csv('tenant.csv',index= False)
    elif ch==3:
        try:
            df=pd.read_csv('property1.csv')
            print(df)
        except FileNotFoundError:
            print("try csv file ' property.csv' does not exist or empty.")
    elif ch==4:
        try:
            tf=pd.read_csv('tenant.csv')
            print(tf)
        except FileNotFoundError:
            print("try csv file ' tenant.csv' does not exist or empty.")
    elif ch==5:
        try:
            df=pd.read_csv('property1.csv')
            area_find=input('ENTER THE AREA OF PROPERTY TO FIND')
            result=df[df['AREA']==area_find]
            if result.empty:
                print('no data found for ')
            else:
                print('found data fro')
                print(result)
                
        except FileNotFoundError:
            print('no data found for ')
    elif ch==6:
        try:
            rf=pd.read_csv('rent.csv')
        except FileNotFoundError :
            rf=pd.DataFrame(columns=['SNO','NAME','PROPERTY ADDRESS','MOBILE NO.','RENT'])
        if rf.empty:
            next_SNO=1
        else :
            l= len(rf)
            next_SNO = l+1
        m= input('ENTER NAME OF TENANT=')
        n=input ('ENTER THE PROPERTY ADDRESS=')
        o=int(input('ENTER MOBILE NO. OF TENANT='))
        p=int(input('ENTER THE RENTED AMOUNTED ='))
        rf.loc[len(rf.index)]=[next_SNO,m,n,o,p]
        rf.to_csv('rent.csv',index= False)
    elif ch==7:
        try:
            rf=pd.read_csv('rent.csv')
            print(rf)
        except FileNotFoundError:
            print("try csv file ' rent.csv' does not exist or empty.")
    elif ch==8:
        try:
            df=pd.read_csv('property1.csv')
            q= int(input("enter pincode to delete"))
            selected_pincode=(df[df["PINCODE"]==q])
            df=df.drop(selected_pincode.index,axis=0)
            print(df)
        except FileNotFoundError:
            print("this pincode does not exist")
    elif ch==9:
        
        df=pd.read_csv('property1.csv')
        print(df)
        plt.bar(df["AREA"],df["RENT"])
        plt.xlabel('AREA')
        plt.ylabel('RENT')
        plt.title('COMPARING RENT RATE ')
        plt.show()
        
    else:
        exit()





