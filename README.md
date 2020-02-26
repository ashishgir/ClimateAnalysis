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

Map of temperatures and analysis of global warming <br>
How does climat change affect different places? <br>
Is The Mercury Rising? <br>
Global Temperature-Forecasting <br>
Visualizations of temperature change <br>
Temperature & Impact on Snowfall <br>

# Implementation
Analyzing a huge data sets is the method of big data which comprises a classes of data types. The big data maintain
a significant amount of data and process that data.  The most popular Big Data handling and processing technique is Hadoop Map-Reduce which is currently used. Map-Reduce is a technique which executes parallel and distributed algorithm across large data using number of
clusters. In the proposed system, Map-Reduce algorithm is used to calculate minimum and maximum temperature of a
particular city and Spatial Cumulative Sum(CUSUM) based algorithm is proposed to detect the changes in the climate
which produces the results in the form of graphs with temperature values. Map-Reduce is a process which will be work in three steps, namely map, shuffle, and reduce. The mapper's job is to process the input data in map stage. In Hadoop file system, the input data is in sort of file and is collected from various weather sites. And the reducer will take the output from the Map as an input and combined that data into a set of tuples. 

