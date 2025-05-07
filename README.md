# In silico Mutagenesis and Stability Analysis of Subtilisin

## Abstract

In this project, I investigated how specific mutations could enhance the stability of the enzyme subtilisin using molecular dynamics (MD) simulations and in silico mutagenesis. I integrated GROMACS simulations with FoldX calculations to analyze protein flexibility (via RMSF), examine conserved functional sites, and predict the effect of mutations on protein stability through ΔΔG values.

---
## Project Goals

This project aims to identify stabilizing mutations in Subtilisin through molecular dynamics and in silico mutagenesis. In addition to improving the enzyme's intrinsic stability, a key focus is to explore mutations that may:
* Reduce the binding affinity of Eglin-C, a known serine protease inhibitor, without compromising enzymatic function.
* Preserve or enhance structural integrity, especially in surface-exposed, flexible loops identified via RMSF.
* Serve as a proof of concept for rational design of protease variants with lower inhibitor sensitivity, relevant in both industrial and biomedical contexts.


---

## Project Structure

```
/input/         → Original PDB files and mutation lists
/simulation/    → GROMACS input and output files (gro, xtc, tpr, mdp)
/foldx/         → All FoldX runs (RepairPDB, BuildModel, PositionScan)
/analysis/      → Scripts for plotting and extracting ddG, RMSD, and RMSF
/docs/          → Figures, diagrams, and reference materials
```

---

## Methods

### System Preparation

* Cleaned the initial PDB structure (removed water and ligands)
* Used AMBER99SB-ILDN force field
* Added water and neutralizing ions
* Defined simulation box for explicit solvation

### Energy Minimization & Equilibration

* Energy minimization using steepest descent
* Equilibration under NVT and NPT ensembles with position restraints
* Ran 10 ns production MD simulation

---

## Analysis

### RMSD and Radius of Gyration

* Used `gmx rms` and `gmx gyrate` to assess global structural changes
* No significant deviations observed → core structure remained stable

### RMSF Analysis

* Calculated Root Mean Square Fluctuation to assess flexibility per residue
* Identified most mobile residues
* Excluded residues in or near the active site from mutation screening

---

## FoldX Mutagenesis

### Mutation Strategy

1. Repaired structure with `RepairPDB`
2. Introduced point mutations using `BuildModel`
3. Conducted AlaScan on highly flexible regions
4. Performed PositionScan on targeted residues (e.g., ASP140)

### Example Stabilizing Mutations

| Residue | Mutation | ΔΔG (kcal/mol) | Comment                     |
| ------- | -------- | -------------- | --------------------------- |
| SER33   | ALA      | -1.37          | Strong stabilization effect |
| SER62   | ALA      | -0.86          | Located in an exposed loop  |
| SER144  | ALA      | -0.77          | On the protein surface      |

---

## ΔΔG Interpretation

* **ΔΔG < 0**: mutation is predicted to stabilize the protein
* **ΔΔG > 0**: mutation may destabilize the structure
* Only non-functional and non-binding site residues were considered (based on UniProt annotations and literature)

---

## Key Insights

* High RMSF alone is not a sufficient criterion for selecting mutation sites
* FoldX is sensitive to PDB formatting and chain identifiers
* ΔΔG values need to be interpreted considering protein structure and function

---

## Appendix

* Key GROMACS commands used
* Example FoldX usage:

```bash
foldx --command=BuildModel --pdb=prot.pdb --mutant-file=individual_list.txt
```

* Useful resources:

  * [FoldX Manual](http://foldxsuite.crg.eu/)
  * [Subtilisin UniProt Entry](https://www.uniprot.org/uniprotkb/P07518/entry)

---

## Visual Extras

* Include PyMOL or VMD snapshots showing RMSF-colored structures
* Overlay structural comparisons of wild-type and mutant forms

---

## About Me

I'm Marco, a Master's student in Industrial Biotechnology. My interests lie at the crossroads of protein engineering and computational biology. I'm currently looking for a PhD opportunity focused on structure-based protein design, mutagenesis, and machine learning applied to biochemical problems.

[LinkedIn](#) | [CV](#) | [Email](#)
