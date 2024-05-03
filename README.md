# SynthAI

Elevating AI development for Pi Network, SynthAI offers state-of-the-art synthetic data generation techniques coupled with advanced deep learning frameworks, enabling robust AI model training in privacy-sensitive environments.

# Introduction

SynthAI is a synthetic dataset generator for training and evaluating machine learning models in the field of Artificial Intelligence. This repository contains the source code for generating various synthetic datasets, which can be used for tasks such as object detection, semantic segmentation, and image classification.

# Features

- Generate customizable synthetic datasets with various parameters
- Support for multiple object categories and backgrounds
- Realistic rendering with physically-based lighting and materials
- Integration with TensorFlow and Keras for training and evaluation

# Getting Started

## Prerequisites

- Python 3.6 or higher
- Virtual environment (optional but recommended)

## Installation

1. Clone the repository:
```
git clone https://github.com/KOSASIH/SynthAI.git
```
2. Navigate to the cloned repository's directory:
```
cd SynthAI
```
3. Create a virtual environment (optional):
```
python3 -m venv venv
```
4. Activate the virtual environment (commands vary based on your operating system):

- For Linux/macOS:
```
source venv/bin/activate
```
- For Windows:
```
venv\Scripts\activate
```

5. Install the required packages:
```
pip install -e .
```

# Usage

To generate a synthetic dataset, use the generate_dataset.py script with the desired parameters. For example, to generate a dataset with 1000 images of size 224x224, containing objects from the 'car' and 'pedestrian' categories, run:

```
python generate_dataset.py --output_dir output --num_images 1000 --image_size 224 --categories car pedestrian
```
This will create a new directory output containing the generated dataset.
For more information on the available options, run:

```
python generate_dataset.py --help
```

# Training and Evaluation

To train and evaluate a machine learning model using the generated dataset, you can use the included Jupyter notebooks or create your own scripts using TensorFlow and Keras.

# Contributing

We welcome contributions to SynthAI! Please submit a pull request if you have any improvements, bug fixes, or new features to add.

# License

SynthAI is released under the MIT License. See the LICENSE file for more information.

# Contact

For any questions, issues, or suggestions, please contact the maintainers at info@synthai.com.
