# Amazon Books: Recommender System

### Problem Statement:

How can we accurately recommend new books to users using a Item-item approach to encourage expanding user preferences to books they may not have otherwise found on their own?

### Context

Recommender systems are widespread in all aspects of user-facing industries, from Netflix, to Amazon, to LinkedIn or to YouTube. Due to the large volumes of content, products or posts being generated daily, users would be overwhelmed with information and simple searches may not generate adequate results that may be relevant to the user.

As a result, recommender systems are a subclass of information filtering systems that provide suggestions for items that are most pertinent to a particular user. For example, over 70% of watch time on YouTube is spent watching videos the underlying recommender algorithm recommends. In this project, a recommender system will be designed for Amazon shoppers that would recommend books they would most likely enjoy based on the reviews of others.

### Criteria for Success

Being able to successfully recommend the top 5 books a user may like based on reviews of others.

### Scope of Solution Space

The solution space would focus on an Item-based collaborative filtering approach for recommending books instead of an alternate User-based approach.

### Constraints within solution space

Due to the presence of potentially millions of possible recommendations, the focus of the recommendation would be narrowing it down to the top 5 books a user might like based on other users.

### Data Source

https://cseweb.ucsd.edu/~jmcauley/datasets/amazon_v2/#subsets

**_Size of Dataset_**: 2GB

## Authors

-   [@kylerodriguez](https://www.github.com/kyleanthonyr)

## Badges

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
![Static Badge](https://img.shields.io/badge/Pyspark-blue)
![Static Badge](https://img.shields.io/badge/Recommender%20System-green)
![Static Badge](https://img.shields.io/badge/Surprise-red?style=plastic&link=https%3A%2F%2Fsurprise.readthedocs.io%2Fen%2Fstable%2Fgetting_started.html)

## Appendix

Some great Resources for Recommender Systems:

Theory:

-   [A Complete Guide To Recommender Systems](https://towardsdatascience.com/a-complete-guide-to-recommender-system-tutorial-with-sklearn-surprise-keras-recommender-5e52e8ceace1)

-   [Introduction to Recommender Systems](https://towardsdatascience.com/introduction-to-recommender-systems-6c66cf15ada)

-   [Build a Recommendation Engine with Collaborative Filtering](https://realpython.com/build-recommendation-engine-collaborative-filtering/#using-python-to-build-recommenders)

Hands-on:

-   [Recommenders-team](https://github.com/recommenders-team/recommenders/blob/main/examples/02_model_collaborative_filtering/als_deep_dive.ipynb)
-   [Databricks Spark Training](https://github.com/databricks/spark-training/blob/master/machine-learning/python/solution/MovieLensALS.py)
-   [Tensorflow Recommenders Tutorial](https://www.tensorflow.org/recommenders/examples/basic_retrieval)

Great Data:

-   [Recommender Systems and Personalization Datasets](https://cseweb.ucsd.edu/~jmcauley/datasets.html)
