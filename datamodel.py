# -*- coding: utf-8 -*-
import peewee


db = peewee.SqliteDatabase("./db/tasks.db")


class Task(peewee.Model):
    title          = peewee.TextField()
    published_at   = peewee.DateField()
    recorded       = peewee.BooleanField()
    edited         = peewee.BooleanField()
    reviewed       = peewee.BooleanField()
    drew_thumbnail = peewee.BooleanField()
    reserved       = peewee.BooleanField()
    released       = peewee.BooleanField()
    drew_comic     = peewee.BooleanField()
    tweeted        = peewee.BooleanField()
    folder_id      = peewee.TextField()
    record_url     = peewee.TextField()
    thumbnail_url  = peewee.TextField()
    comic_url      = peewee.TextField()

    class Meta:
        database = db
