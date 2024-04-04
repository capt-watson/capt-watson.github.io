# import sys
# from packaging import version
# import sklearn as sk

# assert sys.version_info >= (3, 7)

# assert version.parse(sk.__version__) >= version.parse('1.0.1')

from pathlib import Path
import pandas as pd
import tarfile
import urllib.request
import matplotlib.pyplot as plt
pd.set_option('display.max_columns',None)


def load_housing_data():
    tarball_path = Path('datasets/housing.tgz')
    if not tarball_path.is_file():
        Path('datasets').mkdir(parents=True, exist_ok=True)
        url = 'https://github.com/ageron/data/raw/main/housing.tgz'
        urllib.request.urlretrieve(url, tarball_path)
        with tarfile.open(tarball_path) as housing_tarball:
            housing_tarball.extractall(path='datasets')
    return pd.read_csv(Path('datasets/housing/housing.csv'))

housing = load_housing_data()
# print(housing)
# print(housing.head())

# print(housing.info())

# print(housing['ocean_proximity'].value_counts())

# print(housing.describe())


## pd.df.head() represents the first n lines of the data. n=5 default

## pd.df.info() represents info about the df including index, columns, non-null count and memory usage.

IMAGES_PATH = Path() /'images'/'end_to_end_project'
IMAGES_PATH.mkdir(parents=True, exist_ok=True)

def save_fig(fig_id, tight_layout = True, fig_extension='png',resolution=300):
    path = IMAGES_PATH / f'{fig_id}.{fig_extension}'
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution)
    
plt.rc('font',size=14)
plt.rc('axes',labelsize= 14, titlesize= 14)
plt.rc('legend',fontsize=14)
plt.rc('xtick',labelsize=10)
plt.rc('ytick',labelsize=10)

housing.hist(bins=50, figsize=(12,8))
save_fig('attribute_histogram_plots')
plt.show()


## tight_layout is a matplotlib.pyplot function which adjusts subplot params so that the subplot(s) fits into the figure area.

## A histogram is a graph that shows the frequency of numerical data using rectangles.