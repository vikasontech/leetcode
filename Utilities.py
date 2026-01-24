def printStringToArray(self, s: str):
    # Header row (indexes)
    header = "| " + " | ".join(str(i) for i in range(len(s))) + " |"

    # Character row
    chars = "| " + " | ".join(c for c in s) + " |"

    print(header)
    # print(separator)
    print(chars)

def printArray(self, s: list[int]):
    # Header row (indexes)
    header = "| " + " | ".join(str(i) for i in range(len(s))) + " |"

    # Character row
    chars = "| " + " | ".join(c for c in s) + " |"

    print(header)
    # print(separator)
    print(chars)
