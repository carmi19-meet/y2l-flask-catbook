from flask import Flask, request
from flask import render_template
from database import get_all_cats, get_cat_by_id, create_cat

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR-VERY-SECRET-SHHH'

@app.route('/')
def catbook_home():
    cats = get_all_cats()
    return render_template("home.html", cats=cats)
@app.route('/cats/<int:id>')
def catbook_cat_info(id):
    cat = get_cat_by_id(id)
    return render_template("cat.html", cat=cat)
@app.route('/addcat', methods=['GET', 'POST'])
def addpage():
    if request.method == 'GET':
        return render_template("add.html")
    else:
        name = request.form['name']
        create_cat(name,0)
        cats = get_all_cats()        
        return render_template('home.html',cats = cats)


if __name__ == '__main__':
   app.run(debug = True)
