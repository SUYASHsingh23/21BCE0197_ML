My name is Suyash Singh and my registeration number is 21BCE0197

AI Intern Task

Gist: You are required to build a document retrieval system for chat applications to use as context.

Problem Statement: You are required to build a backend for document retrieval. The goal of the task is
to generate context for LLMs to use for inference.

Document Retrieval System for Chat Applications
Overview
This project implements a document retrieval system designed to generate context for Large Language Models (LLMs) in chat applications. The backend is built using Python and Flask, with a focus on retrieving documents efficiently from a database, caching responses for faster results, and managing user requests to optimize performance. The system supports a real-time background scraper that fetches the latest news articles to continuously update the document database.

Key Features
Backend API:

The API is built with Flask, providing endpoints to retrieve documents and monitor the health of the system.
Endpoints:
/health: Returns a random response to check if the API is live.
/search: Accepts query parameters such as text (the search query), top_k (the number of results), and threshold (similarity score). It fetches the top matching documents based on these parameters.
Document Storage:

MongoDB is used as the database to store documents and user information.
Documents are encoded using the BERT model from the transformers library, ensuring high-quality embeddings for accurate search results.
Caching Layer:

Redis is used to cache search results, improving the performance of frequently made queries. The caching strategy is designed to enhance response times by storing document IDs and their similarity scores.
The reasoning for choosing Redis over other caching mechanisms is detailed in the documentation, emphasizing its speed and suitability for this project’s requirements.
User Management and Rate Limiting:

The system tracks the number of requests made by each user, recording user_id in the database. If a user makes more than 5 requests, they receive an HTTP 429 status code, indicating too many requests.
For each user request, the frequency of API calls is incremented, ensuring personalized rate-limiting functionality.
Real-Time Background Scraper:

A separate thread starts when the server is launched, continuously scraping news articles using BeautifulSoup and Scrapy.
The scraper automatically stores fresh articles in the MongoDB database, keeping the document pool up-to-date for accurate context generation.
Logging and Monitoring:

All API requests and responses are logged using Loguru, providing transparency and tracking of system behavior.
Prometheus is integrated to monitor API performance metrics, including inference time for each request, ensuring system health and scalability.
Dockerized Application:

The entire application is containerized using Docker for easy deployment. A Dockerfile and docker-compose.yml are included for running the application in isolated environments.
Docker ensures consistency across various deployment environments, simplifying the setup process.
Bonus: Re-Ranking and Fine-Tuning (Optional)

The project includes an optional re-ranking algorithm (BM25) that re-orders the search results to provide more accurate context for LLMs.
Fine-tuning scripts for retrievers are provided for future performance optimization and improvement of document retrieval quality.
How to Run
Clone the Repository:
bash
Copy code
git clone https://github.com/YourUsername/DocumentRetrievalSystem.git
Install Dependencies:
Copy code
pip install -r requirements.txt
Run the Application:
Copy code
python app.py
Using Docker:
css
Copy code
docker-compose up --build
Design Decisions
Why MongoDB?
MongoDB offers flexibility in storing unstructured documents, which suits this project’s requirement for news articles and text-based content.

Why Redis for Caching?
Redis was chosen for its in-memory data store capabilities, which allows for faster query results and real-time caching compared to alternatives like Memcached.

Why BERT for Encoding?
BERT’s pre-trained model ensures high-quality embeddings for natural language processing tasks, making it ideal for accurate document retrieval in this context.

API Endpoints
Method	    Endpoint	              Parameters	                                                    Description
GET	        /health	                 None	                                     Returns a response to confirm the API is active.
POST	      /search             	text, top_k, threshold,                             Returns a list of top matching documents based on query.
                                      user_id	
