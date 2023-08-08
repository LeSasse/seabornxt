"""Run an example of a plot combining box and stripplot."""

import seaborn as sns
from seabornxt import stripboxplot


def main():
    tips = sns.load_dataset("tips")

    plot = stripboxplot(data=tips, x="day", y="total_bill", hue="smoker")
    fig = plot.get_figure()
    fig.savefig("images/stripboxplot.svg")


if __name__ == "__main__":
    main()
