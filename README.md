**Student Performance Prediction** 


**Problem Statement**

The goal of this project is to understand how various factors affect a student's performance in tests, specifically focusing on test scores. The factors under consideration include:
Gender
Ethnicity
Parental Level of Education
Lunch Type
Test Preparation Course
By analyzing these variables, the project aims to predict student performance based on the provided inputs.


**Project Overview**

This project is designed as a real-life machine learning application. It encompasses all the steps required to develop, evaluate, and deploy a predictive model. Key features include:

Exploratory Data Analysis (EDA): Investigating the dataset to uncover patterns, trends, and correlations.

Model Training: Using machine learning techniques to train a model that predicts student performance.

Data Ingestion and Model Training: Efficient data ingestion pipeline and model training process.

Model Evaluation: Evaluating the model using different metrics to ensure it performs well.

Hyperparameter Tuning: Fine-tuning model parameters to improve predictive accuracy.

Prediction Pipeline: Creating a REST API using Flask that predicts the test scores based on user input.

Deployment: Deploying the Flask app to AWS Elastic Beanstalk for a scalable and accessible solution.
**Deployed**
"http://studentperformance.ap-south-1.elasticbeanstalk.com/"
"http://studentperformance.ap-south-1.elasticbeanstalk.com/predictdata"  


**Technologies Used**

Python 3.9: The main programming language used for the project.

Pandas: For data manipulation and analysis.

Matplotlib/Seaborn: For visualization during exploratory data analysis (EDA).

Scikit-learn: For model training, evaluation, and hyperparameter tuning.

Flask: For creating the prediction pipeline as a web application.

AWS Elastic Beanstalk: For deploying the application in the cloud.

Nginx: As a reverse proxy to serve the Flask app.
