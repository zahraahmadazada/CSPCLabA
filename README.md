# CSPC - Computer Science for Physics and Chemistry
My coursework repository. Each practical is under PW<n>/Lab <X>/.
## Setup
Create the environment for a given lab:
conda env create -f PW<n>/Lab\ <X>/environment.yml
conda activate cspc
---
## PW1 - Lab A: Reproducible Foundations
4
Computer Science for Physics and Chemistry PW1 – Lab A
**What I built:**
- The comparison between speeds that were measured with different methods of radioactive decay simulation 
**Speed comparison (loop vs NumPy):**
- loop : 0.31101344899980177s
- numpy :0.00021564999951806385 s
- speed-up: 1222.1293420946554 x faster
**Tests:** all passing? (yes / no) yes
**Conclusion:**
- All tests passed successfully. The NumPy implementation was faster than the Python loop. I learned how NumPy can be easier to use in certain situations

##PW1 - LAB B

the observed tada decays were compared with analytical law results. Although ther were some uncertainities the general law of both datas were the same.

Snakemake was used to easily create the plotting pipeline. It takes
`decay_observed.csv` as input and runs `plot.py` to generate `figure.png`.