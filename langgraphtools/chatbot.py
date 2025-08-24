## tools
from langchain_community.tools import ArxivQueryRun,WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper,ArxivAPIWrapper

api_wrapper_arxiv = ArxivAPIWrapper(top_k_results=2,doc_content_chars_max=500)
arxiv=ArxivQueryRun(api_wrapper=api_wrapper_arxiv,description="Query arxiv papers")
print(arxiv.name)

api_wrapper_wiki = WikipediaAPIWrapper(top_k_results=1,doc_content_chars_max=500)
wiki=WikipediaQueryRun(api_wrapper=api_wrapper_wiki,description="Query Wikipedia")
print(wiki.name)

from dotenv import load_dotenv
load_dotenv()

import os

os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")
# os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

## Tavily search tool
from langchain_community.tools.tavily_search import TavilySearchResults

tavily = TavilySearchResults()

## combine all these tools in the list
tools = [arxiv, wiki, tavily]

## Initializse the LLM Model
from langchain_groq import ChatGroq

llm=ChatGroq(model="qwen-qwq-32b",api_key="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")
llm_with_tools=llm.bind_tools(tools=tools)

## State Schema
from typing_extensions import TypedDict
from langchain_core.messages import AnyMessage # human message or AI message
from typing import Annotated # labelling 
from langgraph.graph.message import add_messages # Reducers in Langgraph

class State(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages] # list of messages
    
## Entire Chatbot with Langgraph
from IPython.display import Image, display
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode
from langgraph.prebuilt import tools_condition

## Node Defenition
import re
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

def tool_calling_llm(state: State):
    messages = state["messages"]
    
    # Extract the name from the first human message
    user_name = None
    for msg in messages:
        if isinstance(msg, HumanMessage) and "my name is" in msg.content.lower():
            # Use regex to extract the name after "my name is"
            match = re.search(r"my name is (\w+)", msg.content.lower())
            if match:
                user_name = match.group(1).capitalize()
                break
    
    # Create a system prompt to instruct the LLM to use the user's name
    system_prompt = (
        f"You are a helpful assistant. If you know the user's name, address them by their name in your response. "
        f"The user's name is {user_name if user_name else 'unknown'}."
    )
    
    # Prepend the system prompt to the messages
    updated_messages = [SystemMessage(content=system_prompt)] + messages
    
    # Invoke the LLM with the updated messages
    response = llm_with_tools.invoke(updated_messages)
    return {"messages": [response]}

# Build graph
builder=StateGraph(State)
builder.add_node("tool_calling_llm",tool_calling_llm)
builder.add_node("tools",ToolNode(tools))

## Edges
builder.add_edge(START,"tool_calling_llm")
builder.add_conditional_edges(
    "tool_calling_llm",
    # If the latest message(result) from assistant is a tool call --> tools_conditon routes to tools
    # If the latest message(result) from assistant is not a tool call --> END
    tools_condition,
)
builder.add_edge("tools","tool_calling_llm")

graph=builder.compile() 

__all__ = ["graph", "HumanMessage", "AIMessage"]