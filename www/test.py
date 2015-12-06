#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import orm,asyncio
from models import User,Blog,Comment

def test(loop):
    yield from orm.create_pool(loop=loop,user='root',password='123456',db='awesome')
    u=User(name='test1',email='test2@test.com',passwd='test',image='about:blank')
    yield from u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
