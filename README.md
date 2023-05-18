# Assessment

This test assessment was prepared for . 

## Project Structure
Assessment project is built across multiple folders: 
- features: All the .feature files (Gherkin files/BDD Files) are present inside this folder. Also, webdriver_fixture.py is present here which is used for fixtures and much more.
- features/steps: All the step definitions are present inside this folder. file name should match the feature file name.
- pages: I have followed Page Object Model. So all webelements and the functions/methods to interact with them (get/set) are grouped here inside python files for each of the web page. 

## Setup & Installations
##### Python
Python can be downloaded from Download Python [link](https://www.python.org/downloads/).

##### Chrome WebDriver
Chrome WebDriver can be downloaded from this [link](https://chromedriver.chromium.org/downloads).

####  Allure tool
Allure is a tool for hosting test reports. Allure zip can be downloaded from this [link](https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.22.0/).
The path for allure.bat should be added to system path variable so that we can run allure command from any path.

##### Dependencies & Installation
This Python based Test Automation project has the following python dependencies:
- [Selenium] (https://pypi.org/project/selenium/)
- [behave] (https://behave.readthedocs.io/en/latest/)
- [allure-behave](https://docs.qameta.io/allure/)
- [requests](https://pypi.org/project/requests/)

They all are written in file requirement.txt. When user will open this file in any modern Python IDE such as PyCharm Community Edition, IDE will suggest downloading these dependencies and will download itself.
User can run following commands inside Terminal/command prompt to install these python dependencies:

```sh
$  pip install requirements.txt 
```
or install them individually:
```sh
$ pip install selenium 
$ pip install allure-behave
$ pip install behave
$ pip install requests
```

## Execution
Path of the downloaded Chrome WebDriver exe file should be updated in webdriver_fixtures.py. After that project is ready for execution.

##### Way 1 using Terminal (cli)
In terminal, go to the path of root folder using command cd <path>. Afterwards you can run following command:
It will run all the feature files under features folder.
```sh
$ behave -f allure_behave.formatter:AllureFormatter -o allure-results features 
```

##### Way 2 using python file
I have created a python file features_runner.py which can be run as simple python file. It will also execute features files in the path specified inside the file. It's a way around to use terminal and running behave command. I can also configure any CLI parameters in this file.

##### How to maintain multiple runs
We are using allure-behave for running the test and generation of presentable test HTML report.Each time we run our test,test results will be stored inside allure-results folder in JSON format.
This way multiple test results can be maintained.For this project we don't want to store all the results on GitHub that's why we have excluded the JSON files in .gitignore.

##### How to host allure reports on web page
All our test results are stored in allure-results folder. We can generate HTML report by running following command :

```sh
$ allure serve <path to allure-results folder>
```
![Sample test report](test-result.jpg)