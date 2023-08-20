def group_list(group, users):
    members = ', '.join(users)
    return f'{group}: {members}'

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # "Users:"
