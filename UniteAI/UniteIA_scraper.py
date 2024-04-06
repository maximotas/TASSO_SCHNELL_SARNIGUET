from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def fetch_ai_news_selenium():
    print("Fetching AI news with Selenium...")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    url = 'https://www.unite.ai/category/artificial-intelligence/'
    driver.get(url)

    try:
        # Attendez que les articles soient chargés
        articles = WebDriverWait(driver, 60).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'li.mvp-blog-story-wrap.left.relative.infinite-post'))
        )
        print(f"Nombre d'articles trouvés : {len(articles)}")

        articles_list = []
        for article in articles:
            try:
                title_element = article.find_element(By.CSS_SELECTOR, 'h2')
                link_element = article.find_element(By.CSS_SELECTOR, 'a')
                # Utilisation du sélecteur complet pour la date de publication
                date_element = article.find_element(By.CSS_SELECTOR, '.mvp-cd-date.left.relative')

                title = title_element.text if title_element else 'Titre non trouvé'
                link = link_element.get_attribute('href') if link_element else 'Lien non trouvé'
                publication_date = date_element.text if date_element else 'Date non trouvée'

                articles_list.append({'title': title, 'link': link, 'publication_date': publication_date})
            except Exception as e:
                print(f"An error occurred while processing an article: {e}")

        print("Done fetching news with Selenium.")
        return articles_list
    finally:
        # Assurez-vous de fermer le navigateur après avoir terminé
        driver.quit()


def get_article_text(article_url):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(article_url)

    try:
        content_elements = driver.find_elements(By.CSS_SELECTOR, '#mvp-content-body-top')
        article_text = ' '.join([element.text for element in content_elements if element.text.strip()])
    except Exception as e:
        print(f"Une erreur s'est produite lors de l'extraction du contenu de l'article : {e}")
        article_text = ""
    finally:
        driver.quit()

    return article_text


#print( get_article_text("https://www.unite.ai/google-faces-significant-challenges-and-competition-as-it-considers-charging-for-ai-search/"))
# if isinstance(news, list):
#     for article in news:
#         print(f"Title: {article['title']}")
#         print(f"Link: {article['link']}")
#         print(f"Publication Date: {article['publication_date']}\n")
# else:
#     print("Failed to fetch news.")
