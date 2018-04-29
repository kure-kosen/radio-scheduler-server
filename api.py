# -*- coding: utf-8 -*-
from flask import Flask, jsonify, abort, make_response, request, redirect
from flask_cors import CORS
import peewee
import json

from datamodel import *


def convert_for_response(data):
    return make_response(json.dumps(data, ensure_ascii=False))

api = Flask(__name__)
CORS(api)


@api.route('/api/v1/publishing_task/', methods=['GET'])
def get_publishing_tasks():
    try:
      db.connect()
    except Task.DoesNotExist:
        abort(404)

    cursor = db.execute_sql('select * from task order by id desc;')

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
    except Task.DoesNotExist:
        abort(404)

    Task.create(title          = request.form['title'],
                published_at   = request.form['published_at'],
                recorded       = request.form['recorded'],
                edited         = request.form['edited'],
                reviewed       = request.form['reviewed'],
                drew_thumbnail = request.form['drew_thumbnail'],
                reserved       = request.form['reserved'],
                released       = request.form['released'],
                drew_comic     = request.form['drew_comic'],
                tweeted        = request.form['tweeted'],
                folder_id      = request.form['folder_id'],
                record_url     = request.form['record_url'],
                thumbnail_url  = request.form['thumbnail_url'],
                comic_url      = request.form['comic_url'])

    return make_response(jsonify({'result': 'Uploaded'}), 200)
    db.close()


@api.route('/api/v1/publishing_task/<string:id>/', methods=['GET'])
def get_publishing_task(id):
    try:
        db.connect()
        publishing_task = Task.get(Task.id == id)
    except Task.DoesNotExist:
        abort(404)

    cursor = db.execute_sql('select * from task where id =' + id)

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
        publishing_task = Task.get(Task.id == id)
    except Task.DoesNotExist:
        abort(404)

    print(request.form)
    print(request.form['edited'])

    publishing_task.title          = request.form['title']
    publishing_task.published_at   = request.form['published_at']
    publishing_task.recorded       = request.form['recorded']
    publishing_task.edited         = request.form['edited']
    publishing_task.reviewed       = request.form['reviewed']
    publishing_task.drew_thumbnail = request.form['drew_thumbnail']
    publishing_task.reserved       = request.form['reserved']
    publishing_task.released       = request.form['released']
    publishing_task.drew_comic     = request.form['drew_comic']
    publishing_task.tweeted        = request.form['tweeted']
    publishing_task.folder_id      = request.form['folder_id']
    publishing_task.record_url     = request.form['record_url']
    publishing_task.thumbnail_url  = request.form['thumbnail_url']
    publishing_task.comic_url      = request.form['comic_url']

    publishing_task.save()

    return make_response(jsonify({'result': 'Updated'}), 200)
    db.close()


@api.route('/api/v1/publishing_task/<string:id>/', methods=['DELETE'])
def delete_publishing_task(id):
    try:
        db.connect()
        delete_publishing_task = Task.get(Task.id == id)
    except Task.DoesNotExist:
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
