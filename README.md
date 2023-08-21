# Maple-Syrup-Price-Prediction-using-LSTM

## Overview

This project aims to forecast maple syrup prices using a deep learning approach, specifically utilizing Long Short-Term Memory (LSTM) networks. By analyzing historical pricing data and relevant economic indicators, the model predicts future maple syrup prices to aid stakeholders in decision-making.

## Table of Contents

- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Model Architecture](#model-architecture)
- [Data Preprocessing](#data-preprocessing)
- [Training](#training)
- [Evaluation](#evaluation)
- [Results](#results)
- [Future Work](#future-work)

## Dataset

The dataset used for this project includes historical maple syrup prices, as well as associated economic factors such as weather conditions, production levels, and market trends. This combined dataset contains time-series data and is essential for training and evaluating the LSTM model.

## Installation

To set up and run the project, follow these steps:

1. Clone this repository:

   ```bash
   git clone https://github.com/asra0206/Maple-Syrup-Price-Prediction-using-LSTM.git
   cd Maple-Syrup-Price-Prediction
   ```

2. Create a virtual environment (recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

## Usage

1. Ensure your dataset is properly structured and placed in the `data` folder.
2. Modify the model configuration and hyperparameters in `maple3.py` as needed.
3. Run the training script to train the LSTM model:

   ```bash
   python maple3.py
   ```

4. To make price predictions, run the prediction script:

   ```bash
   python maple3.py
   ```

## Model Architecture

The core of this project is the LSTM model. The architecture comprises several LSTM layers, followed by fully connected layers to predict maple syrup prices. The model architecture is defined in `model.py`.

## Data Preprocessing

Data preprocessing is crucial for this project. The `mapel3.py` script takes care of data cleaning, feature engineering, and preparing the dataset in a format suitable for LSTM training.

## Training

The training script (`mapel3.py`) uses the preprocessed data to train the LSTM model. The trained model weights are saved in the `model` file.

## Evaluation

Model performance is evaluated using metrics like Mean Squared Error (MSE) or Root Mean Squared Error (RMSE). 

## Results

The project's results are summarized in the `results` folder. This includes model evaluation metrics, visualizations of predicted prices against actual prices, and any additional insights.

## Future Work

- Experiment with different LSTM architectures and hyperparameters for potential performance improvements.
- Incorporate external data sources for more accurate predictions, such as geopolitical events or supply chain data.
- Develop a web interface to allow users to input their parameters and receive predictions.


---
