KEYWORDS = ["if", "else", "elif", "for", "while", "import", "function", "return"]
BOOLEANS = ["true", "false"]
OPERATORS = ["=", "!", "+", "-", "*", "/", "<", ">"]
BRACKETS = ["(", ")", "[", "]", "{", "}"]
TYPES = ["int", "string", "decimal", "true", "false"]

def is_letter(c):
    return c.isalpha() or c == "_"

def is_digit(c):
    return c.isdigit()

def is_letter_or_digit(c):
    return is_letter(c) or is_digit(c)

def color_lines(line):
    result=""
    l = len(line)
    i = 0
    while i < l:
        c = line[i]
        if c.isspace():
            result += c
            i += 1
            continue
        #number
        if is_digit(c):
            start_of_number = i
            while i < l and is_digit(line[i]):
                i += 1
            result += f'<span class="token-number">{line[start_of_number:i]}</span>'
            continue
        #string
        if c == '"':
            start_of_string = i
            i += 1
            while i < l and line[i] != '"':
                i += 1
            i += 1
            result += f'<span class="token-string">{line[start_of_string:i]}</span>'
            continue
        #identifiers, keywords, etc
        if is_letter(c):
            start_of_identifier = i
            while i < l and is_letter_or_digit(line[i]):
                i += 1
            text = line[start_of_identifier:i]
            if text in KEYWORDS:
                result += f'<span class="token-keyword">{text}</span>'
            elif text in BOOLEANS:
                result += f'<span class="token-boolean">{text}</span>'
            elif text in TYPES:
                result += f'<span class="token-type">{text}</span>'
            else:
                result += f'<span class="token-identifier">{text}</span>'
            continue


        if c in OPERATORS:
            i += 1
            result += f'<span class="token-operator">{c}</span>'
            continue

        if c in BRACKETS:
            i += 1
            result += f'<span class="token-bracket">{c}</span>'
            continue

        if c == "#":
            result += f'<span class="token-comment">{line[i:]}</span>'
            break

        if c == "[":
            start_of_array = i
            i += 1
            while i < l and (is_letter_or_digit(line[i]) or line[i] == " " or line[i] == ","):
                i += 1
            if i < l and line[i] == "]":
                result += f'<span class="token-array">{line[start_of_array:i+1]}</span>'
                continue

        if c == "=" and i > 0 and line[i - 1] == "]":
            result += f'<span class="token-operator">=</span>'
            i += 1
            continue

        result += c
        i += 1
    return result

def color_file(input_file, output_file):
    with open(input_file, "r") as f:
        lines = f.readlines()

    with open(output_file, "w") as f:
        f.write('<html><head><style>\n')
        f.write('.token-string { color: #E75480; }\n')
        f.write('.token-number { color: #550A35; }\n')
        f.write('.token-identifier { color: #872657; }\n')
        f.write('.token-keyword { color: #8B008B; }\n')
        f.write('.token-operator { color: #C25283; }\n')
        f.write('.token-bracket { color: #E38AAE; }\n')
        f.write('.token-type { color: #202071; }\n')
        f.write('.token-comment { color: #946fbc; }\n')
        f.write('.token-array { color: #190d5c; }\n')
        f.write('</style></head><body><pre>\n')

        for line in lines:
            f.write(color_lines(line))

        f.write('\n</pre></body></html>\n')


color_file("input_file.txt", "result.html")