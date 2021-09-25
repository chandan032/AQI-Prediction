# AQI Prediction
Django based webapp to predict the Air Quality Index of a region using climatic conditions






1. **Data Collection**: (execute main-aqi.py)\
For this step, I have written a web scrapper that scraps en.tutiempo.net for climate data from 2013 to 2015 and creates a HTML file for each month.
2. **Data Preprocessing**: (execute main-aqi.py)\
For this step, I have taken the data from Krish Naik's project as it was from a paid API.\
Reference: https://github.com/krishnaik06/AQI-Project/tree/master/Data/AQI. \
This data contained hourly measurements of AQI.\
This was converted into a dictionary format where the dictionary key is the year and values are the daily AQI values. \
Next, the data in step 1 was combined with data of this step to create a new CSV file.
3. **Data Cleaning**: (execute main-aqi.py)\
The CSV file created in step 2 was cleaned to remove null values and improper data. A new resultant CSV file was created.
4. **Feature Engineering and Model Creation**: (execute individual jupyter notebooks)\
Tried various algorithms, like Linear Regression, Lasso and Ridge Regression, Decision Tree Regressor, KNN Regressor, Random Forest Regressor, XGBoost Regressor.\
Random Forest and XGBoost gave best performance. Finally, used XGBoost to perform predictions.
5. **Model Deployment**: Navigate to aqi folder and run the command for running it locally decribed below.


## Installation 📦

>pip install -r requirements.txt



#### Run server locally

```shell
$ python manage.py runserver
```
> Go to localhost:8000

---









