# Book Information Search Engine
Implement Boolean Model on search engine to assist users in finding book titles through synopsis and authors using datasets from GoodReads web crawling results.

In general, if you want to find a book on the Google search engine, we search using the title as a keyword, but if we don't know the title, we will definitely search using a fragment of the story as a keyword. From that, a program will be created to search for books by title and synopsis using a boolean model from the web crawling results of the GoodReads site. Boolean Model is a logic used in searching by adding or using AND, OR, and NOT operators. GoodReads is a site that contains a catalog of books. Goodreads takes book information from the amazon.com site. 


Data retrieval is done by crawling on the GoodReads website to retrieve title, author, and synopsis data from a book. The successfully crawled data is then entered into the corpus in the form of a txt file. This data crawling is done using the beautifulSoup library. In addition, to view more book data, the GoodReads website requires users to login first. For that, using cookies and headers when logging in to the GoodReads web by changing cookies and headers to cURL, then changing cURL to python requests using curl.trillworks.com web.


web crawling -> preprocessing -> incident matrix -> query from user -> change query infix to postfix -> boolean model -> searching document -> search result.
