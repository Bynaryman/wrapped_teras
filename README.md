# TERAS

* Tera is a unit prefix in the metric system denoting multiplication by one trillion, or 10<sup>12</sup>.
* Tera is derived from the Greek word *τέρας* teras, meaning "monster".

Both reasons motivated to name this GEMM accelerator generator "TERAS". Indeed, it can generate arbitrarily large accelerators, hence the monstrous aspect, while delivering >10<sup>12</sup> (tera) floating-point operation per second.

## Introduction

TERAS is a command line generator that produces kernel to compute the BLAS level3 routine GEMM aka Matrix-Matrix Multiplication (MMM). It focuses on arithmetic aspects to be able to save power consumption while offering more precise and reproducible results.

## Generator Overview

The kernels rely on 2D (NxM) meshes implemented by Systolic Arrays. Every signal is transferred by the mean of local and distributed connections to improve scalability (see Fig below).
![overview](https://github.com/Bynaryman/teras/tree/master/pictures/overall_SA.svg?raw=true "Overview_SA")
At each clock cycle, N and M real numbers are taken from rows of input Matrix A and columns of input matrix B, rexpectively. Such numbers arrive in a dense form, which is the computer format they are stored in memory before getting translated into "S3" by "A2S3" modules. S3 is a handmade format that allows to translate any incoming computer format while being optimized for hardware internal cells /  blocks.

Other peculiarities of this generator comprise:

* autoamted pipeline (flopoco)
* HSSD
* fused

## FPGA evaluation

## MPW5 and ASIC adaptation



# License

This project is [licensed under Apache 2](LICENSE)

# Authors

Louis LEDOUX (Binaryman)
