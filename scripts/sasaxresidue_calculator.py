import freesasa
# load pdb file
file=input("which file do you want to analyze? ")
structure = freesasa.Structure(file)
# SASA calculation
result = freesasa.calc(structure)
# SASA calculation for each residue
residue_areas = result.residueAreas()
with open(f"sasa{file}.txt", "w") as f:
    f.write("Residue\tChain\tSASA\n")
    for chain, residues in residue_areas.items():
        for res_id, sasa in residues.items():
            f.write(f"{res_id}\t{chain}\t{sasa.total:.2f}\n")

# Stampa i risultati
for chain, residues in residue_areas.items():
    for res_id, sasa in residues.items():
        print(f"Chain {chain}, Residue {res_id}: Total SASA = {sasa.total:.2f} Å²")

