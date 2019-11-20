# MissiNews
A project for a future website to compare and analyse the Mississauga News with a focus on crime news. Scrapes Tweets from the @MissiNewsRoom twitter account, does a bag of words analysis so you can view the most common topics of the month; will try to separate crime tweets to focus on those. 

## Future Plans:
<li> Categorize tweets and focus on crimes to see what crimes occur during each month, or different seasons </li>
<li> Analyse if crimes have been increasing in Mississauga over the 2018 to 2019 year </li>
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
