from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.agents import Tool, create_react_agent, AgentExecutor
from langchain import hub
from tools.tools import get_profile_url


def lookup(name: str, company: str) -> str:
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    template = """given the full name {name_of_person} working at {company} I want you to get me the link to their profile page of 
    linkedin. Answer should contain only url"""

    tools_for_agent = [
        Tool(
            name="crawl google for profile page",
            func=get_profile_url,
            description="useful when you want to get "
            "the linkedin profile page "
            "details",
        )
    ]
    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)
    # agent = initialize_agent(
    #     tools=tools_for_agent, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
    # )
    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )
    profile_url = agent_executor.invoke(
        {"input": prompt_template.format_prompt(name_of_person=name, company=company)}
    )
    return profile_url
