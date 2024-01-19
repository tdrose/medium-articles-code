import matplotlib.pyplot as plt
import seaborn as sns
data = sns.load_dataset('mpg')


def letter_annotation(ax, xoffset, yoffset, letter):
    ax.text(xoffset, yoffset, letter, transform=ax.transAxes, 
            size=12, weight='bold')

fig = plt.figure(figsize=(10, 7))

# Creating a subfigure for the first and second row
(row1fig, row2fig) = fig.subfigures(2, 1, height_ratios=[1, 1])
# Splitting the bottom row subfigure in two subfigures
(fig_row2left, fig_row2right) = row2fig.subfigures(1, 2, wspace=.08, width_ratios = (1, 2))


# #####
# Row 1 plots
# #####

# Make 4 subplots for the first row subfigure
row1_axs = row1fig.subplots(1, 4)

# Make more space between subplots and extend plots to the left and right borders
# Since `tight_layout` does not work for subfigures we also need to manually increase the space to the bottom 
# to fit the fit the xaxis label
row1fig.subplots_adjust(wspace=0.5, left=0, right=1, bottom=.16) # other parameters: bottom, top, hspace

ax = row1_axs[0]
sns.histplot(data=data, x='mpg', ax=ax)
ax.set_title('MPG')
# Annotate plotots with letters
letter_annotation(ax, -.25, 1, 'A')
# Some styling for figures to make them look better and have a standardized look
sns.despine(offset=5, trim=False, ax=ax)

ax = row1_axs[1]
sns.histplot(data=data, x='displacement', ax=ax)
ax.set_title('Displacement')
letter_annotation(ax, -.25, 1, 'B')
sns.despine(offset=5, trim=False, ax=ax)

ax = row1_axs[2]
sns.histplot(data=data, x='weight', ax=ax)
ax.set_title('Weight')
letter_annotation(ax, -.25, 1, 'C')
sns.despine(offset=5, trim=False, ax=ax)

ax = row1_axs[3]
sns.histplot(data=data, x='horsepower', ax=ax)
ax.set_title('Horsepower')
letter_annotation(ax, -.25, 1, 'D')
sns.despine(offset=5, trim=False, ax=ax)


# #####
# Row 2 plots
# #####

# ##
# Seaborn jointplot
# ##

# Using code from the Seaborn JointGrid class

# size ratio between the main plots and the margin plots
ratio=2
# Defining a gridspec for inside the subfigure
gs = plt.GridSpec(ratio + 1, ratio + 1)
ax_joint  = fig_row2left.add_subplot(gs[1:, :-1])
# Share axis between the margin and main plots
ax_marg_x = fig_row2left.add_subplot(gs[0, :-1], sharex=ax_joint)
ax_marg_y = fig_row2left.add_subplot(gs[1:, -1], sharey=ax_joint)

# Remove Axis labels and ticklabels for the margin plots
plt.setp(ax_marg_x.get_xticklabels(), visible=False)
plt.setp(ax_marg_y.get_yticklabels(), visible=False)
plt.setp(ax_marg_x.get_xticklabels(minor=True), visible=False)
plt.setp(ax_marg_y.get_yticklabels(minor=True), visible=False)

sns.scatterplot(data=data, y='horsepower', x='mpg', ax=ax_joint)
sns.histplot(data=data, y='horsepower', ax=ax_marg_y)
sns.histplot(data=data, x='mpg', ax=ax_marg_x)

sns.despine(offset=5, trim=False, ax=ax_joint)
sns.despine(offset=5, trim=False, ax=ax_marg_y)
sns.despine(offset=5, trim=False, ax=ax_marg_x)

# Leaving some space to the right to remove overlaps
fig_row2left.subplots_adjust(left=0, right=.8)
letter_annotation(ax_marg_x, -.25, 1, 'E')

# ##
# Row 2 right plots
# ##

gs = plt.GridSpec(2, 3)
ax_left   = fig_row2right.add_subplot(gs[:, 0])
ax_middle = fig_row2right.add_subplot(gs[:, 1])
ax_up     = fig_row2right.add_subplot(gs[0, 2])
ax_down   = fig_row2right.add_subplot(gs[1, 2])

fig_row2right.subplots_adjust(left=0, right=1, hspace=.5)

ax = ax_left
sns.scatterplot(data=data, x='model_year', y='weight', hue='origin', ax=ax)
sns.despine(offset=5, trim=False, ax=ax)
letter_annotation(ax, -.3, 1, 'F')

ax = ax_middle
sns.boxplot(data=data, x='origin', y='horsepower', ax=ax)
sns.despine(offset=5, trim=False, ax=ax)
letter_annotation(ax, -.3, 1, 'G')

ax = ax_up
sns.kdeplot(data=data, x='mpg', y='acceleration', ax=ax)
sns.despine(offset=5, trim=False, ax=ax)
letter_annotation(ax, -.3, 1, 'H')

ax = ax_down
sns.histplot(data=data, x='weight', y='horsepower', ax=ax)
sns.despine(offset=5, trim=False, ax=ax)
letter_annotation(ax, -.3, 1, 'I')

plt.show()
