#convert DOM -> tree 
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def extract_text_from_dom(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    text = soup.get_text(separator='\n', strip=True)
    return text

# Example usage
if __name__ == "__main__":
    # Assume 'html_content' contains the HTML content of the website
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
    <title>Sample Page</title>
    </head>
    <body>
    <h1>This is a heading</h1>
    <p>This is a paragraph.</p>
    </body>
    </html>
    """

    text = extract_text_from_dom(html_content)
    sentence = "NLTK is a leading platform for building Python programs to work with human language data."

    tokens = word_tokenize(text)

    print(tokens)
