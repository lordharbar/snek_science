# Get modules
import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
plt.rc("font", size=14)
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
import seaborn as sns
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)
# Get data set
ds = pd.read_csv('/Users/lordharbar/Downloads/vsp_email_retiree.csv')
# View Data
ds.columns
ds.head()
ds.shape
ds['Qualified'].unique()
ds['Qualified'].value_counts()
sns.countplot(x = 'Qualified', data=ds, palette='hls')
plt.show()
plt.savefig('count_plot')
