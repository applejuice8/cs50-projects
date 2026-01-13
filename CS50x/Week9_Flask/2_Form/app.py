from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# youtube.com/greet?name=David
@app.route('/greet', methods=['GET', 'POST'])
def greet():
    name = request.args.get('name')
    name = request.form.get('name') # For POST
    return render_template('index.html', name=name)