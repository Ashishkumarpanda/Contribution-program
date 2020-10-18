# Deploy-ML-model-using-Flask
## About Application 
This is a salary predicting machine learning  project deployed using  Flask.It predicts the salary on the basis of the 3 inputs ( experience , test score and interview score )
After our model is built, we will be saving our trained model using a library called pickle.Python pickle module is used for serializing and de-serializing a Python object structure. Any object in Python can be pickled so that it can be saved on disk. What pickle does is that it “serializes” the object first before writing it to file. 
## Algorithm used 
I have build a simple regression model using scikit-learn’s built-in LinearRegression() function.
## Prerequisites
You must have Scikit Learn, Pandas (for Machine Leraning Model) and Flask (for API) installed.
## Dataset used
This is the [dataset](https://github.com/akrish4/Contribution-program/blob/master/ML_models_Flask/Ananthakrishnan%20Nair%20RS/hiring.csv) used.
It’s a very simple data set with 4 attributes and 8 rows. All the columns are numerical columns and this data used here is clean and is ready to be applied for a classifier.
## Project Structure
This project has four major parts :
1. model.py - This contains code fot our Machine Learning model to predict employee salaries based on trainign data in 'hiring.csv' file.
2. app.py - This contains Flask APIs that receives employee details through GUI or API calls, computes the precited value based on our model and returns it.
3. template - This folder contains the HTML template (index.html) to allow user to enter employee detail and displays the predicted employee salary.
4. static - This folder contains the css folder with style.css file which has the styling required for out index.html file.

## Running the project
1. Ensure that you are in the project home directory. Create the machine learning model by running below command from command prompt -
```
python model.py
```
This would create a serialized version of our model into a file model.pkl

2. Run app.py using below command to start Flask API
```
python app.py
```
By default, flask will run on port 5000.

3. Navigate to URL http://127.0.0.1:5000/ (or) http://localhost:5000

You should be able to view the homepage.

Enter valid numerical values in all 3 input boxes and hit Predict.

If everything goes well, you should  be able to see the predcited salary vaule on the HTML page!
check the output here: http://127.0.0.1:5000/predict
<br>
<br>
![output](https://github.com/akrish4/Deploy-ML-model-using-flask/blob/main/1.png)
<br>
 output
 <br>
![output](https://github.com/akrish4/Deploy-ML-model-using-flask/blob/main/2.png)
