import pandas as pd

""" def getIframe(moodSelected):
    df  = pd.read_csv('Spotify Mood iframes.csv', names= ["mood","mood sub","iframe"], header = None)
    df = df[df.mood == moodSelected]
    df = df.sample()
    return df.iframe.item()
 """
def getIframe(moodSelected,nation):
    df  = pd.read_csv('Moods_Countries.csv', names= ["nation","mood","iframe",'junk'],sep='{', header = None)
    df = df.drop(columns=['junk'])
    #select the mood and country from the dataframe
    df = df[(df["mood"]== moodSelected) & (df["nation"]==nation)]
    print(moodSelected,nation,df)
    return df.iframe.item()