
import mysql.connector as con
myCon = con.connect(user='root', host='localhost', password='Password', database='project') # Enter Personal Database Detailspip
cur = myCon.cursor()

def insert():
    sql = 'insert into Points(Match_No,Team_A,Formation_A,Team_B,Formation_B,Win,Win_Formation,Loss,Loss_Formation,Points_TeamA,Points_TeamB) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    Match_No= int(input('Enter match number: '))
    Team_A = input('Enter the first team to insert : ')
    Formation_A = input('Enter the first team formation to insert : ')
    Team_B = input('Enter the second team to insert : ')
    Formation_B = input('Enter the second team formation to insert : ')
    Loss='None'
    Win = input('Enter who won. In case of Draw, enter Draw : ')
    if Win==Team_A:
        Loss= Team_B
        Points_TeamA=3
        Points_TeamB=0
        Win_Formation=Formation_A
        Loss_Formation=Formation_B
    elif Win==Team_B:
         Loss= Team_A
         Points_TeamA=0
         Points_TeamB=3
         Win_Formation=Formation_B
         Loss_Formation=Formation_A
    elif Win=='Draw':
         Loss='None'
         Points_TeamA=1
         Points_TeamB=1
         Win_Formation= 'Undefined'
         Loss_Formation= 'Undefined'
     
    val = (Match_No,Team_A,Formation_A,Team_B,Formation_B,Win,Win_Formation,Loss,Loss_Formation,Points_TeamA,Points_TeamB)
    cur.execute(sql, val)
    myCon.commit()
    

def show():
    sql = 'select * from Points'
    cur.execute(sql)
    row = cur.fetchall()
    for i in row:
        print(i)
    
def Ideal_Formation(): 
    x=input('Enter Opponent Formation: ')
    sql = "select count(Win_Formation) as Number_Of_Wins, Win_Formation as Ideal_Formation from Points where Loss_Formation=%s group by Win_Formation order by Win Limit 1"
    y=(x,)
    cur.execute(sql,y)
    row = cur.fetchall()
    for i in row:
         print(i)
          
def Compare():
   z=input('Enter Formation 1: ')
   f=input('Enter Formation 2: ')

   query1="SELECT count(Win_Formation) from Points where Win_Formation=%s and Loss_Formation=%s"
   T=(z,f)
   cur.execute(query1,T)
   for row in cur:
      print("Number of 1 times won: ",row[0])
      a=row[0] 
    
   query2="SELECT count(Win_Formation) from Points where Win_Formation=%s and Loss_Formation=%s"
   T=(f,z)
   cur.execute(query2,T)
   for row in cur:
        print("Number of 2 times won: ",row[0])
        b=row[0]
        
   if a>b:
       print('1 is the winner')
   elif b>a:
       print('2 is the winner')
   else:
       print('Both tied')
       
    
   
o='y'
while o=='y':
    ch=input('For insert press 1, For display press 2, 3 for Ideal Formation, 4 for Comparison:')

    if ch=='1':
        insert()
    elif ch=='2':
        show()
    elif ch=='3':
        Ideal_Formation()
    elif ch=='4':
        Compare()
    else:
        print('ERROR, Please Enter Either 1,2,3,4')
    
    o=input('Do you want to continue y or n?:')
    


 
