from flask import Flask, render_template, send_file, request
from scraper import Scraper

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/loading')
def loading():
    url = request.args.get('url').strip()
    return render_template('loading.html', url=url)

@app.route('/scrape', methods=['GET'])
def scrape():
    url = request.args.get('url')
    scraper = Scraper(headless=True)
    scraper.scrape_page(url)

    file_name = 'youtube.csv'
    scraper.export_to_csv(file_name=file_name)
    return render_template('results.html', data=scraper.data)

@app.route('/download')
def download_file():
    return send_file('youtube.csv', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)