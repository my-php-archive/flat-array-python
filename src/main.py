input = [1, [2, [3, [4, 5],[6,[7,[8, 9, 10, [11], [12], 13, 14, 15], 16], 17], 18, [19], 20], 21], 22, [23, [24, [25]]]]
flatList = []

def flat(element):
    if isinstance(element, list):
        for subelement in element:
            if isinstance(subelement, list):
                flat(subelement)
            else:
                flatList.append(subelement)
    else:
        flatList.append(element)


flat(input)

print("input", input)
print("flatten", flatList)
