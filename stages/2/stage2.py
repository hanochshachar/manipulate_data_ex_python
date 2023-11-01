import json

class PolicyAPI2:
    def __init__(self):
        self.policies = {}  
        

    def create_policy(self, json_input):
        policy_data = json.loads(json_input)

        policy_name = policy_data.get("name")
        policy_type = policy_data.get("type")
        
        if policy_type not in ["Frisco", "Arupa"]:
                raise ValueError("Invalid policy type. Must be 'Frisco' or 'Arupa'")

        if policy_name in self.policies and any(policy['type'] == "Arupa" for policy in self.policies[policy_name]) and policy_type == "Arupa":
            raise ValueError("A Arupa policy with the same name and type already exists")

        if policy_name not in self.policies:
            self.policies[policy_name] = []

        self.policies[policy_name].append(policy_data)

        return json.dumps({"name": policy_name})
    
    def update_policy_by_name(self, policy_name, json_input):
        if policy_name not in self.policies:
            return json.dumps({"error": "Policy not found"})

        policy_data = json.loads(json_input)
        policy_type = policy_data.get("type")

        if policy_type not in ["Frisco", "Arupa"]:
            raise ValueError("Invalid policy type. Must be 'Frisco' or 'Arupa'")

        if policy_type == "Arupa":
            for name, policies in self.policies.items():
                for i, policy in enumerate(policies):
                    if policy.get("name") == policy_name:
                        policies[i] = policy_data
            return json.dumps(policies[i])
        else:
            self.policies[policy_name] = [policy_data]
            return json.dumps(self.policies)


    def read_policy(self, policy_name):
        if policy_name in self.policies:
            return json.dumps(self.policies[policy_name])
        else:
            return json.dumps({"error": "Policy not found"})


    

    def delete_policy(self, json_identifier):
            del self.policies[json_identifier]
            policies = list(self.policies.values())
            return json.dumps(policies)
        
    def list_policies(self):

        policy_list = list(self.policies.values())
        return json.dumps(policy_list)
        
