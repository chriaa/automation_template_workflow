
import pandas as pd



print("whippee!!!!")



df = { 
    'alphabet' : ['a', 'b', 'c'],
    'animal' : ["dog", "cat", "fish"]
}


test_df = pd.DataFrame(df)
test_df.to_csv('./outputs/test.csv')