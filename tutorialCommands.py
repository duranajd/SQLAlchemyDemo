# imports required functions 
from sqlalchemy import * #imports all functions
from sqlalchemy import create_engine, text #imports specific functions
from sqlalchemy.orm import Session #imports specific function for session

# create engine with pooling capabilities
global my_engine
my_engine = create_engine(
    "sqlite+pysqlite:///:memory:",
    pool_size=5,  # Set the maximum number of connections in the pool
    max_overflow=10,  # Allow up to 10 additional connections to be created if the pool is exhausted
    pool_timeout=30,  # Set the timeout for getting a connection from the pool (in seconds)
    pool_recycle=3600,  # Automatically recycle connections after 1 hour (in seconds)
)

# simple connection and showing how text works
with my_engine.connect() as conn:
  result = conn.execute(text("select 'SQLAlchemy'"))
  conn.close()

# showing off commit and other sql commands
with my_engine.connect() as conn:
  conn.execute(text("CREATE TABLE newTable (a int, b text)"))
  conn.execute(text("INSERT INTO newTable (a, b) VALUES (:a, :b)"), [{"a": 1, "b": "hello"}])
  conn.commit()
  conn.close()

#do an example of using the python syntax for writing queries
  
#do an example of session stuff (truthfully IDK how to really do this in an example that makes sense)
