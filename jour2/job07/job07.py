import mysql.connector


mydb = mysql.connector.connect(host="localhost",
                                user="root",
                                password="vatefaireencule",
                               database='entreprise'

    )

mycursor = mydb.cursor()
mycursor.execute('select nom,prenom,salaire,id_service from employe where salaire>=3000')
salaire_employe = list(mycursor)
for i in salaire_employe:
    print('nom :',i[0])
    print('prénom :',i[1])
    print('salaire :',i[2])
    print('#####################')

print('')

#recup liste service
service_cursor = mydb.cursor()
service_cursor.execute('select * from services')
service = list(service_cursor)

#recup liste info employe
info_employe_cursor = mydb.cursor()
info_employe_cursor.execute('select nom,prenom,id_service from employe')
info_employe = list(info_employe_cursor)

for i in service:
    print('Poste :', i[1])
    for x in info_employe:
        if x[2] == i[0]:
            print(x[1],x[0])
    print('')

