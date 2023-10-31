import matplotlib.pyplot as plt
import seaborn as sns
data = sns.load_dataset('mpg')


fig = plt.figure(figsize=(10, 7))
(topfig, bottomfig) = fig.subfigures(2, 1)

topfig.set_facecolor('#cbe4c6ff')
topfig.suptitle('Top')

bottomfig.set_facecolor('#c6c8e4ff')
bottomfig.suptitle('Bottom')

top_axs = topfig.subplots(2, 4)

bottom_axs = bottomfig.subplots(3, 7)

plt.show()
