Machine Learning Stock Price Predictor

This project aims to predict stock price movement using cutting-edge machine learning technology and to explore the efficacy of different models and parameters.

Data Sources:
This project uses Yahoo Finance to source historical stock price data and Federal Reserve Economic Data (FRED) to incorporate macroeconomic indicators.

Preprocessing:
Data handling is primarily done with pandas, along with custom-built sequencing scripts to train the model on sequential time series data.

Model Architecture:
The model is built on a Recurrent Neural Network with Long Short-Term Memory (LSTM) layers, implemented using Keras via TensorFlow. The neural network is optimized using the Adam optimizer and utilizes early stopping during the training phase. Specific hyperparameters can be found in the notebook file.

Evaluation:
The primary evaluation techniques are RMSE and directional accuracy. Additionally, a visualization of the predicted price versus the actual price is produced for qualitative assessment.

Results:
The current best results include a 58% directional accuracy score using macroeconomic data with high correlation to the ticker.

Future Improvements:
Implementing a version that incorporates lower time frames for stock price data. Currently working on a version that utilizes Random Forest.

