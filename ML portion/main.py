'''
████████╗██████╗  █████╗ ██████╗  ██████╗██╗   ██╗
╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔════╝╚██╗ ██╔╝
   ██║   ██████╔╝███████║██║  ██║██║  ███╗╚████╔╝
   ██║   ██╔══██╗██╔══██║██║  ██║██║   ██║ ╚██╔╝
   ██║   ██║  ██║██║  ██║██████╔╝╚██████╔╝  ██║
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝   ╚═╝

Tradgy, a machine learning inspired data visualization
project to geographically map natural disasters through
parsed Twitter data.

@2022, HACKUIOWA
TEAM: JP, Rog, Ben, Steven
Machine Learning by JP
'''
from geopy import geocoders
import pandas as pd
import warnings
from sklearn import feature_extraction, linear_model, model_selection

#Small things
gn = geocoders.GeoNames(username='uiowahack')
warnings.simplefilter(action='ignore', category=FutureWarning)

#Training and testing for the model
train_df = pd.read_csv("/Users/jackal/Desktop/HackathonProject/NLP Training/train.csv")
test_df = pd.read_csv("/Users/jackal/Desktop/HackathonProject/NLP Training/test.csv")

#meow
count_vectorizer = feature_extraction.text.CountVectorizer()

#Create training vectors
train_vectors = count_vectorizer.fit_transform(train_df["text"])

#Testing vectors
test_vectors = count_vectorizer.transform(test_df["text"])

#Regression type beat
regModel = linear_model.RidgeClassifier()

#F1 scoring metric
scores = model_selection.cross_val_score(regModel, train_vectors, train_df["target"], cv=3, scoring="f1")

#Fitting model to training data
regModel.fit(train_vectors, train_df["target"])

positiveTweets = pd.read_csv("/Users/jackal/Desktop/HackathonProject/NLP Training/format.csv")
positiveTweets["target"] = regModel.predict(test_vectors)
positiveTweets.to_csv("PositiveTweets.csv", index=False)

refTweets = pd.read_csv("PositiveTweets.csv")
tweetsToMatch = pd.read_csv("/Users/jackal/Desktop/HackathonProject/NLP Training/test.csv")

refTweets = refTweets[refTweets.target != 0]
refTweets = refTweets.reset_index()
del refTweets['index']

refList = []
matchList = []

global finalDataFrame
finalDataFrame = pd.DataFrame(columns=["id","keyword","location","text"])

#Dataframe logistics
for refIndex, refValue in enumerate(refTweets["id"]):
    refList.append(refValue)

for matchIndex, matchValue in enumerate(tweetsToMatch["id"]):
    matchList.append(matchValue)

for listIndex, listValue in enumerate(refList):
    for matchIndex, matchValue in enumerate(matchList):
        if matchValue == listValue:
            finalDataFrame = finalDataFrame.append(tweetsToMatch.loc[tweetsToMatch['id'] == matchValue])

#Dumping tweets that tested positive for disaster
finalDataFrame.to_csv("PositiveOutputs.csv")
inDataFrame = pd.read_csv("Locations.csv", header=None)

#Creating a weighted data frame of all the locations as some are duplicates
global weightsData
weightsData = pd.DataFrame()
weightsData = inDataFrame.value_counts().rename_axis('locations').reset_index(name='counts')

#Data frame massaging
global weightedDataFrame
weightedDataFrame = pd.DataFrame(columns=["latitude","longitude","weight"])
for locationIndex, locationValue in enumerate(weightsData["locations"]):
    location = gn.geocode(weightsData["locations"][locationIndex])
    try:
        weightedDataFrame.loc[len(weightedDataFrame.index)] = [location.raw['lat'], location.raw['lng'], weightsData['counts'][locationIndex]]
    except:
        print("ERROR IN FETCH")
        weightedDataFrame.loc[len(weightedDataFrame.index)] = ["NAN", "NAN", "NAN"]
weightedDataFrame.to_csv("weightedDataFrame.csv", index=False)


