"""Run an example of a plot combining box and stripplot."""

import seaborn as sns
from seabornxt import stripboxplot


def main():
    penguins = sns.load_dataset("penguins")
    plot = stripboxplot(
        data=penguins,
        x="sex",
        y="body_mass_g",
        hue="species",
    )
    fig = plot.get_figure()
    fig.savefig("images/stripboxplot_penguins.svg")


if __name__ == "__main__":
    main()
