AI Intern Task

Gist: You are required to build a document retrieval system for chat applications to use as context.
Problem Statement: You are required to build a backend for document retrieval. The goal of the task is
to generate context for LLMs to use for inference.

To run
1. Clone the Repository:

git clone https://github.com/YourUsername/DocumentRetrievalSystem.git

3. Install Dependencies:
   
pip install -r requirements.txt

5. Run the Application:
   
python app.py

7. Using Docker:
   
docker-compose up --build

API Endpoints
Method	    Endpoint	               Parameters	                                                     Description
GET	        /health	                   None	                                          Returns a response to confirm the API is active.
POST	      /search          	text, top_k, threshold,                                 Returns a list of top matching documents based on query.
                                      user_id	
