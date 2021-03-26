def file(path:str, operation:str = 'r'):
    with open(path, operation) as f:
        return f.read()
