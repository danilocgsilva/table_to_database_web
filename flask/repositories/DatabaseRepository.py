from sqlalchemy.orm import Session
from typing import Optional, List
from models.Database import Database
from cryptography.fernet import Fernet
import os

class DatabaseRepository:
    def __init__(self, session: Session):
        self.session = session
        
    def get_by_id(self, database_id: int) -> Optional[Database]:
        return self.session.query(Database).filter(Database.id == database_id).first()
    
    def get_all(self) -> List[Database]:
        return self.session.query(Database).all()
    
    def create(self, database: Database) -> Database:
        database.password = self._encrypt(database.password)
        try:
            self.session.add(database)
            self.session.commit()
            self.session.refresh(database)
            return database
        except:
            self.session.rollback()
            raise
        
    def update(self, database: Database):
        try:
            self.session.merge(database)
            self.session.commit()
            self.session.refresh(database)
        except:
            self.session.rollback()
            raise
        
    def delete(self, database: Database) -> bool:
        try:
            deleted = self.session.query(Database).filter(Database.id == database.id).delete()
            self.session.commit()
            return deleted > 0
        except:
            self.session.rollback()
            raise
    
    def _encrypt(self, value: str) -> str:
        key = bytes(os.environ.get('ENCRYPTION_KEY'), 'utf-8')
        cipher = Fernet(key)
        encrypted_value = cipher.encrypt(bytes(value, 'utf-8'))
        return encrypted_value.decode('utf-8')
        
