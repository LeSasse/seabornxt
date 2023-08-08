"""Provide a function to combine stripplot and boxplot easily."""

import seaborn as sns
from matplotlib.legend_handler import HandlerTuple
from IPython import embed


def stripboxplot(
    data=None, x=None, y=None, hue=None, strip_kwargs=None, box_kwargs=None
):
    if box_kwargs is None:
        box_kwargs = {"boxprops": {"alpha": 0.5}}
    if strip_kwargs is None:
        strip_kwargs = {"jitter": True, "alpha": 0.8}

    # set a nice default for box transparency if not explicitly set.
    if "boxprops" not in box_kwargs:
        box_kwargs["boxprops"] = {"alpha": 0.4}

    ax = sns.boxplot(data=data, x=x, y=y, hue=hue, dodge=True, **box_kwargs)
    # handles = ax.get_legend_handles_labels()
    # n_cats = len(handles)

    sns.stripplot(
        data=data, x=x, y=y, hue=hue, dodge=True, ax=ax, **strip_kwargs
    )

    handles, labels = ax.get_legend_handles_labels()

    # TODO: Generalise fixing the legend for the appropriate number of
    # categories
    ax.legend(
        title=ax.legend_.get_title().get_text(),
        handles=[(handles[0], handles[2]), (handles[1], handles[3])],
        labels=[labels[0], labels[1]],
        handlelength=4,
        handler_map={tuple: HandlerTuple(ndivide=None)},
    )
    return ax
