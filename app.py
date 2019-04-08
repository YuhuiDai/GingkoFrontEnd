from flask import Flask, render_template, request, jsonify, redirect, url_for
import os
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

# on the home page, when put into search bar
@app.route("/search", methods=['GET','POST'])
def search():
    """API that takes in searching a specific url
    Returns:
        json object of credibility score and its breakdown
    """
    # searchTerm = request.args.get('search')
    # # data = get_score(searchTerm, resources)
    # resources = ["BLOOMBERG", "CNN"]
    # data = get_score_multi(searchTerm, resources, '30')
    # return render_template('articles.html', data = data, level = 0)


if __name__ == '__main__':
    app.run()
