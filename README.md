<img width="305" alt="Screen Shot 2022-06-23 at 9 47 05 AM" src="https://user-images.githubusercontent.com/89664911/175315233-f8cc17a8-18c6-4454-b42d-07a07184e1a8.png">

# Prediction of Diseases using machine learning algorithms

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
<img width="1196" alt="Screen Shot 2022-06-23 at 7 47 18 PM" src="https://user-images.githubusercontent.com/89664911/175433046-0159f8c8-8188-4b92-8d6a-49fa32dadcd5.png">

<img width="761" alt="Screen Shot 2022-06-26 at 2 30 43 AM" src="https://user-images.githubusercontent.com/89664911/176094039-bacedce0-6b74-48fc-bc59-b356de4844ef.png">
<img width="741" alt="Screen Shot 2022-06-26 at 2 31 01 AM" src="https://user-images.githubusercontent.com/89664911/176094055-cef6a137-a0ef-4270-8bd1-489000d86a61.png">



<img width="777" alt="Screen Shot 2022-06-26 at 2 35 26 AM" src="https://user-images.githubusercontent.com/89664911/176094087-faebce35-f1ad-4c3e-bbd2-cd1d1aef2333.png">


<img width="765" alt="Screen Shot 2022-06-26 at 2 35 38 AM" src="https://user-images.githubusercontent.com/89664911/176094101-6e04f131-8bf5-4198-a480-c147f9fb2787.png">



<img width="777" alt="Screen Shot 2022-06-26 at 2 32 19 AM" src="https://user-images.githubusercontent.com/89664911/176094174-e59c4a87-332f-4b3d-9a47-b099bdc4107b.png">
<img width="765" alt="Screen Shot 2022-06-26 at 2 35 38 AM" src="https://user-images.githubusercontent.com/89664911/176094175-5abd7ead-1879-433a-a8ee-82fd3c70c826.png">
<img width="777" alt="Screen Shot 2022-06-26 at 2 35 26 AM" src="https://user-images.githubusercontent.com/89664911/176094176-56c5d15b-82cd-434f-a4e3-e6311408e109.png">
<img width="898" alt="Screen Shot 2022-06-28 at 9 39 40 AM" src="https://user-images.githubusercontent.com/89664911/176193367-208f233f-e4da-4ac0-a288-065c68a47c7a.png">

<img width="939" alt="Screen Shot 2022-06-28 at 9 39 54 AM" src="https://user-images.githubusercontent.com/89664911/176193395-830b0d32-769e-468a-a313-806843c4b3ac.png">




