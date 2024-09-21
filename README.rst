# README

## Project Goal

The goal of this project is to predict employee turnover and identify the key factors that influence employees leaving a company. By understanding which variables play the biggest role in turnover, I aim to provide actionable insights that can help improve employee retention. The project specifically looks into features like employee satisfaction, performance evaluations, tenure, and workload, all of which can impact the likelihood of an employee leaving.

## Project Setup

For this project, I used Python along with libraries like **pandas**, **numpy**, **scikit-learn**, and **seaborn**. The dataset consists of around 12,000 records, capturing various attributes related to employee behavior. To address class imbalance between employees who stayed and those who left, I applied upsampling techniques to improve model accuracy. The analysis was conducted in Jupyter Notebook, with cross-validation used to evaluate model performance.

## Analysis Applied

The analysis involved building a Logistic Regression model to predict turnover. I started with an exploration of feature correlations using a heatmap, which showed that employee satisfaction was the most critical factor. I then implemented logistic regression, handling the class imbalance with upsampling to ensure the model was better at identifying employees likely to leave. Metrics like precision, recall, and F1-score were used to assess model performance, especially after applying the class-balancing techniques.

## Results Found

The most important insight from the analysis was that **satisfaction level** was by far the strongest predictor of whether an employee would leave, with a negative correlation. After balancing the data, the model’s ability to predict employee turnover improved significantly, with an F1-score increasing from 0.34 to 0.79. This showed that the model became more reliable in identifying employees at risk of leaving, while still performing well for employees likely to stay.

## Conclusion

In conclusion, improving employee satisfaction should be the top priority for reducing turnover. The Logistic Regression model, particularly after addressing class imbalance, proved to be an effective tool for predicting which employees are likely to leave. These insights provide a foundation for creating targeted employee retention strategies.
