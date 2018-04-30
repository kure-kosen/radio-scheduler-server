# -*- coding: utf-8 -*-
from flask import Flask, jsonify, abort, make_response, request, redirect
from flask_cors import CORS
import peewee
import json

from datamodel import *


api = Flask(__name__)
CORS(api)


def convert_for_response(data):
    return make_response(json.dumps(data, ensure_ascii=False))


@api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@api.before_request
def before_request_handler():
    db.connect()

@api.teardown_request
def after_request_handler(exc):
    if not db.is_closed():
        db.close()


@api.route('/api/v1/publishing_task/', methods=['GET'])
def get_publishing_tasks():
    cursor = db.execute_sql('select * from task order by id desc;')

    datas = []
    for row in cursor.fetchall():
        x = dict(zip([d[0] for d in cursor.description], row))
        datas.append(dict(x))

    return convert_for_response(datas)


@api.route('/api/v1/publishing_task/', methods=['POST'])
def create_publishing_task():
    Task.create(title          = request.form['title'],
                published_at   = request.form['published_at'],
                recorded       = int(request.form['recorded']),
                edited         = int(request.form['edited']),
                reviewed       = int(request.form['reviewed']),
                drew_thumbnail = int(request.form['drew_thumbnail']),
                reserved       = int(request.form['reserved']),
                released       = int(request.form['released']),
                drew_comic     = int(request.form['drew_comic']),
                tweeted        = int(request.form['tweeted']),
                folder_id      = request.form['folder_id'],
                record_url     = request.form['record_url'],
                thumbnail_url  = request.form['thumbnail_url'],
                comic_url      = request.form['comic_url'])

    return make_response(jsonify({'result': 'Uploaded'}), 200)


@api.route('/api/v1/publishing_task/<string:id>/', methods=['GET'])
def get_publishing_task(id):
    publishing_task = Task.get(Task.id == id)

    cursor = db.execute_sql('select * from task where id =' + id)

    datas = []
    for row in cursor.fetchall():
        x = dict(zip([d[0] for d in cursor.description], row))
        datas.append(dict(x))

    return convert_for_response(datas)


@api.route('/api/v1/publishing_task/<string:id>/', methods=['PATCH'])
def update_publishing_task(id):
    publishing_task = Task.get(Task.id == id)

    publishing_task.title          = request.form['title']
    publishing_task.published_at   = request.form['published_at']
    publishing_task.recorded       = int(request.form['recorded'])
    publishing_task.edited         = int(request.form['edited'])
    publishing_task.reviewed       = int(request.form['reviewed'])
    publishing_task.drew_thumbnail = int(request.form['drew_thumbnail'])
    publishing_task.reserved       = int(request.form['reserved'])
    publishing_task.released       = int(request.form['released'])
    publishing_task.drew_comic     = int(request.form['drew_comic'])
    publishing_task.tweeted        = int(request.form['tweeted'])
    publishing_task.folder_id      = request.form['folder_id']
    publishing_task.record_url     = request.form['record_url']
    publishing_task.thumbnail_url  = request.form['thumbnail_url']
    publishing_task.comic_url      = request.form['comic_url']

    publishing_task.save()

    return make_response(jsonify({'result': 'Updated'}), 200)


@api.route('/api/v1/publishing_task/<string:id>/', methods=['DELETE'])
def delete_publishing_task(id):
    delete_publishing_task = Task.get(Task.id == id)

    delete_publishing_task.delete_instance()

    return make_response(jsonify({'result': 'Deleted'}), 200)


if __name__ == '__main__':
    api.run(host='0.0.0.0', port=3000)
