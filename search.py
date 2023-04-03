# import necessary libraries
import requests
import pandas as pd
import numpy as np
import ast

def edenai_embeddings(text : str, provider: str):
  """
  This function sends a request to the Eden AI API to generate embeddings for a given text using a specified provider.
  """
  url = "https://api.edenai.run/v2/text/embeddings"
  headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Bearer <YOUR_API_KEY>"
  }
  payload = {
      "response_as_dict": True,
      "attributes_as_list": False,
      "show_original_response": False,
      "texts": [text],
      "providers": provider
  }

  response = requests.post(url, json=payload, headers=headers).json()
  try: 
    return response[provider]['items'][0]['embedding']
  except:
    return None

def cosine_similarity(embedding1: list, embedding2: list):
    """
    Computes the cosine similarity between two vectors.
    """
    vect_product = np.dot(embedding1, embedding2)
    norm1 = np.linalg.norm(embedding1)
    norm2 = np.linalg.norm(embedding2)
    cosine_similarity = vect_product / (norm1 * norm2)
    return cosine_similarity

def search_subfeature(description: str):
    """
    This function searches a dataset of subfeature descriptions and returns a list of the subfeatures 
    with the highest cosine similarity to the input description.
    """
    # load the subfeatures dataset into a pandas dataframe
    subfeatures = pd.read_csv('subfeatures_dataset.csv')
    
    # generate an embedding for the input description using the OpenAI provider
    embed_description = edenai_embeddings(description, 'openai')
    
    results = []
    # iterate over each row in the subfeatures dataset
    for subfeature_index, subfeature_row in subfeatures.iterrows(): 
      similarity = cosine_similarity(
          ast.literal_eval(subfeature_row['Description Embeddings']),
          embed_description)
      
    # compute the cosine similarity between the query and all the rows in the corpus
      results.append({
          "score": similarity,
          "subfeature": subfeature_row['Name'],
          })
      
    results = sorted(results, key=lambda x: x['score'], reverse=True)
    return results[:5]