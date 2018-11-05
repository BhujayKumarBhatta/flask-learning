from flask import Flask, jsonify
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/company.db'
db = SQLAlchemy(app)

# Create data storage
class CompanyModel(db.Model):
    __tablename__ = 'COMPANY'
#     __table_args__ = {'autoload':True}  # when auto is enabled manual mapping is not required

############BEGIN MANUAL MAPPING ################################################
    ID = db.Column(db.Integer, primary_key=True)
    NAME = db.Column(db.String)
    AGE = db.Column(db.Integer)
    ADDRESS = db.Column(db.String)
    SALARY = db.Column(db.Float)

    def __init__(self, id, name, age, addreess, salary):
        self.id = id
        self.name = name
        self.age = age
        self.address = address
        self.salary = salary
    def __repr__(self):
        return "<CompanyModel - '%s': '%s'  >"  % (self.id, self.name)

#db.create_all()

@app.route('/persons')
def get_company():
    p = CompanyModel.query.all()    
    return p[0].NAME

# # Create logical data abstraction (same as data storage for this first example)
class PersonSchema(Schema):
     class Meta:
         type_ = 'person'
         self_view = 'person_detail'
         self_view_kwargs = {'id': '<id>'}
         self_view_many = 'person_list'
 
     id = fields.Integer(as_string=True, dump_only=True)
     name = fields.Str(requried=True, load_only=True)
     age = fields.Integer(load_only=True)
     address = fields.Str(requried=True, load_only=True)
     salary = fields.Integer(load_only=True)
     display_name = fields.Function(lambda obj: "{} <{}>".format(obj.name.upper(), obj.email))  
## 
# # Create resource managers
class PersonList(ResourceList):
     schema = PersonSchema
     data_layer = {'session': db.session,
                   'model': CompanyModel}

class PersonDetail(ResourceDetail):
    schema = PersonSchema
    data_layer = {'session': db.session,
                  'model': CompanyModel}    
    

# # Create endpoints
api = Api(app)
api.route(PersonList, 'person_list', '/personsapi')
api.route(PersonDetail, 'person_detail', '/personsapi/<int:id>')
# api.route(PersonRelationship, 'person_computers', '/persons/<int:id>/relationships/computers')
# api.route(ComputerList, 'computer_list', '/computers', '/persons/<int:id>/computers')
# api.route(ComputerDetail, 'computer_detail', '/computers/<int:id>')
# api.route(ComputerRelationship, 'computer_person', '/computers/<int:id>/relationships/owner')

if __name__ == '__main__':
    # Start application
    app.run(debug=True)
    
    
'''
curl --header "Content-Type: application/json"   --request POST   --data '{"data": {"type": "computer","id": "1","attributes": {"serial": "Amstrad 2"}}}'   http://localhost:5000/computers


{
  "data": {
    "attributes": {
      "serial": "Amstrad 2"
    },
    "id": "1",
    "links": {
      "self": "/computers/1"
    },
    "relationships": {
      "owner": {
        "links": {
          "related": "/computers/1/owner",
          "self": "/computers/1/relationships/owner"
        }
      }
    },
    "type": "computer"
  },
  "jsonapi": {
    "version": "1.0"
  },
  "links": {
    "self": "/computers/1"
  }
}

'''    