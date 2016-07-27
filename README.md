linear-regression-python
=============
A simple, basic implementation of linear regression in Python. The understanding of my implementation is explained quite well on this link - http://machinelearningmastery.com/linear-regression-tutorial-using-gradient-descent-for-machine-learning/

Feel free to suggest changes in the code if any. 

This was built in Python 3.4 and please refer to the pre-requistes required for running it successfully. 

Pre-requisites - 
-------
1. Python 3.4 (although it shoudn't have problem running on other Python versions apart from syntactical changes.)
2. csv library - Download it here - https://pypi.python.org/pypi/csv

Usage - 
-------
1. Save the script in your python folder. 
2. Open IDLE or cmd to run python.
3. Run the following code - 
```python
import os
os.chdir('path') #path where script is saved

from linregression import LinearRegression
LinearRegression().main() 
```
```code
Enter filename: aps.csv
Scaling required? Y/N: Y
Total Rows: 508
Coeffecient Matrix: [1.4628658990706878, 0.0, 0.0, 0.0, 0.0, 0.0, 0.005309464301270166, 0.015928392903810498, 0.0, 0.03716625010889116, 0.0]
Enter values separated by , :
3,2,1,1,0,0,1,0,7,0
Predicted value: 0.9309331355738595
```
Dataset - 
-------
The dataset aps.csv has been taken from - https://www.umass.edu/statdata/statdata/data/ 
I have removed some fields and have made some changes in delimiter. You can read about the dataset - https://www.umass.edu/statdata/statdata/data/aps.pdf
