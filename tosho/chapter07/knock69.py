'''
start Flask server:
python knock69.py
'''

from flask import Flask, request
from knock64 import MusicDb

app = Flask(__name__)
db = MusicDb()

@app.route('/')
def index():
    content = '''
    <!DOCTYPE html>
    <html lang="ja">
        <head>
        </head>
        <body>
            <form method="post">
                <input name="text">
                <input type="submit" value="Search">
            </form>
        </bodY>
    </html>
    '''
    return content

@app.route('/', methods=['POST'])
def index_post():
    q = request.form['text']
    like = lambda s: {"$regex": q}
    match = {"$or": [
        {"name": like(q)},
        {"aliases.name": like(q)},
        {"tags.value": like(q)}
    ]}
    pipeline = [
        {"$match": match},
        {"$group": {
            "_id": "$name", 
            "rates": {"$sum": "$rating.count"},
            "tota_rate":{
                "$sum": {
                    "$multiply": ["$rating.count", "$rating.value"]
                }
            }
        }
        },
        {"$sort": {"rates": -1}},
        {"$limit": 10}
    ]

    content = '''
    <!DOCTYPE html>
    <html lang="ja">
        <head>
        </head>
        <body>
            <p tyle="font-size:x-large">Results for '{0}'</p>
            <ul>
    '''.format(q)
    for artist in db.collection.aggregate(pipeline):
        name = artist["_id"]
        votes = artist["rates"]
        if votes != 0:
            avg_points = artist["tota_rate"] / artist["rates"]
        else:
            avg_points = None
        
        text = f'{name} ({votes} votes'
        if votes > 0:
            text += f', {avg_points} points'
        text += ')'

        content += '<li>' + text + '</li>'
    content += '''
            </ul>
            <form method="GET">
                <input type="submit" value="Back">
            </form>
        </bodY>
    </html>
    '''
    return content

def main():
    app.debug = True
    app.run(host='127.0.0.1', port='8081')

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')