from langgraph.graph import StateGraph, END

def acceuil(state):
    print ('Welcome to the workflow')
    return {**state, 'acceuil':True}

def demander_nom(state):
    print ('quel est votre nonm?')
    return {**state, 'nom':input()}

def remerciements(state):
    print (f'Merci pour votre participation {state["nom"]}')
    return END


workflow = StateGraph(dict)

workflow.add_node('acceuil', acceuil)
workflow.add_node('demander_nom', demander_nom)
workflow.add_node('remerciements', remerciements)

workflow.set_entry_point('acceuil')

workflow.add_edge('acceuil', 'demander_nom')
workflow.add_edge('demander_nom', 'remerciements')
workflow.add_edge('remerciements', END)

graph = workflow.compile()

graph.invoke({})


