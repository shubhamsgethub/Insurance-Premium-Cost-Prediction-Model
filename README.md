# Insurance-Premium-Cost-Prediction-Model
This is a StreamLit application which takes Age and your health conditions as its input, and provides the price of Health Insurance Premium

**Problem Statement**
Insurance companies need to accurately predict the cost of health insurance for individuals to set premiums appropriately. However, traditional methods of cost prediction often rely on broad actuarial tables and historical averages, which may not account for the nuanced differences among individuals. By leveraging machine learning techniques, insurers can predict more accurately the insurance costs tailored to individual profiles, leading to more competitive pricing and better risk management.


**insurance.csv** contains the dataset of insurance premium prices records. There are 986 rows and 11 columns : [['Age', 'Diabetes', 'BloodPressureProblems', 'AnyTransplants','AnyChronicDiseases', 'Height', 'Weight', 'KnownAllergies','HistoryOfCancerInFamily', 'NumberOfMajorSurgeries', 'PremiumPrice']]

**insurance_cost_prediction.ipynb** contains detailed exploratory analysis of the data as well as hypothesis testing which tests the dependency of the premium price on various health factors. It also includes the training details of the model. Load it into Jupyter Notebook/Google Colab and upload the 'insurance.csv' file to run all the code again. 

The exploratory data analysis comprises of checking the distribution all of the consumer traits including height, weight, age and all their health conditions. Then we proceed with a correlation matrix showing the correlations between all these features. All the insights from these visualisations are noted in the comments that follow in the notebook itself.

After the exploratory analysis, we proceed with hypothesis testing where we have used tests like t-test, ANOVA and pearson correlation test to test hypotheses about the dependency of premium price on the various features. All the recommendations for the insurance company follow afterwards.

The notebook then proceeds with the model building process where we have utilised both grid search and random search for model parameters, in order to select the best model. The models tested are GradientBoostingRegressor, RandomForest, and MLP, out of which Random Forest has the best MAPE of 0.03 and the best R2_score of 0.9. These metrics have been chosen for their scale independency over something like RMSE, which may be non-interpretable here.

We then proceed to save our best performing model into a file named 'classifier.pkl'

**classifier.pkl** contains the saved model after training had been completed. Load this in conjunction with the InsurancePremiumPredictorApp

**InsurancePremiumPricePredictorApp** contains a python file which is a StreamLit app in which the user can enter their age and details of health conditions, and it provides the Insurance premium price as output. Load the classifier.pkl file before running this. It first takes 10 integers as input which go to a function called "predictor", where we feature engineer 6 more features, all of which are then fed to the saved RandomForestRegressor from the .ipynb notebook.
