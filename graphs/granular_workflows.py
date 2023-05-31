from graphviz import Digraph

dot_goals = Digraph('Create_and_Prioritize_Goals')
dot_goals.attr(rankdir='TB', size='8,5', ratio='compress')

# Nodes
dot_goals.node('1', 'Identify Goals', shape='box', style='filled', fillcolor='lightgreen')
dot_goals.node('2', 'Determine Importance', shape='box', style='filled', fillcolor='lightgreen')
dot_goals.node('3', 'Set Deadlines', shape='box', style='filled', fillcolor='lightgreen')
dot_goals.node('4', 'Assess Dependencies', shape='box', style='filled', fillcolor='lightgreen')
dot_goals.node('5', 'Prioritize Goals', shape='box', style='filled', fillcolor='lightgreen')

# Edges
dot_goals.edges(['12', '23', '34', '45'])

dot_goals.render('./graphs/create_prioritize_goals', view=True, format='pdf')


# Create & Prioritize Tasks
dot_tasks = Digraph('Create_and_Prioritize_Tasks')
dot_tasks.attr(rankdir='TB', size='8,5', ratio='compress')

dot_tasks.node('1', 'Identify Tasks', shape='box', style='filled', fillcolor='lightgreen')
dot_tasks.node('2', 'Estimate Effort', shape='box', style='filled', fillcolor='lightgreen')
dot_tasks.node('3', 'Set Deadlines', shape='box', style='filled', fillcolor='lightgreen')
dot_tasks.node('4', 'Assess Dependencies', shape='box', style='filled', fillcolor='lightgreen')
dot_tasks.node('5', 'Prioritize Tasks', shape='box', style='filled', fillcolor='lightgreen')

dot_tasks.edges(['12', '23', '34', '45'])

dot_tasks.render('./graphs/create_prioritize_tasks', view=False, format='pdf')

# Delegate & Assign Tasks
dot_delegate_tasks = Digraph('Delegate_and_Assign_Tasks')
dot_delegate_tasks.attr(rankdir='TB', size='8,5', ratio='compress')

dot_delegate_tasks.node('1', 'Identify Team Members', shape='parallelogram', style='filled', fillcolor='yellow')
dot_delegate_tasks.node('2', 'Assess Skills & Availability', shape='parallelogram', style='filled', fillcolor='yellow')
dot_delegate_tasks.node('3', 'Assign Tasks', shape='parallelogram', style='filled', fillcolor='yellow')
dot_delegate_tasks.node('4', 'Communicate Expectations', shape='parallelogram', style='filled', fillcolor='yellow')

dot_delegate_tasks.edges(['12', '23', '34'])

dot_delegate_tasks.render('./graphs/delegate_assign_tasks', view=False, format='pdf')

# Create & Prioritize Sub-Tasks
dot_subtasks = Digraph('Create_and_Prioritize_SubTasks')
dot_subtasks.attr(rankdir='TB', size='8,5', ratio='compress')

dot_subtasks.node('1', 'Identify Sub-Tasks', shape='box', style='filled', fillcolor='lightgreen')
dot_subtasks.node('2', 'Estimate Effort', shape='box', style='filled', fillcolor='lightgreen')
dot_subtasks.node('3', 'Set Deadlines', shape='box', style='filled', fillcolor='lightgreen')
dot_subtasks.node('4', 'Assess Dependencies', shape='box', style='filled', fillcolor='lightgreen')
dot_subtasks.node('5', 'Prioritize Sub-Tasks', shape='box', style='filled', fillcolor='lightgreen')

dot_subtasks.edges(['12', '23', '34', '45'])

dot_subtasks.render('./graphs/create_prioritize_subtasks', view=False, format='pdf')

# Delegate & Assign Sub-Tasks
dot_delegate_subtasks = Digraph('Delegate_and_Assign_SubTasks')
dot_delegate_subtasks.attr(rankdir='TB', size='8,5', ratio='compress')

dot_delegate_subtasks.node('1', 'Identify Team Members', shape='parallelogram', style='filled', fillcolor='yellow')
dot_delegate_subtasks.node('2', 'Assess Skills & Availability', shape='parallelogram', style='filled', fillcolor='yellow')
dot_delegate_subtasks.node('3', 'Assign Sub-Tasks', shape='parallelogram', style='filled', fillcolor='yellow')
dot_delegate_subtasks.node('4', 'Communicate Expectations', shape='parallelogram', style='filled', fillcolor='yellow')

dot_delegate_subtasks.edges(['12', '23', '34'])

dot_delegate_subtasks.render('./graphs/delegate_assign_subtasks', view=False, format='pdf')

# Execute Sub-Task
dot_execute_subtask = Digraph('Execute_SubTask')
dot_execute_subtask.attr(rankdir='TB', size='8,5', ratio='compress')

dot_execute_subtask.node('1', 'Start Sub-Task', shape='diamond', style='filled', fillcolor='orange')
dot_execute_subtask.node('2', 'Perform Work', shape='diamond', style='filled', fillcolor='orange')
dot_execute_subtask.node('3', 'Monitor Progress', shape='diamond', style='filled', fillcolor='orange')
dot_execute_subtask.node('4', 'Adjust as Needed', shape='diamond', style='filled', fillcolor='orange')

dot_execute_subtask.edges(['12', '23', '34'])

dot_execute_subtask.render('./graphs/execute_subtask', view=False, format='pdf')

# Check and Test for Success
dot_check_success = Digraph('Check_and_Test_for_Success')
dot_check_success.attr(rankdir='TB', size='8,5', ratio='compress')

dot_check_success.node('1', 'Review Work', shape='diamond', style='filled', fillcolor='orange')
dot_check_success.node('2', 'Verify Outputs', shape='diamond', style='filled', fillcolor='orange')
dot_check_success.node('3', 'Test Functionality', shape='diamond', style='filled', fillcolor='orange')
dot_check_success.node('4', 'Revise as Needed', shape='diamond', style='filled', fillcolor='orange')

dot_check_success.edges(['12', '23', '34'])

dot_check_success.render('./graphs/check_test_success', view=False, format='pdf')
