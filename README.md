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

## PW2 - LAB A

The data of acceleration is noisy because of diffrentiation process ,it makes small errors in position data bigger in accleleration data 

Report:
    The mean acceleration was -8.57 m/s^2,the largest difference was 0.78 .It proves that taking derivative cause noisiness and integration restore preciseness back 
## PW2 --- Lab B
### Part 2 - Optimization Comparison

Easy convex function f(x):
All 3 methods (GD, Newton, SLSQP) show same result x = 3.000.

Harder landscape g(x):

From x0 = 0.0: GD and SLSQP got local minimum x = -1.30, but Newton method went to local maximum x = 0.17 (because g'' < 0).

From x0 = 2.0: All methods found global minimum x = 1.17 (g'' > 0).
Conclusion: Newton method looks for g'(x) = 0 (stationary points), not always minimum. Initial value x0 is very important.

### Part 3 - Reaction Rate Fitting

Fitted rate constant k = 0.250.
Plot saved in kinetics.png.

### Part 4 - Chemical Equilibrium

Reaction extent at equilibrium x = 0.662.
Equilibrium amounts:
nH2 = 0.338 mol
nI2 = 0.338 mol
nHI = 1.325 mol
Plot saved in equilibrium.png.

### Part 5 - Titration Equivalence Point

Equivalence point is at V = 50.0 mL (where derivative dpH/dV is highest).
Plot saved in titration.png.