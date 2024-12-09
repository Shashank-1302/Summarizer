from flask import Flask, request, jsonify
from utils.scraper import extract_article_content
from utils.summarizer import summarize_text
from utils.sentiment import analyze_sentiment
from flask_cors import CORS



app = Flask(__name__)
CORS(app)

@app.route('/summarize', methods=['POST'])
def summarize():
    if request.method == 'OPTIONS':
        response = make_response('', 200)
        response.headers["Access-Control-Allow-Origin"] = "http://localhost:3000"
        response.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type"
        return response
   
    try:
        data = request.json
        url = data.get('url')
        
        if not url:
            return jsonify({"error": "URL is required"}), 400
        
        content = extract_article_content(url)
        if "Error" in content:
            return jsonify({"error": content}), 500
        
        summary = summarize_text(content)
        
        sentiment = analyze_sentiment(content)
        
        return jsonify({
            "summary": summary,
            "sentiment": sentiment
        })
    
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
