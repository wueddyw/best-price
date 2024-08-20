from flask import Flask, request, jsonify
from flask_cors import CORS
from config import Config
from scraper import scrape_amazon_selenium

app = Flask(__name__)
app.config.from_object(Config)  # Load configuration from config.py
CORS(app)  # This allows all domains, which is fine for development

@app.route('/scrape', methods=['POST'])
def scrape():
    data = request.get_json()
    url = data.get('url')
    
    if not url:
        return jsonify({'error': 'URL is required'}), 400
    
    try:
        result = scrape_amazon_selenium(url)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
