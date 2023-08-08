# seabornxt
A few handy extension plots using seaborn API.

```
import seaborn as sns
from seabornxt import stripboxplot


def main():
    tips = sns.load_dataset("tips")

    plot = stripboxplot(data=tips, x="day", y="total_bill", hue="smoker")
    fig = plot.get_figure()
    fig.savefig("images/stripboxplot.pdf")


if __name__ == "__main__":
    main()

```

Results in:

![Alt text](examples/images/stripboxplot.svg)
<img src="examples/images/stripboxplot.svg">
