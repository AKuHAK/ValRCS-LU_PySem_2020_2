def getFileName(prefix="apartments", postfix="xlsx", hasYear=False):
    now = datetime.datetime.now()
    if hasYear:
        return f"{prefix}_{now.year}_{now.month}_{now.hour}\
_{now.minute}_{now.second}.{postfix}"
    else:
        return f"{prefix}_{now.month}_{now.hour}\
_{now.minute}_{now.second}.{postfix}"
