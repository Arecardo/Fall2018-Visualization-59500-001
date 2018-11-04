#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 13:41:02 2018

@author: zhangxinrun
"""

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import os
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator
from os import path


# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__)  if "__file__" in locals() else os.getcwd()

# Read data
data = pd.read_csv('Donald-Tweets.csv')
data.info()

# remove two last null values
data['Unnamed: 10'].replace(np.nan, '0', inplace=True)
data['Unnamed: 11'].replace(np.nan, '0', inplace=True)

# grab data from csv.tweet_text, the data type is string
wordcld = pd.Series(data['Tweet_Text'].tolist()).astype(str)

# Most frequent words in the data set. Using wordcloud
# mask
trump_mask = np.array(Image.open(path.join(d, "trump-mask1.jpg")))

# generate word cloud
cloud = WordCloud(width=900, height=900,
                  background_color="white",
                  max_words=2000,
                  stopwords=('https', 'https co', 'co'), 
                  mask=trump_mask,
                  random_state=42).generate(''.join(wordcld.astype(str)))

# create coloring from image
image_colors = ImageColorGenerator(trump_mask)

# show - this part is not neccessary
# because what we want is to output an image file
fig, axes = plt.subplots(1, 3)
axes[0].imshow(cloud, interpolation="bilinear")
# recolor wordcloud and show
# we could also give color_func=image_colors directly in the constructor
axes[1].imshow(cloud.recolor(color_func=image_colors), interpolation="bilinear")
axes[2].imshow(trump_mask, cmap=plt.cm.gray, interpolation="bilinear")
for ax in axes:
    ax.set_axis_off()
plt.show()

# output image to local file system
cloud.to_file("2222.png")