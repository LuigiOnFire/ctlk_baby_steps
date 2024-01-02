from cltk.data.fetch import FetchCorpus
from cltk import NLP
from cltk.core.data_types import Doc

import cltk.text.lat as jv

with open('data/pl.txt', "r") as f:
    text = f.read()
print(text)

print(text[0:14])
print(text[1305:1330])

text = jv.replace_jv(text)
print(text[0:14])
print(text[1305:1330])
