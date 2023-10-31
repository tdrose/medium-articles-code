import matplotlib.pyplot as plt
import seaborn as sns
data = sns.load_dataset('mpg')


def letter_annotation(ax, xoffset, yoffset, letter):
    ax.text(xoffset, yoffset, letter, transform=ax.transAxes, 
            size=12, weight='bold')

fig = plt.figure(figsize=(10, 7))
(topfig, bottomfig) = fig.subfigures(2, 1)

topfig.set_facecolor('#cbe4c6ff')
topfig.suptitle('Top')
top_axs = topfig.subplots(2, 4)
letter_annotation(top_axs[0][0], -.2, 1.1, 'A')

(bottomleft, bottomright) = bottomfig.subfigures(1, 2, width_ratios=(1,2))


bottomleft.set_facecolor('#c6c8e4ff')
bottomleft.suptitle('Bottom left')
bottoml_axs = bottomleft.subplots(2, 2)
letter_annotation(bottoml_axs[0][0], -.2, 1.1, 'B')

bottomright.set_facecolor('#aac8e4ff')
bottomright.suptitle('Bottom right')
bottomr_axs = bottomright.subplots(3, 3)
letter_annotation(bottomr_axs[0][0], -.2, 1.1, 'C')

# Spacing between subplots
topfig.subplots_adjust(left=.1, right=.9, wspace=.4, hspace=.4)
bottomleft.subplots_adjust(left=.2, right=.9, wspace=.5, hspace=.4)
bottomright.subplots_adjust(left=.1, right=.9, wspace=.4, hspace=.4)

plt.show()
