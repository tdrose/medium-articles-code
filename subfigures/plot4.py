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

# Adding more space between plots and reducing the space to the sides
topfig.subplots_adjust(left=.1, right=.9, wspace=.4, hspace=.4)

# We can also squeeze subplots to the bottom
bottomfig.subplots_adjust(wspace=.5, hspace=.8, top=.7, bottom=.3)

plt.show()
