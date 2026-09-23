def array_of_names(persons):
    name = []

    #loop through dictionary
    for f_name, l_name in persons.items():
        full_name = f_name.capitalize() + " " + l_name.capitalize()
        name.append(full_name)
    return name

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}

print(array_of_names(persons))