# eusa2excel
### note : wrote this document in a hurry, will be updating it with  a better guidefor installation soon.
###  If you are from University of Edinburgh, drop me an email and I can help you set it up.

Currently, if you are a committee member for any EUSA society, you will realize that you have to manually transfer every registered member or paid member into an excel file from the EUSA web page.
This bot will help you do that instantly. It will transfer the name and student ID from the webpage to a csv file.

## Procedure
### Step 1
Make sure you have python installed on your computer.
1.Install selenium.
 [https://selenium-python.readthedocs.io/installation.html](https://selenium-python.readthedocs.io/installation.html)(Only from 1.1 to 1.4)
 2.Install the web driver using the above link for your browser of choice,
 You have to install it in the PATH. 
 If you are from University of Edinburgh, drop me an email and I can help you set it up.
 **Chrome**:

[https://sites.google.com/a/chromium.org/chromedriver/downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads)

**Edge**:

[https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

**Firefox**:

[https://github.com/mozilla/geckodriver/releases](https://github.com/mozilla/geckodriver/releases)

**Safari**:

[https://webkit.org/blog/6900/webdriver-support-in-safari-10/](https://webkit.org/blog/6900/webdriver-support-in-safari-10/)
3. Download "index.py" from above.
### Step 2
Open index.py in IDLE and change the "YOUR-CODE-HERE" to the code from the web page of your society in EUSA website. Change the student ID and password to your own.
### Step 3 
Run the file and it should do everything automatically.

