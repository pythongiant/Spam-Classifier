from textblob.classifiers import NaiveBayesClassifier
import sys
"""
#pottentially spam file
spamFile=open(str(sys.argv[1]),'r')
#read the file
spamFileContent=spamFile.read()
"""
#open the training dataset
with open('train.csv','r') as train:
	classifier=NaiveBayesClassifier(train,format="csv")
test=[
("GENT! We are trying to contact you. Last weekends draw shows that you won a 1000 prize GUARANTEED. Call 09064012160. Claim Code K52. Valid 12hrs only. 150pm",'spam')]
print classifier.classify("GENT! We are trying to contact you. Last weekends draw shows that you won a 1000 prize GUARANTEED. Call 09064012160. Claim Code K52. Valid 12hrs only. 150ppm")
print classifier.accuracy(test)