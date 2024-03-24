# from fastapi import FastAPI, Request
# from fastapi.responses import JSONResponse
# import openai

# # app = FastAPI()

# from tavily import TavilyClient
# tavily = TavilyClient(api_key="Ytvly-EUYWedFGnY0dB6AjQ7OMQhEJsc4o2DyB")

# def get_toys():
#     # For basic search:
#     response = tavily.search(query="Should I invest in Apple in 2024?")
#     # For advanced search:
#     #response = tavily.search(query="Should I invest in Apple in 2024?", search_depth="advanced")
#     # Get the search results as context to pass an LLM:
#     #context = [{"url": obj["url"], "content": obj["content"]} for obj in response.results]
#     print ("response: ", response)

# from tavily import TavilyClient

# tavily = TavilyClient(api_key="Ytvly-EUYWedFGnY0dB6AjQ7OMQhEJsc4o2DyB")

# def get_toys():

#     response = tavily.search(query="Should I invest in Apple in 2024?")
#     print("response: ", response)

from tavily import TavilyClient
import json

tavily = TavilyClient(api_key="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")

def get_toys(prompt):

    response = tavily.search(query=prompt)
    response1 = json.dumps(response)
    response2 = json.loads(response1)
    print(response.keys())
    return response2['results'][0]['content']
    # print("Response:", response)

