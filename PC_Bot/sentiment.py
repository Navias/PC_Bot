import numpy as np
import pandas as pd
import re
import string
import nltk
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import TweetTokenizer

from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
nltk.download('punkt')


warnings.filterwarnings("ignore")

data = pd.read_csv(r'C:\Users\jlore\Desktop\reddit_wsb.csv', encoding='utf8', header=None, skiprows=1, names=['title', 'timestamp'])
data.head()

title_data = data[['title', 'timestamp']].copy()

title_data = title_data.dropna()

# Lower-case all post
title_data.title = title_data.title.str.lower()

# Remove handlers
title_data.title = title_data.title.apply(lambda x: re.sub('@[^\s]+', '', x))

# Remove URLS
title_data.title = title_data.title.apply(lambda x: re.sub(r"http\S+", "", x))

# Remove all the special characters
title_data.title = title_data.title.apply(lambda x: ' '.join(re.findall(r'\w+', x)))

# remove all single characters
title_data.title = title_data.title.apply(lambda x: re.sub(r'\s+[a-zA-Z]\s+', '', x))

# Substituting multiple spaces with single space
title_data.title = title_data.title.apply(lambda x: re.sub(r'\s+', ' ', x, flags=re.I))

# Remove Time From Timestamp
title_data.timestamp = pd.to_datetime(title_data.timestamp).dt.date
