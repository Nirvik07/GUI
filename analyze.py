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
    tokens = nltk.sent_tokenize(pdf_text)
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
    charge_names = ["363","366","376","506","indian penal code", "ipc","498A","304B","34","509","366","354","509","109","crpc","156(3)","326b","342","363","366a","376(1)","370","370(a)(2)","370(1)"]

    # Compile a regular expression pattern to match any of the crime names
    pattern = re.compile("|".join(charge_names), re.IGNORECASE)

    # Iterate over each string in the input list and search for matches
    matches = ["none"]
    for string in strings:
        match = pattern.search(string)
        if match:
            matches.append(match.group(0))

        # Return the list of matches
    return matches


def extract_crime_names(strings):
    # A list of common crime names to search for
    crime_names = ["theft", "robbery", "assault", "murder", "fraud", "burglary", "kidnapping", "arson", "Criminal force", "Outrage of modesty", "Assault of woman","rape","dowry","dowry death","assault with criminal force","Cruelty","insulting the modesty","insult","acid attack","acid","attack","abduction","trafficking","minor","women trafficking"]

    # Compile a regular expression pattern to match any of the crime names
    pattern = re.compile("|".join(crime_names), re.IGNORECASE)

    # Iterate over each string in the input list and search for matches
    matches = ["none"]
    for string in strings:
        match = pattern.search(string)
        if match:
            matches.append(match.group(0))

        # Return the list of matches
    return matches

def assault_weapon(words):
    keywords = ['murder', 'weapon', 'bloodstain', 'DNA','blood', 'fingerprints','Witness']
    items=["none"]
    for keyword in keywords:
        for item in words:
            if re.search(r'\b{}\b'.format(keyword), item, flags=re.IGNORECASE):
                items.append(item)
    return items

def most_frequent(List):
    counter = 0
    num = List[0]
     
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
 
    return num

def unique(list):
    unique_list = []
    for x in list:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

def search_detaile(file_path,search):
    with open(file_path, 'rb') as f:
    # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(f)

    # Loop through each page in the PDF
        for page_num in range(len(pdf_reader.pages)):
        # Get the text content of the current page
            page_text = pdf_reader.pages[page_num].extract_text()

        # Search for the target string in the page text
            target_index = page_text.find(search)

        # If the target string is found, print it and the next string
            if target_index != -1:
            # Get the next string after the target string
                next_index = page_text.find('\n', target_index)
                next_str = page_text[target_index+len(search):next_index].strip()

            # Print the target string and next string
                return (search + ": " + next_str)