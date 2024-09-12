def check_symbols(source_code):
    stack = []
    i = 0
    n = len(source_code)
    
    matching_symbols = {
        '(': ')',
        '{': '}',
        '[': ']',
        '/*': '*/'
    }
    opening_symbols = set(matching_symbols.keys())
    closing_symbols = set(matching_symbols.values())
    
    while i < n:
        if source_code[i:i+2] == '/*':
            symbol = '/*'
            i += 2
        elif source_code[i:i+2] == '*/':
            symbol = '*/'
            i += 2
        else:
            symbol = source_code[i]
            i += 1
        
        if symbol in opening_symbols:
            stack.append(symbol)
        elif symbol in closing_symbols:
            if not stack:
                return "NO\n?-{}".format(symbol)
            top = stack.pop()
            if matching_symbols.get(top) != symbol:
                return "NO\n{}-?".format(top)
    
    if stack:
        return "NO\n{}-?".format(stack[-1])
    
    return "YES"

def read_input():
    import sys
    input = sys.stdin.read()
    source_code = []
    for line in input.splitlines():
        if line.strip() == '.':
            break
        source_code.append(line)
    return '\n'.join(source_code)

def main():
    source_code = read_input()
    result = check_symbols(source_code)
    print(result)

if __name__ == "__main__":
    main()
