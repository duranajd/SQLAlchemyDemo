# check sql version
import sqlalchemy

# connect to a database
from sqlalchemy import create_engine
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

# simple connection and showing how text works
with engine.connect() as conn:
  result = conn.execute(text("select 'SQLAlchemy'"))

# showing off commit and other sql commands
with engine.connect() as conn:
  conn.execute(text("CREATE TABLE newTable (a int, b text)"))
  conn.execute(text("INSERT INTO newTable (a, b) VALUES (:a, :b)"), [{"a": 1, "b": "hello"}])
  conn.commit()

