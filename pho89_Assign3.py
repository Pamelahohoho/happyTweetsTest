##Sentiment Analysis
# Username: pho89

from happy_histogram import drawSimpleHistogram

def main():
    #initialize variables used
    pacificScore =0
    pacificTweets = 0
    pacificKeywords = 0

    mountainScore =0
    mountainTweets = 0
    mountainKeywords = 0

    centralScore=0
    centralTweets = 0
    centralKeywords=0

    easternScore=0
    easternTweets = 0
    easternKeywords = 0


    total= 0

    keywords={} #initialize dictionary to store keywords
    try:
        filename = input("enter keywords file") #checks for valid file
        infile = open(filename, 'r',encoding="utf-8") #can raise an IOError exception
        listOfKeywords = ""
        for line in infile:
            listOfKeywords = line.split(',')
            value = listOfKeywords[0]
            keywords[value] = listOfKeywords[1].strip()

    except IOError:
        print("error: file not found")
        exit()

    try:
        list = [] #list to temp store sections of the tweet
        regionList=[] #list to store longitude and latitude

        fileTweets = input("enter keywords file")
        infile = open(fileTweets, 'r',encoding="utf-8") #can raise an IOError exception
        for line in infile:
            list= line.split(']',1) #isolates longitude and latitude
            regionList = list[0].split(',') #splits tweet by comma
            regionList[0]= float(regionList[0].strip('[')) #strips bracket

            regionList[1] = float(regionList[1])
            tweet = list[1].split(' ',4) #isolates tweet
            tweet = tweet[4] #takes text portion

            region = findRegion(regionList)
            total += 1

            if region == 'pacific': #checks for pacific region
                listOfWords = tweet.split() #splits text into list
                found = False
                for word in listOfWords:
                    word = word.strip('@#$%^&*') #removes extra characters
                    word = word.lower()
                    if word in keywords:
                        pacificScore = pacificScore + int(keywords[word]) #adds to total sentiment values
                        pacificKeywords = pacificKeywords +1 #Adds total keywords from this region
                        found = True

                if found:
                    pacificTweets = pacificTweets + 1 #if a keyword is found add to total tweets


            elif region == 'mountain': #checks for mountain region
                listOfWords = tweet.split()
                found = False
                for word in listOfWords:
                    word = word.strip('@#$%^&*')
                    word = word.lower()
                    if word in keywords:
                        mountainScore = mountainScore + int(keywords[word])
                        mountainKeywords = mountainKeywords +1
                        found =True
                if found:
                    mountainTweets = mountainTweets +1

            elif region == 'central': #checks for central region
                listOfWords = tweet.split()
                found = False
                for word in listOfWords:
                    word = word.strip('@#$%^&*')
                    word = word.lower()
                    if word in keywords:
                        centralScore = centralScore + int(keywords[word])
                        centralKeywords = centralKeywords +1
                        found = True
                if found:
                    centralTweets = centralTweets +1

            elif region == 'eastern': #checks for easter region
                listOfWords = tweet.split()
                found = False
                for word in listOfWords:
                    word = word.strip('@#$%^&*')
                    word = word.lower()
                    if word in keywords:
                         easternScore = easternScore + int(keywords[word])
                         easternKeywords = easternKeywords +1
                         found =True
                if found:
                    easternTweets = easternTweets +1
        #calculates total hapiness score and tweets for each region
        pacificHappy = round(pacificScore/pacificKeywords, 3)
        mountainHappy = round(mountainScore/mountainKeywords,3)
        centralHappy = round(centralScore/centralKeywords,3)
        easternHappy = round(easternScore/easternKeywords,3)

        print("The happiness score for the Pacific region is", pacificHappy, "with", pacificTweets, "tweets!")
        print("The happiness score for the Mountain region is", mountainHappy, "with", mountainTweets, "tweets!")
        print("The happiness score for the Central region is", centralHappy, "with", centralTweets, "tweets!")
        print("The happiness score for the Eastern region is", easternHappy, "with", easternTweets, "tweets!")

        drawSimpleHistogram(easternHappy, centralHappy, mountainHappy, pacificHappy)

    except IOError: #exception error
        print("error: file not found")
        exit()

def findRegion(area): #locate the origin of tweet
    if (area[0] <=49.189787 and area[0] >= 24.660845) and (area[1]>=-125.242264 and area[1]<-115.236428):
        return 'pacific'
    elif (area[0] <=49.189787 and area[0] >= 24.660845) and (area[1]>=-115.236428 and area[1]<-101.998892):
        return 'mountain'
    elif (area[0] <=49.189787 and area[0] >= 24.660845) and (area[1]>=-101.998892 and area[1]<-87.518395):
        return 'central'
    elif (area[0] <=49.189787 and area[0] >= 24.660845) and (area[1]>=-87.518395 and area[1]<=-67.444574):
        return 'eastern'

main()

