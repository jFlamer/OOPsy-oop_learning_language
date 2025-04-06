def scanner(expr):
    tokens_dict = []
    position = 0
    while position < len(expression):
        char = expression[position]
        if char.isspace():
            position += 1
            continue
        elif char.isdigit():
            start = position
            while position < len(expression) and expression[position].isdigit():
                position += 1
            tokens_dict.append(("integer", expression[start:position]))
        elif char.isalpha():
            start = position
            while position < len(expression) and expression[position].isalnum():
                position += 1
            tokens_dict.append(("identifier", expression[start:position]))
        elif char in "+-*/()":
            token_map = {
                "+": "addition",
                "-": "subtraction",
                "*": "multiplication",
                "/": "division",
                "(": "left_parenthesis",
                ")": "right_parenthesis"
            }
            tokens_dict.append((token_map[char], char))
            position += 1
        else:
            error_position = position + 1
            print(f"Error! Unrecognized token '{char}' on position {error_position}")
            position += 1

    return tokens_dict


expression = "2+3*(76+8/3)+ 3*(9-3) &"
tokens = scanner(expression)
for token in tokens:
    print(token)