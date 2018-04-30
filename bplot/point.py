from .check_data import check_data


def point(x, y, color='tab:blue', label='', shape='o', size=36, ax=None,
          **kws):
    """Draw scatter plot.


    Parameters
    ----------
    x : {numpy.array, pandas.core.series.Series}
        The vector of x-axis data for which points are drawn.

    y : {numpy.array, pandas.core.series.Series}
        The vector of y-axis data for which points are drawn.

    color : string, 'tab:blue' by default
        The color of the box.

    label : string, '' (empty) by default
        The label within a potential legend.

    shape : string, 'o' by default
        The shape of the points to draw.

    size : int, 36 by default
        The size of the points to draw.

    ax : matplotlib.pyplot.Axes, None by default
        The axis onto which the box is drawn.  If left as None,
        matplotlib.pyplot.gca() is called to get the current `Axes`.


    Returns
    -------

    out : matplotlib.pyplot.Axes
        The `Axes` onto which the box was drawn.
    """

    x, y, ax = check_data(x, y, ax)

    out = ax.scatter(x, y, c=color, label=label, marker=shape)
    return out