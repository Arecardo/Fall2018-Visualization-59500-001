# Project2 -- Wordcloud
Group member: Xinrun Zhang, Yuzhou Yao and Nusrat Disha  
Instructor: Prof. Chen Bin

## This project includes:
1. trump_wordcloud.py: Main program which implements trump wordcloud.
2. Donalds-Tweets.csv: A collection of Donald Trump tweets in 2015-2016 from [kaggle](https://www.kaggle.com/kingburrito666/better-donald-trump-tweets)
3. trump-mask1.jpg: This image is used as mask 1.
4. trump-mask2.jpg: This image is used as mask 2.
5. Multidimensional Data Visualization.pdf: task file which is given by the professor.  
  
There are also two result images, *result_fromMask1.png, result_fromMask2.png*, to show what the ouptuts should looked like.  
A sample of alice wordcloud is given in folder *Alice_Sample*.

## How to run this project:
1. You should install python3.6 and some libraries in your computer.
2. The libraries which are used in this project include: numpy, pandas, matplotlib, os, PIL and wordcloud.
3. After installing, download files into your computer and put them at a same directory.
4. Run trump_wordcloud.py.
5. If you want to change mask, change the "trump-mask1.jpg" into "trump-mask2.jpg" in line 34:
```ruby
trump_mask = np.array(Image.open(path.join(d, "trump-mask1.jpg")))
```
6. The program will generates the result and outputs a 2222.png file into the directory.
7. The name of output file can also be changed.
8. Welcome any improvement of the program.

## Alice_Sample includes:
1. alice666.py: this is the python file which implements wordcloud.
2. alice-color.jpg: this file is used as mask image.
3. alice.txt: original data text.

## How to run Alice Sample:
Same as trump wordcloud project.
