# TERAS

* Tera is a unit prefix in the metric system denoting multiplication by one trillion, or 10<sup>12</sup>.
* Tera is derived from the Greek word *τέρας* teras, meaning "monster".

Both reasons motivated to name this GEMM accelerator generator "TERAS". Indeed, it can generate arbitrarily large accelerators, hence the monstrous aspect, while delivering >10<sup>12</sup> (tera) floating-point operation per second.

## Introduction

TERAS is a command line generator that produces kernel to compute the BLAS level3 routine GEMM aka Matrix-Matrix Multiplication (MMM). It focuses on arithmetic aspects to be able to save power consumption while offering more precise and reproducible results.  
The original design targets FPGAs even if it is target agnostic. One of the design choice was a heavy use of flip flops as they are present in good quantity in modern FPGAs ( ~2x than LUTs). That is why there is a paragraph on FPGA evaluation and one for the mpw5 adaptation.

## Generator Overview

The kernels rely on 2D (NxM) meshes implemented by Systolic Arrays. Every signal is transferred by the mean of local and distributed connections to improve scalability (see Fig below). 
  
![overall_SA](https://user-images.githubusercontent.com/937470/159264946-99aeecf9-ac5a-43d4-8787-e48fa6afb2f5.png)


At each clock cycle, N and M real numbers are taken from rows of input Matrix A and columns of input matrix B, rexpectively. Such numbers arrive in a dense form, which is the computer format they are stored in memory before getting translated into "S3" by "A2S3" modules. S3 is a handmade format that allows to represent any incoming computer format while being optimized for hardware internal cells /  blocks.

The data in S3 format that represent the coeficients of the matrixes go inside the Processing Elements (PEs). Each PE has the role to do a fused-dot-product (FDP), i.e. a dot-product without any intermediate rounding. Additionally, the PEs pass the data to south and east neighbours. Example in the image below:  
![PE](https://user-images.githubusercontent.com/937470/159266205-8a597991-d8b3-4fc9-b564-84875ed32365.png)

The hardware responsible for the fused dot product is S3FDP and is depicted below:  
  
![s3fdp](https://user-images.githubusercontent.com/937470/159269017-88714630-3ec6-4393-8e5b-f01404c09623.png)


Other peculiarities of this generator comprise:

* automated pipeline (flopoco)
* HSSD

## FPGA evaluation

Following results should have similar trends for ASIC with several less order of magnitude with regard to throughput and performace.

![fpga floorplanning](https://user-images.githubusercontent.com/937470/159265448-f153a1e6-d968-42cf-819d-09c548721586.png)

![fpga dse](https://user-images.githubusercontent.com/937470/159265742-63a7a600-7dc8-4ebc-85d5-d6e5a69e4919.png)

![power9 runtime](https://user-images.githubusercontent.com/937470/159265877-1684e662-3ac7-45ab-ae37-432079b5cffe.png)

![accuracy_vs_en eff](https://user-images.githubusercontent.com/937470/159266031-37893968-c0dd-47cf-9bf4-97b38a5baa04.png)



## MPW5 and ASIC adaptation



# License

This project is [licensed under Apache 2](LICENSE)

# Authors

Louis LEDOUX (Binaryman)
