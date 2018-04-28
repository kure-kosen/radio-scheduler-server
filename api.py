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

@api.route('/api/v1/publishing_task/', methods=['GET'])
def get_publishing_tasks():
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


@api.route('/api/v1/publishing_task/', methods=['POST'])
def create_publishing_task():
    try:
      db.connect()
    except Data.DoesNotExist:
        abort(404)

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
    db.close()


@api.route('/api/v1/publishing_task/<string:id>/', methods=['GET'])
def get_publishing_task(id):
    try:
        db.connect()
        publishing_task = Data.get(Data.id == id)
    except Data.DoesNotExist:
        abort(404)

    cursor = db.execute_sql('select * from data where id =' + id)

    print(publishing_task)
    print(cursor)

    datas = []
    for row in cursor.fetchall():
        x = dict(zip([d[0] for d in cursor.description], row))
        datas.append(dict(x))

    return convert_for_response(datas)
    db.close()


@api.route('/api/v1/publishing_task/<string:id>/', methods=['PATCH'])
def update_publishing_task(id):
    try:
        db.connect()
        publishing_task = Data.get(Data.id == id)
    except Data.DoesNotExist:
        abort(404)

    publishing_task.title         = request.form['title']
    publishing_task.published_at  = request.form['published_at']
    publishing_task.rec           = request.form['rec']
    publishing_task.edit          = request.form['edit']
    publishing_task.censorship    = request.form['censorship']
    publishing_task.thumbnail     = request.form['thumbnail']
    publishing_task.reserve       = request.form['reserve']
    publishing_task.release       = request.form['release']
    publishing_task.comic         = request.form['comic']
    publishing_task.tweet         = request.form['tweet']
    publishing_task.folder_id     = request.form['folder_id']
    publishing_task.rec_url       = request.form['rec_url']
    publishing_task.thumbnail_url = request.form['thumbnail_url']
    publishing_task.comic_url     = request.form['comic_url']

    publishing_task.save()

    return make_response(jsonify({'result': 'Updated'}), 200)
    db.close()

@api.route('/api/v1/publishing_task/<string:id>/', methods=['DELETE'])
def delete_publishing_task(id):
    try:
        db.connect()
        delete_publishing_task = Data.get(Data.id == id)
    except Data.DoesNotExist:
        abort(404)

    delete_publishing_task.delete_instance()

    db.commit()

    return make_response(jsonify({'result': 'Deleted'}), 200)
    db.close()


@api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    api.run(host='0.0.0.0', port=3000)
