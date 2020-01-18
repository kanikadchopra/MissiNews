# News Category Classifier
Build a news category classifier using Huffpost News headlines and then apply transfer learning to use this model to categorize news-related tweets from MississaugaNews. 

The long-term goal would be to have a website that compares and analyzes the different news categories in Missisauga from tweets so you can see common topics or trends, for example increasing crime during certain months. 

## Completed
<li> Trained a news category classifier using Multinomial Naïve Bayes, SVM (Linear, Polynomial, Gaussian), Multinomial Logistic Regression, and Random Forest based on 60k Huffpost headlines
<li> Fine-tuned each model using a variety of parameters with GridSearchCV to achieve a maximum accuracy of 88% with Linear SVM
<li> Engineered features using word count vectors and TF-IDF for word frequency vectors
<li> Collecting and labelling categories for Mississauga News tweets to apply transfer learning to classify news-related tweets 
<li> Created a general visualization for crime related data 

## Steps to Run:
1. Install virtualenv: `pip install virtualenv`
2. Create your virtual environment: `virtualenv news`
3. Activate your virtual environment: `source news\bin\activate`
4. Install pip packages: `pip install -r requirements.txt`
5. Downloaded nltk data files: `python -m nltk.downloader all`
6. Create virtual environment kernal for jupyter notebook `ipython kernel install --user --name=MissiNews_Analysis`
7. Run jupyter notebook: `jupyter notebook`

## Model Training Files 
- **NewsHeadlines.ipynb:** Data preprocessing and training the following models to classify news categories - Multinomial Naive Bayes, Linear SVM, Polynomial SVM (degree = 2,3,4), Gaussian SVM, Logistic Regression, Random Forest
- **News_Category_Dataset_v2.json:** Dataset with 200K Huffpost article data 

## Tweet Analysis Files

- **MissiNews.ipynb**: Mississauga News Analysis; Looks at the crime in January as a demo 
- **MissiNews_Visualizations.ipynb**: Visualizations for the year 2019 to compare crime in each month so far
- **nlp.py**: Helper functions for some of the NLP process using both nltk and spaCy
- **similarity.py**: Helper functions to check for cosine similiarity and jacard similarity with the sentences
- **MissiNews_2019.png**: Snapshot of the Plot.ly Interactive Plot with the 2019 Analysis from MissiNews_Visualizations


## Future Plans
### SHORT TERM
<li> Try reducing features to reduce overfitting 
<li> Learn how to handle imbalanced datasets and see if this helps increase the accuracy 
<li> Collect and label more news-related tweets 
<li> Apply transfer learning to train the model on the news-related tweets 
<li> Use cosine_similarity to make sure tweets based on the same topic are not double counted </li>
### LONG TERM 
<li> Analyze crime trends over 2018 to 2020 on a monthly and seasonal basis </li>
<li> Create more interactive visualizations so user can choose a category and time span and see the news activity during that range
<li> Collect location or general area data for each crime and plot it on an interactive geographic map </li>
<li> Eventually do this with other cities as well </li> 
