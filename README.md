# Student Performance Indicator End-to-End CD ML Project

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-1.1.2-green.svg)](https://flask.palletsprojects.com/)
[![AWS](https://img.shields.io/badge/AWS-Elastic%20Beanstalk-orange.svg)](https://aws.amazon.com/elasticbeanstalk/)

## Project Overview
This project aims to predict student performance using machine learning techniques. By analyzing various parameters, the model helps in identifying factors that contribute to student success or struggles, providing valuable insights for educators and institutions.

## Architecture
The architecture of the project is divided into several components:
- **src/**: Contains the source code for the application.
- **components/**: Holds reusable components for the application.
- **Templates/**: Stores HTML templates for rendering the web application.

## Installation Instructions
To get started with this project, follow these steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/sanjayravichander/Student-Performance-Indicator-End-to-End-CD-ML-Project.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Student-Performance-Indicator-End-to-End-CD-ML-Project
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Technology Stack
- **Backend**: Flask
- **Programming Language**: Python
- **Machine Learning Libraries**: scikit-learn, CatBoost, etc.

## Model Performance Metrics
The performance of the model is evaluated using various metrics such as:
- Accuracy
- Precision
- Recall
- F1 Score

## AWS Deployment Setup
To deploy this project on AWS Elastic Beanstalk, create a `.ebextensions` directory in the root of your project and include configuration files to set up the environment.

## Usage Examples
After setting up the project, you can run the application using:
```bash
flask run
```
You can then access the application at `http://127.0.0.1:5000`.

## Project Structure
The project directory structure is as follows:
```
Student-Performance-Indicator-End-to-End-CD-ML-Project/
│
├── artifacts/
├── catboost_info/
├── notebook/
├── src/
│   ├── components/
│   └── templates/
└── requirements.txt
```

## Contact Information
For inquiries, you can reach out to **sanjayravichander** at [GitHub](https://github.com/sanjayravichander).