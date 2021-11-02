<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://pbs.twimg.com/media/ExhNq4jXEAoEAmR?format=jpg&name=medium" alt="Project logo"></a>
</p>

<h3 align="center">ITB Menfess Website</h3>

---

<p align="center"> Website Menfess untuk memenuhi kebutuhan Tugas Besar Pengenalan Komputasi ITB
    <br> 
</p>

## 📝 Table of Contents
- [About](#about)
- [Dekomposisi](#dekomposisi)
- [Built Using](#built_using)
- [Authors](#authors)

## 🧐 About <a name = "Tentang"></a>
Seiring berjalannya waktu, mention confess tidak hanya dilakukan melalui twitter, namun dapat melalui website tertentu, seperti yang telah dilaksanakan oleh mahasiswa/i Sekolah Teknik Elektro dan Informatika, Institut Teknologi Bandung angkatan 2021 pada Main Event Gathering STEI 2021. Kami mengamati proses paling sederhana yang dilakukan oleh google form sebagai media menfess. Sebagai alat untuk menfess, google form melakukan tiga hal penting secara urut yaitu input, menyimpan data, dan output data.

Kami mengamati bahwa melakukan menfess dengan menggunakan google form cukup baik. Namun terdapat hal yang menjadi alasan tidak efektifnya penggunaan google form dalam menfess. Pertama adalah ketika menerima hasil dari input, tampilan output dari menfess tidak bisa langsung dipublikasikan kepada pengguna. Konsekuensinya, pemilik form haruslah membuat suatu desain baru sebagai output dari menfess. Hal ini akan memberikan waktu tambahan bagi pengguna untuk menunggu output, dan menambah pekerjaan bagi pemilik form.

Oleh karena itu, kami mencoba mengembangkan suatu website yang lebih efisien dan terfokus bagi pelaksanaan menfess. Kami mengadaptasi ketiga proses sederhana yang dilakukan oleh google form dalam hal menfess. Modifikasi proses yang dilakukan adalah pengguna dapat langsung melihat output dari menfess pada saat itu juga dengan tampilan yang menarik. Diharapkan website ini dapat menjadi wadah mention confess yang efisien karena tidak membutuhkan waktu bagi pengguna untuk melihat hasil menfess dan tidak membutuhkan pekerjaan tambahan bagi pemilik form untuk menampilkan hasil menfess dengan tampilan yang menarik.

## 🎈 Dekomposisi <a name = "dekomposisi"></a>
Dekomposisi fungsi masing-masing kode di dalam backend
### Import
```
# app.py
#Import necessary packages
from flask import Flask
from flask_restful import Resource, reqparse, Api 
from flask_cors import CORS
```

```
# base.py
#Importing sqlalchemy
from flask_sqlalchemy import SQLAlchemy
```

Mengimport library-library yang akan digunakan oleh backend. Library-library yang digunakan adalah :
- [Flask](https://flask.palletsprojects.com/en/2.0.x/) - Server Environment 
- [SQLite](https://www.sqlite.org/index.html) - Database
- [Flask-Restful](https://flask-restful.readthedocs.io/en/latest/) - Flask Library untuk membuat RESTful API
- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/) - Flask Library untuk mengelola Cross-Origin Resource Sharing agar dapat database dapat diakses oleh front-end
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) - Flask Library untuk menginisiasi dan mengelola database sqlite dalam Flask

### Inisiasi / Deklarasi
```
# app.py
# Instantiate a flask object 
app = Flask(__name__)

#Instantiate Api object
api = Api(app)

# Initiate CORS
cors = CORS(app)
cors = CORS(app, resources={r"/*": {"origins": "https://steimenfess.vercel.app/"}})
```
Mendeklarasikan Server Flask, API dan CORS yang akan digunakan oleh backend. "app" adalah Objek Flask itu sendiri, "api" adalah penghubung antara database dengan backend Flask dan Front-End (Next.JS), dan "cors" adalah Cross-Origin Resource Sharing untuk mengelola kepada siapa saja data dapat diambil agar tidak mudah diakses oleh semua orang di Internet

```
# base.py
#Instantiating sqlalchemy object
db = SQLAlchemy()
```
Mendeklarasikan Database dari SQLAlchemy

```
#Setting the location for the sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base.db'

#Adding the configurations for the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True 
```
Mendeklarasikan Lokasi dari Database dan mengatur pengaturan dari sqlalchemy dalam hal Data Tracking dan Propagasi Data.
### Database on base.py
```
#Creating database class
class Fess(db.Model):   
    #Creating field/columns of the database as class variables
    id = db.Column(db.Integer, primary_key=True)    
    name = db.Column(db.String(80),unique=False, nullable=False)                                            
    menfess = db.Column(db.String(500), nullable=False)
    faculty = db.Column(db.String(500), nullable=False)

    def __init__(self, name, menfess,faculty):                 
        self.name = name        
        self.menfess = menfess               
        self.faculty = faculty

    #Method to show data as dictionary object
    def json(self):        
        return {'name': self.name, 'menfess': self.menfess,'faculty': self.faculty}        
 
    #Method to find the query movie is existing or not
    @classmethod    
    def find_by_id(cls,id):     
        return cls.query.filter_by(id=id).first()
        
#Method to save data to database
    def save_to(self):        
        db.session.add(self)        
        db.session.commit()
#Method to delete data from database
    def delete_(self):        
        db.session.delete(self)        
        db.session.commit()

    def delete_all():        
        db.session.query(Fess).delete()       
        db.session.commit()
```
#### Creating Database
```
#Creating field/columns of the database as class variables
    id = db.Column(db.Integer, primary_key=True)    
    name = db.Column(db.String(80),unique=False, nullable=False)                                            
    menfess = db.Column(db.String(500), nullable=False)
    faculty = db.Column(db.String(500), nullable=False)

    def __init__(self, name, menfess,faculty):                 
        self.name = name        
        self.menfess = menfess               
        self.faculty = faculty
    
    #Method to show data as dictionary object for parsing
    def json(self):        
        return {'name': self.name, 'menfess': self.menfess,'faculty': self.faculty} 
```
Membuat Table dari Database yang memiliki 3 Kolom yaitu name, menfess, dan faculty dan memiliki id sebagai primary key. Lalu didefine dengan method __init_() agar tiap data dalam tabel memiliki objek didalam python dan di parsing menjadi json oleh method json().

#### Databases Method
```
@classmethod    
    def find_by_id(cls,id):     
        return cls.query.filter_by(id=id).first()
        
    # Method to save data to database
    def save_to(self):        
        db.session.add(self)        
        db.session.commit()

    # Method to delete a data from database
    def delete_(self):        
        db.session.delete(self)        
        db.session.commit()
    
    # Method to delete all data from database
    def delete_all():        
        db.session.query(Fess).delete()       
        db.session.commit() 
```
- [find_by_id] - Mencari data dalam database menggunakan ID 
- [save_to]- Menyimpan data ke dalam database
- [delete_]- Menghapus sebuah data dalam database
- [delete_all]- Menghapus seluruh data dalam database


### Database initialization on app.py
```
#Import necessary classes from base.py
from base import Fess, db

#Link the app object to the Fess database 
db.init_app(app)
app.app_context().push()

#Create the databases
db.create_all() 
```
Mengimport modul database dari base.py kedalam app.py untuk diinisialisasi dengan method init_app() dan dibuat didalam database dengan method create_all().

### Method-Method inside the API
```
class Menfess_List(Resource):    
    
#Instantiating a parser object to hold data from message payload
    parser = reqparse.RequestParser()     
    parser.add_argument('name', type=str, required=False, help='name of the menfess')                 
    parser.add_argument('menfess', type=str, required=False, help='Content of the menfess')    
    parser.add_argument('faculty', type=str, required=False, help='F of the menfess')    
    
#Creating the get method
    def get(self, fess):        
        item = Fess.find_by_id(fess)        
        if item:            
            return item.json()        
        return {'Message': 'Fess is not found'}        

#Creating the delete method
    def delete(self, fess_id):        
        item  = Fess.find_by_id(fess_id)        
        if item:            
            item.delete_()            
            return {'Message': '{} has been deleted from records'.format(fess_id)}        
        return {'Message': '{} is already not on the list'.format(fess_id)}

#Creating a class to get all the movies from the database.
class All_Fess(Resource): 

#Instantiating a parser object to hold data from message payload
    parser = reqparse.RequestParser()     
    parser.add_argument('name', type=str, required=False, help='name of the menfess')                 
    parser.add_argument('menfess', type=str, required=False, help='Content of the menfess')
    parser.add_argument('faculty', type=str, required=False, help='F of the menfess')  

#Defining the get method
    def get(self):        
        return {'Fess': list(map(lambda x: x.json(), Fess.query.all()))}

    def post(self):                
        args = All_Fess.parser.parse_args()        
        item = Fess(args["name"], args['menfess'],args['faculty'])   
        
        item.save_to()        
        return item.json()
#Creating the delete method
    def delete(self):
        Fess.delete_all()
        if Fess.delete_all():                       
            return {'Message': 'data has been deleted from records'}              
        return {'Message': 'data is already not on the list'}
```
Membuat class yang berisi method-method yang diperlukan untuk membuat operasi CRUD (CREATE, READ, UPDATE, DELETE). Method-Method ini yang akan digunakan untuk menghapus data menfess, menambahkan data menfess, dan lain-lain. Penjelasan tiap-tiap method:
- [get] - Mencari menfess di dalam database. 
- [post]- Mengupload data menfess dari front-end dan disimpan didalam database.
- [delete]- Dalam class Menfess_List, Menghapus sebuah data dalam database. Dalam class All_Fess, menghapus seluruh data dalam database.

### Routing and Running
```
# Adding the URIs to the api
api.add_resource(All_Fess, '/')
api.add_resource(Menfess_List, '/<int:fess_id>') 

# Running the Backend App
if __name__=='__main__':        
    #Run the applications
    app.run()
```
Menginisiasi route-route untuk api agar dapat diakses oleh front-end melalui data fetching. app.run() berfungsi untuk menjalankan server Flask, yang akan diinisiasi saat diupload ke cloud server.

## ⛏️ Built Using <a name = "built_using"></a>
- [Flask](https://flask.palletsprojects.com/en/2.0.x/) - Server Environment 
- [SQLite](https://www.sqlite.org/index.html) - Database
- [NextJS](https://nextjs.org/) - Web Framework

## ✍️ Authors <a name = "authors"></a>
- [Raden Dizi Assyafadi Putra](https://www.instagram.com/__dejee__/)
- [Tabitha Permalla](https://www.instagram.com/tabitha_permalla/)
- [Michael Kharisma Bintang Yudanto](https://www.instagram.com/mc.bin_/)
