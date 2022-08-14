from models.user import User
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from os import getenv

classes = {"User": User}

class DBStorage:
    __engine = None

    def __init__(self):
        MANY_MENU_MYSQL_USER = getenv('MANY_MENU_MYSQL_USER')
        MANY_MENU_MYSQL_PWD = getenv('MANY_MENU_MYSQL_PWD')
        MANY_MENU_MYSQL_HOST = getenv('MANY_MENU_MYSQL_HOST')
        MANY_MENU_MYSQL_DB = getenv('MANY_MENU_MYSQL_DB')
        MANY_MENU_ENV = getenv('MANY_MENU_ENV')
        
        print("--------------", MANY_MENU_MYSQL_HOST, MANY_MENU_MYSQL_DB)
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(MANY_MENU_MYSQL_USER,
                                             MANY_MENU_MYSQL_PWD,
                                             MANY_MENU_MYSQL_HOST,
                                             MANY_MENU_MYSQL_DB), pool_size=20, max_overflow=0)

    def all(self, cls=None):
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)
    
    def new(self, obj):
        self.session.add(obj)

    def save(self):
        self.session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        self.__session.remove()

    def get(self, cls, id):
        if type(cls) == str and cls in classes:
            cls = classes[cls]
        get_obj = "{}.{}".format(cls.__name__, id)
        if get_obj in self.all():
            return self.all()[get_obj]
        return None

    def count(self, cls=None):
        num_objs = 0
        print("-----> {}".format(cls))
        if type(cls) == str and cls in classes:
            cls = classes[cls]
        if cls is not None and cls.__name__ in classes:
            num_objs = self.__session.query(cls).count()
        elif cls is None:
            for clases in classes.values():
                num_objs += self.__session.query(clases).count()
        return num_objs