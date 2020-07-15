input = ""

def result(word, style):
    if style.upper() == "BOLD":
        return "<b>" + word + "/<b>"
    elif style.upper() == "UNDERLINE":
        return "<p><ins>" + word + "</ins></p>"
    elif style.upper() == "ITALICIZE":
        return "<i>" + word + "</i>"