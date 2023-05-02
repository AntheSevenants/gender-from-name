# gender-from-name
Estimate someone's gender from their name using Python

This Python library allows you to guess someone's gender from their name. This is useful in cases where you need gender information in your dataset, but you only have names (i.e. in Twitter data). **The included dataset is tailored to Belgian names**, but you could easily add support for other countries given that you have the right data.

This library is also available for [R](https://github.com/AntheSevenants/gender-from-name-r).

## Installation

Either...

- Add this repository as a submodule:  
 `git submodule add https://github.com/AntheSevenants/gender_from_name.git`
- [Download the repository](https://github.com/AntheSevenants/gender_from_name/archive/refs/heads/main.zip) and extract it to its own directory in your own project's folder

## Usage

First, make sure you have imported the `get_gender` function:
```python
from gender_from_name.detector import get_gender
```

Now, you can supply any name to this function. It will return whatever gender it thinks the name represents:

```
>>> get_gender("Marie Verhulst")
'female'
>>> get_gender("Jonas Geirnaert")
'male'
>>> get_gender("Sam Gooris")
'male'
>>> get_gender("Sofie Van Moll")
'female'
```

If the program cannot find a match, it returns None:

```
>>> get_gender("qwertyuiop")
None
```

## How it works

This library is based on [public data on first names from the Belgian government](https://statbel.fgov.be/nl/themas/bevolking/namen-en-voornamen/voornamen-van-vrouwen-en-mannen#figures). Every year, the government publishes a dataset with first name frequencies for the entire country. All first names belonging to at least five people in Belgium are included. I extracted the country-wide data for both genders. My library finds the longest first name it can match and checks for what gender that name is most frequent. In this way, ambiguous cases like "Sam" and "Pascal" are treated. Of course, this means the library is not perfect, but since it follows the principle of "maximum likelihood", this is the best possible solution.

You can supply noisy data to the gender detector as long as the first name comes first in the supplied string. For example, "margauxkevdv" will be processed correctly, but "ikbenjonathan" will not.

Since the Belgian government does not supply data for genders outside of male and female, the library only supports those two genders.

## Custom datasets

You can supply data for your own country by replacing the datasets in `data/female_names.csv` and `data/male_names.csv`.