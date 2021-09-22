![VCU](media/VCU_logo.png "VCU")

## VCU Virtual Pharmacology Lab Worksheet. I. Single-Drug Dose-Effect Curves

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/VCU-SOM/VPLW/HEAD?filepath=VCU-VPLW.ipynb)

This module generates a simulated dose-effect curve for a single drug based on data you enter for the following variables:

- Doses (enter up to 10 doses)

- Drug Affinity for its target receptor (Kd)

- Drug Efficacy at its target receptor (E)

- Receptor number in the biological system (Rt)

- Transduction efficiency for receptor signaling in the biological system (f)   

- Threshold level of Receptor Activation required for effect detection in the assay (T)

- Capacity level of Receptor Activation that can be detected in the assay (C)

The simulated data in Experiment 1 can then be compared to simulated data under conditions with other drug variables (Kd, E), other biological-system variables (Rt, f), or other assay variables (C, T).  Data are generated, presented in tables, and graphed using the following formulas:

• RA(Dose) determines degree of Receptor Activation RA for a given dose A as RA=fRtE*(A/(A+Kd))

• Effect(C-T) determines gross effect as %MPE in assay given Threshold T and Ceiling C as Effect=((RA-T)/(C-T))*100

• Effect(Assay) sets all values ≤0 to 0 and all values ≥100 to 100

 ## VCU Virtual Pharmacology Lab Worksheet. II. Drug Interactions

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/VCU-SOM/VPLW/HEAD?filepath=VCU-VPLW-Phase2.ipynb)

This module generates simulated dose-effect curves resulting from the combination of two ligands here called Drug A and Drug B (either two different drugs, or a drug in combination with basal tone for an endogenous neurotransmitter).  You will enter the following variables

- Doses of Drug A (enter up to 10 doses)

- A single dose of Drug B

- Affinties of each drug for a common target receptor (KdA and KdB)

- Efficacies of each drug at its target receptor (EA and EB)

- Receptor number in the biological system (Rt)

- Transduction efficiency for receptor signaling in the biological system (f) 

- Threshold level of Receptor Activation required for effect detection in the assay (T)

- Capacity level of Receptor Activation that can be detected in the assay (C)

In general, Experiment 1 will show a Drug A dose-effect curve when the dose of Drug B=0.  These data can then be compared to simulated data from subsequent experiments that manipulate the dose of Drug B while all other variables stay constant.  Data are generated, presented in tables, and graphed using the following formulas:

• RA(Dose) determines degree of Receptor Activation RA for given doses A and B as RA=fRt * [(EA*(A/{A+KdA[B/(1+KdB)]}) + [(EB*(B/{B+KdB[A/(1+KdA)]}) 

• Effect(C-T) determines gross effect as %MPE in assay given Threshold T and Ceiling C as Effect=((RA-T)/(C-T))*100

• Effect(Assay) sets all values ≤0 to 0 and all values ≥100 to 100

## Contact

For project queries, please email:

sidney.negus@vcuhealth.org

For technical queries, please email:

james.percy@vcuhealth.org
