#!/usr/bin/env python
# coding: utf8
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, Boolean, \
    Float, Unicode, Date
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import UniqueConstraint


Base = declarative_base()


def init_db(engine):
    Base.metadata.create_all(bind=engine)

# Put your models here


class GPDM(Base):
    """股票代码表"""
    __tablename__ = 'gpdm'
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 市场代码，0代表深圳，1代码上海
    SCDM = Column(Unicode(1), nullable=False)
    # 股票代码
    GPDM = Column(Unicode(10), nullable=False)
    # 市场简称，SZ代表深圳，SH代表上海
    SCJC = Column(Unicode(2), nullable=False)
    # 股票名称
    GPMC = Column(String(10), nullable=False)
    # 识别代码, '市场代码 + 股票代码'
    CODE = Column(Unicode(10), nullable=False)
    # CODE = Column(String(10), primary_key=True)
    __table_args__ = (
        # ForeignKeyConstraint(['id'], ['remote_table.id']),
        UniqueConstraint('CODE'),
        # {'autoload': True}  # 最后的参数可以用字典 想想*argsand **kwargs
    )


class RXHQ(Base):
    """日线行情"""
    __tablename__ = 'rxhq'
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 识别代码, '市场代码 + 股票代码'
    CODE = Column(Unicode(10), nullable=False, index=True)
    #交易日期
    JYRQ = Column(Date, nullable=False, index=True)
    #开盘价格
    OPEN = Column(Integer, nullable=False, default=0)
    #最高价格
    HIGH = Column(Integer, nullable=False, default=0)
    #最低价格
    LOW = Column(Integer, nullable=False, default=0)
    #收盘价格
    CLOSE = Column(Integer, nullable=False, default=0)
    #昨日收盘价格
    PCLOSE = Column(Integer, nullable=False, default=0)
    #昨日最高价格
    PHIGH = Column(Integer, nullable=False, default=0)
    #昨日最低价格
    PLOW = Column(Integer, nullable=False, default=0)
    #成交量
    VOL = Column(Integer, nullable=False, default=0)
    #成交额
    AMT = Column(Integer, nullable=False, default=0)
    #均价
    AVG = Column(Integer, nullable=False, default=0)
    #涨幅
    CHG = Column(Float, nullable=False, default=0)
    #换手
    TOR = Column(Float, nullable=False, default=0)
    __table_args__ = (
        UniqueConstraint('CODE', 'JYRQ'),
    )


class GBBQ(Base):
    """股本变迁"""
    __tablename__ = 'gbbq'
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 识别代码, '市场代码 + 股票代码'
    CODE = Column(Unicode(10), nullable=False, index=True)
    #交易日期
    BGRQ = Column(Date, nullable=False, index=True)
    #总股本
    TOTAL = Column(Integer, nullable=False, default=0)
    #流通A股
    FLOW = Column(Integer, nullable=False, default=0)
    #实际A股
    REAL = Column(Integer, nullable=False, default=0)
    #市盈率
    EARN = Column(Float, nullable=False, default=0)
    #流通市值
    TMV = Column(Float, nullable=False, default=0)
    #利润同比
    YOYG = Column(Float, nullable=False, default=0)
    #净利润率
    NPR = Column(Float, nullable=False, default=0)
    #攻击波
    ATTACK = Column(Float, nullable=False, default=0)
    __table_args__ = (
        UniqueConstraint('CODE', 'BGRQ'),
    )


class KZHQ(Base):
    """扩展行情，经过复权处理"""
    __tablename__ = 'kzhq'
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 识别代码, '市场代码 + 股票代码'
    CODE = Column(Unicode(10), nullable=False, index=True)
    #交易日期
    JYRQ = Column(Date, nullable=False, index=True)
    #开盘价格
    OPEN = Column(Integer, nullable=False, default=0)
    #最高价格
    HIGH = Column(Integer, nullable=False, default=0)
    #最低价格
    LOW = Column(Integer, nullable=False, default=0)
    #收盘价格
    CLOSE = Column(Integer, nullable=False, default=0)
    #昨日收盘价格
    PCLOSE = Column(Integer, nullable=False, default=0)
    #昨日最高价格
    PHIGH = Column(Integer, nullable=False, default=0)
    #昨日最低价格
    PLOW = Column(Integer, nullable=False, default=0)
    #成交量
    VOL = Column(Integer, nullable=False, default=0)
    #复权成交量
    CVOL = Column(Integer, nullable=False, default=0)
    #成交额
    AMT = Column(Integer, nullable=False, default=0)
    #三日成交额
    AMT3 = Column(Integer, nullable=False, default=0)
    #均价
    AVG = Column(Integer, nullable=False, default=0)
    #复权均价
    CAVG = Column(Integer, nullable=False, default=0)
    # 5日均价
    AVG5 = Column(Integer, nullable=False, default=0)
    #涨幅
    CHG = Column(Float, nullable=False, default=0)
    # 5日涨幅
    CHG5 = Column(Float, nullable=False, default=0)
    #换手率TurnOver Ratio
    TOR = Column(Float, nullable=False, default=0)
    #复权换手率TurnOver Ratio
    ATOR = Column(Float, nullable=False, default=0)
    #总股本
    TOTAL = Column(Integer, nullable=False, default=0)
    #流通A股
    FLOW = Column(Integer, nullable=False, default=0)
    #实际A股
    REAL = Column(Integer, nullable=False, default=0)
    #流通市值
    TMV = Column(Float, nullable=False, default=0)
    #十日内最大三日金额之和大于今日金额倍数
    MUL = Column(Float, nullable=False, default=0)
    #中心价
    CEN = Column(Float, nullable=False, default=0)
    # 5天内最高价与最低价之比
    GOD = Column(Float, nullable=False, default=0)
    # 5天内均价方差
    MOD = Column(Float, nullable=False, default=0)
    #选中
    SEL = Column(Float, nullable=False, default=0)
    __table_args__ = (
        UniqueConstraint('CODE', 'JYRQ'),
    )


class BKDM(Base):
    """板块代码"""
    __tablename__ = 'bkdm'
    id = Column(Integer, primary_key=True, autoincrement=True)
    #板块代码
    BKDM = Column(Unicode(10), nullable=False)
    #板块名称
    BKMC = Column(Unicode(10), nullable=False)
    __table_args__ = (
        UniqueConstraint('BKDM'),
    )


class BKGP(Base):
    """板块股票"""
    __tablename__ = 'bkgp'
    id = Column(Integer, primary_key=True, autoincrement=True)
    #板块代码
    BKDM = Column(Unicode(10), nullable=False)
    # 识别代码, '市场代码 + 股票代码'
    CODE = Column(Unicode(10), nullable=False)
    __table_args__ = (
        UniqueConstraint('BKDM', 'CODE'),
    )


class GNBK(Base):
    """概念板块"""
    __tablename__ = 'gnbk'
    id = Column(Integer, primary_key=True, autoincrement=True)
    #概念类型
    GNLX = Column(Unicode(10), nullable=False)
    #板块代码
    BKDM = Column(Unicode(10), nullable=False)
    __table_args__ = (
        UniqueConstraint('GNLX', 'BKDM'),
    )


class INFO(Base):
    """资讯"""
    __tablename__ = 'info'
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 识别代码, '市场代码 + 股票代码'
    CODE = Column(Unicode(10), nullable=False)
    #交易日期
    TIME = Column(DateTime, nullable=False)
    #标题
    TITLE = Column(Unicode(100), nullable=False)
    __table_args__ = (
        UniqueConstraint('CODE', 'TIME'),
    )
