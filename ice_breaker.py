import os
from dotenv import load_dotenv
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.chat_models import google_palm
from langchain_google_genai import GoogleGenerativeAI
from grpc import insecure_channel
import os

from agents.lookup_agent import lookup
from third_parties.linkedin import scrape_profile

if __name__ == "__main__":
    load_dotenv()
    os.environ["REQUESTS_CA_BUNDLE"] = "/Users/srivatsav.gorti/Downloads/certs.pem"
    profile_url = lookup(name="chiranjeevi karthik phenom", company="Phenom")
    print(profile_url)
    summary_template = """
    given the linkedin information {information} about a person I want you to write up:
    1. brief summary
    2. interesting facts
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    # llm = GoogleGenerativeAI(model="gemini-pro", google_api_key="AIzaSyA8W04xbp4aR8xq1Z3DNWfnn3qhDW0HvOA")
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data = scrape_profile(profile_url=profile_url)
    res = chain.invoke(input={"information": linkedin_data})

    print(res.get("text"))
