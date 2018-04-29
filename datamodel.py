# -*- coding: utf-8 -*-
import peewee


db = peewee.SqliteDatabase("./db/datas.db")


class Data(peewee.Model):
    title         = peewee.TextField()
    published_at  = peewee.DateField()
    rec           = peewee.BooleanField()
    edit          = peewee.BooleanField()
    censorship    = peewee.BooleanField()
    thumbnail     = peewee.BooleanField()
    reserve       = peewee.BooleanField()
    release       = peewee.BooleanField()
    comic         = peewee.BooleanField()
    tweet         = peewee.BooleanField()
    folder_id     = peewee.TextField()
    rec_url       = peewee.TextField()
    thumbnail_url = peewee.TextField()
    comic_url     = peewee.TextField()

    class Meta:
        database = db
