from pyspark.sql import SparkSession
import matplotlib.pyplot as plt
import seaborn as sns
import pyspark.sql.functions as f

spark = SparkSession.builder.getOrCreate()


def movies_per_year(df):
    movies_per_year_df = df.groupBy("startYear").count().orderBy(f.col("startYear"))
    pandas_df = movies_per_year_df.toPandas()

    pandas_df.plot(x="startYear", y="count", kind="line")
    plt.title("Number of Movies per Year")
    plt.xlabel("Year")
    plt.ylabel("Number of Movies")
    plt.grid(True)

    plt.savefig("/usr/local/spark/data/movies_per_year.png")


def avg_runtime_per_year(df):
    average_runtime_per_decade_df = (
        df.filter((f.col("titleType") == "movie"))
        .groupBy("decade")
        .agg(f.round(f.avg("runtimeMinutes"), 2).alias("avg"))
        .orderBy("decade")
    )

    pandas_df = average_runtime_per_decade_df.toPandas()

    sns.set(style="whitegrid")

    plt.figure(figsize=(10, 6))
    sns.lineplot(x='decade', y='avg', data=pandas_df, marker='o', color='blue', linewidth=2)

    plt.title('Average Movie Runtime per Decade', fontsize=16)
    plt.xlabel('Decade', fontsize=14)
    plt.ylabel('Average Runtime (minutes)', fontsize=14)

    plt.grid(True)
    plt.savefig('/usr/local/spark/data/avg_runtime_per_decade.png')


def most_common_genres(df):
    genres = df.withColumn("genre", f.explode(f.split("genres", ","))).filter(f.col("genre") != "\\N")
    most_common_genres_df = genres.groupBy("genre").count().orderBy("count", ascending=False)
    pandas_df = most_common_genres_df.toPandas()

    sns.set(style="whitegrid")

    plt.figure(figsize=(12, 6))
    bar_plot = sns.barplot(x='genre', y='count', data=pandas_df, palette='viridis')

    bar_plot.yaxis.get_major_formatter().set_scientific(False)

    bar_plot.set_xticklabels(bar_plot.get_xticklabels(), rotation=45, horizontalalignment='right')

    plt.title('Most Common Genres', fontsize=16)
    plt.xlabel('Genre', fontsize=14)
    plt.ylabel('Number of Movies', fontsize=14)

    plt.tight_layout()
    plt.savefig('/usr/local/spark/data/most_common_genres.png')
    plt.show()


try:
    df = (
        spark.read.csv("/usr/local/spark/tmp/title.basics.tsv", sep=r"\t", header=True)
        .withColumn("decade", f.floor(f.col("startYear") / 10) * 10)
        .filter(
            (f.col("startYear") != "\\N")
            & (f.col("startYear") <= 2023)
            & (f.col("titleType").isin("movie", "tvMovie"))
        )
    )
except Exception as e:
    raise e


movies_per_year(df)
avg_runtime_per_year(df)
most_common_genres(df)
