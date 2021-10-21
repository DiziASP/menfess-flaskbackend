#app.py
#Import necessary packages
from flask import Flask
from flask_restful import Resource, reqparse, Api 
from flask_cors import CORS

#Instantiate a flask object 
app = Flask(__name__)

#Instantiate Api object
api = Api(app)

# Initiate CORS
cors = CORS(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
#Setting the location for the sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base.db'
#Adding the configurations for the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True 

#Import necessary classes from base.py
from base import Fess, db
#Link the app object to the Movies database 
db.init_app(app)
app.app_context().push()

#Create the databases
db.create_all() 
#Creating a class to create get, post, put & delete methods
class Menfess_List(Resource):    
    
#Instantiating a parser object to hold data from message payload
    parser = reqparse.RequestParser()     
    parser.add_argument('name', type=str, required=False, help='name of the menfess')                 
    parser.add_argument('menfess', type=str, required=False, help='Content of the menfess')    
      
    
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

#Defining the get method
    def get(self):        
        return {'Fess': list(map(lambda x: x.json(), Fess.query.all()))}

    def post(self):                
        args = All_Fess.parser.parse_args()        
        item = Fess(args["name"], args['menfess'])   
        
        item.save_to()        
        return item.json()
#Creating the delete method
    def delete(self):
        Fess.delete_all()
        if Fess.delete_all():                       
            return {'Message': 'data has been deleted from records'}              
        return {'Message': 'data is already not on the list'}


#Adding the URIs to the api
api.add_resource(All_Fess, '/')
api.add_resource(Menfess_List, '/<int:fess_id>') 


if __name__=='__main__':        
    #Run the applications
    app.run()