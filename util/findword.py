def findword(word, root):
    for entry in root:
        readings = entry.findall('.//keb') + entry.findall('.//reb')
        readings = map(lambda x: x.text, readings)
        if word in readings:
            return entry
    return None
