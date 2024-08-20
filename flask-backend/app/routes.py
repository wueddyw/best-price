from flask import Blueprint, request, jsonify
from app.scraper import scrape_amazon_selenium  # Import the function from scraper.py

main = Blueprint('main', __name__)

@main.route('/scrape', methods=['POST'])
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
