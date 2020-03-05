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
Big Data Social Network Analysis (BDSNA) is the focal computational and graphical study of powerful techniques that can be used to identify clusters, patterns, hidden structures, generate business intelligence, in social relationships within social networks in terms of network theory. This study applies various social network analysis and visualization tools to examine the structure and patterns of interdisciplinary collaborations, as well as the recently evolving overall pattern.

# Load the data
BigQuerysupports the following data formats when loading data into tables: CSV, JSON, AVRO, or Cloud Datastore backups. Data can be loaded into BigQuery using a job or by streaming records individually. 
Load jobs support three data sources:
•Objects inGoogle Cloud Storage<br>
•Data sent with the job orstreaming insert<br>
•Google Cloud Datastorebackup<br>

<br><img src="https://github.com/ashishgir/ClimateAnalysis/blob/master/Images/Storage1.PNG"> <br>
<br><img src="https://github.com/ashishgir/ClimateAnalysis/blob/master/Images/BigQuery1.PNG"> <br>

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

# PROPOSED ALGORITHM
The proposed framework for detection of climate change and raw weather station data are shown in Fig.2. A big
climatic data is reduced with Hadoop MapReduce framework. Proposed Spatial Cumulative Sum algorithm is used to
monitor the day wise changes in the climate from many years. MapReduce algorithm is used to create a table also.

# Cumulative Sum Method(CUSUM)
Cumulative Sum method [3] is use to find drastic changes in the mean value of quantity of interest. Here cumulative
sum method is used to monitor the changes in the climate. For ‘n’ data points X1, X2,…, Xn, calculate average by
equation as follows:
 X¯ = X1 + X2 + . . . + Xn
The Cumulative Sum value SI is calculated by the equation:
 SI = Si−1 + Xi − X¯ for i = 1, 2, …, n
 where consider, S0 = 0
Calculate maximum and minimum, by equation given in below :
 S_max = max i=0, 1,..., n Si
 S_min = min i=0,1, ..., n Si
Find S_diff values to detect the changes in cumulative sum value SI, by equation as :
 S_diff = S_max – S_min 
 
 
