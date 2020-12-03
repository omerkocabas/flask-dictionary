from flask import Flask, render_template, request, redirect

import requests, json, config

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/words', methods=['GET', 'POST'])
def words():
    if request.method == 'POST':
        input_word = request.form['title']


        return redirect('/words/'+input_word)
    else:
        return render_template('search.html')





@app.route('/words/<string:searched_word>', methods=['GET'])
def meaning(searched_word):
    http_link = "https://dictionary.yandex.net/api/v1/dicservice.json/lookup"
    parameters = {'key': config.api_key,
         'lang': 'en-tr', 'text': searched_word}

    api_response = requests.get(http_link, params=parameters)
    response_dictionary = api_response.json()

    if(api_response.status_code!=200):
        return "Invalid input"
    elif(api_response.status_code==200):
        if(len(response_dictionary["def"])==0):
            return "No such word exists."
        else:
            all_meanings = response_dictionary["def"][0]["tr"]
            length = len(all_meanings)
            return render_template('word.html', value=all_meanings, length = length)



if __name__ == "__main__":
    app.run(debug=True)

