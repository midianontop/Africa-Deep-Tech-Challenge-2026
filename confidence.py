def get_confidence(severity):

    if severity == "Critical":
        return "95%"

    elif severity == "High":
        return "90%"

    elif severity == "Medium":
        return "80%"

    else:
        return "70%"