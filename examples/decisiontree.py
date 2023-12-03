"""
examples/decisiontree.py

Using flowa.Encoder, flowa.Tree and their methods respectively.

(flowa/Encoder)  -> flowa.Encoder
(flowa/Tree) -> flowa.Tree
"""

from flowa import (
    Encoder,
    Tree,
    Dataset,
    read_csv,
    convert
)

classifier: Tree = Tree()
encoder: Encoder = Encoder()

dataset: str = convert(Dataset.get_music_data())
csv: object = read_csv(dataset)

dataframe: object = encoder.df(csv, 'gender')

X_matrix: object = dataframe.drop('genre', axis=1).values
y_column: object = encoder(dataframe['genre'].values)

classifier.fit(X_matrix, y_column)

age, gender = encoder.new(30, 'female')
fix: list = encoder.fix(age, gender)

prediction: list[int] = classifier.predict(fix)
print(encoder.inverse(prediction))

#>>> ['Pop']
