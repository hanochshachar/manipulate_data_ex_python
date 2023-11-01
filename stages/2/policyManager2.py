import json
from stage2 import PolicyAPI2


api = PolicyAPI2()

forbidden = {
        "name": "forbidden",
        "description": "permission required",
        "type": "Frisco"
    }
api.create_policy(json.dumps(forbidden))

    
OK = {
        "name": "OK",
        "description": "work fine",
        "type": "Arupa"
    }
api.create_policy(json.dumps(OK))

"""
OK2 = {
        "name": "OK",
        "description": "work fine",
        "type": "Frisco2"
    }
api.update_policy(json.dumps(OK2))

"""

new_policy_data = {
    "name": "Ok",
    "description": "updated description successfully",
    "type": "Frisco"
}
update =  api.update_policy_by_name("forbidden", json.dumps(new_policy_data))


specific_policy = api.read_policy("OK")

#delete = api.delete_policy("OK")
print(update)