from datetime import datetime

from sqlalchemy.exc import DatabaseError

from ..main import flask_db as db


class Template(db.Model):
    __abstract__ = True

    def save(self):
        db.session.add(self)
        self._flush()
        return self

    def update(self, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return self.save()

    def delete(self):
        db.session.delete(self)
        self._flush()

    def _flush(self):
        try:
            db.session.flush()
        except DatabaseError:
            db.session.rollback()
            raise


class GameState(Template):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    time_created = db.Column(db.DateTime, default=datetime.utcnow)
    time_modified = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class GameEvent(Template):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    time_created = db.Column(db.DateTime, default=datetime.utcnow)