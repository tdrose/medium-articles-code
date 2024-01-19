import matplotlib.pyplot as plt
import seaborn as sns
data = sns.load_dataset('mpg')


fig = plt.figure(figsize=(10, 7))
(topfig, bottomfig) = fig.subfigures(2, 1)

topfig.set_facecolor('#cbe4c6ff')
topfig.suptitle('Top')
top_axs = topfig.subplots(2, 4)


(bottomleft, bottomright) = bottomfig.subfigures(1, 2, width_ratios=(1,2))


bottomleft.set_facecolor('#c6c8e4ff')
bottomleft.suptitle('Bottom left')
bottom_axs = bottomleft.subplots(2, 2)

bottomright.set_facecolor('#aac8e4ff')
bottomright.suptitle('Bottom right')
bottom_axs = bottomright.subplots(3, 3)

# Spacing between subplots
topfig.subplots_adjust(left=.1, right=.9, wspace=.4, hspace=.4)
bottomleft.subplots_adjust(left=.2, right=.9, wspace=.5, hspace=.4)
bottomright.subplots_adjust(left=.1, right=.9, wspace=.4, hspace=.4)

plt.show()
