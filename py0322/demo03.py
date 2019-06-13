from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker,relationship,backref
engine = create_engine("mysql+mysqlconnector://root:123456@localhost:3306/Qiku", encoding='utf8', echo=True)
Base = declarative_base()


class Tea(Base):
    __tablename__ = "teacher"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(20), nullable=False)


class Stu(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(20), nullable=False)
    teaid = Column(Integer, ForeignKey("teacher.id"), nullable=False)
    tea = relationship("Tea", backref="t")
# Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()

res = session.query(Tea).first().t
print(res)
# 添加命令
# session.add(Tea(id=0, name="teacher1"))
# session.add(Tea(id=0, name="teacher2"))
# session.add(Stu(id=0, name="student1", teaid=1))
# session.add(Stu(id=0, name="student2", teaid=1))
# session.add(Stu(id=0,name="student3", teaid=2))
# session.commit()
# 查询命令
# result = session.query(Stu.id, Stu.name, Stu.teaid).filter(Stu.id == 1).all()
# print(result)
# result = session.query(Tea.id, Tea.name).filter(Tea.id == 1).all()
# print(result)
# 修改命令
# session.query(Stu).filter(Stu.id == 2).update({Stu.name: "student"})
# session.commit()
# 删除命令
# session.query(Stu).filter(Stu.id == 2).delete()
# session.commit()
# session.close()