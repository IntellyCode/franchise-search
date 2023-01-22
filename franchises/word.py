from typing import Counter
import requests
from bs4 import BeautifulSoup
def word(x,y):

    # prepare a word counter
    word_count = Counter()
    franch = 0
    str1=y
    # lets get our web page (adjust to the url you want to review)
        
    base_url = x
    r = requests.get(base_url)

    # parse the webpage into an element hierarchy and store in soup 
    soup = BeautifulSoup(r.text, 'html.parser')
    
    # Get only the main text of the page as list of words
    all_words = soup.get_text(" ", strip=True).lower().split()
    #count words
    for word in all_words:
        cln_word = word.strip('.,?')
        # ignore words less 4 char long
        if len(cln_word) > 3:
            # ignore words in our custom stop list
            word_count[cln_word] += 1
        if str1 in cln_word:
            franch+=1
    # print 50 most common words
    
    return franch
  
