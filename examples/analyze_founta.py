from toxicTrig import toxicTrig
import pandas as pd #type: ignore
import time

df = pd.read_csv("example_data/ND_founta_trn_dial_pAPI.csv")
text = df["tweet"].tolist()

tt = toxicTrig()
start_time = time.time()
tt.text_analysis(text, batch_size=100)
end_time = time.time()

time_taken = round(end_time - start_time, 2)
print("Total time taken: ", time_taken, " seconds")

# Count tokens in text
total_tokens = sum([len(t.split()) for t in text])
print("Total tokens in text: ", total_tokens)