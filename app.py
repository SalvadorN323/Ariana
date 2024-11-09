from flask import Flask, render_template, request, jsonify
import os
import openai
from dotenv import load_dotenv

app = Flask(__name__)

# Set up the OpenAI API key
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route('/')
def home():
    return render_template('index.html')
 
@app.route('/gallery', methods=['GET'])
def gallery():
    # List of image file paths to display in the gallery
    images = [
        {'src': '/static/1D124B69-1D52-4552-8967-8E3392C6C41A.JPG', 'alt': 'Image 1'},
        {'src': '/static/1D760E52-9EAD-4A8A-9480-8F6D25A66BE7.JPG', 'alt': 'Image 2'},
        {'src': '/static/9E0211CE-A6D5-4BA3-8D5E-842EDBFD6CE3.JPG', 'alt': 'Image 3'},
        {'src': '/static/73633DC3-E2CB-4CCD-A560-DE79146F2155.JPG', 'alt': 'Image 4'},
        {'src': '/static/272198FE-BCBD-4D65-A973-12D5BBF0C921.jpg', 'alt': 'Image 5'},
        {'src': '/static/IMG_3307.JPG', 'alt': 'Image 6'},
        {'src': '/static/IMG_3335.jpg', 'alt': 'Image 7'},
        {'src': '/static/IMG_3348.jpg', 'alt': 'Image 8'},
        {'src': '/static/IMG_3357.JPG', 'alt': 'Image 9'},
        {'src': '/static/IMG_3359.jpg', 'alt': 'Image 10'},
        {'src': '/static/IMG_3358.JPG', 'alt': 'Image 11'},
        {'src': '/static/7C5CB58D-9CE8-4DB7-8461-F913979D7978.JPG', 'alt': 'Image 12'},
        {'src': '/static/38AE4975-525F-44AC-B27B-C27D54E85E59.JPG', 'alt': 'Image 13'},
        {'src': '/static/E78814E8-14B8-42D7-86CA-1D1490602F32.JPG', 'alt': 'Image 14'},
        {'src': '/static/IMG_3251.jpg', 'alt': 'Image 15'},
        {'src': '/static/IMG_3367.JPG', 'alt': 'Image 16'},
        {'src': '/static/742EFA65-D701-4D66-A30B-73ED32C266D5.JPG', 'alt': 'Image 17'}
        # Add more images as needed
    ]
    return render_template('poem.html', images=images)

@app.route('/create', methods=['GET'])
def create():
    return render_template('poem_gen.html')

@app.route('/generate_poem', methods=['POST'])
def generate_poem():
    theme = request.json.get('theme')
    if not theme:
        return jsonify({"error": "No theme provided"}), 400

    prompt = f"Write a poem based on the theme: '{theme}'"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # You can use "gpt-4" or "gpt-4-turbo" depending on your access
            messages=[{"role": "user", "content": prompt}]
        )
        poem = response['choices'][0]['message']['content'].strip()
        return jsonify({"poem": poem})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/improve_poem', methods=['POST'])
def improve_poem():
    existing_poem = request.json.get('poem')
    if not existing_poem:
        return jsonify({"error": "No poem provided"}), 400

    prompt = f"Here is a poem:\n\n{existing_poem}\n\nPlease suggest improvements to enhance its rhythm, imagery, and word choice."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # You can use "gpt-4" or "gpt-4-turbo" depending on your access
            messages=[{"role": "user", "content": prompt}]
        )
        improved_poem = response['choices'][0]['message']['content'].strip()
        return jsonify({"improved_poem": improved_poem})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(debug=False, host='0.0.0.0', port=port)
