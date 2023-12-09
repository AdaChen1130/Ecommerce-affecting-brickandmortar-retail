# E-Commerce Impact Analysis on Brick-and-Mortar Retail in China

## Introduction

This project aims to analyze the impact of E-Commerce on Brick-and-Mortar Retail in China. By crawling consumption data from 2019-2023 released by the National Bureau of Statistics of China, processing this data, and conducting a visual analysis, this project seeks to contribute to the broader dialogue on the future of retail in the digital age.
The project mainly analyzes the online and offline sales pattern, tries to figure out the logistics behind the phenomenon, the main figure is as shown below.

![Camparison of online and offline sales pattern](https://github.com/AdaChen1130/Ecommerce-affecting-brickandmortar-retail/blob/main/img/online_offline_Compare.png)

The results are shown in [statistic_analysis_retail.ipynb](https://github.com/AdaChen1130/Ecommerce-affecting-brickandmortar-retail/blob/main/statistics_analysis_retail.ipynb). After we processed the collected data, we conducted descriptive analysis, t-test and regression analysis on the data.

## Environment Setup

To run this project, the following Python packages need to be installed:

- requests
- numpy
- pandas
- BeautifulSoup4
- matplotlib
- plotly
- statsmodels

### Installation Steps

Ensure Python version 3.x is installed on your system. Download and install it from the [official Python website](https://www.python.org/downloads/).

Use pip, Python's package manager, to install the required packages:

## Data Source

The project utilizes data scraped from the official website of the National Bureau of Statistics of China. More information can be found at [National Bureau of Statistics of China](https://www.stats.gov.cn/english/).

### Data Crawler

For detailed scraping progress and methodologies, refer to the notebook:

- [`CNStatsCrawler.ipynb`](https://github.com/AdaChen1130/Ecommerce-affecting-brickandmortar-retail/blob/main/src/CNStatsCrawler.ipynb) - A Jupyter Notebook designed for scraping and analyzing statistical data from 2018-2021. It employs Python along with various data processing and visualization libraries.

### Data Preprocessing

The following notebook is dedicated to the preprocessing of the scraped data:

- [`Preprocessing.ipynb`](https://github.com/AdaChen1130/Ecommerce-affecting-brickandmortar-retail/blob/main/src/Preprocessing.ipynb) - This Jupyter Notebook focuses on data preprocessing techniques, including data cleaning, transformation, and preparation for analysis or machine learning models using Python's data manipulation libraries.

##Analysis
### Visual Analysis
In the [e_commerce_update](https://github.com/AdaChen1130/Ecommerce-affecting-brickandmortar-retail/blob/main/e_commerce_update.ipynb) file, we visualized data from almost all categories and created visualizations in different views based on the type of data. This process helped in uncovering elements that are significant for analysis.

### Regression Analysis
In the [statistics_analysis_retail](https://github.com/AdaChen1130/Ecommerce-affecting-brickandmortar-retail/blob/main/statistics_analysis_retail.ipynb) file, we conducted trend analysis and significance testing on key parts of the above code. This helped in understanding the dependencies between variables.

### Conclusion
We have compiled the main conclusions and visualizations of the project in [Ecommerce_affecting_Slides.pdf](https://github.com/AdaChen1130/Ecommerce-affecting-brickandmortar-retail/blob/main/Ecommerce_affecting_Slides.pdf) and [Ecommerce_Affecting_Report.pdf](https://github.com/AdaChen1130/Ecommerce-affecting-brickandmortar-retail/blob/main/Ecommerce_Affecting_Report.pdf).

