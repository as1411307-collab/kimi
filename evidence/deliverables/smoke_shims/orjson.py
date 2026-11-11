import json as _json

def dumps(obj, *a, **k):
    return _json.dumps(obj, default=str).encode()

def loads(data, *a, **k):
    if isinstance(data, (bytes, bytearray)):
        data = data.decode()
    return _json.loads(data)

class JSONDecodeError(_json.JSONDecodeError):
    pass
