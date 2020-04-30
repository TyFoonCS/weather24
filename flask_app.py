import flask
import random
import logging
import requests
import json
import time
import os

carousel_day = (
    "static/images/d1.jpg",
    "static/images/d2.jpg",
    "static/images/d3.jpg",
    "static/images/d4.jpg"
)
carousel_night = (
    "static/images/n1.jpg",
    "static/images/n2.jpg",
    "static/images/n3.jpg",
    "static/images/n4.jpg"
)


def get_pics(day):
    if day:
        word = 'd'
    else:
        word = 'n'
    images = os.listdir(path="static/images")
    pics = list()
    for image in images:
        if image[0] == word and "static/images/" + image not in pics:
            pics.append("static/images/" + image)
    res = random.choices(pics, k=4)
    while len(set(res)) != 4:
        res = random.choices(pics, k=4)
    return res


def mat_filter(msg):
    mat = ['6ля', '6лядь', '6лять', 'b3ъeб', 'cock', 'cunt', 'e6aль', 'ebal', 'eblan', 'eбaл', 'eбaть', 'eбyч', 'eбать',
           'eбёт', 'eблантий', 'fuck', 'fucker', 'fucking', 'xyёв', 'xyй', 'xyя', 'xуе,xуй', 'xую', 'zaeb', 'zaebal',
           'zaebali', 'zaebat', 'архипиздрит', 'ахуел', 'ахуеть', 'бздение', 'бздеть', 'бздех', 'бздецы', 'бздит',
           'бздицы',
           'бздло', 'бзднуть', 'бздун', 'бздунья', 'бздюха', 'бздюшка', 'бздюшко', 'бля', 'блябу', 'блябуду', 'бляд',
           'бляди', 'блядина', 'блядище', 'блядки', 'блядовать', 'блядство', 'блядун', 'блядуны', 'блядунья', 'блядь',
           'блядюга блять', 'вафел', 'вафлёр', 'взъебка', 'взьебка', 'взьебывать', 'въеб', 'въебался', 'въебенн',
           'въебусь',
           'въебывать', 'выблядок', 'выблядыш', 'выеб', 'выебать', 'выебен', 'выебнулся', 'выебон', 'выебываться',
           'выпердеть', 'высраться', 'выссаться', 'вьебен', 'гавно', 'гавнюк', 'гавнючка', 'гамно', 'гандон', 'гнид',
           'гнида', 'гниды', 'говенка', 'говенный', 'говешка', 'говназия', 'говнецо', 'говнище', 'говно', 'говноед',
           'говнолинк', 'говночист', 'говнюк', 'говнюха', 'говнядина', 'говняк', 'говняный', 'говнять', 'гондон',
           'доебываться', 'долбоеб', 'долбоёб', 'долбоящер', 'дрисня', 'дрист', 'дристануть', 'дристать', 'дристун',
           'дристуха', 'дрочелло', 'дрочена', 'дрочила', 'дрочилка', 'дрочистый', 'дрочить', 'дрочка', 'дрочун', 'е6ал',
           'е6ут', 'еб твою мать', 'ёб твою мать', 'ёбaн', 'ебaть', 'ебyч', 'ебал', 'ебало', 'ебальник', 'ебан',
           'ебанамать', 'ебанат', 'ебаная', 'ёбаная', 'ебанический', 'ебанный', 'ебанныйврот', 'ебаное', 'ебануть',
           'ебануться', 'ёбаную', 'ебаный', 'ебанько', 'ебарь', 'ебат', 'ёбат', 'ебатория', 'ебать', 'ебать-копать',
           'ебаться', 'ебашить', 'ебёна', 'ебет', 'ебёт', 'ебец', 'ебик', 'ебин', 'ебись', 'ебическая', 'ебки', 'ебла',
           'еблан', 'ебливый', 'еблище', 'ебло', 'еблыст', 'ебля', 'ёбн', 'ебнуть', 'ебнуться', 'ебня', 'ебошить',
           'ебская',
           'ебский', 'ебтвоюмать', 'ебун', 'ебут', 'ебуч', 'ебуче', 'ебучее', 'ебучий', 'ебучим', 'ебущ', 'ебырь',
           'елда',
           'елдак', 'елдачить', 'жопа', 'жопу', 'заговнять', 'задрачивать', 'задристать', 'задрота', 'зае6', 'заё6',
           'заеб',
           'заёб', 'заеба', 'заебал', 'заебанец', 'заебастая', 'заебастый', 'заебать', 'заебаться', 'заебашить',
           'заебистое', 'заёбистое', 'заебистые', 'заёбистые', 'заебистый', 'заёбистый', 'заебись', 'заебошить',
           'заебываться', 'залуп', 'залупа', 'залупаться', 'залупить', 'залупиться', 'замудохаться', 'запиздячить',
           'засерать', 'засерун', 'засеря', 'засирать', 'засрун', 'захуячить', 'заябестая', 'злоеб', 'злоебучая',
           'злоебучее', 'злоебучий', 'ибанамат', 'ибонех', 'изговнять', 'изговняться', 'изъебнуться', 'ипать',
           'ипаться',
           'ипаццо', 'Какдвапальцаобоссать', 'конча', 'курва', 'курвятник', 'лох', 'лошарa', 'лошара', 'лошары',
           'лошок',
           'лярва', 'малафья', 'манда', 'мандавошек', 'мандавошка', 'мандавошки', 'мандей', 'мандень', 'мандеть',
           'мандища',
           'мандой', 'манду', 'мандюк', 'минет', 'минетчик', 'минетчица', 'млять', 'мокрощелка', 'мокрощёлка', 'мразь',
           'мудak', 'мудaк', 'мудаг', 'мудак', 'муде', 'мудель', 'мудеть', 'муди', 'мудил', 'мудила', 'мудистый',
           'мудня',
           'мудоеб', 'мудозвон', 'мудоклюй', 'на хер', 'на хуй', 'набздел', 'набздеть', 'наговнять', 'надристать',
           'надрочить', 'наебать', 'наебет', 'наебнуть', 'наебнуться', 'наебывать', 'напиздел', 'напиздели',
           'напиздело',
           'напиздили', 'насрать', 'настопиздить', 'нахер', 'нахрен', 'нахуй', 'нахуйник', 'не ебет', 'не ебёт',
           'невротебучий', 'невъебенно', 'нехира', 'нехрен', 'Нехуй', 'нехуйственно', 'ниибацо', 'ниипацца', 'ниипаццо',
           'ниипет', 'никуя', 'нихера', 'нихуя', 'обдристаться', 'обосранец', 'обосрать', 'обосцать', 'обосцаться',
           'обсирать', 'объебос', 'обьебать обьебос', 'однохуйственно', 'опездал', 'опизде', 'опизденивающе',
           'остоебенить',
           'остопиздеть', 'отмудохать', 'отпиздить', 'отпиздячить', 'отпороть', 'отъебись', 'охуевательский',
           'охуевать',
           'охуевающий', 'охуел', 'охуенно', 'охуеньчик', 'охуеть', 'охуительно', 'охуительный', 'охуяньчик',
           'охуячивать',
           'охуячить', 'очкун', 'падла', 'падонки', 'падонок', 'паскуда', 'педерас', 'педик', 'педрик', 'педрила',
           'педрилло', 'педрило', 'педрилы', 'пездень', 'пездит', 'пездишь', 'пездо', 'пездят', 'пердануть', 'пердеж',
           'пердение', 'пердеть', 'пердильник', 'перднуть', 'пёрднуть', 'пердун', 'пердунец', 'пердунина', 'пердунья',
           'пердуха', 'пердь', 'переёбок', 'пернуть', 'пёрнуть', 'пи3д', 'пи3де', 'пи3ду', 'пиzдец', 'пидар', 'пидарaс',
           'пидарас', 'пидарасы', 'пидары', 'пидор', 'пидорасы', 'пидорка', 'пидорок', 'пидоры', 'пидрас', 'пизда',
           'пиздануть', 'пиздануться', 'пиздарваньчик', 'пиздато', 'пиздатое', 'пиздатый', 'пизденка', 'пизденыш',
           'пиздёныш', 'пиздеть', 'пиздец', 'пиздит', 'пиздить', 'пиздиться', 'пиздишь', 'пиздища', 'пиздище',
           'пиздобол',
           'пиздоболы', 'пиздобратия', 'пиздоватая', 'пиздоватый', 'пиздолиз', 'пиздонутые', 'пиздорванец',
           'пиздорванка',
           'пиздострадатель', 'пизду', 'пиздуй', 'пиздун', 'пиздунья', 'пизды', 'пиздюга', 'пиздюк', 'пиздюлина',
           'пиздюля',
           'пиздят', 'пиздячить', 'писбшки', 'писька', 'писькострадатель', 'писюн', 'писюшка', 'по хуй', 'по хую',
           'подговнять', 'подонки', 'подонок', 'подъебнуть', 'подъебнуться', 'поебать', 'поебень', 'поёбываает',
           'поскуда',
           'посрать', 'потаскуха', 'потаскушка', 'похер', 'похерил', 'похерила', 'похерили', 'похеру', 'похрен',
           'похрену',
           'похуй', 'похуист', 'похуистка', 'похую', 'придурок', 'приебаться', 'припиздень', 'припизднутый',
           'припиздюлина',
           'пробзделся', 'проблядь', 'проеб', 'проебанка', 'проебать', 'промандеть', 'промудеть', 'пропизделся',
           'пропиздеть', 'пропиздячить', 'раздолбай', 'разхуячить', 'разъеб', 'разъеба', 'разъебай', 'разъебать',
           'распиздай', 'распиздеться', 'распиздяй', 'распиздяйство', 'распроеть', 'сволота', 'сволочь', 'сговнять',
           'секель', 'серун', 'серька', 'сестроеб', 'сикель', 'сила', 'сирать', 'сирывать', 'соси', 'спиздел',
           'спиздеть',
           'спиздил', 'спиздила', 'спиздили', 'спиздит', 'спиздить', 'срака', 'сраку', 'сраный', 'сранье', 'срать',
           'срун',
           'ссака', 'ссышь', 'стерва', 'страхопиздище', 'сука', 'суки', 'суходрочка', 'сучара', 'сучий', 'сучка',
           'сучко',
           'сучонок', 'сучье', 'сцание', 'сцать', 'сцука', 'сцуки', 'сцуконах', 'сцуль', 'сцыха', 'сцышь', 'съебаться',
           'сыкун', 'трахае6', 'трахаеб', 'трахаёб', 'трахатель', 'ублюдок', 'уебать', 'уёбища', 'уебище', 'уёбище',
           'уебищное', 'уёбищное', 'уебк', 'уебки', 'уёбки', 'уебок', 'уёбок', 'урюк', 'усраться', 'ушлепок',
           'х_у_я_р_а',
           'хyё', 'хyй', 'хyйня', 'хамло', 'хер', 'херня', 'херовато', 'херовина', 'херовый', 'хитровыебанный',
           'хитрожопый', 'хуeм', 'хуе', 'хуё', 'хуевато', 'хуёвенький', 'хуевина', 'хуево', 'хуевый', 'хуёвый', 'хуек',
           'хуёк', 'хуел', 'хуем', 'хуенч', 'хуеныш', 'хуенький', 'хуеплет', 'хуеплёт', 'хуепромышленник', 'хуерик',
           'хуерыло', 'хуесос', 'хуесоска', 'хуета', 'хуетень', 'хуею', 'хуи', 'хуй', 'хуйком', 'хуйло', 'хуйня',
           'хуйрик',
           'хуище', 'хуля', 'хую', 'хуюл', 'хуя', 'хуяк', 'хуякать', 'хуякнуть', 'хуяра', 'хуясе', 'хуячить', 'целка',
           'чмо', 'чмошник', 'чмырь', 'шалава', 'шалавой', 'шараёбиться', 'шлюха', 'шлюхой', 'шлюшка', 'ябывает']
    for bad in mat:
        if bad in msg:
            msg = msg.replace(bad, "***")
    return msg


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
    donat_res = dict()
    res['fact'] = weather['fact'].copy()
    res['now'] = weather['now']
    res['date'] = weather['now_dt']
    donat_res['donates'] = json.loads(donates.text)['donates'].copy()
    for don in donat_res['donates']:
        don['msg'] = mat_filter(don['msg'])
    res.update(donat_res.copy())
    return res


