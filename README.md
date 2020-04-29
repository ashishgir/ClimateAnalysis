# ClimateAnalysis
In this project we have analysed Climate Change: Earth Surface Temperature dataset using MapReduce , Hive, Spark and BigQuery in Google Cloud Platform(GCP).

# Abstract
Climate science as a data-intensive subject has affected by the era of big data and relevant technological revolutions, such as big data solutions and data analytics. The successes of big data analytics in diverse areas over the past decade have prompted the expectation of big data and its efficacy on the big problem, i.e., —climate change. However, big data analytics encountered more challenges in climate science than other subjects regardless of the extensive resources of climate data.. As an emerging topic, climate change has been at the forefront of the climate data analytics, and exhaustive research have been carried out covering a variety of topics. It is also expected to serve as a one-stop reference directory for researchers and stakeholders with an overview of this trending subject at a glance, which can be useful in guiding future research and improvements in the exploitation of big climate data. Data mining for climate change delivers rich understanding of climate-related big data techniques and highlights how to navigate huge amount of climate data and resources. It guides future directions and will boom data-driven researches on modeling, diagnosing and predicting climate change and mitigating related impacts. As part of the Administration's Climate Data Initiative, provides access to Federal resources to help America’s communities, businesses, and citizens plan and prepare for climate change. For climate scientists, the utility of big data is not a new approach, and machine learning has seen the use of modeling the global climate system. However, big data techniques are still emerging in the socioeconomic aspects of climate research. In this project big data system will be employed for quantitative climate-conflict research by using Google Cloud Platform to upload the Data sets along with BigQuery for cost-effective and fast analysis of big data and visualizing BigQuery using Data Studio tool. We mainly focused on these problem statements, such as Map of temperatures and analysis of global warming, How does climate change affect different places?, Visualizations of temperature change and Temperature & Impact on Snowfall by applying MapReduce model, Spark, Hive and BigQuery to come up with the best result.

# Dataset
Some say climate change is the biggest threat of our age while others say it’s a myth based on dodgy science. We are turning some of the data over to you so you can form your own view. In this dataset, we have include several files:

Global Land and Ocean-and-Land Temperatures (GlobalTemperatures.csv):

Date: starts in 1750 for average land temperature and 1850 for max and min land temperatures and global ocean and land temperatures <br>
LandAverageTemperature: global average land temperature in celsius <br>
LandAverageTemperatureUncertainty: the 95% confidence interval around the average <br>
LandMaxTemperature: global average maximum land temperature in celsius <br>
LandMaxTemperatureUncertainty: the 95% confidence interval around the maximum land temperature <br>
LandMinTemperature: global average minimum land temperature in celsius <br>
LandMinTemperatureUncertainty: the 95% confidence interval around the minimum land temperature <br>
LandAndOceanAverageTemperature: global average land and ocean temperature in celsius <br>
LandAndOceanAverageTemperatureUncertainty: the 95% confidence interval around the global average land and ocean temperature <br>
Other files include:

Global Average Land Temperature by Country (GlobalLandTemperaturesByCountry.csv) <br>
Global Average Land Temperature by State (GlobalLandTemperaturesByState.csv) <br>
Global Land Temperatures By Major City (GlobalLandTemperaturesByMajorCity.csv) <br>
Global Land Temperatures By City (GlobalLandTemperaturesByCity.csv) <br>
The raw data comes from the Berkeley Earth data page. <br>

<img src="https://github.com/ashishgir/ClimateAnalysis/blob/master/Capture.PNG"> <br>

# Problem Statement
We mainly focused on these problem statements,

Analysis of global warming affect in different places using K-means Clustering technique to group similar data and classification that categorizes data objects into the predefined groups involving Social Network Analysis Technique <br>
<br>
Visualizations of temperature change by Mapping it on Dynamic Map in Jupyter, using "plotly" that shows changes in average temperature of countries with 10 years period <br>
<br>
# Social Network Analysis Technique
Big Data Social Network Analysis (BDSNA) is the focal computational and graphical study of powerful techniques that can be used to identify clusters, patterns, hidden structures, generate business intelligence, in social relationships within social networks in terms of network theory. This study applies various social network analysis and visualization tools to examine the structure and patterns of interdisciplinary collaborations, as well as the recently evolving overall pattern. Centering around a few important disciplines, all fields related to Big Data research are aggregated into communities, suggesting some related research areas, and directions for Big Data research. An ever-changing roster of related disciplines provides support, as illustrated by the evolving graph of communities.

