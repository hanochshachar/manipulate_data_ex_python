import json


class PolicyAPI3:
    def __init__(self):
        self.policies = {}  # Dictionary to store policies
        self.rules = {}  # Dictionary to store Arupa rules
        
        
    def create_policy(self, json_input):
        policy_data = json.loads(json_input)

        policy_name = policy_data.get("name")
        policy_type = policy_data.get("type")
        
        
        if policy_type not in ["Frisco", "Arupa"]:
                raise ValueError("Invalid policy type. Must be 'Frisco' or 'Arupa'")

        if policy_name in self.policies and any(policy['type'] == "Arupa" for policy in self.policies[policy_name]) and policy_type == "Arupa":
            raise ValueError("A Arupa policy with the same name and type already exists")
        #elif policy_name in self.policies and any(policy['type'] == "Frisco" for policy in self.policies[policy_name]) or policy_name in self.policies and policy_type == "Frisco":
            #raise ValueError("Frisco rule name must be unique globally within Frisco policies")
        
        #elif policy_type == "Frisco" and policy_name in self.policies:
            #raise ValueError("An policy with the same name already exists")
        
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
        
    def create_rule(self, json_policy_identifier, json_rule_input):
        policy_name = json_policy_identifier
        new_rule = json_rule_input
        new_rule_name = new_rule.get("name")
        
        FR_rule = [rule for rule in self.rules.values() if "source_subnet" in rule]
        AR_rule = [rule for rule in self.rules.values() if "destination_ip" in rule]
        
        
        if new_rule_name in self.rules and policy_name == "Frisco":
            raise ValueError("Frisco rule name must be unique globally within Frisco policies")
        for rule in FR_rule:
            if rule["name"] == new_rule_name:
                raise ValueError("Frisco rule name must be unique globally within Frisco policies")
        for rule in AR_rule:
            if rule["name"] == new_rule_name and policy_name == "Arupa":
                raise ValueError("A Arupa rule with the same name and type already exists ")
            
        if new_rule_name not in self.rules:
            self.rules[new_rule_name] = []
        self.rules[new_rule_name].append(new_rule)
        
        return json.dumps({"name": new_rule_name})
           
    def update_rule(self, json_identifier, json_rule_input) -> None:
        
        if json_identifier not in self.rules:
            return json.dumps({"error": "rule not found"})
        self.rules[json_identifier] = [json_rule_input]
        return json.dumps(self.rules)
    
    def read_rule(self, json_identifier: str) -> str:
        if json_identifier in self.rules:
            return json.dumps(self.rules[json_identifier])
        else:
            return json.dumps({"error": "Rule not found"})
        
    def delete_rule(self, json_identifier: str) -> None:
        if json_identifier in self.rules:
            del self.rules[json_identifier]
            return json.dumps(self.rules.values())
        else:
            return json.dumps({"error": "Rule not found"})
        
        
        
    
    def list_rules(self, json_policy_identifier: str) -> str:
        
        FR_rule = [rule for rule in self.rules.values() if json_policy_identifier not in rule]
        AR_rule = [rule for rule in self.rules.values() if json_policy_identifier in rule]
        
        
        
        return json.dumps(AR_rule) if json_policy_identifier == "destination_ip" else json.dumps(FR_rule)
