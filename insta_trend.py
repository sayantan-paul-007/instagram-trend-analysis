import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
data = pd.read_csv("Instagram_data.csv", encoding='latin1')
newdata = pd.DataFrame(data)
newdata.head()
newdata.tail()
newdata.info()
data.shape
newdata.shape
newdata.isnull().sum()
#Performance Analysis
total_impressions = newdata['Impressions'].sum()
total_saves = newdata['Saves'].sum()
total_comments = newdata['Comments'].sum()
total_shares = newdata['Shares'].sum()
total_likes = newdata['Likes'].sum()
engagement_rate = (total_likes+total_comments+total_shares)/total_impressions
print("Engagement rate:", engagement_rate)
print(f"Total Impressions:{total_impressions}")
print(f"Total Saves:{total_saves}")
print(f"Total Comments:{total_comments}")
print(f"Total Shares:{total_shares}")
print(f"Total Likes:{total_likes}")
print(f"Engagement Rate:{engagement_rate:.2%}")
#Source Analysis
# plt.figure(figsize=(10,8))
# plt.style.use('fivethirtyeight')
# plt.title("Distribution of Impressions From Home")
# sns.distplot(data['From Home'])
# plt.show()
# plt.title("Distribution of Impressions From Hashtags")
# sns.distplot(data['From Hashtags'])
# plt.show()
# plt.title("Distribution of Impressions From Explore")
# sns.distplot(data['From Explore'])
# plt.show()
# plt.title("Distribution of Impressions From Other")
# sns.distplot(data['From Other'])
# plt.show()
# Home = newdata['From Home'].sum()
# Hashtags = newdata['From Hashtags'].sum()
# Explore = newdata['From Explore'].sum()
# Other = newdata['From Other'].sum()
# labels = ['From Home','From Hashtags','From Explore', 'Other']
# values = [Home, Hashtags, Explore, Other]
# fig = px.pie(data, values=values, names=labels, title="Impressions on Instagram postsfrom various sources", hole=0.5)
# fig.show()
#Behavioural Analysis
# total_profile_visits = newdata['Profile Visits'].sum()
# total_follows = newdata['Follows'].sum()
# total_profile_visits = newdata['Profile Visits'].sum()
# print(f"Total Profile Visits:{total_profile_visits}")
# print(f"Total Follows:{total_follows}")
# print(f"Total Likes:{total_likes}")
# plt.figure(figsize=(8,6))
# plt.bar(['Profile Visits','Follows','Likes'], [total_profile_visits, total_follows, total_likes])
# plt.title('User Behaviour Analysis')
# plt.ylabel('Count')
# plt.show()
#Analysing Relationships
#Relationship between Likes and Impressions
figure = px.scatter(data_frame=data, x='Impressions', y='Likes', size="Likes", trendline='ols', title="Relationship between Likes and Impressions")
figure.show()
#Relationship between Comments and Impressions
figure1 = px.scatter(data_frame=newdata, x='Impressions', y='Comments', size="Comments", trendline='ols', title="Relationship between Comments and Impressions")
figure1.show()
#Relationship between Shares and Impressions
figure2 = px.scatter(data_frame=newdata, x='Impressions', y='Shares', size="Shares", trendline='ols', title="Relationship between Shares and Impressions")
figure2.show()
#Relationship between Saves and Impressions
figure3 = px.scatter(data_frame=data, x='Impressions', y='Saves', size="Saves", trendline='ols', title="Relationship between Saves and Impressions")
figure3.show()
correlation = newdata.corr()
print(correlation['Impressions'].sort_values(ascending= False))
conversion_rate = (newdata['Follows'].sum()/newdata['Profile Visits'].sum())*100
print(conversion_rate)
#Relationship between Follows and Profile Visits
figure4 = px.scatter(data_frame=data, x='Profile Visits', y='Follows', size="Follows", trendline='ols', title="Relationship between Follows and Profile Visits")
figure4.show()