# This backend check must be performed prior to any following calls to
# matplotlib. If performed later, behaviour becomes unpredictable.
import matplotlib
if matplotlib.get_backend() == 'Agg':
  import platform
  if platform.system() == 'Darwin':
    print("Forcing backend to MacOSX")
    matplotlib.use("MacOSX")
  else:
    print("Backend is 'Agg'. Plotting will be unsupported until TK is installed.")

import matplotlib.pyplot as plt

def show(*args, **kws):
  """Show a window with the given plot data. Blocks until window is closed.

  Parameters
  ----------
  *args : pyplot args
  **kws : pyplot kw

  Examples
  --------
  Plot a line.

        >>> bplot.line(x, y)
        >>> bplot.show()
  """
  plt.show(*args, **kws)
