from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
# 创建实例连接
engine = create_engine("mysql+mysqlconnector://root:123456@localhost:3306/goods", encoding='utf8', echo=True)
result = engine.execute("show tables")
print(result.fetchall())
# 创建会话
Session = sessionmaker(bind=engine)
print(Session)

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(20), nullable=False)
    addr = Column(String(50), nullable=False)


# class Orders(Base):
#     __tablename__ = 'orders'
#     id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
#     userid = Column(Integer, ForeignKey('user.id'), nullable=False)

# 可以进行对象关系映射自动生成表
# Base.metadata.create_all(engine)
session = Session()
result = session.query(User.id, User.name, User.addr).filter(User.id == 1).first()
print(result)
# session.add(User(id=0, name="newuser", addr="newaddr"))
# session.commit()
# t5 = session.query(User).filter(User.id == 9).first()
# t5.name = "oldname"
# session.commit()
t4 = session.query(User).filter(User.id == 9).first()
session.delete(t4)
session.commit()
