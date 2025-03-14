"Reverse a string"
def reverse(s):
    stack = []
    output = ""
    for i in s:
        stack.append(i)
    while stack:
        output += stack.pop()
    return output

print(reverse("Issac"))