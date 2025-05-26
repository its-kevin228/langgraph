from langgraph.graph import StateGraph, END

def panier(state):
    print ('panier validé')
    return {**state, 'panier':True}

def verfication_paiement(state):
    if state['paiement'] == True:
        return {**state, 'confirmation':True}
   

def paiement(state):
    print ('paiement validé')
    return {**state, 'paiement':True}

def confirmation(state):
    print ('commande confirmée')
    return {**state, 'confirmation':True}


workflow = StateGraph(dict)

workflow.add_node('panier', panier)
workflow.add_node('verification_paiement', verfication_paiement)
workflow.add_node('paiement', paiement)
workflow.add_node('confirmation', confirmation)

workflow.set_entry_point('panier')

workflow.add_edge('panier', 'verification_paiement')
workflow.add_conditional_edges(
    'verification_paiement',
    lambda x: 'confirmation' if x.get('paiement', False) else 'paiement'
)
workflow.add_edge('paiement', 'confirmation')
workflow.add_edge('confirmation', END)

graph = workflow.compile()

graph.invoke({})


