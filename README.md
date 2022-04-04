# TERAS

* Tera is a unit prefix in the metric system denoting multiplication by one trillion, or 10<sup>12</sup>.
* Tera is derived from the Greek word *τέρας* teras, meaning "monster".

Both reasons motivated to name this GEMM accelerator generator "TERAS". Indeed, it can generate arbitrarily large accelerators, hence the monstrous aspect, while delivering >10<sup>12</sup> (tera) floating-point operation per second.

## Introduction

TERAS is a command line generator that produces kernel to compute the BLAS level3 routine GEMM aka Matrix-Matrix Multiplication (MMM). It focuses on arithmetic aspects to be able to save power consumption while offering more precise and reproducible results.  
The original design targets FPGAs even if it is target agnostic. One of the design choice was a heavy use of flip flops as they are present in good quantity in modern FPGAs ( ~2x than LUTs). That is why there is a paragraph on FPGA evaluation and one for the mpw5 adaptation.

## Generator Overview

The kernels rely on 2D (NxM) meshes implemented by Systolic Arrays. Every signal is transferred by the mean of local and distributed connections to improve scalability (see Fig below). 
  
![overall_SA](https://user-images.githubusercontent.com/937470/161559284-bda5cf49-2cf6-426a-a57b-295eebc6874b.png)


At each clock cycle, N and M real numbers are taken from rows of input Matrix A and columns of input matrix B, rexpectively. Such numbers arrive in a dense form, which is the computer format they are stored in memory before getting translated into "S3" by "A2S3" modules. S3 is a handmade format that allows to represent any incoming computer format while being optimized for hardware internal cells /  blocks.

The data in S3 format that represent the coeficients of the matrixes go inside the Processing Elements (PEs). Each PE has the role to do a fused-dot-product (FDP), i.e. a dot-product without any intermediate rounding. Additionally, the PEs pass the data to south and east neighbours. Example in the image below:  
![PE](https://user-images.githubusercontent.com/937470/161559537-d5735fe3-31c7-48f2-baac-6a2b806efcbf.png)

The hardware responsible for the fused dot product is S3FDP and is depicted below:  
  
![s3fdp](https://user-images.githubusercontent.com/937470/161559861-dd94410d-38a9-4bf8-9945-821b69895a8f.png)


Other peculiarities of this generator comprise:

* automated pipeline (flopoco)
* HSSD

## FPGA evaluation

Following results should have similar trends for ASIC with several less order of magnitude with regard to throughput and performace.
  
![fpga_dse](https://user-images.githubusercontent.com/937470/161560423-e654d06a-f39e-46b4-aeec-1d6739de8396.png)

![fpga_floorplanning](https://user-images.githubusercontent.com/937470/161560261-af9f6d1a-434a-4d74-aeea-5e722e9bc8b5.png)

![power9_runtime](https://user-images.githubusercontent.com/937470/161560583-5ad7011e-e3c7-4923-a9a8-28a448d63288.png)

![accuracy_vs_en eff](https://user-images.githubusercontent.com/937470/159266031-37893968-c0dd-47cf-9bf4-97b38a5baa04.png)



## MPW5 and ASIC adaptation



# License

This project is [licensed under Apache 2](LICENSE)

# Authors

Louis LEDOUX (Binaryman)
