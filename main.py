from langchain_ollama import ChatOllama
from mytools import get_user_Details


llm = ChatOllama(
    model="qwen2.5:1.5b",
).bind_tools([get_user_Details])

tool_map={
    "get_user_Details": get_user_Details
}

while True:
    query = input("user: ")

    if query.lower in  ['bye', 'exit']:
        exit()
    
    res = llm.invoke(query)

    if res.tool_calls:
            tool = res.tool_calls[0]
            tool_name = tool['name']
            tool_args= tool['args']
            print(f"Calling {tool_name}")

            tool_res = tool_map[tool_name].invoke(tool_args)
            print(tool_res)
    else:
        print(res.content)
                    



