# -*- coding: utf-8 -*-
from flask import Flask, jsonify, abort, make_response, request, redirect
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

@api.route('/api/v1/data/', methods=['GET', 'POST'])
def get_datas():
    try:
      db.connect()
    except Data.DoesNotExist:
        abort(404)

    if request.method == 'POST':
        Data.create(title         = request.form['title'],
                    published_at  = request.form['published_at'],
                    rec           = request.form['rec'],
                    edit          = request.form['edit'],
                    censorship    = request.form['censorship'],
                    thumbnail     = request.form['thumbnail'],
                    reserve       = request.form['reserve'],
                    release       = request.form['release'],
                    comic         = request.form['comic'],
                    tweet         = request.form['tweet'],
                    folder_id     = request.form['folder_id'],
                    rec_url       = request.form['rec_url'],
                    thumbnail_url = request.form['thumbnail_url'],
                    comic_url     = request.form['comic_url'])

        return make_response(jsonify({'result': 'Uploaded'}), 200)

    elif request.method == 'GET':
        cursor = db.execute_sql('select * from data;')

        datas = []
        for row in cursor.fetchall():
            x = dict(zip([d[0] for d in cursor.description], row))
            datas.append(dict(x))

        return convert_for_response(datas)

    db.close()


@api.route('/api/v1/data/<string:id>', methods=['GET', 'POST', 'DELETE'])
def get_data(id):
    try:
        db.connect()
        radio = Data.get(Data.id == id)
    except Data.DoesNotExist:
        abort(404)

    if request.method == 'GET':
        cursor = db.execute_sql('select * from data where id =' + id)

        datas = []
        for row in cursor.fetchall():
            x = dict(zip([d[0] for d in cursor.description], row))
            datas.append(dict(x))

        return convert_for_response(datas)

    elif request.method == 'POST':
        radio.title         = request.form['title']
        radio.published_at  = request.form['published_at']
        radio.rec           = request.form['rec']
        radio.edit          = request.form['edit']
        radio.censorship    = request.form['censorship']
        radio.thumbnail     = request.form['thumbnail']
        radio.reserve       = request.form['reserve']
        radio.release       = request.form['release']
        radio.comic         = request.form['comic']
        radio.tweet         = request.form['tweet']
        radio.folder_id     = request.form['folder_id']
        radio.rec_url       = request.form['rec_url']
        radio.thumbnail_url = request.form['thumbnail_url']
        radio.comic_url     = request.form['comic_url']

        radio.save()

        return make_response(jsonify({'result': 'Updated'}), 200)

    elif request.method == 'DELETE':
        del_data = Data.get(Data.id == id)
        del_data.delete_instance()

        db.commit()

        return make_response(jsonify({'result': 'Deleted'}), 200)

    db.close()

@api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    api.run(host='0.0.0.0', port=3000)
