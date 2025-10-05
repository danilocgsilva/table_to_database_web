from sqlalchemy.orm import Session
from typing import Optional, List
from models.Database import Database

class DatabaseRepository:
    def __init__(self, session: Session):
        self.session = session
        
    def get_by_id(self, database_id: int) -> Optional[Database]:
        return self.session.query(Database).filter(Database.id == database_id).first()
    
    def get_all(self) -> List[Database]:
        return self.session.query(Database).all()
    
    def create(self, database: Database) -> Database:
        try:
            self.session.add(database)
            self.session.commit()
            self.session.refresh(database)
            return database
        except:
            self.session.rollback()
            raise
    
