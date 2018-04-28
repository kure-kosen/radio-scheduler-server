# -*- coding: utf-8 -*-
import peewee

# データベースを指定
db = peewee.SqliteDatabase("./db/datas.db")

# ユーザーモデルを定義
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

# title, published_at, rec, edit, censorship, thumbnail, reserve, release, comic, tweet, folder_id, rec_url, thumbnail_url, comic_url

# ユーザーテーブル作成
Data.create_table()

# tsvファイルを一行ずつ読み込んでタブで分割し，それぞれをデータベースに登録
for line in open("datas.tsv", "r"):
    (title, published_at, rec, edit, censorship, thumbnail, reserve, release, comic, tweet, folder_id, rec_url, thumbnail_url, comic_url) = tuple(line[:-1].split("\t"))
    Data.create(title         = title,
                published_at  = published_at,
                rec           = rec,
                edit          = edit,
                censorship    = censorship,
                thumbnail     = thumbnail,
                reserve       = reserve,
                release       = release,
                comic         = comic,
                tweet         = tweet,
                folder_id     = folder_id,
                rec_url       = rec_url,
                thumbnail_url = thumbnail_url,
                comic_url     = comic_url)
