"""
examples/datasets.py

Using flowa.Dataset and its methods.

(datasets/music_data.csv)  -> flowa.Dataset.get_music_data()
(datasets/play_tennis.csv) -> flowa.Dataset.get_play_tennis()
"""

# Play Tennis (datasets/play_tennis.csv)
from flowa import (
    Dataset,
    read_csv,
    convert
)

dataset = Dataset.get_play_tennis()

csv = read_csv(convert(dataset))





# Music Data (datasets/music_data.csv)
from flowa import (
    Dataset,
    read_csv,
    convert
)

dataset = Dataset.get_music_data()

csv = read_csv(convert(dataset))