# Load the data
BigQuerysupports the following data formats when loading data into tables: CSV, JSON, AVRO, or Cloud Datastore backups. Data can be loaded into BigQuery using a job or by streaming records individually. 
Load jobs support three data sources:<br>
•Objects inGoogle Cloud Storage<br>
•Data sent with the job orstreaming insert<br>
•Google Cloud Datastorebackup<br>

<br><img src="https://github.com/ashishgir/ClimateAnalysis/blob/master/Images/Storage1.PNG"> <br>

# BigQuery
BigQuery leverages a columnar storage format and compression algorithm to store data in Colossus in the most optimal way for reading large amounts of structured data. Colossus allows BigQuery users to scale to dozens of Petabytes in storage seamlessly, without paying the penalty of attaching much more expensive compute resources —typical with most traditional databases.

<br><img src="https://github.com/ashishgir/ClimateAnalysis/blob/master/Images/BigQuery1.PNG"> <br>

# Cloud Dataproc

Cloud Dataproc is a managed Spark and Hadoop service that lets you take advantage of open source data tools for batch processing, querying, streaming, and machine learning. Cloud Dataproc automation helps you create clusters quickly, manage them easily, and save money by turning clusters off when you don't need them. With less time and money spent on administration, you can focus on your jobs and your data.

# IMPLEMENTATION

# Mapreduce Programming
Analyzing a huge data sets is the method of big data which comprises a classes of data types. The big data maintain
a significant amount of data and process that data.  The most popular Big Data handling and processing technique is Hadoop Map-Reduce which is currently used. Map-Reduce is a technique which executes parallel and distributed algorithm across large data using number of
clusters. In the proposed system, Map-Reduce algorithm is used to calculate minimum and maximum temperature of a
particular city and Spatial Cumulative Sum(CUSUM) based algorithm is proposed to detect the changes in the climate
which produces the results in the form of graphs with temperature values. Map-Reduce is a process which will be work in three steps, namely map, shuffle, and reduce. The mapper's job is to process the input data in map stage. In Hadoop file system, the input data is in sort of file and is collected from various weather sites. And the reducer will take the output from the Map as an input and combined that data into a set of tuples. 

# Mapper Operation 
The mapping is a simple process in that the variables which matched certain will be sent to the reducer. It consider
mappers is acts like a distributed search capability and pull (key, value) pairs of a file. The input file format reader of
hadoop opens files and which starts to read file for (key, value) pairs. Once it determine (key, value) pair, it reads both
key and values which passes to the mapper and mapping operator which is used to filter out (key, value) pairs which
not match the criteria. Since mapper is not a part of Hadoop which read data. The mapper is collecting data from input
file format reader and input file format reader is modified to read sequenced files. This routine opens a file and
performs a simple loop to read each (key, value) within file. The desired key if filter matched, then values which are read into memory and passed to the mapper. If filter is not match, then values were skipped. In the mapper, null values
is to filter for calculation of a place, id is used as a key and combination of date and place is used as Key.

# Reduce Operation 
The resulting (key, value) pairs which matched the criteria is analyzed and forward to reducer with sequencing and
complete mapping process, Once a (key, value) object has created, a comparator is needed to order keys. If data is
combined, a group comparator is also needed. In a partitioner must be created in order to handle partitioning data into
groups of sorted keys.With all these components in place, Hadoop takes the (key, value) pairs which is created by using
mappers and group and sort them as specified way. Hadoop assumes that all values share a key will sent to same
reducer and a single operation over a large data set will employ on one reducer, This gives us result in number of output
files. 

# Map-Reduce Model
The Map-Reduce process which is executed for minimum and maximum operation on the National climatic data is
given as follows :
1. Weather data set files is inserted into sequence files on head node of Hadoop Distributed File System.
2. The sequence files which are loaded into Hadoop file system with replica factor three.
3. The job provides Map-Reduce operation which is submitted to head node to run. The head node schedules
with job tracker and on cluster jobs which is to be run. Hadoop distributes mappers to all data nodes which
contains data to analyze.
4. For reading the input format reader opens up each sequence file which passes all the (key, value) pairs to map
function on each node.
5. The mapper determines, if key matches the criteria for query. If mapper keeps (key, value) pairs for delivery to
the reducer. If not, The pair is discarded. The keys, values in a file are read and also analyze by using the
mapper.
6. The (key, value) pairs will match query are to sent to reducer and reducer performing the average function on
the sorted pairs to create final (key, value) pair results.
7. In a Hadoop Distributed File System as a sequence file, the final output is stored.

# Spark Programming

