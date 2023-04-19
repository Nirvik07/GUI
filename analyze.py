import PyPDF2
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
import string


def file_preprocese(file_path):
    pdf_file = open(file_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    pdf_text = ''
    for page in range(len(pdf_reader.pages)):
        page_obj = pdf_reader.pages[page]
        pdf_text += page_obj.extract_text()
    tokens = nltk.word_tokenize(pdf_text)
    lowercase_words = [word.lower() for word in tokens]
    stop_words = set(stopwords.words('english'))
    words = [word for word in lowercase_words if word not in stop_words]
    stemmed_words = stem_list(words)
    # create an instance of the WordNetLemmatizer
    lemmatizer = WordNetLemmatizer()
    # lemmatize each word in the list
    lemmatized_words = [lemmatizer.lemmatize(
        word) for word in stemmed_words]
    # Create a string containing all punctuation characters
    punctuation_chars = string.punctuation
    # Use a list comprehension to filter out the punctuations
    my_list_without_punctuations = [
        word for word in lemmatized_words if word not in punctuation_chars]
    return my_list_without_punctuations


def stem_list(lst):
    stemmed_lst = []
    for word in lst:
        stemmed_word = PorterStemmer().stem(word)
        stemmed_lst.append(stemmed_word)
    return stemmed_lst


def extract_charges_names(strings):
    # A list of common crime names to search for
    crime_names = ["363", "366", "376", "506",
                   "509", "indian penal code", "ipc"]

    # Compile a regular expression pattern to match any of the crime names
    pattern = re.compile("|".join(crime_names), re.IGNORECASE)

    # Iterate over each string in the input list and search for matches
    matches = []
    for string in strings:
        match = pattern.search(string)
        if match:
            matches.append(match.group(0))

        # Return the list of matches
    return matches


def extract_crime_names(strings):
    # A list of common crime names to search for
    crime_names = ["theft", "robbery", "assault", "murder", "fraud", "burglary", "kidnapping",
                   "arson", "Criminal force", "Outrageof modesty", "Assault of woman", "rape"]

    # Compile a regular expression pattern to match any of the crime names
    pattern = re.compile("|".join(crime_names), re.IGNORECASE)

    # Iterate over each string in the input list and search for matches
    matches = []
    for string in strings:
        match = pattern.search(string)
        if match:
            matches.append(match.group(0))

        # Return the list of matches
    return matches

def assault_weapon(words):
    keywords = ['murder', 'weapon', 'bloodstain', 'DNA','blood', 'fingerprints','Witness']
    for keyword in keywords:
        for item in words:
            if re.search(r'\b{}\b'.format(keyword), item, flags=re.IGNORECASE):
                return item