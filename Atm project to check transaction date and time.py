import datetime
import mysql.connector
class transaction:
    def __init__(self):
        self.conn=mysql.connector.connect(host='localhost',user='root',password='7777777',database='student')
        self.cur=self.conn.cursor()



    def registration(self):
        username=input('Enter username:')
        userid=int(input('Enter user id:'))
        query='select *from cstmer where cname=%s and cid=%s'
        values=(username,userid)
        self.cur.execute(query,values)
        if self.cur.fetchone():
            print('Successfull \n')
        else:
            print('User not available \n')
            choice=input('You want to Register Yourself yes/no ')
            if choice=='yes':
                try:
                    id=int(input('Enter id:'))
                    username=input('Enter username:')
                    balance=int(input('Enter amount:'))
                    caccountnumber=int(input('Enter caccountnumber:'))
                    query='insert into cstmer(cid,cname,balance,caccountnumber)values(%s,%s,%s,%s)'
                    values=(id,username,balance,caccountnumber)
                    self.cur.execute(query,values)
                
                    transactiontime=datetime.datetime.today()
                    query='insert into transactn(transaction_time,transaction_history,cid)values(%s,%s,%s)'
                    values=(transactiontime,balance,id)
                    self.cur.execute(query,values)

                    print('user register successfully')
                    self.conn.commit()
                except Exception as e:
                    print(e)
                finally:
                    print('Thank you')
            else:
                print('Thank you')
    def existingusertransaction(self):
        cid=int(input('Enter customer id:'))
        query='select transaction_history from transactn where cid=%s'
        values=(cid,)
        self.cur.execute(query,values)
        data=self.cur.fetchone()
        if data:
            print('Your last transaction of rs.',data[0])
        else:
            print('You are new user')  
    

        query='select transaction_time from transactn where cid=%s'
        values=(cid,)
        self.cur.execute(query,values)
        data=self.cur.fetchone()
        if data:
            print('Time and data of yur last transaction is:',data[0])
            print('Thank you')
        else:
            print('you didt make any transaction ')

    
    def depositamt(self):
        cid=int(input('Enter your pin:'))
        caccountnumber=int(input('enter enteraccountno:'))
        query='select *from cstmer where cid=%s and caccountnumber=%s'
        values=(cid,caccountnumber)
        self.cur.execute(query,values)
        data=self.cur.fetchone()
        if data:
            deposit_amt=int(input('Enter amount you want to deposit:'))
            if deposit_amt>0:
                nbalance=data[2]+deposit_amt
                transactiontime=datetime.datetime.today()
                query='update cstmer set balance=%s where cid=%s and caccountnumber=%s '
                values=(nbalance,cid,caccountnumber)
                self.cur.execute(query,values)

                query='update transactn set transaction_history=%s where cid=%s'
                values=(nbalance,cid)
                self.cur.execute(query,values)
                print('record updated successfully')
                
                query='update transactn set transaction_time=%s where cid=%s'
                values=(transactiontime,cid)
                self.cur.execute(query,values)

                choice=input('you want to check balance amount yes /no:')
                if choice=='yes':
                    print('your current balance is:',nbalance,'\n')
                else:
                    print('Thank you \n')
            else:
                print('you dont have enough funds')
        else:
            print('Invallid pin or account number')                                        
        self.conn.commit()
        



    def withdrawamt(self):
        cid=int(input('Enter your pin:'))
        caccountnumber=int(input('enter enteraccountno:'))
        query='select *from cstmer where cid=%s and caccountnumber=%s '
        values=(cid,caccountnumber)
        self.cur.execute(query,values)
        data=self.cur.fetchone()
        if data:
            withdrawamt=int(input('Enter withdraw amount:'))
            if withdrawamt<=data[2]:
                nbal=data[2]-withdrawamt
                transactiontime=datetime.datetime.today()
                query='update cstmer set balance=%s where cid=%s and caccountnumber=%s '
                values=(nbal,cid,caccountnumber)
                self.cur.execute(query,values)

                query='update transactn set transaction_history=%s where cid=%s'
                values=(nbal,cid)
                self.cur.execute(query,values)

                query='update transactn set transaction_time=%s where cid=%s'
                values=(transactiontime,cid)
                self.cur.execute(query,values)

                print('record updated successfully')


                choice=input('you want to check balance amount yes /no:')
                if choice=='yes':
                    print('your new balance is:',nbal)
                else:
                    print('Thank you \n')
                
                self.conn.commit()
            else:
                print('you dont have enough amount')
        else:
            print('Invallid pin or account number')
        

    def conn_close(self):
        self.cur.close()
        self.conn.close()

a=transaction()

while True:
    print('*****************WELCOME TO SBI ATM*******************')
    print('1.Login user')
    print('2.Check history')
    print('3.Credit(Deposit)')
    print('4.Debit(Withdraw)')
    print('5.Exit')
    choice=int(input('Enter your choice:'))      

    if choice==1:
        a.registration()
    elif choice==2:
        a.existingusertransaction()
    elif choice==3:
        a.depositamt()
    elif choice==4:
        a.withdrawamt()  
    elif choice==5:
        print('Exit')
        a.conn_close()
        break        
    else:
        print('Wrong Choice')








