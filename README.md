# Toxic Triggers

Toxic Triggers is a Python package that provides access to a dataset of text triggers that have been categorized as offensive or harmless to minorities. This package can be useful for researchers and developers who want to understand how offensive language can affect marginalized groups and how it can be detected and prevented.

## Features

- Access to a dataset of text triggers categorized as offensive or harmless to minorities
- Provides easy access to subsets of the dataset based on categorization
- Built with Pandas for easy data manipulation

## Installation

To install the package, you can use pip:


## Usage

Here's an example of how to use the package:

```python
from your_package_name import Toxic_Triggers

tt = Toxic_Triggers()

# Print the name and description of the dataset
print(tt.name)
print(tt.description)

# Print the first 5 rows of the dataset
print(tt.data.head())

# Print the number of triggers categorized as offensive to minorities
print(len(tt.OI))

# Print the number of triggers categorized as harmless to minorities
print(len(tt.NOI))

# Print the number of triggers categorized as offensive but not targeting minorities
print(len(tt.ONI))
```
The package will automatically load the dataset into a Pandas DataFrame when you create a Toxic_Triggers object. You can then access the dataset and its subsets using the data, OI, NOI, and ONI attributes.

# License
This package is released under the MIT License. See the LICENSE file for more details.

# Credits
This package was developed by Xuhui Zhou and Maarten Sap.