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

* automated pipeline ([flopoco](https://flopoco.org/))  
An open source framework to generate FLOting POints COres but not only. Flopoco philosophy is that it allows to generate just what is needed for the computation without mimicking general purpose processors floating-points units. Flopoco takes as input, some behavioral hardware description and the couple (freq + target), and then outputs the necessary and sufficient synthetizable VHDL.  
In this work, I have made many FloPoCo Operators, including the whole Systolic Array, which allows me to generate any configuration I wish in less than a second. Example below:  

```
./flopoco SystolicArray N=3 M=3 arithmetic_in=posit:8:0 arithmetic_out=same msb_summand=12 lsb_summand=-12 nb_bits_ovf=7 has_HSSD=true chunk_size=-1 frequency=400 target=Kintex7 name=SystolicArray outputFile=SystolicArray.vhdl

*** Final report ***
Output file: SystolicArray.vhdl
Target: Kintex7 @ 400 MHz
|   |---Entity LZOCShifter_6_to_6_counting_8_F400_uid18
|   |      Pipeline depth = 1
|---Entity Arith_to_S3
|      Pipeline depth = 2
|   |---Entity LZOCShifterSticky_32_to_7_counting_64_F400_uid22
|   |      Pipeline depth = 3
|   |---Entity RightShifterSticky8_by_max_8_F400_uid24
|   |      Pipeline depth = 2
|---Entity l2a
|      Pipeline depth = 7
|   |   |   |   |---Entity DSPBlock_6x6_F400_uid35
|   |   |   |   |      Not pipelined
|   |   |   |---Entity IntMultiplier_F400_uid31
|   |   |   |      Not pipelined
|   |   |   |---Entity LeftShifter12_by_max_31_F400_uid38
|   |   |   |      Pipeline depth = 1
|   |   |---Entity s3fdp
|   |   |      Pipeline depth = 2
|   |---Entity PE_S3
|   |      Not pipelined
|---Entity SystolicArrayKernel
|      Not pipelined
Entity SystolicArray
   Not pipelined

```


* HSSD (Half Speed Sink Down)  
It is a mechanism I developped to allow the output-stationnary systolic array to output intermediate and final results while still receiving data.  
This is important to me because my final setup to evaluate the arrays is with CAPI2, OpenCAPI ([capi_wiki](https://en.wikipedia.org/wiki/Coherent_Accelerator_Processor_Interface)), which povide duplex throughputs approaching 20GB/s.  
Without HSSD, therefore, without pipelining input and output operations, the 20GB/s would be significantly lowered. However, as the below code snippet shows, there is possibility to generate the array without HSSD, which creates global routes and big muxes.  
HSSD comes at the cost of N*M*2*size_accumulator Flip Flops.  
This is not a problem in the case of modern FPGAs as they contain ~2x FFs more than LUTs. This is a problem for ASIC as FFs are expensive.

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
