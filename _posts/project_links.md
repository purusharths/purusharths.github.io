Some Projects that were done 

Masters thesis code:
Python Paraview Visualizations: 


- **GRAF++**: A header only library used for generation of Gaussian Random Fields via circulant embeddings. Built on top of xetnsor and uses fftw3 backend.
@TODO add Karhunen-Lourve expansion to incorporate PDE Constraint Bayesian Inverse Problems <br>
https://emcl-gitlab.iwr.uni-heidelberg.de/purusharth.saxena/graf


- **PDE Based Sampling**:
  Simple illustration of Sampling via SPDEs based on [Khristenko et.al, 2018](https://arxiv.org/pdf/1809.07570.pdf), [Lindgren et. al, 2011](https://doi.org/10.1111/j.1467-9868.2011.00777.x). <br>
  In a nutshell,

  Basically, here the link link between the $C^{-1}$ (inv. of covariance operator) and stochastic PDEs is utilized.<br/>
  For example, Matérn fields can be sampled by solving the sPDE:
    
$$(\kappa^{2}-\Delta)^{\beta}a(x,\omega)=^{d}\mathcal{W}(x,\omega) \text{ in } \mathbb{R}^d,$$

    
  where $\Delta$ is the Laplacian and $\mathcal{W}$ is Gaussian white noise on $\mathbb{R}^d$. The resulting RF a is Gaussian with Matérn covariance with parameters
  https://github.com/purusharths/pde_based_sampling

---

- **Computational Molecular Biology**: Electrostatic Calculations with Adaptive poission boltzman solver (APBS) on Ubiqutin (1UBQ refined at 1.8 Angstroms Resolution)[8] and its complex with a SH3 Domain - the 2K6D
Molecule.
https://github.com/purusharths/cmb-ubq-2k6d

- Some infrequent contributions to [um-bridge](https://github.com/purusharths/umbridge), manim
--

- **Dicontinious Gelarkin method for Cavity Stokes**: Based on Di Petro and Ern's book on [Mathematical Aspects of Discontinuous Galerkin Methods](https://link.springer.com/book/10.1007/978-3-642-22980-0)
Chapter 2, 6.1

--
- https://github.com/purusharths/dg-CavityStokes
- **Magnus Effect in Navier Stokes**: [Magnus Effect](https://www.youtube.com/watch?v=2OSrvzNW9FE) simulated for a ball in a free flow boundary condition in hiflow3

https://github.com/purusharths/magnus-effect-navier-stokes




Cancer:
  Add link for presentations in seminars

MIT Benchmark for heat driven convection
<add paper link>
<add link for github repo>


- **Sparse Matrix Benchmark**: Based on Yousuf Saad's book on [Iterative methods for Sparse Linear Systems](https://www-users.cse.umn.edu/~saad/IterMethBook_2ndEd.pdf). 
  https://gitlab.com/purusharths/sparse-matrix-benchmark

- **Symmetric Gauss Sidel**: OpenMP based parallelization of [Symmetric Gauss Sidel](https://arxiv.org/abs/2311.14138)
- 
https://github.com/purusharths/symmetric-gauss-seidel-parallel

Hardware aware computing

/hiflow3.org/hiflow3/-/wikis
Code for workshops
math.animations
Similarity index analysis (add papers: <>, <>)

Control Theory simulations

