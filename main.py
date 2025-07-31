import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import plotly.express as plx
import plotly.io as pio
pio.renderers.default = "browser"
import seaborn as sns



labels = ['show_id', 'type', 'title', 'country', 'date_added', 'release_year',
              'rating', 'duration', 'listed_in', 'description']

#reading file
df = pd.read_csv("DataCleaning\\netflix_titles.csv")

#Dropping unimportant columns with empty data
df = df.drop(["director", "cast"], axis='columns')

#Replacing empty data for "country" with Unknown
df["country"] = df["country"].fillna("Unknown")

#Dropping na
df = df.dropna(subset=["date_added", "rating", "duration"])

#Editing date
df["date_added"] = df["date_added"].str.strip()
df["date_added"] = pd.to_datetime(df["date_added"])

#Number of different types
num_movie = (df["type"] == "Movie").sum()
num_series = (df["type"] == "TV Show").sum()

#Data of Country count
most_country = df["country"].value_counts().idxmax()
most_country_count = df["country"].value_counts().max()

#Top5 country 
top6 = df["country"].value_counts().head(6)
top6 = top6.to_dict()
top5_country_df = pd.DataFrame(list(top6.items()), columns=["Country", "Count"])

#dropping row 3 because it was the number of unknown countries
top5_country_df = top5_country_df.drop(2)

#Number per year(added to netflix)
number_per_year = df["date_added"].dt.year.value_counts()
number_per_year_dict = number_per_year.to_dict()
number_year_df = pd.DataFrame(list(number_per_year_dict.items()), columns=["Year", "Count"])
number_year_df = number_year_df.sort_values("Year")

#Line chart for number for year
fig = plx.line(number_year_df, x="Year", y="Count", markers=True, title="Number Per Year")
fig.show()

#Bar chart for count per country using plx
bar = plx.bar(top5_country_df, x="Country", y="Count", title="Bar Chart for Countries")
bar.show()

#Using plt
plt.bar(top5_country_df["Country"], top5_country_df["Count"])
plt.title("Bar Chart for Countries")
plt.xlabel("Country")
plt.ylabel("Count")
plt.show()

#Using sns
sns.barplot(x="Country", y="Count", data=top5_country_df)
plt.show()

#Pie chart for number of movies and TV shows
plt.pie([num_movie, num_series], labels=["Movie", "TV Show"], autopct="%1.1f%%", startangle=90)
plt.axis("equal")
plt.show()