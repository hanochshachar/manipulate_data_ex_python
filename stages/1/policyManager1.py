import json
from stage1 import PolicyAPI


api = PolicyAPI()

forbidden = {
        "name": "forbidden",
        "description": "permission required",
    }
api.create_policy(json.dumps(forbidden))

    
OK = {
        "name": "OK",
        "description": "work fine"
    }
api.create_policy(json.dumps(OK))

    
policies = api.list_policies()
print(policies)
