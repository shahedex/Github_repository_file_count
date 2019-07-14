from flask import Flask, jsonify, render_template
from flask import request
import psycopg2
import requests
import time

app = Flask(__name__)
headers = {'token':'72987d96909fb524de3a646b0c882e4fc55f8c20'}

@app.route('/')
def runpy():
    print("Homepage Loading....")
    return render_template('index.html')

@app.route('/getfilecount')
def uploaddata():
    print("uploading data....")
    user_url = request.args.get('user_url')
    print(user_url)
    #user_url = 'https://github.com/blemasle/arduino-sim808/tree/master/src'
    repo_url = user_url[user_url.find('github.com') + 11:]
    username = repo_url[:repo_url.find('/')]
    rest_repo_name = repo_url[repo_url.find('/')+1:]
    repo_name = ''
    rest_url = ''
    if rest_repo_name.find('/') == -1:
        repo_name = rest_repo_name
    else:
        repo_name = rest_repo_name[:rest_repo_name.find('/')]
        rest_url = rest_repo_name[rest_repo_name.find('/')+1:]

    if rest_url != repo_name:
        rest_url = rest_url[11:]

    print(username)
    print(repo_name)
    print(rest_url)

    url = 'https://api.github.com/repos/' + username + '/' + repo_name + '/contents' + rest_url
    print(url)
    r = requests.get(url, headers=headers)
    file_count = len(r.json())
    print(file_count)
    return jsonify(file_count = file_count)

if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug=True)
