## Task 1
[File](https://github.com/IlyaKusakin/FiveTasks/blob/main/Task1_product%20analysis.pdf) with product analysis.
## Task 2
[Notebook](https://github.com/IlyaKusakin/FiveTasks/blob/main/task2/Task2_classification.ipynb) with classification research. 
[File](https://github.com/IlyaKusakin/FiveTasks/blob/main/task2/task2_result.xlsx) with predicted labels for test dataset.
![](https://github.com/IlyaKusakin/FiveTasks/blob/main/Task5/images/ROC_curve.jpg)
## Task 3
[Notebook](https://github.com/IlyaKusakin/FiveTasks/blob/main/Task3_regression.ipynb) with regression research.
![](https://github.com/IlyaKusakin/FiveTasks/blob/main/Task5/images/log_target.jpg)
## Task 4
[Notebook](https://github.com/IlyaKusakin/FiveTasks/blob/main/Task4_segmentation.ipynb) with group segmentation and clusters analysis
![](https://github.com/IlyaKusakin/FiveTasks/blob/main/Task5/images/groups.jpg)
## Task 5
Flask [application](https://github.com/IlyaKusakin/FiveTasks/tree/main/Task5) for probability predicting.

Necessary input fields for classifier:
* "age"
* "job"
* "month"
* "nr.employed"

### Run to install all necessary libraries
```
pip install -r requirements.txt
```
### Run to test util functions
```
pytest function_tests.py
```
![](https://github.com/IlyaKusakin/FiveTasks/blob/main/Task5/images/tests_screen.jpg)
### Run to start application
```
python app.py
```
### Input cases with outputs
Case1: normal input 
```
input
{
 "age": 40, 
 "month": "mar", 
 "job": "student", 
 "nr.employed": 5000
}

output 
{
    "error_code": null,
    "proba": 0.71,
    "status": 200
}
```
Case2: missed necessary "month" field
```
input
{
"age": 40, 
"job": "student", 
"nr.employed": 5000
}

output
{
    "error_code": "incorrect fields",
    "proba": null,
    "status": 401
}
```
Case3: incorrect type of "age"
```
input
{
"age": "twenty",
"month": "mar", 
 job": "student",
 "nr.employed": 5000
 }
 
output
{
    "error_code": "incorrect format",
    "proba": null,
    "status": 402
}
```
