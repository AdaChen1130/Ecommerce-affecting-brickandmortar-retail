# E-Commerce Impact Analysis on Brick-and-Mortar Retail in China

## Introduction

This project aims to analyze the impact of E-Commerce on Brick-and-Mortar Retail in China. By crawling consumption data from 2018-2021 released by the National Bureau of Statistics of China, processing this data, and conducting a visual analysis, this project seeks to contribute to the broader dialogue on the future of retail in the digital age.
The project mainly analyzes the online and offline sales pattern, tries to figure out the logistics behind the phenomenon, the main figure is as shown below.

![Camparison of online and offline sales pattern](https://github.com/AdaChen1130/Ecommerce-affecting-brickandmortar-retail/blob/main/img/online_offline_Compare.png)

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

