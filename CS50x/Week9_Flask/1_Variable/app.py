from flask import Flask, render_template, request

app = Flask(__name__)

# youtube.com/?name=David
@app.route('/')
def index():
    # name = request.args['name']
    name = request.args.get('name', 'world') # World is default
    return render_template('index.html', name=name)