from datetime import datetime

from rmon.extensions import db


class BaseModel(db.Model):
    
    __abstract__=True
    update_at=db.Column(db.DateTime,default=datetime.utcnow)
    create_at=db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self):
        try:
            identifier=self.name
        except AttributeError:
            identifier=self.id
        return "<{} {}>".format(self.__class__.__name__,identifier)

    def save(self):
        db.session.add(self)
        db.session.commit(self)

    def delete(self):
        db.session.add(self)
        db.session.commit(self)





