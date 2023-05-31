from graphviz import Digraph

dot = Digraph('GPT_MVP_Workflow')
dot.attr(rankdir='TB', size='20,20', ratio='compress', fontsize='20', fontname='Open Sans')

# Nodes with different shapes and colors
dot.node('0', 'Start', shape='circle', style='filled', fillcolor='white', borderRadius='3')
dot.node('A', 'Plan Idea', shape='ellipse', style='filled', fillcolor='lightblue')
dot.node('B', 'Prioritize Goals\n(using a sophisticated system)', shape='box', style='filled', fillcolor='lightgreen')
dot.node('D', 'Prioritize Tasks\n(using a sophisticated system)', shape='box', style='filled', fillcolor='lightgreen')
dot.node('C', 'Identify Dependencies\n& Blockers', shape='box', style='filled', fillcolor='lightgreen')
dot.node('C1', 'Resolve Dependencies\n& Blockers', shape='box', style='filled', fillcolor='pink', fontsize='18')
dot.node('E', 'Delegate &\nAssign Tasks to GPTs', shape='parallelogram', style='filled', fillcolor='yellow')
dot.node('F', 'Create &\nPrioritize Sub-Tasks', shape='box', style='filled', fillcolor='lightgreen')
dot.node('G', 'Delegate &\nAssign Sub-Tasks to GPTs', shape='parallelogram', style='filled', fillcolor='yellow')
dot.node('H', 'Execute Sub-Task', shape='diamond', style='filled', fillcolor='orange')
dot.node('I', 'Check and\nTest for Success', shape='diamond', style='filled', fillcolor='orange')
dot.node('J', 'Is Sub-Task Successful?', shape='diamond', style='filled', fillcolor='orange')
dot.node('K', 'Proceed to Next Sub-Task', shape='circle', style='filled', fillcolor='gray')
dot.node('L', 'Reattempt/Adjust Sub-Task', shape='circle', style='filled', fillcolor='gray')
dot.node('M', 'Are All Sub-Tasks Completed?', shape='diamond', style='filled', fillcolor='orange')
dot.node('N', 'Proceed to Next Task', shape='circle', style='filled', fillcolor='gray')
dot.node('O', 'Update Goal Progress', shape='parallelogram', style='filled', fillcolor='yellow')
dot.node('P', 'Are All Goals Achieved?', shape='diamond', style='filled', fillcolor='orange')
dot.node('PA', 'Monitor Performance\n& Adjust', shape='hexagon', style='filled', fillcolor='purple', fontsize='18')
dot.node('Q', 'Project Completed', shape='doublecircle', style='filled', fillcolor='lightblue')
dot.node('R', 'Periodic Review & Adjustments', shape='hexagon', style='filled', fillcolor='purple')
dot.node('S', 'Reevaluate & Adjust Goals/Tasks', shape='hexagon', style='filled', fillcolor='purple')
dot.node('T', 'Any Remaining Tasks?', shape='diamond', style='filled', fillcolor='lightblue')
dot.node('U', 'Identify & Resolve\nTask Blockers', shape='box', style='filled', fillcolor='pink', fontsize='18')
dot.node('V', 'Identify & Resolve\nSub-Task Blockers', shape='box', style='filled', fillcolor='pink', fontsize='18')
dot.node('W', 'Review &\nAdjust Tasks', shape='hexagon', style='filled', fillcolor='purple', fontsize='18')
dot.node('X', 'Review &\nAdjust Sub-Tasks', shape='hexagon', style='filled', fillcolor='purple', fontsize='18')
dot.node('Y', 'Instantiate New GPT\nInstances for Adjustments', shape='parallelogram', style='filled', fillcolor='yellow', fontsize='18')
dot.node('Z', 'End (Optional)', shape='circle', style='filled', fillcolor='white')

