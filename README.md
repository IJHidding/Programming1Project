# Programming1Project

### Prerequisites
A python interpreter is required for running this program. Access to pip3 is recommend for ease of installing the 
required packages.

Python packages required for running:
- pandas
- sklearn
- bokeh

Install by running

`pip3 install -r requirements.txt` 

### Installing
To install this program simply clone or download this repository. If downloaded unpack it at the desired location.

### Running
This program can be run from the command line or from within any Python IDE. Running it from the command line gives the 
option to select desired provinces. By default all twelve Dutch provinces are selected. When run the analysis is 
performed and the result will be loaded in the default browser as an image. 
The PCA plot is interactive and has tools for zooming in and out. 

To run use any of these commands:

Default all provinces:
`python main.py`

Select province by adding the name of the province after -p:
`python main.py -p Groningen Friesland`


### Design choices
For this analysis of the data it was chosen to try and combine all factors potentially influencing age death. Then a
PCA was performed to identify groups and regression was performed to see which of the found 
factors had the highest influence on deaths. The data was designed starting with the number of deaths. This was taken
for both genders combined. The number of deaths was divided by the population of that province and then multiplied 
by 100.000 to get the average deaths per 100.000 people in that province. This is done to normalize the data for the 
number of people per province. Then the population data per age in percentage is merged into the same age groups as the 
deaths data is. Afterwards data that is the same for each age group is added behind each column per province. 
After this is done for every province selected the data frames are concatenated on top of each other.

This data frame is passed to the PCA. Here all features (column names) are taken from the dataset to serve as the 
features for the analysis. The Province names are removed as the are not part of the analysis and the number of deaths
is removed as well. These two factors are added as colors to the PCA plot to show how the other factors are grouped 
without these factors. 

The same factors are used for the regression. Here provinces are ignored and all data is used to detect the influence of 
each factor on the relative number of deaths. 

The plots are combined by setting a large PCA plot on the left and a smaller regression horizontal bar plot on the right.
Below this a text box is added in the empty space with information about the selected provinces and the fragment of 
variance explained by both principal components. The text is made by making an empty Bokeh plot and adding a label on 
top of it that covers the whole plot.

It is possible that I have over analysed the data and that this data format does not lend itself well 
to this type of analysis although I'm not sure as this is the first PCA and regression I have done.  


#### Design pattern
The design pattern used is a version of the abstract factory. Many objects in this program have a similar structure and 
output similar data frames. An abstract version of the parsers, visualizers and processors is made. Which is then used 
as a basis for the main functions. This was all output is compatible data frames. Or plots in case of the visualizers.


#### Unit tests
The most important unit tests run are the online test, which indicate if the online source has been changed. And the csv parser,
this tests if the coding for the provinces is the same. An additional check is done on the single rowed data. If all three pass 
the data is the same and the analysis will run properly. 

Unit tests can be run using the command: `python Unittest.py`
It will run three tests and as long as these come out fine the program should work. 

### Disclaimer & Copyright
Copyright 2020 Iwan Hidding

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

### Author and version

Author: Iwan Hidding

Version: 1.0,  Released: 9/feb/2020

### Additional mentioned
Code for the abstract factory design pattern was adapted from the NOB sleep app and 
from the [refactoring.guru](https://refactoring.guru/design-patterns/abstract-factory) website.

Code for the PCA analysis was adapted from the 
[towards data science website](https://towardsdatascience.com/pca-using-python-scikit-learn-e653f8989e60).


