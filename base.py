#base.py
#Importing sqlalchemy
from flask_sqlalchemy import SQLAlchemy

#Instantiating sqlalchemy object
db = SQLAlchemy()

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