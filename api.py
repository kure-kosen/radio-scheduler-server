# -*- coding: utf-8 -*-
from flask import Flask, jsonify, abort, make_response
import peewee
import json

db = peewee.SqliteDatabase("./db/datas.db")

def convert_for_response(data):
    return make_response(json.dumps(data, ensure_ascii=False))

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

api = Flask(__name__)

@api.route('/api/v1/data/', methods=['GET'])
def get_datas():
    try:
      db.connect()
    except Data.DoesNotExist:
        abort(404)

    cursor = db.execute_sql('select * from data;')

    datas = []
    for row in cursor.fetchall():
        x = dict(zip([d[0] for d in cursor.description], row))
        datas.append(dict(x))

    return convert_for_response(datas)

    db.close()


@api.route('/api/v1/data/<string:id>', methods=['GET'])
def get_data(id):
    try:
        db.connect()
        radio = Data.get(Data.id == id)
    except Data.DoesNotExist:
        abort(404)

    cursor = db.execute_sql('select * from data where id =' + id)

    datas = []
    for row in cursor.fetchall():
        x = dict(zip([d[0] for d in cursor.description], row))
        datas.append(dict(x))

    return convert_for_response(datas)

    db.close()


@api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    api.run(host='0.0.0.0', port=3000)
