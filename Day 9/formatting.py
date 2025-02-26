message = """Hello, {name}! \n Thank you for stay with us."""

def format_message(name):
    msg = message.format(name=name)
    return msg