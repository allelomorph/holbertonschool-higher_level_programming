#!/usr/bin/python3

def magic_string():
    # function objects can have attributes, here at global count of calls
    if hasattr(magic_string, 'calls'):
        magic_string.calls += 1
    else:
        magic_string.calls = 1

    return ', '.join(['Holberton'] * magic_string.calls)

# Original solution
#
# #!/usr/bin/python3
# def magic_string():
#     setattr(magic_string, 'rep', getattr(magic_string, 'rep', -1) + 1)
#     return 'Holberton' + ', Holberton' * getattr(magic_string, 'rep', 0)
