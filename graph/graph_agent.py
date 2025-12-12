from langgraph.graph import StateGraph, START, END, MessagesState

def llm(state: MessagesState):
    return {
        "messages": [
            {"role": "ai" ,"content": "Hello Abhi"}
        ]
    }


graph = StateGraph(MessagesState)

graph.add_node(llm)
graph.add_edge(START, "llm")
graph.add_edge("llm", END)

graph = graph.compile()

res = graph.invoke(
    {
        "messages": [
            {"role": "user", "content": "Hello"}
        ]
    }
)

print(res)