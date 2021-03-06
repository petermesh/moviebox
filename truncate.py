#!/usr/bin/env python
# coding:utf-8
import sys

import MySQLdb

import settings


db = MySQLdb.connect(**settings.MYSQL_CONF)


def truncate(*tables):
    cursor = db.cursor()
    for table in tables:
        sql = "delete from %s" % table
        cursor.execute(sql)
        print("Truncate table %s." % table)
    db.commit()
    print("finish.")


if __name__ == '__main__':
    arg_tables = sys.argv[1:]
    all_tables = [
        'category', 'category_trans', 'movie',
        'recommend', 'trailer', 'trailer_source',
        'tv', 'tv_episode', 'tv_season',
        'app_upgrade', 'actor', 'actor_trans',
        'distributor', 'distributor_trans',
        'director', 'director_trans'
    ]

    truncate(*(arg_tables or all_tables))
