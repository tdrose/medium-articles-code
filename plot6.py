import matplotlib.pyplot as plt
import seaborn as sns
data = sns.load_dataset('mpg')


fig = plt.figure(figsize=(10, 7))
(topfig, bottomfig) = fig.subfigures(2, 1)

topfig.set_facecolor('#cbe4c6ff')
topfig.suptitle('Top')
top_axs = topfig.subplots(2, 4)

# We are using the bottom left subfigure for the jointplot
(bottomleft, bottomright) = bottomfig.subfigures(1, 2, width_ratios=(1,2))


# This parameter defines the size ratio between the main plot and the margin plots
ratio=2

# Defining a gridspec where the subplots are places
gs = plt.GridSpec(ratio + 1, ratio + 1)
# The main scatterplot
ax_joint  = bottomleft.add_subplot(gs[1:, :-1])
# The margin plots are sharing an axis with the main plot
ax_marg_x = bottomleft.add_subplot(gs[0, :-1], sharex=ax_joint)
ax_marg_y = bottomleft.add_subplot(gs[1:, -1], sharey=ax_joint)

# Axis labels and ticklabels for the margin plots are set to not visible
# Since they are shared with the main plot, 
# removing them for the margin will also remove them from the main plot
plt.setp(ax_marg_x.get_xticklabels(), visible=False)
plt.setp(ax_marg_y.get_yticklabels(), visible=False)
plt.setp(ax_marg_x.get_xticklabels(minor=True), visible=False)
plt.setp(ax_marg_y.get_yticklabels(minor=True), visible=False)

# Filling the plots with data:
sns.scatterplot(data=data, y='horsepower', x='mpg', ax=ax_joint)
sns.histplot(data=data, y='horsepower', ax=ax_marg_y)
sns.histplot(data=data, x='mpg', ax=ax_marg_x)


bottomright.set_facecolor('#aac8e4ff')
bottomright.suptitle('Bottom right')
bottom_axs = bottomright.subplots(3, 3)

# Spacing between subplots
topfig.subplots_adjust(left=.1, right=.9, wspace=.4, hspace=.4)
bottomright.subplots_adjust(left=.1, right=.9, wspace=.4, hspace=.4)

plt.show()
