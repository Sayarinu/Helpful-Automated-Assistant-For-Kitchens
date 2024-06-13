import nltk
import json
from nltk.corpus import stopwords

def load_files() -> tuple:
    cuisines = {}
    with open("../text_files/cuisines.json", "r") as file:
        cuisines = json.loads(file.readline())
    file.close()
    search_terms = []
    with open("../text_files/search_words_query.txt", "r") as file:
        search_terms = [line.strip() for line in file]
    file.close()
    return cuisines, search_terms

def find_cuisine(plain_text, tagged_words: list, cuisines: list):
    cuisine = []
    
    for word in tagged_words:
        if ((word[1][0] == 'N' or word[1][0] == 'J') and (word[0] in cuisines)):
            cuisine.append(cuisines[word[0]])
    
    for key, value in cuisines.items():
        if key in plain_text and value not in cuisine:
            cuisine.append(value)

    #print(cuisine)
    return cuisine

def handle_text(text: str) -> dict:
    response = {}
    tokens = pre_process_text(text)
    tagged = make_lowercase(tag_text(tokens))
    response["categories"] = find_cuisine(text, tagged, cuisines) 
    response["search"] = define_request(tagged, search_terms)
    return response

def define_request(tagged_words: list, search_words: list) -> bool:
    count = 0
    for word in tagged_words:
        if ((word[1][0] == 'N' or word[1][0] == 'V' or word[1][0] == 'R') and (word[0] in search_words)):
            count += 1
    return count > 0

def pre_process_text(text: str):
    lemmatizer = nltk.WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))

    # Tokenize the text
    words = nltk.word_tokenize(text.lower())

    # Remove punctuation and stopwords, and lemmatize
    cleaned_words = [lemmatizer.lemmatize(word) for word in words if word.isalnum() and word not in stop_words]
    return cleaned_words

def tag_text(tokens: list):
    # N - Noun
    # I - Preposition
    # D - Determiner
    # J - Adjective
    # V - Verb
    # R - Adverb
    # CC tag - Coordinating conjunction
    # CD tag - Cardinal number
    tagged = nltk.pos_tag(tokens)
    return tagged

def make_lowercase(tagged_words: list):
    for word in tagged_words:
        word = (word[0].lower(), word[1])
    return tagged_words

def extract_locations(text):
    locations = []
    words = nltk.word_tokenize(text)
    tagged_words = nltk.pos_tag(words)
    named_entities = nltk.ne_chunk(tagged_words)
    
    for subtree in named_entities:
        if isinstance(subtree, nltk.Tree) and subtree.label() == 'GPE':
            # Join the words in the named entity to get the location as a string
            location = ' '.join([word for word, tag in subtree.leaves()])
            locations.append(location)
    
    return locations

cuisines = load_files()[0]
search_terms = load_files()[1]
