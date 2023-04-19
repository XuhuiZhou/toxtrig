# Toxic Triggers

Toxic Triggers is a Python package that provides access to a dataset of text triggers that have been categorized as offensive or harmless to minorities. This package can be useful for researchers and developers who want to understand how offensive language can affect marginalized groups and how it can be detected and prevented.

## Features

- Access to a dataset of text triggers categorized as offensive or harmless to minorities
- Provides easy access to subsets of the dataset based on categorization
- Built with Pandas for easy data manipulation
- Analyze the text for the presence of toxic triggers

### Taxonomy of Toxic Triggers
`text_analysis` function returns a dictionary with the following keys:
- `harmless-minority`: Non-offensive minority identity mentions (NOI)
- `offensive-minority-reference`: Possibly offensive minority identity mentions (OI)
- `offensive-not-minority`: Possibly offensive non-identity mentions (ONI)
Please refer to our [paper](https://aclanthology.org/2021.eacl-main.274.pdf) for more details.


## Installation

To install the package, you can use `pip install toxicTrig`


## Usage

Here's an example of how to use the package:

```python
from toxicTrig import toxicTrig
import pandas as pd #type: ignore
import time

df = pd.read_csv("example_data/ND_founta_trn_dial_pAPI.csv")
text = df["tweet"].tolist() # A list of strings as the input

tt = toxicTrig()
start_time = time.time()
tt.text_analysis(text, batch_size=100)
end_time = time.time()

time_taken = round(end_time - start_time, 2)
print("Total time taken: ", time_taken, " seconds")

# Count tokens in text
total_tokens = sum([len(t.split()) for t in text])
print("Total tokens in text: ", total_tokens)
```

# Contribution
### Install dev options
```bash
pip install -e ".[dev]"
mypy --install-types --non-interactive toxicTrig
pip install pre-commit
pre-commit install
```
### New branch for each feature
`git checkout -b feature/feature-name` and PR to `main` branch.
### Before committing
Run `pytest` to make sure all tests pass (this will ensure dynamic typing passed with beartype) and `mypy --strict .` to check static typing.
(You can also run `pre-commit run --all-files` to run all checks)

# Citation
If you use this package in your research, please cite the following paper:

```bibtex
@inproceedings{zhou-etal-2021-debiasing,
  title = {Challenges in Automated Debiasing for Toxic Language Detection},
  author = {Zhou, Xuhui and Sap, Maarten and Swayamdipta, Swabha and Choi, Yejin and Smith, Noah A.},
  booktitle = {EACL},
  year = {2021},
}
```

# License
This package is released under the MIT License. See the LICENSE file for more details.

# Credits
This package was developed by Xuhui Zhou and Maarten Sap.