#
# Update edges with bold and dashed styles
dot.edge('0', 'A', style='bold')
dot.edges(['AB', 'BC', 'CD', 'DE', 'EF', 'FG', 'GH', 'HI'])
dot.edge('C', 'C1', style='dashed')
dot.edge('I', 'J', label='Yes', style='bold')
dot.edge('J', 'K', label='Yes', style='bold')
dot.edge('J', 'L', label='No', style='dashed')
dot.edge('K', 'M', style='dashed')
dot.edge('K', 'F', style='dashed')
dot.edge('L', 'M', style='dashed')
dot.edge('N', 'O', style='bold')
dot.edge('M', 'G', label='No', style='dashed')
dot.edge('M', 'N', label='No', style='dashed')
dot.edge('O', 'P', style='bold')
dot.edge('P', 'Q', label='Yes', style='bold')
dot.edge('P', 'S', label='No', style='dashed')
dot.edge('P', 'PA', label='No', style='dashed')
dot.edge('PA', 'S', style='dashed')
dot.edge('S', 'B', style='bold')
dot.edge('Q', 'R', label='Periodic Review', style='dashed')
dot.edge('R', 'S', label='Adjustments', style='dashed')
dot.edge('M', 'T', label='Yes', style='dashed')
dot.edge('T', 'A', label='No', style='dashed')
dot.edge('T', 'E', label='Yes', style='bold')
dot.edge('D', 'U', style='dashed')
dot.edge('U', 'E', style='dashed')
dot.edge('F', 'V', style='dashed')
dot.edge('V', 'G', style='dashed')
dot.edge('Q', 'Z', label='Stop', color='red', style='dashed')

# Add double edges for parallelism
dot.edge('E', 'F', style='invis')
dot.edge('F', 'G', style='invis')
dot.edge('G', 'H', style='invis')


# Add edges for review and adjust steps
dot.edge('E', 'W')
dot.edge('W', 'U')
dot.edge('G', 'X')
dot.edge('X', 'V')

# Add edges for instantiating new GPT instances
dot.edge('W', 'Y')
dot.edge('Y', 'E')
dot.edge('X', 'Y')
dot.edge('Y', 'G')

# Add descriptions
dot.node('Parallel1', 'Goals can be\nexecuted in parallel', shape='note', fontsize='14', color='blue')
dot.edge('Parallel1', 'B', style='dashed', arrowhead='vee', color='blue')
dot.node('Parallel2', 'Sub-tasks can be\nexecuted in parallel', shape='note', fontsize='14', color='blue')
dot.edge('Parallel2', 'F', style='dashed', arrowhead='vee', color='blue')

# Planning cluster
with dot.subgraph(name='cluster_planning') as c:
    c.attr(label='Planning', fontsize='24', color='blue', style='filled,rounded', fillcolor='azure')
    c.node('A', 'Plan Idea', shape='ellipse', style='filled,rounded', fillcolor='lightblue')
    c.node('B', 'Prioritize Goals\n(using a sophisticated system)', shape='box', style='filled,rounded', fillcolor='lightgreen')
    c.edges(['AB'])

# Task management cluster
with dot.subgraph(name='cluster_task_management') as c:
    c.attr(label='Task Management', fontsize='24', color='blue', style='filled,rounded', fillcolor='azure')
    c.node('C', 'Identify Dependencies\n& Blockers', shape='box', style='filled,rounded', fillcolor='lightgreen')
    c.node('D', 'Prioritize Tasks\n(using a sophisticated system)', shape='box', style='filled,rounded', fillcolor='lightgreen')
    c.edges(['BC', 'CD'])

# Execution cluster
with dot.subgraph(name='cluster_execution') as c:
    c.attr(label='Execution', fontsize='24', color='blue', style='filled,rounded', fillcolor='azure')
    c.node('E', 'Delegate &\nAssign Tasks to GPTs', shape='parallelogram', style='filled,rounded', fillcolor='yellow')
    c.node('F', 'Create &\nPrioritize Sub-Tasks', shape='box', style='filled,rounded', fillcolor='lightgreen')
    c.edges(['DE', 'EF'])

# Review cluster
with dot.subgraph(name='cluster_review') as c:
    c.attr(label='Review', fontsize='24', color='blue', style='filled,rounded', fillcolor='azure')
    c.node('R', 'Periodic Review & Adjustments', shape='hexagon', style='filled,rounded', fillcolor='purple')
    c.edges(['QR'])



# Add edges for review and adjust steps
dot.edge('E', 'W', style='dashed')
dot.edge('W', 'U', style='dashed')
dot.edge('G', 'X', style='dashed')
dot.edge('X', 'V', style='dashed')

# Add edges for instantiating new GPT instances
dot.edge('W', 'Y', style='dashed')
dot.edge('Y', 'E', style='dashed')
dot.edge('X', 'Y', style='dashed')
dot.edge('Y', 'G', style='dashed')



dot.render('gpt_mvp_workflow', view=True, format='svg')