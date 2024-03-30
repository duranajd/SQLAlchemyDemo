from sqlalchemy import String, create_engine, select, text
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship
from os import environ as env

#pulled from env file
DATABASE_URL = env.get("DATABASE_URL")

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user_account"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(40))
    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, email={self.email})"

#Engine setup to a database, The pool connection can be changed to your liking
engine = create_engine(
    DATABASE_URL,
    pool_size=5,  # Set the maximum number of connections in the pool
    max_overflow=10,  # Allow up to 10 additional connections to be created if the pool is exhausted
    pool_timeout=30,  # Set the timeout for getting a connection from the pool (in seconds)
    pool_recycle=3600,  # Automatically recycle connections after 1 hour (in seconds)
)

Base.metadata.create_all(engine)

with Session(engine) as session:
    spongebob = User(
        name="spongebob",
        email="spongebob@sqlalchemy.org",
    )
    sandy = User(
        name="sandy",
        email="SandyCheeks@sql.alchemy",
    )
    patrick = User(name="patrick", email="PatrickStar@gmail.com")
    session.add_all([spongebob, sandy, patrick])
    session.commit()

with Session(engine) as session:

    stmt = select(User).where(User.name.in_(["spongebob", "sandy"]))

    for user in session.scalars(stmt):
        print(user)
