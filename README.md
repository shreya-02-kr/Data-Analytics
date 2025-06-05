# Data-Analytics
This project focuses on leveraging data analytics to gain a deeper understanding of mental health trends, contributing factors, and potential insights for interventions. In an increasingly complex world, mental well-being is a critical aspect of public health. By analyzing relevant datasets, this project aims to identify patterns, correlations, and anomalies that can inform research, policy-making, and individual awareness regarding mental health.
This repository contains the data, analysis scripts, and visualizations for a data analytics project focused on understanding student mental health. Our goal is to explore patterns, potential risk factors, and insights related to student well-being through data-driven approaches.
Student Mental health.csv:
This is the primary dataset used for the analysis. It contains raw or minimally processed survey responses related to student mental health, including demographic information and various mental health indicators.
DataSets:
This directory is reserved for any additional datasets used in the project, such as external demographic data, academic performance records, or pre-processed versions of the main dataset, if applicable.
Mental health.py:
This is the main Python script for the project. It handles data loading (currently configured with synthetic data for demonstration, but easily switchable to your actual CSV), performs initial data exploration, and generates all the data visualizations. It also includes sections for outlier detection and data transformations, crucial steps in preparing mental health data for reliable analysis.
age_distribution_histogram.png: A histogram illustrating the distribution of student ages.
gender_distribution_piechart.png: A pie chart showing the proportion of different genders in the dataset.
students_by_year_gender_countplot.png: A bar chart visualizing the number of students in each study year, grouped by gender.
anxiety_vs_depression_countplot.png: A bar chart displaying the relationship between reported anxiety and depression levels.
anxiety_by_gender_countplot.png: A bar chart depicting anxiety levels among different genders.
depression_by_gender_countplot.png: A bar chart illustrating depression levels among different genders.
anxiety_by_study_year_countplot.png: A bar chart showing anxiety levels across various years of study.
depression_by_study_year_countplot.png: A bar chart illustrating depression levels across various years of study.
panic_attack_by_cgpa_countplot.png: A bar chart exploring the relationship between panic attacks and CGPA categories.
