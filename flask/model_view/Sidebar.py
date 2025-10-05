from typing import List
from repositories.DatabaseRepository import DatabaseRepository
from models.Database import Database
from db import db

class Sidebar:
    def __init__(self):
        self._databases = DatabaseRepository(db.session).get_all()
    
    @property
    def databases(self) -> List[Database]:
        return self._databases