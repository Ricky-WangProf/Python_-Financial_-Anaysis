import pandas as pd
import numpy as np

from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

print(__version__) # requires version >= 1.9.0

import cufflinks as cf

# For Notebooks
init_notebook_mode(connected=True)

# For offline use
cf.go_offline()

df = pd.DataFrame(np.random.randn(100,4),columns='A B C D'.split())

df.head()

df.iplot(kind='scatter',x='A',y='B',mode='markers',size=10)