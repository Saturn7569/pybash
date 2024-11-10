def parse_command(cmd):
    tokens = []
    # print(cmd)

    current_token = ""
    for c in cmd:
        # print(c, current_token)
        if c in " \t\n" and current_token:
            tok = current_token
            if not tok:
                return None
            tokens.append(tok)
            current_token = ""
            continue
        current_token += c

    if current_token:
        tok = current_token
        if not tok:
            return None
        tokens.append(tok)

    return tokens


def format_token(tok):
    if not tok:
        return None
    if tok.isdigit():
        return int(tok)
    return tok
