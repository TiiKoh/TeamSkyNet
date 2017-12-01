import urllib3, simplejson

http = urllib3.PoolManager()
# title:Banana
response =  http.request('GET','http://localhost:8983/solr/fiwiki/select?indent=on&q=title:Banana&wt=json')
print(response.status)
json = simplejson.loads(response.data.decode('utf-8'))
print(json['response']['numFound'], "documents found.")

# Print the fields of each document.
for document in json['response']['docs']:
    for doc_key in document:
        print(doc_key, "=", document[doc_key])
