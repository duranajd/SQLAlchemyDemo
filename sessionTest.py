from sqlalchemy import String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user_account"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(40))
    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, email={self.email})"

engine = create_engine("sqlite://", echo=True)
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
