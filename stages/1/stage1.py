import json

class PolicyAPI:
    def __init__(self):
        self.policies = {}  

    def create_policy(self, json_input):
       
        policy_data = json.loads(json_input)

        policy_name = policy_data.get("name")
        if policy_name in self.policies:
            raise ValueError("Policy with the same name already exists")

        self.policies[policy_name] = policy_data

        return json.dumps({"name": policy_name})

    def list_policies(self):

        policy_list = list(self.policies.values())
        return json.dumps(policy_list)
    
    
