import matplotlib.pyplot as plt
import seaborn as sns
data = sns.load_dataset('mpg')

figure = plt.figure(figsize=(10, 7))
figs = figure.subfigures(2, 2, height_ratios=(2,1), width_ratios=(2,1))

figs = figs.flatten()

for i, fig in enumerate(figs):
    fig.suptitle(f'Subfigure {i}')
    axs = fig.subplots(2, 2)

plt.show()
