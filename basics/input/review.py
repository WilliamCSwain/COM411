print("Enter an eye character")
eye = input()
print("Enter length of glasses")
length = int(input())

# Display of glasses

print(f"#####{' ' * length}#####")
print(f"# {eye} {'#' * (length + 2)} {eye} #")
print(f"#####{' ' * length}#####")