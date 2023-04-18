import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize = (10, 7))
sns.barplot(data = DF,
            x = DF.index,
            y = 'Height')