# D&G Test Assignemnt

Python - Selenium Libraries are used to automate tests, pytest framework used to encapsulate python scripts and further caipaibility of running selective test, assertions and generating html reports.

# Minimum requirement

1. Python Versions/2.7 or Versions/3.0 or any higher latest version

2. pytest installation (use command : pip install pytest (on python 2.7) or pip3 install pytest (on python 3))

3. Selenium library installation (use command : pip install selenium (on python 2.7) or pip3 install selenium (on python 3))



# Usage

After python, pytest and selenium library installation download package from github and run tests as per below.

Navigate to folder where you have dowloaded tests and open terminal and use commands to run tests.

1. Run all tests -
       pytest test_run.py <enter>

2. Run specific test -
      pytest dry_run.py -m test_1 <enter>

3. Generate html report for executed tests -
      pytest -v -s --html=DG_Test_Assignment.html --self-contained-html test_run.py <enter>
      Note: Install pytest-html library using pip install pytest-html
       
       
Note: Test repo has Chrome driver for Mac to get the same test running on through Windows machine needs Windows supported Chrome driver exe downloaded from https://www.selenium.dev/downloads/ and kept in the floder where test scripts are downloaded.


Here is a description of Tests Automated:

1. TC_01_Product Search for Product - Cooker : Parameter passed for Product, Brand, guarantee and expected price

Checks performed: Product Name and Price validated on view basket page

2. TC_02_Product Search for Product - Fridge Freezer : Parameter passed for Product, Brand, guarantee and expected price

Checks performed: Product Name and Price validated on view basket page

3. TC_03_Product Search for Product - Condenser Dryer : Parameter passed for Product, Brand, guarantee and expected price

Checks performed: Product Name and Price validated on view basket page

4. TC_04_Product Search for Product - Combination Boiler : Parameter passed for Product, Brand, guarantee and expected price

Checks performed: Product Name and Price validated on view basket page

Working condition, Price range and date are hard code in test as of now however same can be made dynamic and referred from data provider dictionary.

Test Framework has seperate "helper.py" file for web element locators, navigation and validation through functions and already parameterised hence no change in code required for adding additional tests (except sub-category specific products (i.e. cooking and boiler)), any additional data combination specific test can be added by just adding data and test in file "test_run.py"

Please note If conditions for sub-catageory specific products : Cooking and Boiler also need to be updated in helper.py to cover sub-category flow condition for these products.

# Documentation

Refer Folder : src/test
Test file: test_run.py
Report/Logs: console log and DG_Test_Assignment.html


Test Run Console Log :

=========================================================================================== test session starts ============================================================================================
platform darwin -- Python 3.8.5, pytest-6.0.1, py-1.9.0, pluggy-0.13.1 -- /Library/Frameworks/Python.framework/Versions/3.8/bin/python3.8
cachedir: .pytest_cache
metadata: {'Python': '3.8.5', 'Platform': 'macOS-10.15.6-x86_64-i386-64bit', 'Packages': {'pytest': '6.0.1', 'py': '1.9.0', 'pluggy': '0.13.1'}, 'Plugins': {'metadata': '1.10.0', 'html': '2.1.1'}}
rootdir: /Users/rudrakshawasthy/Documents/Selenium_Tests/DG_test assignment
plugins: metadata-1.10.0, html-2.1.1
collected 4 items                                                                                                                                                                                          

test_run.py::test_tc01_search_product

************ Test Run **************
Test Validation Successfull
Searched Customer Product :Beko Cooker matched
Selected Product Price :£7.50 matched
PASSED
test_run.py::test_tc02_search_product

************ Test Run **************
Test Validation Successfull
Searched Customer Product :Bush Fridge Freezer matched
Selected Product Price :£3.39 matched
PASSED
test_run.py::test_tc03_search_product

************ Test Run **************
Test Validation Successfull
Searched Customer Product :Bosch Condenser Dryer matched
Selected Product Price :£7.50 matched
PASSED
test_run.py::test_tc04_search_product

************ Test Run **************
Test Validation Successfull
Searched Customer Product :Baxi Combination Boiler matched
Selected Product Price :£17.50 matched
PASSED

------------------------------------------ generated html file: file:///Users/rudrakshawasthy/Documents/Selenium_Tests/DG_test assignment/DG_Test_Assignment.html ------------------------------------------
================================================================================ 4 passed in 141.98s (0:02:21) =================================================================================

# Help

Send your questions to the
- [rudraksh awasthy - rudraksh_awasthy@yahoo.com]

Refer standard pytest framework documentation 	
- [https://docs.pytest.org/en/3.0.1/contents.html]
