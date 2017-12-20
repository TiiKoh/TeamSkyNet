# TeamSkyNet

KIK-LG211 Building NLP Applications (2017)

# How to Use

Before running our program, [Solr](http://lucene.apache.org/solr/) needs to be properly installed and configured, and all data you plan to use must be indexed. Solr must be running and the correct core must be selected. Our program expects Solr to be running on port 8983, which is the default for Solr. 

Please note that our project is configured for Finnish Wikipedia articles.

Once this is done, run attempt.py in the console. Make sure you are in the same directory you saved our program to.

If on Windows:
```bash
py attempt.py
```

If on Unix/Linux:
```bash
python attempt.py
```
The program will prompt the user to give it a search term. It will return the number of documents found with the search term in the title and/or text, as well as the names and ids of the first 10 of these documents. It will also show a highlighted snippet for these documents.

The program will then prompt the user to enter another search term, or press 'enter' to quit.
