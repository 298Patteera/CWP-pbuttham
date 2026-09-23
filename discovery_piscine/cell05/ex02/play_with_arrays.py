og_arr = [2, 8, 9, 48, 8, 22, -12, 2]
new_arr = []
for i in og_arr:
    if i > 5:
        i += 2
        new_arr.append(i)

print(f"{og_arr}\n{new_arr}")