Analysis  for  the  same  dataset  using spark  query  was  so  much  easy  and  took  very  less  efforts  than  MapReduce  and  Hive. We  implemented  one  spark  query  with  mapper  and  reducer functions to find the count of the parameters occurred in one state. So, in this all the states are listed and thus we get to  know  the  count  of  it.  The  lambda  function  is  called  inside  the  mapper  function  to  map  the  parameter   count   of the respective  parameter  names  of  a  specific  state.  Later,  the  records   are   reduced   by   key   to   aggregate   all   the   similar   instances  to  get  the  count  of  occurrence  of  the  number  of  pollutants  in  a  state  required  for  analysis.  “SaveAsTextFile” command helps in saving the output of the spark program into a file called result1.

# Implementation using Colab

Google Colabcolab.research.google.com
Data science. With Colab you can harness the full power of popular Python libraries to analyze and visualize data.
<br>
Google Colaboratory is an online platform to perform data analysis. It enables you to create interactive Jupyter notebooks that mix text with Python code to run queries and display data analysis results. Stored on Google Drive you'll be able to run notebooks and collaborate with peers through Google's cloud services. As a programmer, you can perform the following using Google Colab.
-> Write and execute code in Python
-> Document your code that supports mathematical equations
-> Create/Upload/Share notebooks
-> Import/Save notebooks from/to Google Drive
-> Import/Publish notebooks from GitHub
-> Import external datasets e.g. from Kaggle
-> Integrate PyTorch, TensorFlow, Keras, OpenCV
-> Free Cloud service with free GPU

<br><img src="https://github.com/ashishgir/ClimateAnalysis/blob/master/Images/Colab1.PNG"> <br>
<br><img src="https://github.com/ashishgir/ClimateAnalysis/blob/master/Images/Colab2.PNG"> <br>
<br><img src="https://github.com/ashishgir/ClimateAnalysis/blob/master/Images/Colab3.PNG"> <br>
<br><img src="https://github.com/ashishgir/ClimateAnalysis/blob/master/Images/Colab4.PNG"> <br>
<br><img src="https://github.com/ashishgir/ClimateAnalysis/blob/master/Images/Colab5.PNG"> <br>
<br><img src="https://github.com/ashishgir/ClimateAnalysis/blob/master/Images/Colab6.PNG"> <br>
<br><img src="https://github.com/ashishgir/ClimateAnalysis/blob/master/Images/Colab7.PNG"> <br>
<br><img src="https://github.com/ashishgir/ClimateAnalysis/blob/master/Images/Colab8.PNG"> <br>
<br><img src="https://github.com/ashishgir/ClimateAnalysis/blob/master/Images/Colab9.PNG"> <br>

# Linear regression 
Linear regression  is a basic and commonly used type of predictive analysis.  The overall idea of regression is to examine two things: (1) does a set of predictor variables do a good job in predicting an outcome (dependent) variable?  (2) Which variables in particular are significant predictors of the outcome variable, and in what way do they–indicated by the magnitude and sign of the beta estimates–impact the outcome variable? There are multiple benefits of using regression analysis. They are as follows:
It indicates the significant relationships between dependent variable and independent variable.
It indicates the strength of impact of multiple independent variables on a dependent variable.
Regression analysis also allows us to compare the effects of variables measured on different scales, such as the effect of price changes and the number of promotional activities. These benefits help market researchers / data analysts / data scientists to eliminate and evaluate the best set of variables to be used for building predictive models.

# Visualization
Data visualization is another form of visual art that grabs our interest and keeps our eyes on the message. When we see a chart, we quickly see trends and outliers. If we can see something, we internalize it quickly. It’s storytelling with a purpose. If you’ve ever stared at a massive spreadsheet of data and couldn’t see a trend, you know how much more effective a visualization can be.
For better visualization of data, I choosed to work with COLAB and then a web application where the user selects data present in the excel sheet as a user input in a dropdown list which process the linear regression and presents the output in graph format as a data visualization part.



<br><img src="https://github.com/ashishgir/ClimateAnalysis/blob/master/Images/Web1.PNG"> <br>
<br><img src="https://github.com/ashishgir/ClimateAnalysis/blob/master/Images/Web2.PNG"> <br>
<br><img src="https://github.com/ashishgir/ClimateAnalysis/blob/master/Images/Web3.PNG"> <br>
<br><img src="https://github.com/ashishgir/ClimateAnalysis/blob/master/Images/Web4.PNG"> <br>

# End thoughts
Unanswered question: why is the "Cold Weather" getting hotter more rapidly than the "Hot Weather"? 
As always, I hope that this small analysis inspires people and makes them a smidge more conscious about what surrounds us and how we can start making a positive impact on these changes.
