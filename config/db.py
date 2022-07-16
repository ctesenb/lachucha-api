from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#DATABASE_URL = "mysql+mysqlconnector://user:pass@host:port/dbname"
engine = create_engine("mysql+pymysql://admin:cFVp6Wko@mysql-82904-0.cloudclusters.net:19589/lachucha")

meta = MetaData()

conn = engine.connect()

##SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

##Base = declarative_base()