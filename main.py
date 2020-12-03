from os import path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image

df = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)

text = " ".join(review for review in df.description)
print ("There are {} words in the combination of all review.".format(len(text)))