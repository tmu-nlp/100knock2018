from flask import Flask, render_template, request, request, redirect, url_for
import pymongo
import webbrowser



app = Flask(__name__)

def search_artist(txt, option):
    client = pymongo.MongoClient()
    db = client.MusicBrainz
    collection = db.artist

    results = []
    for each_artist in collection.find({option:txt}).sort('rating.count', -1).limit(30):
        result = []
        for key, value in sorted(each_artist.items()):
            result.append('[ {} ] : {}'.format(key, value))
        results.append(result)
    return results


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        search_txt = request.form['txt']
        search_option = request.form['option']
        results = search_artist(search_txt, search_option)
        if results == []:
            results = [['条件にマッチするアーティストが見つかりませんでした。やり直してください。']]
        return render_template('index.html', results=results)
    else:
        return redirect(url_for('index'))


if __name__ == "__main__":
    webbrowser.open('http://127.0.0.1:5000/', new=1, autoraise=True)
    app.run()
