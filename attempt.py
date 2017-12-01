import urllib3, simplejson

http = urllib3.PoolManager()

searchTerm = input("Give me a search term:")
print(searchTerm)

#Contructs url query for title field using user's search term
urlTitle = "http://localhost:8983/solr/fiwiki/select?indent=on&q=title:" + searchTerm + "&wt=json"
responseTitle =  http.request('GET', urlTitle)
#print(responseTitle.status)
jsonTitle = simplejson.loads(responseTitle.data.decode('utf-8'))

print("Articles with title " + searchTerm)
print(jsonTitle['response']['numFound'], "documents found.")

# Print the id and title fields of each document for title search.
for document in jsonTitle['response']['docs']:
    print("\tid = " + document['id'] + ":\n\t\t" + document['title'])
    #for doc_key in document:
    #    print(doc_key, "=", document[doc_key])

#Contructs url query for text field using user's search term
urlText = "http://localhost:8983/solr/fiwiki/select?indent=on&q=text:" + searchTerm + "&wt=json"
responseText =  http.request('GET', urlText)
#print(responseText.status)
jsonText = simplejson.loads(responseText.data.decode('utf-8'))

print("Articles with text containing " + searchTerm)
print(jsonText['response']['numFound'], "documents found.")

# Print the id and title fields of each document for text search.
for document in jsonText['response']['docs']:
    print("\tid = " + document['id'] + ":\n\t\t" + document['title'])
    #for doc_key in document:
    #    print(doc_key, "=", document[doc_key])