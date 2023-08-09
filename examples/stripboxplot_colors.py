"""Run an example of a plot combining box and stripplot."""

import seaborn as sns
from seabornxt import stripboxplot


def main():
    tips = sns.load_dataset("tips")

    plot = stripboxplot(
        data=tips,
        x="day",
        y="total_bill",
        hue="smoker",
        strip_kwargs={"jitter": True, "alpha": 0.8},
        box_kwargs={"boxprops": {"alpha": 0.4}},
    )
    fig = plot.get_figure()
    fig.savefig("images/stripboxplot_colors.svg")


if __name__ == "__main__":
    main()
