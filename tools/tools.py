from langchain.serpapi import SerpAPIWrapper
from langchain_community.tools.tavily_search import TavilySearchResults


def get_profile_url(text: str) -> str:
    """searches for linkedin profile page"""
    search = TavilySearchResults()
    res = search.run(f"{text}")
    return res[0]["url"]
