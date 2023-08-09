"""Provide a function to combine stripplot and boxplot easily."""

import seaborn as sns
from matplotlib.legend_handler import HandlerTuple


def stripboxplot(
    data=None,
    x=None,
    y=None,
    hue=None,
    strip_kwargs=None,
    box_kwargs=None,
):
    if box_kwargs is None:
        box_kwargs = {"showfliers": False}
    if strip_kwargs is None:
        strip_kwargs = {"jitter": True, "alpha": 0.4, "color": "k"}

    ax = sns.boxplot(data=data, x=x, y=y, hue=hue, dodge=True, **box_kwargs)
    if hue is not None:
        n_cats_hue = len(data[hue].unique())

    sns.stripplot(
        data=data, x=x, y=y, hue=hue, dodge=True, ax=ax, **strip_kwargs
    )

    if hue is None:
        return ax

    handles, labels = ax.get_legend_handles_labels()

    new_handles = []
    new_labels = []
    for i in range(n_cats_hue):
        new_handles.append((handles[i], handles[i + n_cats_hue]))
        new_labels.append(labels[i])

    ax.legend(
        title=ax.legend_.get_title().get_text(),
        handles=new_handles,
        labels=new_labels,
        handlelength=4,
        handler_map={tuple: HandlerTuple(ndivide=None)},
    )
    return ax
