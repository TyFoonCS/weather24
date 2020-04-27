import flask
import logging
import requests
import random
import json
from datetime import datetime
import time


def get_masha():
    masha = (
        "Маша", "Машенька", "Мария", "MariaDB", "Мари", "Маня", "Маша", "Машенька", "Мария", "Маша", "Машенька",
        "Мария")
    sweet = ("милаша", "симпотяша", "любит кашу", "няша", "сибирь наша!")
    return random.choice(masha) + " - " + random.choice(sweet)


def get_weather():
    api_key = "bec88e6c-1b0b-4ac7-a582-a2d55a6c2971"
    weather = requests.get(
        "https://api.weather.yandex.ru/v1/informers?lat=56.84665833710527&lon=53.220355002882044&extra=true",
        headers={
            "X-Yandex-API-Key": api_key,
        }
    )
    donates = requests.post("https://api.vkdonate.ru",
                            params={"key": "e79dce2a3546e97874ac", "action": "donates"})
    weather = json.loads(weather.text)
    res = {}
    donat_res = {}
    res['fact'] = weather['fact'].copy()
    res['now'] = weather['now']
    res['date'] = weather['now_dt']
    donat_res['donates'] = json.loads(donates.text)['donates'].copy()
    for don in donat_res['donates']:
        don['msg'] = mat_filter(don['msg'])
    res.update(donat_res.copy())
    return json.dumps(res)


logging.basicConfig(level=logging.INFO)

data = open('/home/Timurg3000/mysite/req.json', 'r')
now = json.loads(data.read())
data.close()

if abs(int(time.time()) - int(now['now'])) > 3600:  # - 3
    data = open('/home/Timurg3000/mysite/req.json', 'w')
    data.write(str(get_weather()))
    data.close()
    data = open('/home/Timurg3000/mysite/req.json', 'r')
    now = json.loads(data.read())
    data.close()

app = flask.Flask(__name__)


@app.route('/get', methods=['GET'])
def main():
    resp = flask.Response(json.dumps(now))
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp


@app.route('/', methods=['GET'])
def wet():
    weather = now['fact']
    date = now['date'][:10].split('-')
    date.reverse()

    if weather['daytime'] == 'd':
        card = "card"
        back = "http://www.fonstola.ru/pic/201310/2560x1600/fonstola.ru-132983.jpg"
        font = "black"
    else:
        card = "card #4527a0 deep-purple darken-3"
        back = "https://img5.goodfon.ru/original/2560x1600/9/5a/gora-gory-mount-mounts-luna-moon-mesiats-zakat-dymnoe-nebo-o.jpg"
        font = "white"
    return """
<html>
<head>
    <meta charset="utf-8">
    <title> Погода 24 </title>
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <link type="text/css" rel="stylesheet" href="static/css/materialize.min.css" media="screen,projection"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <style>
        .her {
            height: 280;
            width: 600px;
            display: block;
            margin: 0 auto;
            border: none;
        }
        .my_col {
            width: 350px;
            height: 100%;

        }
        .card-content {
            text-align: center;
            color: """ + font + """;
        }
        .pymy {
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .temp {
            font-size: 75px;
        }
        .card-action {
            text-align: center;
        }
        body {
            background-image: url(""" + back + """);
        }
    </style>
</head>
<body>
<script type="text/javascript" src="static/js/materialize.min.js"></script>

<div class="pymy">
    <div class="row">
        <div class="my_col">
            <div class="card """ + card + """ darken-3">
                <div class="card-image">
                    <img src="https://yastatic.net/weather/i/icons/blueye/color/svg/""" + weather['icon'] + """.svg" class="her">
                </div>
                <div class="main_con">
                <div class="card-content">
                    <p class="temp">""" + str(weather['temp']) + """°С</p>
                    <p>Чувствуется как: """ + str(weather['feels_like']) + """°С</p>
                    <p>Скорость ветра: """ + str(weather['wind_speed']) + """ м/с</p>
                    <p> Дата обновления: """ + '.'.join(date) + """</p>
                </div>
                </div>
                <div class="card-action">
                    <a href="http://timurg3000.pythonanywhere.com/" class="act">""" + get_masha() + """</a>
                </div>
            </div>
        </div>
    </div>
</div>
</body>
</html>
"""


if __name__ == '__main__':
    app.run()
