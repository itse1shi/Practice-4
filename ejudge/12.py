import json

def diff(A, B, path = "", difference = None):
    if difference is None:
        difference = []
    keys = set(A.keys()) | set(B.keys())
    for key in keys:
        full_key = f"{path}.{key}" if path else key
        a_val = A.get(key)
        b_val = B.get(key)
        a_str = json.dumps(a_val, separators=(",", ":"))
        b_str = json.dumps(b_val, separators=(",", ":"))
        if a_val == None:
            difference.append(f"{full_key} : <missing> -> {b_str}")
        elif b_val == None:
            difference.append(f"{full_key} : {a_str} -> <missing>")
        elif isinstance(a_val, dict) and isinstance(b_val, dict):
            diff(a_val, b_val, full_key, difference) 
        else:
            if a_val != b_val:
                difference.append(f"{full_key} : {a_str} -> {b_str}") 
    return difference

A = json.loads(input())
B = json.loads(input())

result = diff(A, B)
if not result:
    print("No differences")
else:
    for line in sorted(result):
        print(line)