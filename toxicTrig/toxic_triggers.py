import re
import pkg_resources
import pandas as pd #type: ignore
from collections import Counter

from typing import Pattern
data_path = pkg_resources.resource_filename('toxicTrig', 'data/word_based_bias_list.csv')

class toxicTrig:
    def __init__(self) -> None:
        self.name = "toxicTrig"
        self.description = "Toxic Triggers"
        self.data = pd.read_csv(data_path)
        self.NOI = self.data[self.data['categorization'] == 'harmless-minority'].word.tolist()
        self.OI = self.data[self.data['categorization'] == 'offensive-minority-reference'].word.tolist()
        self.ONI = self.data[self.data['categorization'] == 'offensive-not-minority'].word.tolist()
        self.idtyRe = re.compile(r"\b"+r"\b|\b".join(self.NOI)+"\b",re.IGNORECASE)
        self.oiRe = re.compile(r"\b"+r"\b|\b".join(self.OI)+"\b",re.IGNORECASE)
        self.oniRe = re.compile(r"\b"+r"\b|\b".join(self.ONI)+"\b",re.IGNORECASE)

    def text_analysis(self, text: list[str], batch_size: int = 100) -> dict[str,int]:
        preds_all: list[str] = []
        inputs: list[str] = []
        assert batch_size <= len(text), "Batch size must be smaller or equal than the number of texts to analyze"
        for row in text:
            if not row or row.strip() == '': continue
            inputs.append(row)
            if len(inputs) == batch_size:
                preds_noi = self.taxonomy_classification(inputs, self.idtyRe, "harmless-minority")
                preds_oi = self.taxonomy_classification(inputs, self.oiRe, "offensive-minority-reference")
                preds_oni = self.taxonomy_classification(inputs, self.oniRe, "offensive-not-minority")
                preds_all.extend(preds_noi)
                preds_all.extend(preds_oi)
                preds_all.extend(preds_oni)
                inputs = []
        counts = Counter(preds_all)
        print("Done text analysis!")
        print("Total number of predictions: ", len(preds_all))
        print("Number of predictions per category: ", counts)
        return counts

    def taxonomy_classification(self, batched_inputs: list[str], pattern: Pattern[str], category: str) -> list[str]:
        preds = []
        for text_input in batched_inputs:
            # search for the pattern in the string
            matches = pattern.findall(text_input)
            # loop through the matches and print corresponding values from the dictionary
            if len(matches)>0:
                preds.append(category)
        return preds