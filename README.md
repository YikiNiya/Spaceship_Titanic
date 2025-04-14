# Spaceship Titanic Analysis

## Objective

This project aims to predict whether passengers aboard the Spaceship Titanic were transported to another dimension during a galactic anomaly, based on various behavioral, demographic, and activity-related features.

## Analysis

### Key Steps:

1. Exploratory Data Analysis (EDA) and Statistical Analysis Overview:
- Explored the dataset and identified relationships between features.
- Found that features related to on-board spending and activity usage (e.g., RoomService, FoodCourt, Spa, VRDeck) were strong predictors of whether a passenger was transported.
- Traditional demographic features like VIP, CryoSleep, and HomePlanet were less impactful in predicting transport status.

2. Data Preprocessing:
- Handled missing values using group-wise and median imputation.
- Encoded categorical variables using one-hot encoding.
- Engineered new features such as ServiceCount, the total of all service spending categories.
- Cleaned and transformed data to ensure readiness for model training.

3. Building Pipeline and Machine Learning Models Applied:
- Random Forest
- XGBoost
- Logistic Regression
- LightGBM
- CatBoost
- Ensemble Method: Soft Voting Classifier (combining multiple models for better performance)

4. Model Evaluation & Selection:
- The CatBoost model achieved the highest validation accuracy of 81.9%.
- The Soft Voting Ensemble model, combining CatBoost, XGBoost, and Logistic Regression, achieved a validation accuracy of 79.6% and a cross-validation accuracy of 80.8%, with improved generalization and reduced overfitting.
- Performance Metrics:
  - Test Accuracy: 82.58%
  - Balanced Classification Metrics across both transported and non-transported classes.

5. Model Interpretability:
- Used SHAP (SHapley Additive Explanations) to gain insights into the model's decision-making process.
- Key influential features: Spa, VRDeck, and ServiceCount.
- Demographic features like VIP and CryoSleep had lower predictive importance.

### Key Findings:

- CatBoost was the top-performing model, achieving the highest accuracy and generalization ability on the test set.
- The Soft Voting Ensemble model provided a good balance between model accuracy and generalization, reducing overfitting seen in individual models like Random Forest and XGBoost.
- Service-related features such as Spa, VRDeck, and ServiceCount were found to be the most influential in predicting whether a passenger was transported, reflecting the importance of passenger engagement and activity onboard.

## Future Enhancements

- Feature Engineering: Adding group-level or interaction features, or considering more advanced spending ratio features, could improve model performance.
- Advanced Ensembling: Exploring stacking or blending techniques could enhance model performance by leveraging complementary strengths of different algorithms.
- Extended Hyperparameter Tuning: Further fine-tuning of hyperparameters using Optuna could yield even better performance, especially for high-variance models like XGBoost and LightGBM.

## How to Run the Analysis

1. Requirements: Install necessary Python libraries which are in a file called requirements.txt
   ```bash
   pip install -r requirements.txt

2. Running the Notebook: Open the Jupyter Notebook file (spaceship_titanic_analysis.ipynb) and run the cells to perform the analysis.