from flask import Flask, request, render_template
from flask_cors import cross_origin

import get_allMan

app = Flask(__name__)


@app.route("/")
@cross_origin()
def home():
    return render_template("index.html", title="My Home Page")

@app.route('/get-page-home-items/<int:id>')
@cross_origin()
def get_page_home_items(id):
    data = get_allMan.get_page_home_items(id)
    return data

@app.route('/get-page-category/<string:catey>/page/<int:id>')
@cross_origin()
def get_page_category(catey , id):
    data = get_allMan.get_page_category_items(catey,id)
    return data

@app.route("/get-page-single-item/<string:name>")
@cross_origin()
def get_page_single_item(name):
    data = get_allMan.get_page_single_item(name)
    return data

@app.route("/get-page-single-chapter/<string:name>/<string:chapter>")
@cross_origin()
def get_page_single_chapter(name,chapter):
    data = get_allMan.get_page_single_chapter(name,chapter)
    # data = {"name" : name ,"chapter" : chapter}
    return data




if __name__ == '__main__':
    app.run(debug=True)
