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
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [TODO](../TODO.md)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

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
- [SQLite](https://www.sqlite.org/index.html) - Server Framework
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
## 🔧 Running the tests <a name = "tests"></a>
Explain how to run the automated tests for this system.

### Break down into end to end tests
Explain what these tests test and why

```
Give an example
```

### And coding style tests
Explain what these tests test and why

```
Give an example
```

## 🎈 Usage <a name="usage"></a>
Add notes about how to use the system.

## 🚀 Deployment <a name = "deployment"></a>
Add additional notes about how to deploy this on a live system.

## ⛏️ Built Using <a name = "built_using"></a>
- [MongoDB](https://www.mongodb.com/) - Database
- [Express](https://expressjs.com/) - Server Framework
- [VueJs](https://vuejs.org/) - Web Framework
- [NodeJs](https://nodejs.org/en/) - Server Environment

## ✍️ Authors <a name = "authors"></a>
- [@kylelobo](https://github.com/kylelobo) - Idea & Initial work

See also the list of [contributors](https://github.com/kylelobo/The-Documentation-Compendium/contributors) who participated in this project.

## 🎉 Acknowledgements <a name = "acknowledgement"></a>
- Hat tip to anyone whose code was used
- Inspiration
- References