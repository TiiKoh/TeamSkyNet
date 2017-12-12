import urllib3, simplejson


# If user query is more than one words, modify output for reading.
def fixQuery(searchTerm):

    char_list = list(searchTerm)    # Break characters in words to a list.
    char_list[0] = char_list[0].upper() # Capitalize the first letter in query.
    capitalizeNext = 0

    if str(" ") in char_list:  # Check if query has whitespaces.
        for idx, char in enumerate(char_list):

            if char == str(" "):
                char_list[idx] = "%20"  # Replace whitespaces with %20 (for url).
                capitalizeNext = 1
            else:
                capitalizeNext = 0

            if capitalizeNext:  # Capitalize the first letter after whitespace.
                idc = idx + 1
                char_list[idc] = char_list[idc].upper()

    searchTerm = ''.join(char_list)
    searchTerm = ''.join(('"', searchTerm, '"'))
    return(searchTerm)



http = urllib3.PoolManager()

# Run searchTerm through fixQuery. If query consists of several words,
# capitalize each individual word.
searchTerm_raw = input("Give me a search term: ")
searchTerm_output = ''.join(('"', searchTerm_raw, '"'))
searchTerm = fixQuery(searchTerm_raw)

#Contructs url query for title field using user's search term
urlTitle = "http://localhost:8983/solr/fiwiki/select?indent=on&q=title:" + searchTerm + "&wt=json"
responseTitle =  http.request('GET', urlTitle)
#print(responseTitle.status)
jsonTitle = simplejson.loads(responseTitle.data.decode('utf-8'))

print("Articles with title " + searchTerm_output)
print(jsonTitle['response']['numFound'], "documents found.")

# Print the id and title fields of each document for title search.
for document in jsonTitle['response']['docs']:
    print("\tid = " + document['id'] + ":\n\t\t" + document['title'])
    #for doc_key in document:
    #    print(doc_key, "=", document[doc_key])

# Contructs url query for text field using user's search term
urlText = "http://localhost:8983/solr/fiwiki/select?hl.fl=text&hl=on&q=text:" + searchTerm + "&wt=json"
responseText =  http.request('GET', urlText)
#print(responseText.status)
jsonText = simplejson.loads(responseText.data.decode('utf-8'))

print("Articles with text containing " + searchTerm_output)
print(jsonText['response']['numFound'], "documents found.")

# Print the id and title fields of each document for text search.
for document in jsonText['response']['docs']:
    print("\tid = " + document['id'] + ":\n\t\t" + document['title'])
    #for doc_key in document:
    #    print(doc_key, "=", document[doc_key])

# Print the highlighting stuff.
for document in jsonText['highlighting']:
    print(jsonText['highlighting'][document]['text'])