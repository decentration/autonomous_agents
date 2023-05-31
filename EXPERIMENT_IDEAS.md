# Ideas to experiment 

Create workers and workflows. 

thereafter aim to automate those work flows

but until then just create fixed workflows and build from there. 




## Workflow with JSON response 

### Initial Validation 

- Tell GPT to respond with JSON schema provide 
- Have some parameters that the validation updates the JSON object with. `is_complete: boolean`, etc. 
- Check response contains complete or incomlpete spec (true or false)
- If incomplete change is_complete to false and provide the missing parameters in ask it to respond with the schema provided and include missing parameters.

Steps:

1. Create/update schema
2. create system message which includes schema 
3. write a parser that validates the response. 
4. Error handle for is_complete
5. Write logic for is_complete: false
6. The return logic should contain a prompt message including some variables which include any mising parameters. 


system message:

codingMessage = "You are a diligent programmer working for a tech company. You are given tasks and your job is to write code for the taks. You MUST write all your responses within a JSON object, this is the schema:

```
{JSONSCHEMA}
```

If you receive any further replies then you must make sure to continue to respond within the JSON schema.
"


