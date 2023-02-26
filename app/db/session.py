from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql://root:mysqlpw@localhost:49153/dev")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


engine_dest = create_engine("mysql://root:mysqlpw@localhost:49154/dev")
SessionLocal_dest = sessionmaker(autocommit=False, autoflush=False, bind=engine_dest)



