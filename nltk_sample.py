# # import os
# # import nltk
# # from nltk.tokenize import sent_tokenize

# # # Ensure current dir nltk_data is added
# # #nltk.data.path.append(os.path.join(os.getcwd(), 'nltk_data'))

# # # Example corpus
# # corpus = "Your text here. Another sentence! One more?"

# # # Sentence tokenization
# # sentences = sent_tokenize(corpus)
# # print(sentences)

# import nltk
# nltk.download('wordnet')

# import nltk
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize

# # Download required resources
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('stopwords')

# text = "Shopify and Amazon both offer seller APIs for developers."
# words = word_tokenize(text)
# words = [word for word in words if word.lower() not in set(stopwords.words('english'))]
# pos_tag = nltk.pos_tag(words)

# print(pos_tag)

import nltk
nltk.download('averaged_perceptron_tagger_eng')