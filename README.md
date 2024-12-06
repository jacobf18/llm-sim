# LLM-Sim

This repo contains the code for LLM-Sim, an LLM-based simulation-based optimization system to emulate (or surpass) human-level skills at adapting to changing environments. This hinges on the idea that for a control environment (or just real-world environment in general), getting external reward data is often very costly compared to running a computer simulation of the external environment. Thus, programmers develop simulations of the external environment to mimic real-world at a much lower cost. However, it is up to the programmer to write the simulation and update it when the external environment changes. This upfront cost and update cost can be prohibitive not just in programmers needed to write/update a simulation, but also in hours worked. For instance, in highly dynamic environments where the external dynamics are not well known ahead of time, having a programmer in the loop updating the simulation as decisions need to be made takes too long to effectively make decisions. Thus, we propose LLM-Sim, which seeks to replace programmers mainly during the update step of simulations when the external environment changes. The code is written in Python and utilizes open-source large models.

## Benchmarks

We modify and extend existing benchmarks to evaluate the performance of LLM-Sim. The benchmarks include:

* [Gymnasium](https://gymnasium.farama.org/) : A collection of reinforcement learning environments (previously OpenAI's Gym).
* [ARC-AGI](https://arcprize.org) : A collection of complex human-level reasoning tasks.

## System architecture

The system architecture of LLM-Sim is given in the following figure:

![System architecture](./LLM-Sim.pdf)
