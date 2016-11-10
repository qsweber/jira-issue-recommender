# JIRA Issue Recommender

Examines the content of tickets and finds similar tickets. Adds a comment to tickets with links to related tickets.

## Installation

    pip3 install jira_issue_recommender

## Usage

    jira-issue-recommender \
        --jira-server-url 'https://jira.example.com/' \
        --username **** \
        --password **** \
        --finished-issues-query 'status = Done and timespent > 0' \
        --new-issues-query 'status = "To Do" and timeestimate is null' \
        --comment-preface 'Consider looking at:'

For each ticket returned by new-issues-query, a set of related tickets will be found amongst the tickets returned in finished-issues-query.

## Explanation

### Document representation with tf-idf

We must represent the ticket (document) in such a way that it is easily compared to other tickets (the corpus). To do this, we use tfidf, or "Term-frequency * Inverse Document Frequency".

#### term-frequency (tf)

For each document, we create a dictionary of word counts.

Let us start with this document:

    The dog and the cat live in the house.

The term-frequency representation of this document is:

    {'the': 3, 'dog': 1, 'and': 1, 'cat': 1, 'live': 1, 'in': 1, 'house': 1}


   
#### inverse document frequency (idf)

Imagine we have a collection of 1000 documents with a wide-range of topics and words. For each unique word, we generate a number which is equal to:

    log( # documents / ( 1 + # of documents with word ) )
    
So we might wind up with the following dictionary to represent the entire corups:

    {'the': ~0, 'dog': 4.5, 'and': ~0, 'cat': 5.6, 'live': 1.4, 'in': ~0, 'house': 4.1}
    
These values can be thought of as weights. Rare words ("dog", "house") receive a high weight while common words ("the", "in") receive a low weight.
    
#### tf * idf

For each document, we take the `tf` (dictionary of word counts for that document) and matrix-multiply by the `idf` (dictionary of word weights for the entire corpus).

This gives us one tf-idf vector for each document.

### Calculating distance between documents

The euclidian distance between documents can be found with the following psuedocode:

    # Assume we have a dictionary called tfidf which is
    # keyed on document index and contains the tfidf vector for each document.
    distances = []
    for index_outer in range(len(documents)):
        for index_inner in range(len(documents)):
            distance[(index_outer, index_inner)] = tfidf[index_outer] * tfidf[index_inner]

We take it one step further and use the cosine distance, which essentially just normalizes for document length.

## TODO

- Since each added comment on JIRA generates an email, we could require the user to respond to an input like "This will generate 34 emails. Confirm by typing '34': "
