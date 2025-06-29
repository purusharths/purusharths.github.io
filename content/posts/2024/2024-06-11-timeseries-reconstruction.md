---
layout: post
title: Dynamical behaviour and timeseries reconstruction with Lorrenz Attractor
summary: 
tags:
  - python
  - dynamical-system
  - timeseries
  - chaotic-system
  - neural-odes
  - echo-state-networks
---
# Neural Ordinary Differential Equations (Neural ODEs)

Neural dODEs combine ordinary differential equations (ODEs) and neural networks. These are relatively simple and a seemingly obvious choice for systems governed by a set of differential equations. Rather than discretizing time into fixed intervals as in conventional RNN, the network's hidden states evolve continuously over time. These continuous-time dynamics are governed by an ordinary differential equation, which describes how the hidden states change as a function of time and the current state.

There can be two lines of thought for understanding Neural ODEs (NODEs): NN trained with a numerical ODE solver or "numerical method" that happened to use a neural net to approximate a system of differential equations. 

In a traditional numerical setting, to solve an IVP or Initial Value Problem, we need an initial condition $y_0$, a time-stepping scheme ($h$), and the derivative $\frac{d}{dt}$. In the case of NODEs, the neural network represents the derivative $\frac{d}{dt}$; the initial value is the input. Hence, we can model the system using a neural network (as a governing ODE) and solve it using pre-existing ODE solvers. The main challenge here is to be able to take derivatives of functions of an ODE solver with respect to neural network parameters. This is where the adjoint sensitivity method comes in, where a differential equation is solved to obtain the gradients of the loss function. 

### Implementation for Loren63 & Lorenz96 systems

•⁠  ⁠Reconstructions and Loss v Epoch Plots for Lorenz63 system
<table><tr>
<td> <img src="figures/loss_l63_node.png" alt="Drawing" style="width: 450px;"/> </td>
<td> <img src="figures/node_l63_comparision.png" alt="Drawing" style="width: 450px;"/> </td>
</tr></table>


<center><img src="figures/node_l63_3d.png" alt="Drawing" style="width: 650px;"/> </center>

•⁠  ⁠Reconstructions and Loss v Epoch Plots for Lorenz96 system
<table><tr>
<td> <img src="figures/node_l96_loss.png" alt="Drawing" style="width: 450px;"/> </td>
<td> <img src="figures/node_l96_comparision.png" alt="Drawing" style="width: 450px;"/> </td>
</tr></table>


<center><img src="figures/specific_triplets_3d.png" alt="Drawing" style="width: 9500px;"/> </center>
 
 

Note: exploration of hyperparameter configurations was a bit limited by computational resources, and the model could not run for a very long time, but even with these limited iterations, we see good reconstructions and a rapidly converging loss function for L63. The difference between a very high dimensional model like lorenz96 and a lower dimensional model like Lorenz 63 can be seen from the Loss vs. epoch plots. While the L63 model converges rapidly, L96 exhibits a slow but steady convergence. The could learn more as the loss curve hasn't plateaued yet.


While there might be some even more interesting setups out there, it was not possible to try out more experiments (Google Colab, which was used for some experiments, was also exhausted).

Pros:
NODEs are good at modeling continuous-time dynamics. 
Parameter Efficiency: Requires fewer parameters than traditional neural networks in general, making them more memory-efficient.
Adaptive: Timestepping schemes are chosen adaptively by the underlying numerical ODE solvers. 
(In the ⁠` torchdiffeq` ⁠ package, `⁠odeint` ⁠ acts as the layer for building deep models)

Cons:
Can model the continuous dynamics well but might be computationally intensive.
It is challenging to train in comparison to other models made for such purposes (see ESN). 
Solving ODEs numerically is an expensive task, and there is a chance that the model will not converge if an incoherent ODE solver is chosen.
High sensitivity to hyperparameters, which makes it difficult to narrow into the most efficient set of the same for a given model.

<hr>


# Echo State Networks (ESNs)
ESNs belong to a class Reservoir Computing. Here a fixed, randomly initialized dynamical system, called a reservoir, is used to process the input data and generates the output predictions based on the non-linear dynamics. It can also be thought of as a different way of training Recurrent Neural Networks (RNN) by not training the hidden connections at all, instead just fix them randomly. The model would then learn the timeseries by just training how these hidden connections affect the outputs. In this case the hidden to h

<center><img src="figures/esn_illustration.jpg" width=400px></center>

This means only the output layer is learned, i.e., ESN gives a linear model (from reservoir to output). This is done in a way such that the biggest eigenvalue of the reserviour is ~1, i.e spectral radius of the weight matrix is ~1; which is trivial for a linear system. For non-linear systems, the reservoir's recurrent connections are set in such a way that the input can "echo" or reverberate within the reservoir states. Hence, captures the non-linear dynamics because of the non-linear transformations in the reservoir.

Even though there is some sensitivity to the hyperparameters, learning is very fast which allows for a more involved fine tuning. 

Let 
if $u = (x,y,z)$, and the ODE is given by $y_k = u_{k+1} \forall k=1...T$ in $\mathbb{R}^{T \times 3 }$
consider $u \subset U \in \mathbb{R}^{T\times 3}$ be input and $y \subset Y\in \mathbb{R}^{T\times 3}$ be the output, then the evolution of the state is given by 
$x_k = \tanh(Wx_{k-1}+W_{in}u_k)$ where $W$ and $W_{in}$ are weight and input weight matrices respectively. $W_{out}$ is the output weight matrix given by $W_{out} = Y^{T}(X^{T})^{\dagger}$ then the next step is given by:
$$x_{k} = \tanh(Wx_{k-1}+W_{in}y_{k-1}); \quad y_k = W_{out} x_k$$

