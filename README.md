# Student Exam Performance Indicator

## Overview
This project aims to predict a student's math score based on various factors such as Gender, Race or Ethnicity, Parental Level of Education, Lunch Type, and Test Preparation Course. The prediction is done using a machine learning model trained on a dataset containing historical student data.


https://github.com/Anujdh8755/Student_performance_indicator/assets/114329073/e648aee5-85b0-47c6-a228-5028740ccda5



## Installation
1. Clone the repository to your local machine.
💿 Installing
1. Environment setup.
```
conda create --prefix venv python==3.8 -y
```
```
conda activate venv/
````
2. Install Requirements and setup
```
pip install -r requirements.txt
```
5. Run Application
```
python app.py
```

🔧 Built with
- flask
- Python 3.8
- Machine learning
- Scikit learn

## Usage
1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Run the Flask application using the following command:

4. The application should now be running locally at `http://localhost:5000`.
5. Access the application in your web browser.

## How to Use
1. Fill out the form on the web page with the required information:
- Select your Gender (Male/Female).
- Select your Race or Ethnicity (Group A, Group B, Group C, Group D, Group E).
- Select your Parental Level of Education.
- Select your Lunch Type (Free/Reduced or Standard).
- Select whether you have completed a Test Preparation Course (Yes/No).
- Enter your Writing Score out of 100.
- Enter your Reading Score out of 100.
2. Click on the "Predict your Math Score" button to see the predicted math score based on the provided information.

## Data
The dataset used for training the prediction model is not included in this repository. The 'data.csv' file should contain the following columns:
- Gender
- Race or Ethnicity
- Parental Level of Education
- Lunch
- Test Preparation Course
- Math Score (target variable)
- Reading Score
- Writing Score

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- The dataset used in this project is from [Kaggle](https://www.kaggle.com/spscientist/students-performance-in-exams).

