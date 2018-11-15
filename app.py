from flask import Flask, request
from flask import render_template
from database import get_all_cats, get_cat_by_id, create_cat, add_vote

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR-VERY-SECRET-SHHH'

@app.route('/')
def catbook_home():
    cats = get_all_cats()
    return render_template("home.html", cats=cats)
@app.route('/cats/<int:id>', methods=['GET', 'POST'])
def catbook_cat_info(id):
    if request.method == 'GET':
    	cat = get_cat_by_id(id)
    	return render_template("cat.html", cat=cat)
    else:
    	add_vote(id)
    	cat = get_cat_by_id(id)
    	return render_template("cat.html", cat=cat)
@app.route('/addcat', methods=['GET', 'POST'])
def addpage():
    if request.method == 'GET':
        return render_template("add.html")
    else:
        name = request.form['name']
        link = request.form['link']
        create_cat(name,0,link)
        cats = get_all_cats()
        return render_template('home.html',cats = cats)


if __name__ == '__main__':
   app.run(debug = True)
