import pkg_resources
import pandas as pd
data_path = pkg_resources.resource_filename('your_package_name', 'data/my_data.csv')

class Toxic_Triggers:
    def __init__(self):
        self.name = "Toxic Triggers"
        self.description = "Toxic Triggers"
        self.data = pd.read_csv(data_path)
        self.NOI = self.data[self.data['categorization'] == 'harmless-minority']
        self.OI = self.data[self.data['categorization'] == 'offensive-minority-reference']
        self.ONI = self.data[self.data['categorization'] == 'offensive-not-minority']