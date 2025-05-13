import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/dustywhite7/Econ8310/master/AssignmentData/cookie_cats.csv"
data = pd.read_csv(url)
data.head()
data.tail()

# Count and display the number of unique players
print("Number of players: \n", data.userid.nunique(), '\n',
        "Number of records: \n", len(data.userid),'\n')

data.describe()
data.dtypes

def na_counter(data):
    print("NaN Values per column:")
    print("NA")
    for i in data.columns:
        percentage = 100 - ((len(data[i]) - data[i].isna().sum())/len(data[i]))*100

        # Only return columns with more than 5% of NA values
        if percentage > 5:
            print(i+" has "+ str(round(percentage)) +"% of Null Values")
        else:
            continue

# Execute function
na_counter(data)

# Convert boolean to integer (optional but useful for calculations)
data['retention_1'] = data['retention_1'].astype(int)
data['retention_7'] = data['retention_7'].astype(int)

# Check average retention by group
ret1 = data.groupby('version')['retention_1'].mean()
ret7 = data.groupby('version')['retention_7'].mean()

print("1-day Retention Rate:\n", ret1)
print("7-day Retention Rate:\n", ret7)

data['retention_1'] = data['retention_1'].astype(int)
ret1 = data.groupby('version')['retention_1'].mean()
print("1-day Retention Rate:\n", ret1)

data['retention_7'] = data['retention_7'].astype(int)
ret7 = data.groupby('version')['retention_7'].mean()
print("7-day Retention Rate:\n", ret7)

grouped = data.groupby('version')[['retention_1', 'retention_7']].mean()
print(grouped)

# Convert boolean to int for plotting
data['retention_1_int'] = data['retention_1'].astype(int)
data['retention_7_int'] = data['retention_7'].astype(int)

plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
sns.violinplot(x='version', y='retention_1_int', data=data)
plt.title('Violin Plot: 1-Day Retention')

plt.subplot(1,2,2)
sns.violinplot(x='version', y='retention_7_int', data=data)
plt.title('Violin Plot: 7-Day Retention')
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 5))

# 1-Day Retention KDE Plot
plt.subplot(1, 2, 1)
sns.kdeplot(data=data[data['version'] == 'gate_30']['retention_1'], label='gate_30', fill=True)
sns.kdeplot(data=data[data['version'] == 'gate_40']['retention_1'], label='gate_40', fill=True)
plt.title("Normal Distribution - 1-Day Retention")
plt.xlabel("Retention (1 = Yes, 0 = No)")
plt.legend()

# 7-Day Retention KDE Plot
plt.subplot(1, 2, 2)
sns.kdeplot(data=data[data['version'] == 'gate_30']['retention_7'], label='gate_30', fill=True)
sns.kdeplot(data=data[data['version'] == 'gate_40']['retention_7'], label='gate_40', fill=True)
plt.title("Normal Distribution - 7-Day Retention")
plt.xlabel("Retention (1 = Yes, 0 = No)")
plt.legend()

plt.tight_layout()
plt.show()

ret1 = data.groupby("version", as_index=False)['retention_1'].mean()
ret7 = data.groupby("version", as_index=False)['retention_7'].mean()

plt.figure(figsize=(12, 5))

# 1-day retention
plt.subplot(1, 2, 1)
sns.barplot(data=ret1, x='version', y='retention_1')
plt.title("1-Day Retention Rate by Version")
plt.ylabel("Retention Rate")
plt.ylim(0, 0.5)

# 7-day retention
plt.subplot(1, 2, 2)
sns.barplot(data=ret7, x='version', y='retention_7')
plt.title("7-Day Retention Rate by Version")
plt.ylabel("Retention Rate")
plt.ylim(0, 0.5)

plt.tight_layout()
plt.show()
