#%%
from code import interact

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt, widgets
from matplotlib.widgets import Button
from ipywidgets import interact, widgets
from IPython.display import display

#%%
df = pd.read_csv('C:/Users/Msi/Desktop/CALISMALAR/'
                 'Real Estate Sales/Real_Estate_Sales_2001-2020_GL.csv')
df.replace('Nan', pd.NA, inplace=True)
df = df.dropna()
df.info()
#%%
#TODO
#Average assessed value of properties from year to year?
#Average sale amount of properties from year to year?
#Average sales ratio of properties from year to year?
#How long, on average, did it take for the different property types to get sold?
#How long, on average, did it take for the different residential types to get sold?
#Which towns saw the most property sales in 2020?
#%%
#######
#### Average assessed value of properties from year to year?
######
#%%
print(df.head())
mean_value_todo1 = df.groupby('List Year')['Assessed Value'].mean().reset_index()
#%%
plt.figure(figsize=(10, 6))
sns.lineplot(x='List Year', y='Assessed Value', marker='D',
             data=mean_value_todo1, color='green', linestyle='dashed')
plt.title('Average assessed value of properties from year to year')
plt.xlabel('Year')
plt.ylabel('Mean Values')
plt.grid(True)
plt.show()
#%%
#%%
#######
#### Average sales ratio of properties from year to year
######
#%%
print(df.head())
mean_value_todo2 = df.groupby('List Year')['Sale Amount'].mean().reset_index()
#%%

plt.figure(figsize=(10, 6))
sns.lineplot(x='List Year', y='Sale Amount', marker='D',
             data=mean_value_todo2, color='red', linestyle='dotted')
plt.title('Average sale amount of properties from year to year')
plt.xlabel('Year')
plt.ylabel('Mean Values')
plt.grid(True)
plt.show()

#%%
#######
#### Average sale amount of properties from year to year?
######
#%%
print(df.head())
mean_value_todo3 = df.groupby('List Year')['Sales Ratio'].mean().reset_index()
#%%
plt.figure(figsize=(10, 6))
sns.lineplot(x='List Year', y='Sales Ratio', marker='D',
             data=mean_value_todo3, color='blue', linestyle='dotted')
plt.title('Average sale amount of properties from year to year')
plt.xlabel('Year')
plt.ylabel('Mean Values')
plt.grid(True)
plt.show()
#%%
fig, ax1 = plt.subplots(figsize=(12, 8))

# Graph 1
ax1.plot(mean_value_todo1['List Year'], mean_value_todo1['Assessed Value'],
         marker='D', color='green', linestyle='dashed', label='Assessed Value')
ax1.plot(mean_value_todo2['List Year'], mean_value_todo2['Sale Amount'],
         marker='D', color='red', linestyle='dotted', label='Sale Amount')

ax1.set_xlabel('Year')
ax1.set_ylabel('Mean Values (Assessed Value and Sale Amount)', color='black')
ax1.tick_params('y', colors='black')

# THIS FOR SALES RATIO BECAUSE SALES RATIO'S VALUES LOWER THAN OTHERS
ax2 = ax1.twinx()
ax2.plot(mean_value_todo3['List Year'], mean_value_todo3['Sales Ratio'],
         marker='D', color='blue', linestyle='dotted', label='Sales Ratio')
ax2.set_ylabel('Mean Values (Sales Ratio)', color='black')
ax2.tick_params('y', colors='black')
plt.title('Average Values of Properties from Year to Year')
plt.grid(True)
fig.tight_layout()
plt.show()
#%%
#######
#### How long, on average, did it take for the different property types to get sold?
######
#%%
mean_value_todo4 = df.groupby('Property Type')['Years until sold'].mean().reset_index()
#%%
plt.figure(figsize=(12, 8))
sns.set_style("whitegrid")

# Custom color palette
custom_palette = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

sns.barplot(x='Property Type', y='Years until sold', data=mean_value_todo4, palette=custom_palette, ci=None)

plt.title('Average Years Until Sold for Different Property Types', fontsize=16)
plt.xlabel('Property Type', fontsize=14)
plt.ylabel('Average Years Until Sold', fontsize=14)
plt.xticks(rotation=45, ha='right')
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adding data labels on top of each bar
for p in plt.gca().patches:
    plt.gca().annotate(f'{p.get_height():.2f}', (p.get_x() + p.get_width() / 2., p.get_height()),
                       ha='center', va='center', xytext=(0, 10), textcoords='offset points',
                       fontsize=10, color='black')

plt.show()

#%%
#######
#### How long, on average, did it take for the different residential types to get sold?
######
#%%
mean_value_todo5 = df.groupby('Residential Type')['Years until sold'].mean().reset_index()
#%%
plt.figure(figsize=(12, 8))
sns.set_style("whitegrid")

# Custom color palette
custom_palette = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

sns.barplot(x='Residential Type', y='Years until sold', data=mean_value_todo5, palette=custom_palette, ci=None)

plt.title('Average Years Until Sold for Different Property Types', fontsize=16)
plt.xlabel('Property Type', fontsize=14)
plt.ylabel('Average Years Until Sold', fontsize=14)
plt.xticks(rotation=45, ha='right')
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adding data labels on top of each bar
for p in plt.gca().patches:
    plt.gca().annotate(f'{p.get_height():.2f}', (p.get_x() + p.get_width() / 2., p.get_height()),
                       ha='center', va='center', xytext=(0, 10), textcoords='offset points',
                       fontsize=10, color='black')

plt.show()
#%%
#######
#### Which towns saw the most property sales in 2020?
######

#%%
df_2020 = df[df['List Year'] == 2020]
#%%
total_sales_by_town = df_2020.groupby('Town')['Sale Amount'].sum().reset_index()
sorted_sales_by_town = total_sales_by_town.sort_values(by='Sale Amount', ascending=False)
sorted_sales_by_town = sorted_sales_by_town.head(10)
#%%
colors = ['skyblue', 'salmon', 'lightgreen', 'orange', 'lightblue', 'pink', 'yellow']
plt.figure(figsize=(10, 6))
plt.barh(sorted_sales_by_town['Town'], sorted_sales_by_town['Sale Amount'], color=colors)
plt.title('Total Sales by Towns in 2020')
plt.xlabel('Total Sale Amount')
plt.ylabel('Town')
plt.tight_layout()
plt.show()
#%%

#%%
#%%
#%%
#%%
#%%
