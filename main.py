import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText().strip()


@app.route('/')
def home():
    fact = get_fact()
    fact_post = {'input_text':fact}

    req = requests.post('http://hidden-journey-62459.herokuapp.com/piglatinize/',
                        allow_redirects=False,
                        data=fact_post)
    
    pig_url = req.headers['Location']

    return "<a href='{}'>{}</a>".format(pig_url, pig_url)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

