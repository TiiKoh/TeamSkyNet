import urllib3, simplejson, re

http = urllib3.PoolManager()


# Function to call Solr.
def searchSolr(searchTerm):
    searchTerm_raw = searchTerm
    searchTerm = ''.join(('"', searchTerm_raw.replace(' ', '%20'), '"'))

    # Contructs url query for title field using user's search term.
    urlTitle = "http://localhost:8983/solr/fiwiki/select?indent=on&q=title:" + searchTerm + "&wt=json"
    responseTitle =  http.request('GET', urlTitle)
    jsonTitle = simplejson.loads(responseTitle.data.decode('utf-8'))

    print("\n\nArticles with title " + '"' + searchTerm_raw + '".')
    print(jsonTitle['response']['numFound'], "documents found.")
    if jsonTitle['response']['numFound'] >= 10:
        print("\nShowing first 10 results:\n")

    # Print the id and title fields of each document for title search.
    for document in jsonTitle['response']['docs']:
        print("\tid = " + document['id'] + ":\n\t\t" + document['title'])

    # Contructs url query for text field using user's search term.
    urlText = "http://localhost:8983/solr/fiwiki/select?hl.fl=text&hl=on&q=text:" + searchTerm + "&wt=json"
    responseText =  http.request('GET', urlText)
    jsonText = simplejson.loads(responseText.data.decode('utf-8'))

    print("\n\nArticles with text containing " + '"' + searchTerm_raw + '".')
    print(jsonText['response']['numFound'], "documents found.")
    if jsonText['response']['numFound'] >= 10:
        print("\nShowing first 10 results:\n")

    idx = 0
    # Print the id and title fields of each document for text search.
    for textDocument, hlDocument in zip(jsonText['response']['docs'], jsonText['highlighting']):
        text_hl = jsonText['highlighting'][hlDocument]['text']
        idx = idx + 1
        seq = ("-----------------\n", "SEARCH RESULT #", str(idx), ":")
        print(''.join(seq))
        print("\n\tid = " + textDocument['id'] + ":\n\t\t" + textDocument['title'])
        # If id fields in plain documents and highlighted documents match,
        # run highlighted document through cleaning.
        if hlDocument == textDocument['id']:
            cleanHighlighting(text_hl)


# Clean text snippets from redundant clutter and print output.
def cleanHighlighting(text):
    text = ''.join(text)
    text = text.replace('\n\n', '\n')
    text = text.replace('\n', '\n>>> ')
    text = text.replace("'''", "'")
    text = text.replace("''", "'")

    text = re.sub(r'\[\[\w*\ *\w*\||\|\w*|\<ref name=\w*', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\[\[|\]\]|\{\{|\}\}|\<br|\/>|\<em>|\</em>', '', text, flags=re.IGNORECASE)

    print("\n>>> "+ text, "\n")


def main():
    searchTerm = searchSolr(input("Give me a search term: "))
    while True:
        prompt = input("\nWould you like to search again? If not, press enter to exit. ")
        if prompt != '':
            searchTerm = searchSolr(prompt)
        elif prompt == '':
            break

main()
