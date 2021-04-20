# PHYS 490 Project #
## A Convolutional Neural Network Approach to Gravitational Wave Data Analysis ##
Group 7: Michael Astwood, Madison Buitenhuis, Jensen Lawrence, Catie Terrey

## Introduction ##

This project follows the paper ["Improved deep learning techniques in gravitational-wave data analysis"](https://arxiv.org/pdf/2011.04418.pdf) by Xia et al. The objective of this project is to develop convolutional neural networks capable of classifying gravitational wave signals from spin-aligned binary black hole mergers.

To classify gravitational wave signals, we recreate the convolutional neural network "ConvNet5" presented in the paper, since this model performed the best out of the six models presented. As well, we develop our own Bayesian convolutional neural network.

## Packages Used ##

Please see [`requirements.txt`](https://github.com/jensen-lawrence/Phys490-Project/blob/main/package_requirements.txt) for a complete list of packages used in this project.

## Setup ##

To utilize this project, first clone this repo onto a device of your choice. Next, install all of the packages listed in [`requirements.txt`](https://github.com/jensen-lawrence/Phys490-Project/blob/main/package_requirements.txt). Finally, generate the training and testing data sets using the scripts `generate_training_data.py` and `generate_testing_data.py` provided under [`data_generation/ggwd`](https://github.com/jensen-lawrence/Phys490-Project/tree/main/data_generation/ggwd). Further instructions are provided in this folder's README file.

## Usage ##

To run this program, navigate to the `Phys490-Project` directory on the command line, i.e., `cd path/to/Phys490-Project`. Then, on the command line, run the command
```
python main.py --model MODEL --param path/to/model_params.json --train path/to/training_data --test path/to/test_data --res path/to/results -v V
```
It is important to note that on computers with Python 2 and Python 3 installed, it may be necessary to use `python3` instead of `python` in the previous command.

The first flag, `--model`, is mandatory. Its argument, `MODEL`, is a string. This is the model that will be trained and validated. Options are `BNN` to train the Bayesian convolution neural network, and `CNN` to train the convolutional neural network.

The second flag, `--param`, is mandatory. Its argument, `path/to/model_params.json`, is a string. This is the path to the .json file containing the model hyperparameters. For the BNN, the appropriate path is `param/bnn_params.json`. For the CNN, the appropriate path is `param/cnn_params.json`.

The third flag, `--train`, is mandatory. Its argument, `path/to/training_data`, is a string. This is the path to the folder containing all the .hdf files for a given training data set, generated by `generate_training_data.py`.

The fourth flag, `--test`, is optional. Its argument, `path/to/test_data`, is a string. This is the path to the folder containing all the .hdf files for a given test data set, generated by `generate_testing_data.py`. Its default value is `''`; this means that by default, no testing will take place after training and validation.

The fifth flag, `--res`, is mandatory. Its argument, `path/to/results`, is a string. This is the path to the folder where the model performance graphs will be saved. These graphs document the loss, accuracy, AUC score, and ROC curve for the training and validation data.

The sixth flag, `-v`, is optional. Its argument, `V`, is an integer. This is the verbosity of the console output during training and validation. Its default value is `1`. If an alternate value is provided as the argument, this value will be used for the verbosity.

## Resources / Credits ##

Main paper: https://arxiv.org/pdf/2011.04418.pdf

Data generation reference paper: https://journals.aps.org/prd/pdf/10.1103/PhysRevD.100.063015

TensorFlow: https://www.tensorflow.org/

PyTorch: https://pytorch.org/

BLiTZ - Bayesian Layers in Torch Zoo (a Bayesian Deep Learing library for Torch): https://github.com/piEsposito/blitz-bayesian-deep-learning 

Package provided by reference paper: https://github.com/timothygebhard/ggwd

LALSuite documentation: https://lscsoft.docs.ligo.org/lalsuite/

LALSimulation repo: https://git.ligo.org/lscsoft/lalsuite/-/tree/master/lalsimulation
