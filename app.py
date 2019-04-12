from flask import Flask, render_template, request, jsonify, redirect, url_for
import os
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('home.html')

# on the home page, when put into search bar
@app.route("/search", methods=['GET','POST'])
def search():
    """API that takes in a specific url and assess its credibility
    Parameter: Url
    Returns:
        json object of credibility score and its breakdowns
    """
    searchUrl = request.args.get('websiteAddress')
    print(searchUrl)

    # data = get_json(searchTerm, resources, '30')
    data = searchUrl
    credibility = 70
    return render_template('search.html', data = data, credibility= credibility)



if __name__ == '__main__':
    app.run()
