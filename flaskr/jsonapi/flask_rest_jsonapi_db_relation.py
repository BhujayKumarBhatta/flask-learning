from flask import Flask
from flask_rest_jsonapi import Api, ResourceDetail, ResourceList, ResourceRelationship
from flask_rest_jsonapi.exceptions import ObjectNotFound
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm.exc import NoResultFound
from marshmallow_jsonapi.flask import Schema, Relationship
from marshmallow_jsonapi import fields

# Create the Flask application
app = Flask(__name__)
app.config['DEBUG'] = True

# Initialize SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test3.db'
db = SQLAlchemy(app)

# Create data storage
class Person(db.Model):
#     __tablename__ = 'Person'
#     __table_args__ = {'autoload':True,
#                        'autoload_with': db.engine
#                        }  # when auto is enabled manual mapping is not required
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    birth_date = db.Column(db.Date)
    password = db.Column(db.String)

class Computer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    serial = db.Column(db.String)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    person = db.relationship('Person', backref=db.backref('computers'))
    
  
db.create_all()

# Create logical data abstraction (same as data storage for this first example)
class PersonSchema(Schema):
    class Meta:
        type_ = 'person'
        #self_view = 'person_detail'
        #self_view_kwargs = {'id': '<id>'}
        self_view_many = 'person_list'

    id = fields.Integer(as_string=True, dump_only=True)
    name = fields.Str(requried=True, load_only=True)
    email = fields.Email(load_only=True)
#    birth_date = fields.Date()
    display_name = fields.Function(lambda obj: "{} <{}>".format(obj.name.upper(), obj.email))

class ComputerSchema(Schema):
    class Meta:
        type_ = 'computer'
        self_view = 'computer_detail'
        self_view_kwargs = {'id': '<id>'}
        
    id = fields.integer(as_String=True, dump_only=True)
    serial = fields.Str(required)
    

# Create resource managers
class PersonList(ResourceList):
    schema = PersonSchema
    data_layer = {'session': db.session,
                  'model': Person}
    methods = ['GET', 'POST']

# Create endpoints
api = Api(app)
api.route(PersonList, 'person_list', '/persons')


if __name__ == '__main__':
    # Start application
    app.run(debug=True)
    
    
'''

curl --header "Content-Type: application/json"   --request POST   --data '{"data": {"type": "person","id": "4","name": "bhujay" , "email": "bhujay@abc.com"}}'   http://localhost:5000/persons

{
  "data": {
    "id": "4",
    "type": "person"
  },
  "jsonapi": {
    "version": "1.0"
  }
}

curl http://localhost:5000/persons


{
  "data": [
    {
      "id": "1",
      "type": "person"
    },
    {
      "id": "2",
      "type": "person"
    },
    {
      "id": "3",
      "type": "person"
    },
    {
      "id": "4",
      "type": "person"
    }
  ],
  "jsonapi": {
    "version": "1.0"
  },
  "links": {
    "self": "http://localhost:5000/persons"
  },
  "meta": {
    "count": 4
  }
}    

'''
    
