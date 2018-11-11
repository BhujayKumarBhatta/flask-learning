from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
 
engine = create_engine('sqlite:///test.db', echo=True)
Base = declarative_base(engine)
########################################################################
class CompanyModel(Base):
    """"""
    __tablename__ = 'COMPANY'
#     __table_args__ = {'autoload':True}  # when auto is enabled manual mapping is not required

############BEGIN MANUAL MAPPING ################################################
    ID = Column(Integer, primary_key=True)
    NAME = Column(String)
    AGE = Column(Integer)
    ADDRESS = Column(String)
    SALARY = Column(Float)

    def __init__(self, id, name, age, addreess, salary):
        self.id = id
        self.name = name
        self.age = age
        self.address = address
        self.salary = salary
    def __repr__(self):
        return "<Company - '%s': '%s'  >"  % (self.id, self.name )
# ######################END MANUAL MAPPING #############################################    
#----------------------------------------------------------------------
def loadSession():
    """"""
    metadata = Base.metadata
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
 
if __name__ == "__main__":
    session = loadSession()
    res = session.query(CompanyModel).all()
    for i in res:
      print (i.NAME+'  '+ str(i.AGE) + '  ' + i.ADDRESS + '  ' + str(i.SALARY))
      
      
'''
        could also do it using mapper 
        from sqlalchemy import create_engine, Column, MetaData, Table
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import mapper, sessionmaker
 
class Bookmarks(object):
    pass
 
#----------------------------------------------------------------------
def loadSession():
    """"""
    dbPath = 'places.sqlite'
 
    engine = create_engine('sqlite:///%s' % dbPath, echo=True)
 
    metadata = MetaData(engine)    
    moz_bookmarks = Table('moz_bookmarks', metadata, 
                          Column('id', Integer, primary_key=True),
                          Column('type', Integer),
                          Column('fk', Integer),
                          Column('parent', Integer),
                          Column('position', Integer),
                          Column('title', String),
                          Column('keyword_id', Integer),
                          Column('folder_type', Text),
                          Column('dateAdded', Integer),
                          Column('lastModified', Integer)
                          )
 
    mapper(Bookmarks, moz_bookmarks)
 
    Session = sessionmaker(bind=engine)
    session = Session()
 
if __name__ == "__main__":
    session = loadSession()
    res = session.query(Bookmarks).all()
    print res[1].title
    
    
    '''
        