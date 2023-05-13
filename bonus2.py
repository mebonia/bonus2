import requests
import sqlite3
from bs4 import BeautifulSoup
from tabulate import tabulate
conn = sqlite3.connect('Crypto.sqlite3')
cur = conn.cursor()
conn.execute('''
    CREATE TABLE cryptoMarket
    (naame TEXT,
    price TEXT,
    change TEXT,
    percentage_change TEXT,
    market_cap TEXT);
''')

url ='https://finance.yahoo.com/crypto/'
r = requests.get(url)
con = r.content
soup=BeautifulSoup(con,'html.parser')
body =soup.find('body')
id=body.find('div',id='app')
clas1=id.find('div',id='render-target-default')
clas2=clas1.find('div',style='margin-top:175px')
clas3=clas2.find('div',{'class':"YDC-Lead"})
clas4=clas3.find('div',id="YDC-Lead-Stack")
clas5=clas4.find('div',id="YDC-Lead-Stack-Composite")
clas6=clas5.find('div',id="mrt-node-Lead-5-ScreenerResults")
clas7=clas6.find('div',id="Lead-5-ScreenerResults-Proxy")
clas8=clas7.find('section',id="screener-results")
clas9=clas8.find('div',id='fin-scr-res-table')
clas10=clas9.find('div',id='scr-res-table')
clas11=clas10.find('div',{'class':'Ovx(a) Ovx(h)--print Ovy(h) W(100%)'})
clas12=clas11.find('table')
clas13=clas12.find('tbody')
all_info=clas13.find_all('tr')
sia=[]
for i in all_info:
    name=i.find('td',{'aria-label':"Name"}).text
    price=i.find('td',{'aria-label':'Price (Intraday)'}).text
    change=i.find('td',{'aria-label':'Change'}).text
    procent_change=i.find('td',{'aria-label':'% Change'}).text
    market_cap=i.find('td',{'aria-label':'Market Cap'}).text
    tupl=(name,price,change,procent_change,market_cap)
    sia.append(tupl)
cur.executemany('INSERT INTO cryptoMarket (naame, price,change,percentage_change,market_cap) VALUES (?, ?, ?, ?, ?)',
                sia)
data=cur.execute('select  * from cryptoMarket' )
d=[]
for i in data:
    i=list(i)
    d.append(i)
    print(tabulate(data,headers=['naame', 'price','change','percentage_change','market_cap']))
conn.commit()
conn.close()

#N2
class Disease:
    def __init__(self, ID, disease):
        self.ID = ID
        self.name = disease

    def __str__(self):
        return f"დაავადების აიდი: {self.ID}, დაავადების სახელი: {self.name}"


class Doctor:
    def __init__(self, doctor, department):
        self.name = doctor
        self.department = department
        self.patients = []

    def __str__(self):
        return f"ექიმის სახელი: {self.name}, დეპარტამენტი: {self.department}, ფაციენტების რაოდენობა: {len(self.patients)}"

    def add_patient(self, patient):
        if len(self.patients) < 20:
            self.patients.append(patient)
            patient.attending_physician = self
            return True
        else:
            print("ექიმის მიმაგრება ვერ მოხდება")
            return False


class Patient:
    def __init__(self, personal_number, name, disease=None, mkurnali_eqimi=None):
        self.personal_number = personal_number
        self.name = name
        if disease is None:
            self.diseases = []
        else:
            self.diseases = [disease]
        self.attending_physician = mkurnali_eqimi

    def __str__(self):
        disease_names = []
        for disease in self.diseases:
            disease_names.append(disease.name)
        return f"ფაციენტის პრსრონალური ნომერი: {self.personal_number}, პაციენტის სახელი: {self.name}, დაავადება: {disease_names[0]}, ექიმია {self.attending_physician.name}"

    def make_diagnosis(self, disease, doctor=None):
        self.diseases.append(disease)
        if doctor is not None:
            return doctor.add_patient(self)
        return True


d1 = Disease(1, "COVID-19")
d2 = Disease(2, "დალტონიზმი")

doc1 = Doctor("gia", "kardiologi")
doc2 = Doctor("geluka", "pediatri")

p1 = Patient('12345', "bacho")
p2 = Patient("5678", "gio", d2)
p3 = Patient("9101", "pavle", d2, doc2)

p1.make_diagnosis(d1, doc1)
doc1.add_patient(p3)
doc1.add_patient(p2)

doc1.add_patient(p1)

print('', d1, '\n', d2, '\n', doc1, '\n', doc2,'\n',p1,'\n',p2,'\n',p3 )
# print(d2)
# print(doc1)
# print(doc2)
# print(p1)
# print(p2)
# print(p3)
