from os import path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image


text = " ".join(review for review in df.description)
print ("There are {} words in the combination of all review.".format(len(text)))