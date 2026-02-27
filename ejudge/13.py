import json

def query(J, q):
    for _ in range(q):
        current = J
        que = input()
        que = que.replace("[", ".").replace("]", "")
        parts = [p for p in que.split(".") if p != ""]
        
        try:
            for part in parts:
                if isinstance(current, list):
                    current = current[int(part)]
                else:
                    current = current[part]
            print(json.dumps(current, separators=(",", ":")))
        except:
            print("NOT_FOUND")

J = json.loads(input())
q = int(input())
query(J, q)