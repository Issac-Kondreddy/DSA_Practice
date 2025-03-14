"""
Problem Statement
You are given a string containing just the characters '(', ')', '{', '}', '[', and ']'.
Your task is to determine if the input string's brackets are balanced in such a way
that every opening bracket has a corresponding and correctly placed closing bracket.
"""

def balanced_parentheses(s):
    stack = []
    matching_parentheses = {"(":")","{":"}","[":"]"}
    for i in s:
        if i == "{" or i == '[' or i == '(':
            stack.append(i)
        else:
            if len(stack)==0:
                print("String not balanced")
                return
            elif i != matching_parentheses[stack.pop()]:
                print("String not balanced")
                return
    if stack:
        print("String not balanced")
        return
    else:
        print("String balanced")

s1= "{[()]}"
s2 = "()"
s3 = "{{}}))"
print("S1", end = " ")
balanced_parentheses(s1)
print("s2", end =" ")
balanced_parentheses(s2)
print("s3", end= " ")
balanced_parentheses(s3)

