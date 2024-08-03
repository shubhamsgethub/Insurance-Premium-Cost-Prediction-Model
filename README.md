# Insurance-Premium-Cost-Prediction-Model
This is a StreamLit application which takes Age and your health conditions as its input, and provides the price of Health Insurance Premium

**insurance.csv** contains the dataset of insurance premium prices records. There are 986 rows and 11 columns : [['Age', 'Diabetes', 'BloodPressureProblems', 'AnyTransplants','AnyChronicDiseases', 'Height', 'Weight', 'KnownAllergies','HistoryOfCancerInFamily', 'NumberOfMajorSurgeries', 'PremiumPrice']]

**insurance_cost_prediction.ipynb** contains detailed exploratory analysis of the data as well as hypothesis testing which tests the dependency of the premium price on various health factors. It also includes the training details of the model. Load it into Jupyter Notebook/Google Colab and upload the 'insurance.csv' file to run all the code again.

**classifier.pkl** contains the saved model after training had been completed. Load this in conjunction with the InsurancePremiumPredictorApp

**InsurancePremiumPricePredictorApp** contains a python file which is a StreamLit app in which the user can enter their age and details of health conditions, and it provides the Insurance premium price as output. Load the classifier.pkl file before running this.