logging.basicConfig(level=logging.INFO)

data = open('req.json', 'r')
now = json.loads(data.read())
wishes = {'wishes': now['wishes']}
print(wishes)
data.close()

if abs(int(time.time()) - int(now['now'])) > 3600:  # - 3
    data = open('req.json', 'w')
    to_write = get_weather()
    to_write.update(wishes)
    data.write(json.dumps(to_write))
    data.close()
    data = open('req.json', 'r')  # /home/Timurg3000/mysite/
    now = json.loads(data.read())
    data.close()

app = flask.Flask(__name__)


@app.route('/get', methods=['GET'])
def main():
    resp = flask.Response(json.dumps(now))
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp


@app.route('/', methods=['GET', 'POST'])
def wet():
    wish = False

    if flask.request.method == 'POST' and flask.request.form.get('wish'):
        mat_filter(flask.request.form.get('wish'))
        data_wish = open('req.json', 'r', encoding="utf-8")
        now_wish = json.loads(data_wish.read())
        data_wish.close()
        wish = mat_filter(flask.request.form.get('wish')).replace(';', '')
        if not wish.replace(' ', ''):
            wish = False
        if wish:
            now_wish['wishes'] = now_wish['wishes'] + ";;" + wish
            wish = random.choices(now_wish['wishes'].split(";;"), k=4)
            wish[0] = mat_filter(flask.request.form.get('wish'))
            data_wish = open('req.json', 'w', encoding="utf-8")
            data_wish.write(str(json.dumps(now_wish)))
            data_wish.close()

    if not wish:
        data_wish = open('req.json', 'r', encoding="utf-8")
        now_wish = json.loads(data_wish.read())
        data_wish.close()
        print(now_wish)
        wish = random.choices(now_wish['wishes'].split(";;"), k=4)
        print(wish, 144)

    weather = now['fact']
    date = '.'.join(now['date'][:10].split('-')[::-1])

    if weather['daytime'] == 'd':
        card = "card"
        back = "http://www.fonstola.ru/pic/201310/2560x1600/fonstola.ru-132983.jpg"
        font = "black"
        alerts_back = "https://www.culture.ru/storage/images/8ba9d7a028dfc838942957ef12f67936/8234d8564039f6a12306998f9f61eac5.jpg"
        carousel_pics = get_pics(True)
    else:
        card = "card #4527a0 deep-purple darken-3"
        back = "https://img5.goodfon.ru/original/2560x1600/9/5a/gora-gory-mount-mounts-luna-moon-mesiats-zakat-dymnoe-nebo-o.jpg"
        font = "white"
        alerts_back = "https://s1.1zoom.ru/big3/687/Milky_Way_Lake_Stars_Sky_458932.jpg"
        carousel_pics = get_pics(False)

    return flask.render_template('index.html', temp=weather['temp'],
                                 feels_like=weather['feels_like'],
                                 wind_speed=weather['wind_speed'],
                                 date=date,
                                 masha=get_masha(),
                                 alerts_back=alerts_back,
                                 card=card,
                                 back=back,
                                 font=font,
                                 icon=weather['icon'],
                                 wish=wish,
                                 carousel_pics=carousel_pics
                                 )


if __name__ == '__main__':
    app.run()
