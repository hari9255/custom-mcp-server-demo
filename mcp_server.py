from mcp.server.mcpserver import MCPServer
import os
import random
from langchain_tavily import TavilySearch

os.environ["TAVILY_API_KEY"] = "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"
mcp = MCPServer("MCP_Server")

@mcp.tool(description="use this tool to get latest or current information from web search")
def web_search_tool(query: str):
    '''
    use this tool to get latest or current information from web search

    '''
    print("web search tool is called")
    web_search = TavilySearch(max_results=3, topic="general")
    context = web_search.invoke(query)
    return context




@mcp.tool(description="use this tool to generate a random number")
def random_number_generator():
    '''
    use this tool to generate a random number

    '''
    print("random generator tool is called")
    return random.randint(300,400)


mcp.run(transport="streamable-http")
