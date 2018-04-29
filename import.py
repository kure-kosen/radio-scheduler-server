# -*- coding: utf-8 -*-
import peewee

from datamodel import *


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
