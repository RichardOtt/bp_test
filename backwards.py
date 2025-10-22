def reverse_text(line):
    return ''.join(reversed(line))

print("What would you like reversed?")
text = input()

print(reverse_text(text))