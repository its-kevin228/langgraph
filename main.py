from langgraph.graph import StateGraph, END

def start(state):
    print ('Starting...')
    return {'step':'etape1'}

def etape1(state):
    print ('Etape 1...')
    return {'step':'etape2'}

def etape2(state):
    print ('Etape 2...')
    return {'step':'etape3'}

def etape3(state):
    print ('Etape 3...')
    return END


workflow = StateGraph(dict)

workflow.add_node('start', start)
workflow.add_node('etape1', etape1)
workflow.add_node('etape2', etape2)
workflow.add_node('etape3', etape3)



