# IMDb Analysis

This project leverages the IMDb `title.basics` dataset for PySpark analysis. PySpark is employed for its distributed computing capabilities, making it suitable for handling large-scale datasets.

### Dataset
The dataset used in this project is sourced from IMDb and includes information about various titles, providing a rich set of data for analysis. `title.basics` is one of the IMDb public datasets available for access and non-commercial use. (See [IMDb Non-Commercial Datasets](https://developer.imdb.com/non-commercial-datasets/))

### Docker container
To simplify the setup and ensure a consistent environment, the project runs within a Docker container. The Dockerfile provided in the repository configures the necessary dependencies for running the PySpark analysis script.

### Dataset Analysis

The PySpark script conducts three key analyses on the IMDb title.basics dataset. To ensure the accuracy and reliability of the analysis results, the IMDb title.basics dataset underwent a thorough cleaning process. The core functionality of the IMDb data analysis is encapsulated within the `imdb_analysis.py` script. 

Key features of `imdb_analysis.py` include:

- Data loading and preprocessing to prepare the dataset for analysis.
- Execution of PySpark queries for three distinct analyses on the IMDb title.basics dataset.
- Utilization of `matplotlib` and `seaborn` libraries to visualize and present the analysis results.


#### 1. **Analysis 1:** Movies Per Year

![](/data/movies_per_year.png)

#### 2. **Analysis 2:** Average Runtime Per Decade

![](/data/avg_runtime_per_decade.png)

#### 3. **Analysis 3:** Most Common Movie Genres

![](/data/most_common_genres.png)


### Usage
Before running the script, make sure you have Docker installed in your system. You can download it from [here](https://docs.docker.com/get-docker/).

First, clone the repository to your machine:

    $ git clone https://github.com/leonardosantosdev/imdb-analysis


Under root directory, build the spark Docker image:

    $ docker build -t spark-image .

Start Docker containers running docker-compose.yaml.

    $ docker compose up -d

Enter one of the spark worker containers and run the PySpark application:

    $ docker exec -it pyspark-spark-worker-1-1 bash -c 'spark-submit --master spark://spark-master:7077 /usr/local/spark/src/imdb_analysis.py'
