#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    defs = dir(hidden_4)
    for i in range(0, len(defs)):
        if defs[i][0] != '_' and defs[i][1] != '_':
            print(defs[i])
