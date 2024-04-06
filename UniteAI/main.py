from flask import Flask, jsonify, request, render_template, send_file
from UniteIA_scraper import fetch_ai_news_selenium, get_article_text
from io import BytesIO
import base64
from wordcloud import WordCloud

app = Flask(__name__)

articles_data=None

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/get_data', methods=['GET'])
def get_data():
    global articles_data
    articles_data = fetch_ai_news_selenium()
    return render_template('data_loaded.html')


@app.route('/articles', methods=['GET'])
def articles():
    global articles_data
    if not articles_data:
        return render_template('articles.html', articles=None)
    else:
        articles_with_number = [{"number": i+1, **article} for i, article in enumerate(articles_data)]
        return render_template('articles.html', articles=articles_with_number)



@app.route('/article/<int:number>', methods=['GET'])
def article(number):
    global articles_data
    if not articles_data:
        return render_template('error.html', message="Les données n'ont pas été chargées, veuillez essayer /get_data pour les charger en premier.")
    else:
        if 1 <= number <= len(articles_data):
            return render_template('article_details.html', article=articles_data[number-1])
        else:
            return render_template('error.html', message="Numéro d'article hors de portée"), 404


def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    return wordcloud


@app.route('/ml', defaults={'number': None}, methods=['GET'])
@app.route('/ml/<int:number>', methods=['GET'])
def ml(number):
    global articles_data
    if not articles_data:
        return jsonify({"error": "The data has not been loaded, please try /get_data to load it first"})

    articles_with_clouds = []

    if number is None:
        # Générer des nuages de mots pour les 5 premiers articles
        for article in articles_data[:5]:
            article_text = get_article_text(article['link'])
            wordcloud = generate_wordcloud(article_text)
            image = wordcloud.to_image()
            img = BytesIO()
            image.save(img, 'PNG')
            img.seek(0)
            # Encoder l'image pour une utilisation dans le HTML
            encoded_img = base64.b64encode(img.getvalue()).decode('utf-8')
            articles_with_clouds.append({'title': article['title'], 'encoded_img': encoded_img})
    else:
        # Générer un nuage de mots pour un article spécifique
        if 1 <= number <= len(articles_data):
            article = articles_data[number-1]
            article_text = get_article_text(article['link'])
            wordcloud = generate_wordcloud(article_text)
            image = wordcloud.to_image()
            img = BytesIO()
            image.save(img, 'PNG')
            img.seek(0)
            encoded_img = base64.b64encode(img.getvalue()).decode('utf-8')
            articles_with_clouds.append({'title': article['title'], 'encoded_img': encoded_img})
        else:
            return render_template('error.html', message="Numéro d'article hors de portée"), 404

    return render_template('wordclouds.html', articles=articles_with_clouds)


app.run(debug=True)
