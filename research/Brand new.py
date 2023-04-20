#!/usr/bin/env python
# coding: utf-8

# In[1]:


import PyPDF2
import nltk
pdf_file = open('D:/State_vs_Mr_Amit_Kumar_on_23_May_2013.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file)


# In[2]:


pdf_text = ''
for page in range(pdf_reader.getNumPages()):
    page_obj = pdf_reader.getPage(page)
    pdf_text += page_obj.extractText()


# In[3]:


print(pdf_text)


# In[4]:


tokens = nltk.word_tokenize(pdf_text)


# In[5]:


print(tokens)


# In[6]:


type(tokens)


# In[7]:


lowercase_words = [word.lower() for word in tokens]
print(lowercase_words)


# In[8]:


import nltk
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

# Remove stopwords
words = [word for word in lowercase_words if word not in stop_words]

print(words)


# In[9]:


from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
def stem_list(lst):
    stemmed_lst = []
    for word in lst:
        stemmed_word = stemmer.stem(word)
        stemmed_lst.append(stemmed_word)
    return stemmed_lst
#calling stemming function
stemmed_words = stem_list(words)
print(stemmed_words)


# In[10]:


import nltk
from nltk.stem import WordNetLemmatizer

# create an instance of the WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

# lemmatize each word in the list
lemmatized_words = [lemmatizer.lemmatize(word) for word in stemmed_words]

print(lemmatized_words)


# In[11]:


#removing punctuation
import string

# Create a string containing all punctuation characters
punctuation_chars = string.punctuation

# Use a list comprehension to filter out the punctuations
my_list_without_punctuations = [word for word in lemmatized_words if word not in punctuation_chars]

print(my_list_without_punctuations)


# In[12]:


import re

def extract_crime_names(strings):
    # A list of common crime names to search for
    crime_names = ["theft", "robbery", "assault", "murder", "fraud", "burglary", "kidnapping", "arson", "Criminal force", "Outrageof modesty", "Assault of woman","rape"]

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


# In[13]:


#calling function to extract crime names
crime_names = extract_crime_names(my_list_without_punctuations)
print(crime_names)


# In[14]:


import re

def extract_charges_names(strings):
    # A list of common crime names to search for
    crime_names = ["363","366","376","506","indian penal code", "ipc"]

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


# In[15]:


#calling function to extract crime names
crime_names = extract_charges_names(my_list_without_punctuations)
print(crime_names)


# In[18]:


#to get the FIR number
import PyPDF2

# Prompt the user for the target string and file name
target_str = input("Enter the target string: ")
file_name = input("Enter the file name: ")

# Open the PDF file in read binary mode
with open(file_name, 'rb') as f:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfFileReader(f)

    # Loop through each page in the PDF
    for page_num in range(pdf_reader.numPages):
        # Get the text content of the current page
        page_text = pdf_reader.getPage(page_num).extractText()

        # Search for the target string in the page text
        target_index = page_text.find(target_str)

        # If the target string is found, print it and the next string
        if target_index != -1:
            # Get the next string after the target string
            next_index = page_text.find('\n', target_index)
            next_str = page_text[target_index+len(target_str):next_index].strip()

            # Print the target string and next string
            print(target_str + ": " + next_str)


# In[19]:


#program to find any assault weapon
import re

# Search for keywords related to a murder
keywords = ['murder', 'weapon', 'bloodstain', 'DNA','blood', 'fingerprints','Witness']
for keyword in keywords:
    for item in my_list_without_punctuations:
        if re.search(r'\b{}\b'.format(keyword), item, flags=re.IGNORECASE):
            print('Found evidence related to {}:'.format(keyword))
            print(item)


# In[20]:


#program to find any assault weapon
import re

# Search for keywords related to a murder
keywords = ['Accused', 'Alleged', 'Apprehended', 'Arrested', 'Detained', 'Defendant', 'Embroiled', 'Implicated', 'Involved', 'Under investigation', 'Person of interest']
for keyword in keywords:
    for item in my_list_without_punctuations:
        if re.search(r'\b{}\b'.format(keyword), item, flags=re.IGNORECASE):
            print('Found evidence related to {}:'.format(keyword))
            print(item)


# In[21]:


#program to find the death type
import re

# Search for keywords related to a murder
keywords = ['suicide', 'murder']
for keyword in keywords:
    for item in my_list_without_punctuations:
        if re.search(r'\b{}\b'.format(keyword), item, flags=re.IGNORECASE):
            print('Death by {}:'.format(keyword))
            print(item)


# In[22]:


import nltk

# Function to extract criminal names from sentences
def extract_criminal_names(sentences):
    criminal_names = []
    for sentence in sentences:
        # Tokenize sentence into words
        words = nltk.word_tokenize(sentence)
        
        # Apply Part-of-Speech (POS) tagging to words
        pos_tags = nltk.pos_tag(words)
        
        # Extract proper nouns tagged as 'NNP' or 'NNPS'
        proper_nouns = [word for word, tag in pos_tags if tag in ['NNP', 'NNPS']]
        
        # Add proper nouns to criminal names list
        criminal_names += proper_nouns
    
    return criminal_names

# Call the function to extract criminal names
criminal_names = extract_criminal_names(my_list_without_punctuations)

# Print the extracted criminal names
print(criminal_names)


# In[23]:


import PyPDF2
import nltk
import re

# Load the PDF file
pdf_file = open('D:/State_vs_Mr_Amit_Kumar_on_23_May_2013.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

# Extract the text from the PDF file
text = ''
for page in range(pdf_reader.numPages):
    text += pdf_reader.getPage(page).extractText()

# Tokenize the text into sentences
sentences = nltk.sent_tokenize(text)

# Identify person names using named entity recognition (NER)
person_names = []
for sentence in sentences:
    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)
    entities = nltk.chunk.ne_chunk(tagged)
    for entity in entities:
        if hasattr(entity, 'label') and entity.label() == 'PERSON':
            person_names.append(' '.join(c[0] for c in entity.leaves()))

# Print the extracted person names
print('Person names found in the document:')
print(person_names)

# Print the relationships between the person names
print('\nRelationships between the person names:')
for i in range(len(person_names)):
    for j in range(i+1, len(person_names)):
        relation = nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(person_names[i] + ' is son of ' + person_names[j])))
        for entity in relation:
            if hasattr(entity, 'label') and entity.label() == 'PERSON':
                print(person_names[i] + ' is son of ' + person_names[j])

