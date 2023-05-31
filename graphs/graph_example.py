from graphviz import Digraph

dot = Digraph('LogicalDecisionFlow')

dot.node('A', 'Start')
dot.node('B', 'Is input valid?')
dot.node('C', 'Process input')
dot.node('D', 'Is output format correct?')
dot.node('E', 'Post-process output')
dot.node('F', 'Does output make sense?')
dot.node('G', 'Use output')
dot.node('H', 'Adjust input and retry')
dot.node('I', 'Adjust model parameters and retry')

dot.edges(['AB', 'BC', 'CD', 'DE', 'EF'])
dot.edge('F', 'G', label='Yes')
dot.edge('F', 'H', label='No')
dot.edge('D', 'I', label='No')

dot.render('logical_decision_flow.gv', view=True)
