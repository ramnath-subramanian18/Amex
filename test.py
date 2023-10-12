# Try nltk
text1 = "ZIPCAR TRIP JUN03 BOSTON MA"
text2 = "AMAZON.COM*KH4FH8VW3 AMZN"

import nltk

from nltk.tokenize import word_tokenize
nltk.download('punkt')  # Download the Punkt tokenizer data

tokenized_text1 = word_tokenize(text1)
tokenized_text2 = word_tokenize(text2)

print(tokenized_text1)
print(tokenized_text2)