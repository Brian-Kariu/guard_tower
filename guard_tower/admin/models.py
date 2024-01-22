"""App models"""
import datetime as dt

from flask_login import UserMixin
from sqlalchemy.ext.hybrid import hybrid_property
from guard_tower.user.models import User

from guard_tower.database import Column, PkModel, db, reference_col, relationship
from guard_tower.extensions import bcrypt

class App(PkModel):
    """An app containing users"""

    __tablename__ = "apps"
    name = Column(db.String(80), unique=True, nullable=False)
    link = Column(db.String(80), nullable=True)
    
    def __init__(self, name, **kwargs):
        """Create instance."""
        super().__init__(name=name, **kwargs)

    def __repr__(self):
        """Represent instance as a unique string."""
        return f"<App({self.name})>"

    def get_users(self):
        """Gets all users associated with the app"""
        users = db.session.query(User).filter(User.app_id == self.id).all()
        return users