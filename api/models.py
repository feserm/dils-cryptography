from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    ...
    
class User(Base):
    __tablename__ = 'USERS'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    hashed_password: Mapped[str]
    