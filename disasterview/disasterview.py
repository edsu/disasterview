from flask import Flask
from flask import render_template
from pymongo import MongoClient

app = Flask(__name__)

def connect():
    client = MongoClient()
    db = client['disasters']
    return db
    
db = connect()    

@app.route('/')
def single_disaster():
    hurricane = db.hurricanes.find_one()
    title = hurricane['sourceResource']['title']
    thumb = hurricane['object']
    return render_template('index.html', title=title, thumb=thumb)
    
@app.route('/hurricanes/')
def browse(): 
    return 'Hurricane images will be here'

@app.route('/floods/')
def browse_images(): 
    return 'Flood images will be here'


if __name__ == '__main__':
    app.run(debug=True)
    