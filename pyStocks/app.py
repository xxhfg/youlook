#!/usr/bin/env python
# coding: utf8
import sys
import os
import libs
from database import *
from models import *


def main():
    init_db(engine)
    db_session.add_all([
        GPDM(CODE='1', GPMC='1', SCDM='1', GPDM='1', SCJC='1'),
        GPDM(CODE='2', GPMC='2', SCDM='2', GPDM='2', SCJC='2'),
    ])
    db_session.commit()
    for n in db_session.query(GPDM).all():
        print n.CODE, n.GPMC
    db_session.query(GPDM).all()

if __name__ == '__main__':
    main()