such that $(X^{T})^{\dagger}$ is the pseudoinverse of X transpose.

As shown here, training an ESN involves optimizing only the weights of the output layer, typically using simple linear regression techniques. More efficient optimization algorithms can also be used. This decoupling of the reservoir dynamics from the learning process greatly simplifies training, making ESNs efficient and scalable.

### Implemntation for Loren63 & Lorenz96 systems

•⁠  ⁠Lorenz 63 Regeneration
<center><img src="figures/esn_lorenz63_comparision.png" alt="Drawing" style="width: 9500px;"/> </center>

<center><img src="figures/esn_lorenz63_attractor3d.png" alt="Drawing" style="width: 500px;"/> </center>
In the case of Lorenz63, ESN provices good predictions (owing to their capability to handle chaotic systems). In addition to that, their simplicity makes them quite attractive.

•⁠  ⁠Lorenz 96 Regeneration
<center><img src="figures/esn_lorenz96_comparision.png" alt="Drawing" style="width: 9500px;"/> </center>

<center><img src="figures/esn_specific_triplets_3d.png" alt="Drawing" style="width: 900px;"/> </center>

In the case of L96, even though we get very good regeneration (comparatively), it also hints that ESN might struggle with the higher dimensionality and complex interactions within the system, which could be assuaged by extensive hyperparameter tuning. Leaky rate and Spectral Radius are two important parameters. The leaky rate was chosen to be between 0.7, which means that 70% of the new state is influenced by the current input and the existing reservoir state, while 30% is retained from the previous state.

ESN are extremely fast compared to Neural ODEs and transformers, giving better reconstructions for this particular example. This leads to an empirical conclusion/observation that these might be the best models for such time series input. This configuration, along with the spectral radius of 0.9, would indicate that it can model temporal dependencies effectively without becoming too sensitive to noise or being unstable.

Pros:
It is relatively simple to implement and does not require backpropagation through time as only the output layer is trained. Fast learning. 
Computationally efficient since the reservoir (hidden layer) is fixed and not trained.
Effective in predicting chaotic time series due to their reservoir dynamics.<br>
Cons:
Might face challenges with high-dimensional state spaces
The fixed nature of the reservoir might limit the flexibility and adaptability of the model to different types of time series data; For example, high dimensional video or preprocessed speech input.
Might struggle with large datasets or complex systems compared to other deep learning approaches (see transformers).
At the same time, it is possible to combine RNN with ESN, i.e initilize RNN with ESN.

<hr>


# Transformers
Deep learning encoder-decoder architecture along with a mechanism called "self-attention". This allows them to weigh the important parts of the sequence while making predictions. Typically used for Natural Language Processing tasks like LLM.


<center><img src="figures/transformer_illustration.jpeg" width=400px/></center><br>
In this figure, input is on the bottom part, whereas output is on the top. Instead of words, the input comes from timeseries which is the same as embedding and classification (with words there is just the additional step to project words into vector space and then the generated vectors back to text via embeddings).

<table><tr>
<td> <img src="figures/l63_transformer.png" alt="Drawing" style="width: 350px;"/> </td>
<td> <img src="figures/l96_transformers.png" alt="Drawing" style="width: 350px;"/> </td>
    <td> <img src="figures/Transformer_bloop_96.png" alt="Drawing" style="width: 350px;"/> </td>
</tr></table>




However, transformers might not be the best bet for time series predictions as shown in various publications mentioned in [*]. Despite this there are some advantages of using transformers -- especially if the data is high dimensional with dependencies. For this example of Lorenz63 and Lorenz96, the regeneration did not happen, even though the error seemingly converged in the case of Lorenz96. The generated time series prediction bifurcated after a point (Rightmost image). 

A hypothesis for why the relative performance of Lorenz96 was slightly better could be due to the fact that it was a high dimensional data -- something that suits well for transformers.


Pros:
Transformers can handle long-range dependencies in time series data efficiently (due to their self-attention mechanism).

Cons:
Might be an overkill for time series. In case of Lorenz 96 they be advantageous for capturing complex, high-dimensional dependencies, but require careful tuning and significant resources.
Apart from what is mentioned in [*], we saw that the trasnformers are very resource intesive and need large amount of data. Moreover, implementing a transformers model is a complex with a lot of moving parts that needs to be fine-tuned which adds up to the complexity of the model.

[*] https://github.com/valeman/Transformers_Are_What_You_Dont_Need

<hr>

Adam optimizer, used in Neural ODEs and transformers offers adaptive learning rates for each parameter, efficiently combines momentum and RMSprop techniques, and is robust to noisy or sparse gradients, resulting in faster convergence and better performance in training neural networks

### Lorenz 63

|                      | Neural ODEs | ESN    | Transformers |
| -------------------- | ----------- | ------ | ------------ |
| Power Spectrum Error | 0.139       | 0.0663 | 0.187        |
| KL Divergence        | 0.346       | 0.0356 | 10.834       |

<hr>
### Lorenz 96
|  | Neural ODEs | ESN | Transformers |
|----------|----------|----------|----------|
|  Power Spectrum Error  |  0.0876 |  0.0773  |  0.317  |
|  KL Divergence  |  0.265  |  0.012  |  3.550  |

