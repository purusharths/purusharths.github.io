---
layout: post
title: Link to Previous Projects
Summary: A repository of Previous Projects
category: unlisted
---

### Masterarbeit: <br>
**_Abstract:_** In this work, we use the Finite Element model to simulate colorectal cancer progression using the Fischer KPP equation in the microenvironment of colonic
crypts. Emphasizing the role of initial conditions and crypt geometry, the thesis shows their impact on in silico cancer development. We use a novel approach with
Gaussian Random Fields to model heterogeneous cancer growth, showcasing varied influences under different covariances. Comparative analysis with histological
images validate empirical estimations based on the rate of change of probabilities. Additionally, a stochastic approach identifies crypt areas vulnerable to cancer
growth, offering a comprehensive view based on random fields and crypt geometry.<br>

Full Text: https://heibox.uni-heidelberg.de/f/f6a8c4a3d57f44fab2ac/ <br>

**Masters thesis code**:
- FEM Code: https://emcl-gitlab.iwr.uni-heidelberg.de/purusharth.saxena/tmp_thesis_codebkp
- Python Paraview Visualizations: https://emcl-gitlab.iwr.uni-heidelberg.de/purusharth.saxena/paraviewvisualization
- Thesis Plots: https://github.com/purusharths/thesis_plots

Random Fields Analysis
- **GRAF++**: A header only library used for generation of Gaussian Random Fields via circulant embeddings. Built on top of xetnsor and uses fftw3 backend. Used specficially for hiflow (in masterarbeit)<br>
  [Ongoing] @TODO add Karhunen-Lourve expansion to incorporate PDE Constraint Bayesian Inverse Problems <br>
  GitLab: https://emcl-gitlab.iwr.uni-heidelberg.de/purusharth.saxena/graf


- **PDE Based Sampling**:
  [Ongoing] Simple illustration of Sampling via SPDEs based on [Khristenko et.al, 2018](https://arxiv.org/pdf/1809.07570.pdf), [Lindgren et. al, 2011](https://doi.org/10.1111/j.1467-9868.2011.00777.x). <br>
  In a nutshell,

  Basically, here the link link between the $C^{-1}$ (inv. of covariance operator) and stochastic PDEs is utilized.<br/>
  For example, Matérn fields can be sampled by solving the sPDE:
    
  $$(\kappa^{2}-\Delta)^{\beta}a(x,\omega)=^{d}\mathcal{W}(x,\omega) \text{ in } \mathbb{R}^d,$$
    
  where $\Delta$ is the Laplacian and $\mathcal{W}$ is Gaussian white noise on $\mathbb{R}^d$. The resulting RF a is Gaussian with Matérn covariance with parameters
  https://github.com/purusharths/pde_based_sampling

---

- **Computational Molecular Biology**: Electrostatic Calculations with Adaptive poission boltzman solver (APBS) on Ubiqutin (1UBQ refined at 1.8 Angstroms Resolution) and its complex with a SH3 Domain - the 2K6D Molecule. <br>
GitHub: https://github.com/purusharths/cmb-ubq-2k6d

- **Single Cell Omics:** [Ongoing] Analyzing Single Cell Omics code through self-study with a mathematical cone of view.<br>
GitHub IO: https://purusharths.github.io/sco_intro_math

- **Umbridge**: Umbrige is a framework that connects FEM software backend (dune, hiflow, dealii etc) with UQ backend (pymc, MUQ etc) eliminating the need to rewrite MC codes
- [Hiflow integration with Umbridge](https://emcl-gitlab.iwr.uni-heidelberg.de/purusharth.saxena/fkpp-colorectal-adenoma/-/tree/umbridge/hiflow3-master/exercises/fischerKPP?ref_type=heads) and [um-bridge collaborations](https://github.com/purusharths/umbridge)

- **Comparision Monte Carlo / Quasi-Monte Carlo Methods**: Comparing different monte carlo approximations in Python [@TODO Python vs Julia]
  GitHub: https://github.com/purusharths/nb_monte_carlo_benchmarks

- **Numerical Methods for Baysiean Inverse Problems / Uncertainity Quantification**: Solving DE Constraint Baysiean Inverse Problem with Python
  GitHub: https://github.com/purusharths/mcmc_test
---

- **Dicontinious Gelarkin method for Cavity Stokes**: Based on Di Petro and Ern's book on [Mathematical Aspects of Discontinuous Galerkin Methods](https://link.springer.com/book/10.1007/978-3-642-22980-0) Chapters 2, and 6.1 <br>
GitHub: https://github.com/purusharths/dg-CavityStokes <br>

- **Magnus Effect in Navier Stokes**: [Magnus Effect](https://www.youtube.com/watch?v=2OSrvzNW9FE) simulated for a ball in a free flow boundary condition in hiflow3 <br>
GitHub: https://github.com/purusharths/magnus-effect-navier-stokes<br>

- **MIT Benchmark for heat driven convection**: Replication study for [Computational Predictability of Natural Convection Flows In Enclosures](https://www.osti.gov/servlets/purl/15006259-x0JCRo/native/) done with Hiflow3. This benchmark describes the heat driven cavity flow in a 8:1 rectangular domain at near-critical Rayleigh number. <br>
GitHub: https://github.com/purusharths/mit_benckmark_heat_driven_cavity/

---

- **Sparse Matrix Benchmark**: Based on Yousuf Saad's book on [Iterative methods for Sparse Linear Systems](https://www-users.cse.umn.edu/~saad/IterMethBook_2ndEd.pdf). <br>
Benchmarking done on different storage paradigm for Sparse Matrices (CSR/COO etc).<br>
GitLab: https://gitlab.com/purusharths/sparse-matrix-benchmark<br>

- **Symmetric Gauss Sidel**: OpenMP based parallel implementation of [Symmetric Gauss Sidel](https://arxiv.org/abs/2311.14138)<br>
GitHub: https://github.com/purusharths/symmetric-gauss-seidel-parallel<br>

---

- **PyBind Hiflow**: Generating Python Wrapper for Hiflow3<br>
GitLab: https://emcl-gitlab.iwr.uni-heidelberg.de/hiflow_v3/pyhiflow<br>

- **GeoSpatial Analysis Based on Similarity Index**: Numerical Simulations based on [Bray-Curtis's formula](https://esajournals.onlinelibrary.wiley.com/doi/10.2307/1942268) for Similarity Index (1957) comparing pollutions for different cities
    1. https://arxiv.org/abs/1906.08756
    2. https://arxiv.org/abs/1806.02263 <br>

- **Control Theory simulations**: Control Theory specific simulations with Manim under Prof. Sachin Patwardhan, Prof. Belur (IIT Bombay)
https://github.com/purusharths/control_theory_simulations
---

- **Hardware aware computing**: From the lecutre on Hardware Aware Scientific Computing. Contains good starting points for MPI, OpenMP, MPI+X, and TBB along with some n-body simulations with the same.
GitLab: https://gitlab.com/purusharths/hasc

- **Mathematical Animations Backend**: Python Backend for [math.animations.fossee.in](https://math.animations.fossee.in/) that hosts of the lecture notes for Calculus, Linear Algebra and Transformations @ math.animations.fossee.in created under the IIT-Bombay fossee Fellowship of 2020. 
GitHub: https://github.com/purusharths/django_math.animations

- **Ill Conditioned Matrices**: Generic motivation for why matrices are badly conditioned and why it matters. Presented in Banglore Python Meetup<br>
GitHub: https://github.com/purusharths/ill-conditioned-matrices

- **Presentation Scipy India 2019:** https://github.com/purusharths/scipy2019





