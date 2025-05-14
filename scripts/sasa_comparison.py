# load files
path_prot1=input("Enter the path to the first protein file: ")
path_prot2=input("Enter the path to the second protein file: ")
# Read the files
with open(f{path_prot1}, "r") as f1:
    sasa_full = f1.readlines()
with open(f{path_prot2}, "r") as f2:
    sasa_noini = f2.readlines()    

def combine(a, b):
    return a + b

def get_dict(file):
    d = {}
    for row in file:
        if not row.startswith("Residue"):
            l = row.split()
            d[combine(l[0], l[1])] = float(l[2])
    return d

dict_full = get_dict(sasa_full)
dict_noini = get_dict(sasa_noini)

def compare_dict(dict1, dict2):
    dict_diff = {}
    for key, value in dict1.items():
        if key in dict2:
            if value != dict2[key]:
                diff= dict2[key] - value
                dict_diff[key] = [value, dict2[key],f"{diff:.2f}"]
        else:
            print(f"{key} not found in second dictionary")
    return dict_diff

dict_diff = compare_dict(dict_full, dict_noini)
print(dict_diff)

# Write results including the difference
with open(r"X:\Projects\subtilisin\sasa_diff.txt", "w") as f:
    f.write("Residue SASA_with_inhibitor SASA_without_inhibitor Delta_SASA\n")
    for key, value in dict_diff.items():
        f.write(f"{key} {value[0]:.2f} {value[1]:.2f} {value[2]}\n")
