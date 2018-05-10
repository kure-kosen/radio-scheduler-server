# Environment
## Python version
```bash
% python3 -V
Python 3.6.5
```

## pip3
```bash
% pip3 -V
pip 10.0.1

% pip3 freeze
Flask==1.0
peewee==3.3.1
flask-cors==3.0.4
python-dateutil==2.7.2
```

# Usage
## Pre-need
- DBに読み込ませるためのtsvファイル

## Setup
```bash
pip3 install Flask==1.0
pip3 install flask-cors==3.0.4
pip3 install peewee==3.3.1
pip3 install python-dateutil==2.7.2

git clone git@github.com:kobakazu0429/radio-scheduler-server.git
cd radio-scheduler-server
python3 api.py
```

## Description
以下の箇所は自分の環境に合わせて変更して下さい。
- import.pyの5行目 `db = peewee.SqliteDatabase("./db/datas.db")`
- import.pyの33行目 `for line in open("Untitled.csv", "r"):`
- api.pyの6行目 `db = peewee.SqliteDatabase("./db/datas.db")`
- `Class Data(peewee.Model)`

## Check
```bash
% open http://localhost:3000
% open http://localhost:3000/api/v1/publishing_task/
% open http://localhost:3000/api/v1/data/1
```
