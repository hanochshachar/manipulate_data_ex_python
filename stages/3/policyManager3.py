import json
from stage3 import PolicyAPI3

api = PolicyAPI3()

forbidden = {
        "name": "forbidden4",
        "description": "permission required",
        "type": "Frisco"
    }
api.create_policy(json.dumps(forbidden))

forbidden2 = {
        "name": "forbidden4",
        "description": "permission required",
        "type": "Arupa"
    }
api.create_policy(json.dumps(forbidden2))
    
OK = {
        "name": "OK2",
        "description": "work fine",
        "type": "Arupa"
    }
api.create_policy(json.dumps(OK))








list1 = api.list_policies()
print(list1)

Fr_rule1 = {
    "name": "Rule1",
    "ip_proto": 6,        
    "source_port": 80,    
    "source_subnet": "192.168.1.0/24"
    }

api.create_rule("forbidden4", Fr_rule1)

Ar_rule1 = {
    "name":"rule2",
    "ip_proto": 6,
    "source_port":8080,
    "source_ip":"192.168.1.0",
    "destination_ip":"192.168.1.8"

}

api.create_rule("Frisco", Ar_rule1)

list1 = api.list_rules("destination_ip")
print(list1)

