# Config variables
from config import * 

# Imports
import mlend
from mlend import download_spoken_numerals

# Empty dict = Download all data
subset = {}


# Download data
datadir = download_spoken_numerals(
    save_to = AUDIO_DATA_PATH,
    subset = subset, 
    verbose = 1,
    overwrite = False
)