from flask import Flask, request, render_template
from flask_cors import cross_origin

import get_allMan

app = Flask(__name__)




@app.route('/get_page_home_items/<int:id>')
@cross_origin()
def get_page_home_items(id):
    data = get_allMan.get_page_home_items(id)
    return data

@app.route('/get_page_category/<string:catey>/page/<int:id>')
@cross_origin()
def get_page_category(catey , id):
    data = get_allMan.get_page_category_items(catey,id)
    return data

@app.route("/get_page_single_item/<string:name>")
@cross_origin()
def get_page_single_item(name):
    data = get_allMan.get_page_single_item(name)
    return data

@app.route("/get_page_single_chapter/<string:name>/<string:chapter>")
@cross_origin()
def get_page_single_chapter(name,chapter):
    data = get_allMan.get_page_single_chapter(name,chapter)
    # data = {"name" : name ,"chapter" : chapter}
    return data


@app.route("/api")
@cross_origin()
def api():
    value = get_allMan.p()
    return {"id": ["nn" , "ddd" , "ddd", value] }

if __name__ == '__main__':
    app.run(debug=True)
