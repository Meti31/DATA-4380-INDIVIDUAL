<img width="305" alt="Screen Shot 2022-06-23 at 9 47 05 AM" src="https://user-images.githubusercontent.com/89664911/175315233-f8cc17a8-18c6-4454-b42d-07a07184e1a8.png">

# Prediction of Diseases using machine learning Algorithms

This repository holds an attempt to compare the performance of different machine learning algorithms on two dataset.And also attempts to build web app using streamlit to predict the likelihood of a person having these disease based on the given datasets. The datasets  used are "Diabetes Dataset"( https://www.kaggle.com/datasets/mathchi/diabetes-data-set) and "Heart Failure Prediction Dataset" (https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction)

# Overview

The "Diabetes Dataset" contains the diagnosis of females at least 21 years old of Pima Indian heritage based on factors like Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI,DiabetesPedigreeFunction,Age. The outcomes are described as 0 or 1 with 0 being tested negative for diabetes and 1 being tested positive for diabetes.

The other Dataset used in this repository is "Heart Failure Prediction Dataset"  which is combinatiion of 5 heart disease datasets . The dataset contains a diagnosis of patients based on factors like Age,Sex,ChestPainType,RestingBP,Cholesterol,FastingBS,RestingECG,maximum heart rate achieved,ExerciseAngina,Oldpeak and the slope of the peak exercise ST segment.The diagnosis are described as 0 0r 1 with 0 being not having heart failture and 1 being having heart failture.

# Summary of Workdone

Data: 
  Type:
        Input: The datasets are csv files that have 8 attrubute for the diabetes dataset and 11 atributes for heart failture dataset.
  Size: 
                The "Heart Failure Prediction Dataset" dataset have 918 instances and "Diabetes Dataset" have 768 instances. In both dataset 33% was used as a test data and the remaining were used as train.
         
# Data Visualization

<img width="764" alt="Screen Shot 2022-06-23 at 3 44 09 PM" src="https://user-images.githubusercontent.com/89664911/175424760-cd94f129-6a60-4d41-8386-7acc047c3924.png">

<img width="792" alt="Screen Shot 2022-06-23 at 6 19 28 PM" src="https://user-images.githubusercontent.com/89664911/175424810-a925933b-010c-4a57-99da-61345b3f16e4.png">


##The first picture shows the correlation of the attributes in "Diabetes Dataset"  and the second picture shows the correlation among the attributes in  "Heart Failure Prediction Dataset" .

# Problem Formulation and Training
The first step was cleaning the datasets individually. After that the datasets were divided in to training and testing data. In each dataset 33% were used to train it.Both datasets were trained using Random Forest classifier,support Vector classifier,Logistic Regression, Desicion Tree and Gaussian Naive Bayes. 

# Performance Comparison
In both datasets the Random forest classifier had the highest accuracy score which was 0.874587 for "Heart Failure Prediction Dataset" and "Diabetes Dataset" .Then the Random forest classifier model was saved for both datasets. Then Streamlit was used to develop web app that takes an inputs from users and predict if they are prone to Diabetes or Heart Failture. The pictures below will show how the app look and works.


<img width="1192" alt="Screen Shot 2022-06-28 at 10 19 01 AM" src="https://user-images.githubusercontent.com/89664911/176202342-bb91c33e-a6cc-4b24-af8f-d37d37a85ae6.png">















<img width="898" alt="Screen Shot 2022-06-28 at 9 39 40 AM" src="https://user-images.githubusercontent.com/89664911/176193367-208f233f-e4da-4ac0-a288-065c68a47c7a.png">


<img width="939" alt="Screen Shot 2022-06-28 at 9 39 54 AM" src="https://user-images.githubusercontent.com/89664911/176253741-0bc511cb-e82d-427f-8477-ed680cc920af.png">



<img width="1083" alt="Screen Shot 2022-06-28 at 9 57 53 AM" src="https://user-images.githubusercontent.com/89664911/176197873-02518757-4b43-4a2c-bceb-b318b85ffa8c.png"><img width="1074" alt="Screen Shot 2022-06-28 at 9 57 38 AM" src="https://user-images.githubusercontent.com/89664911/176197896-2e3532b6-371f-40d4-8038-e807bdb10389.png">

<img width="1055" alt="Screen Shot 2022-06-28 at 9 59 45 AM" src="https://user-images.githubusercontent.com/89664911/176197860-bb8d7254-6fc1-4802-a0da-f6c8d96123d6.png">

# Conclusions


Comparing random Forest classifier,support Vector classifier,Logistic Regression, Desicion Tree and Gaussian Naive Bayes, Random forest classifier have the highest accuracy score on those datasets. And the predictor was able to predict the likelyhood of having these disease based on the trained model.


# Future work

In the future I am planning to add more similar datasets to broaden the work. And Eventhough streamlite makes it easy to build the web app , it sometimes stop working so it is not reliable. So in the future I am planning to use other open source app framework in python to build the webapp.


# How to reproduce results

The cleanData notebook contains how to clean and train the datasets and then using the Heart Diasease predictor and Diabetes predictor notebook one can reproduce results.

# Citation

1.https://docs.streamlit.io/library/get-started/create-an-app

2.https://www.geeksforgeeks.org/machine-learning-with-python/











