# CSE-5001-Fall-2021
This repository is the course project for CSE 5001 Advanced Artificial Intelligence Fall 2021 at SUSTech. In this project, we investigated the problem on genetic algorithm for multiple traveling salesman.

## Introduction
Multiple Travelling Salesman Problem (MTSP) is an extension of the famousTravelling Salesman Problem (TSP) that visiting each city exactly once withno sub-tours. MTSP involves assigningmsalesmen toncities, and each citymust be visited by a salesman while requiring a minimum total cost. In this project, we investigated baseline method, IPGA and VNS-GA .A novel genetic algorithm named Polar-IPGA is proposed by combing IPGA and VNS-GA. Statistical comparison is conducted on 6 datasets with varying city numbers andlayouts.The proposed method achieved superior performance on all 6 datasetscompared to baseline method within the runtime consumption limitation.

## Usage
### Baseline
The original code implementation can be found [here](https://github.com/Anupal/GA-for-mTSP/tree/master/mtsp). 
To run the baseline method, 
```
$ cd ./baseline/
$ python main.py -d NAME_OF_YOUR_DATASET (mtsp51, mtsp100, mtsp150, pr76, pr152, pr226)
```
### NN-IPGA
The original code implementation of NN-IPGA can be found [here](https://github.com/alex-cornejo/mTSP-IPGA). 
To run NN-IPGA, 
```
$ cd ./NN-IPGA/
$ python main.py -d NAME_OF_YOUR_DATASET (mtsp51, mtsp100, mtsp150, pr76, pr152, pr226)
```
### Polar-IPGA
To run the proposed Polar-IPGA: 
```
$ cd ./Polar-IPGA/
$ python main.py -d NAME_OF_YOUR_DATASET (mtsp51, mtsp100, mtsp150, pr76, pr152, pr226)
```

## Acknowledge
The projetc is done jointly with Jieting Zhao, Zhirui Sun, Jiamin Zheng, and Mingzhe Lv. Thanks for our group's effort.

