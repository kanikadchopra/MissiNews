# MissiNews
A project for a future website to compare and analyse the Mississauga News with a focus on crime news. Scrapes Tweets from the @MissiNewsRoom twitter account, does a bag of words analysis so you can view the most common words for the month. For the crime analysis, it focuses on tweets mentioning the police, shootings, stabbings, assaults and robberies. 

## Future Plans:
<li> Use cosine_similarity to make sure tweets based on the same topic are not double counted </li>
<li> Analyse if crimes have been increasing in Mississauga over the 2018 to 2019 year </li>
<li> Categorize tweets and focus on crimes to see what crimes occur during each month, or different seasons using text classification </li>
<li> Collect location or general area data for each crime and plot it on an interactive geographic map </li>
<li> Eventually do this with other topics within the news and extend past crimes </li> 

## Steps to Run:
1. Install virtualenv: `pip install virtualenv`
2. Create your virtual environment: `virtualenv news`
3. Activate your virtual environment: `source news\bin\activate`
4. Install pip packages: `pip install -r requirements.txt`
5. Downloaded nltk data files: `python -m nltk.downloader all`
6. Download Spacy models: `python -m spacy download en_core_web_lg` and `python -m spacy download spacy download en_vectors_web_lg`
7. Create virtual environment kernal for jupyter notebook `ipython kernel install --user --name=MissiNews_Analysis`
8. Run jupyter notebook: `jupyter notebook`

## Files:

- **MissiNews.ipynd**: Mississauga News Analysis; Looks at the crime in January as a demo 
- **MissiNews_Visualizations.ipynd**: Visualizations for the year 2019 to compare crime in each month so far
- **nlp.py**: Helper functions for some of the NLP process using both nltk and spaCy
- **similarity.py**: Helper functions to check for cosine similiarity and jacard similarity with the sentences
