from sqlalchemy import Column, Integer, BigInteger, String, Float, Date, ForeignKey, Boolean, DateTime

from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    telegram_id = Column(Integer, primary_key=True, unique=True)
    number_of_clicks = Column(BigInteger, nullable=False, default=0)
    time_of_last_click = Column(DateTime, nullable=True)
    password = Column(String, nullable=True)

    bought = relationship("Bought", lazy="joined")


class Bought(Base):
    __tablename__ = "bought"

    id = Column(Integer, primary_key=True, unique=True)

    user_id = Column(Integer, ForeignKey("user.telegram_id"), nullable=False)
    item_id = Column(Integer, ForeignKey("item.id"), nullable=False)

    items = relationship("Item", lazy="joined")


class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(BigInteger, nullable=False)

    boost = relationship("Boost", back_populates="item", lazy="joined")


class Boost(Base):
    __tablename__ = "boost"

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    boost = Column(Integer, nullable=False, default=0)
    x_boost = Column(Integer, nullable=False, default=0)

    item_id = Column(Integer, ForeignKey("item.id"), nullable=False)
    item = relationship("Item", back_populates="boost", lazy="joined")
