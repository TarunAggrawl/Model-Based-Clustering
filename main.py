

from Document import Document
from Model import Model
import json
import time
import sys
import nltk

def printExecutionTime(startTime, str=""):
    print(str+ " time elapsed: {:.2f}s".format(time.time() - start_time))
    return time.time()

def outputFileNameFormatter(resultDir, dataset, outputPrefix, ALPHA, BETA, LAMDA, decay):
    output = ""
    if decay == True:
        output = resultDir + "/" + dataset + outputPrefix + "_ALPHA" + str(ALPHA) + "_BETA" + str(
            BETA) + "_LAMDA" + str(LAMDA) + ".txt"
    else:
        output = resultDir + "/" + dataset + outputPrefix + "_ALPHA" + str(ALPHA) + "_BETA" + str(BETA) + ".txt"
    print("ALHA " + str(ALPHA) + " -  BETA " + str(BETA))
    return output

def outputFileNameFormatter_active(resultDir, dataset, outputPrefix, ALPHA, BETA, LAMDA, decay):
    output = ""
    if decay == True:
        output = resultDir + "/" + dataset + "_active" + outputPrefix + "_ALPHA" + str(ALPHA) + "_BETA" + str(
            BETA) + "_LAMDA" + str(LAMDA) + ".txt"
    else:
        output = resultDir + "/" + dataset + "_active" + outputPrefix + "_ALPHA" + str(ALPHA) + "_BETA" + str(BETA) + ".txt"
    print("ALHA " + str(ALPHA) + " -  BETA " + str(BETA))
    return output

def outputFileNameFormatter_delete(resultDir, dataset, outputPrefix, ALPHA, BETA, LAMDA, decay):
    output = ""
    if decay == True:
        output = resultDir + "/" + dataset + "_delete" + outputPrefix + "_ALPHA" + str(ALPHA) + "_BETA" + str(
            BETA) + "_LAMDA" + str(LAMDA) + ".txt"
    else:
        output = resultDir + "/" + dataset + "_delete" + outputPrefix + "_ALPHA" + str(ALPHA) + "_BETA" + str(BETA) + ".txt"
    print("ALHA " + str(ALPHA) + " -  BETA " + str(BETA))
    return output

def outputFileNameFormatter_active_word_wid_map(resultDir, dataset, outputPrefix, ALPHA, BETA, LAMDA, decay):
    output = ""
    if decay == True:
        output = resultDir + "/" + dataset + "_active_word_wid_map" + outputPrefix + "_ALPHA" + str(ALPHA) + "_BETA" + str(
            BETA) + "_LAMDA" + str(LAMDA) + ".txt"
    else:
        output = resultDir + "/" + dataset + "_active_word_wid_map" + outputPrefix + "_ALPHA" + str(ALPHA) + "_BETA" + str(BETA) + ".txt"
    print("ALHA " + str(ALPHA) + " -  BETA " + str(BETA))
    return output

def outputFileNameFormatter_active_cluster(resultDir, dataset, outputPrefix, ALPHA, BETA, LAMDA, decay):
    output = ""
    if decay == True:
        output = resultDir + "/" + dataset + "_active_cluster" + outputPrefix + "_ALPHA" + str(ALPHA) + "_BETA" + str(
            BETA) + "_LAMDA" + str(LAMDA) + ".txt"
    else:
        output = resultDir + "/" + dataset + "_active_cluster" + outputPrefix + "_ALPHA" + str(ALPHA) + "_BETA" + str(BETA) + ".txt"
    print("ALHA " + str(ALPHA) + " -  BETA " + str(BETA))
    return output



def outputFileNameFormatter_delete_cluster(resultDir, dataset, outputPrefix, ALPHA, BETA, LAMDA, decay):
    output = ""
    if decay == True:
        output = resultDir + "/" + dataset + "_delete_cluster" + outputPrefix + "_ALPHA" + str(ALPHA) + "_BETA" + str(
            BETA) + "_LAMDA" + str(LAMDA) + ".txt"
    else:
        output = resultDir + "/" + dataset + "_delete_cluster" + outputPrefix + "_ALPHA" + str(ALPHA) + "_BETA" + str(BETA) + ".txt"
    print("ALHA " + str(ALPHA) + " -  BETA " + str(BETA))
    return output    

def outputFileNameFormatter_delete_cluster_keyword(resultDir, dataset, outputPrefix, ALPHA, BETA, LAMDA, decay):
    output = ""
    if decay == True:
        output = resultDir + "/" + dataset + "_delete_cluster_keyword" + outputPrefix + "_ALPHA" + str(ALPHA) + "_BETA" + str(
            BETA) + "_LAMDA" + str(LAMDA) + ".txt"
    else:
        output = resultDir + "/" + dataset + "_delete_cluster_keyword" + outputPrefix + "_ALPHA" + str(ALPHA) + "_BETA" + str(BETA) + ".txt"
    print("ALHA " + str(ALPHA) + " -  BETA " + str(BETA))
    return output

def outputFileNameFormatter_active_cluster_keyword(resultDir, dataset, outputPrefix, ALPHA, BETA, LAMDA, decay):
    output = ""
    if decay == True:
        output = resultDir + "/" + dataset + "_active_cluster_keyword" + outputPrefix + "_ALPHA" + str(ALPHA) + "_BETA" + str(
            BETA) + "_LAMDA" + str(LAMDA) + ".txt"
    else:
        output = resultDir + "/" + dataset + "_active_cluster_keyword" + outputPrefix + "_ALPHA" + str(ALPHA) + "_BETA" + str(BETA) + ".txt"
    print("ALHA " + str(ALPHA) + " -  BETA " + str(BETA))
    return output

def outputFileNameFormatter_word(resultDir, dataset, outputPrefix, ALPHA, BETA, LAMDA, decay):
    output = ""
    if decay == True:
        output = resultDir + "/" + dataset + "_word" + outputPrefix + "_ALPHA" + str(ALPHA) + "_BETA" + str(
            BETA) + "_LAMDA" + str(LAMDA) + ".txt"
    else:
        output = resultDir + "/" + dataset + "_word" + outputPrefix + "_ALPHA" + str(ALPHA) + "_BETA" + str(BETA) + ".txt"
    print("ALHA " + str(ALPHA) + " -  BETA " + str(BETA))
    return output


dataDir = "data/"
resultDir = "result"

# dataset = "News"
dataset = "tweet_corona_clean_10.json"
# dataset = "america_election.json"
# dataset = "reuters21578"


LAMDA = 0.000004      #0.000006
betas =  [0.0015]     #0.0004

alphas = [0.002]

# LAMDA =0.000006
# betas =  [0.0004]




decay = True
applyICF = True
applyCWW = True
start_index = 0

outputPrefix = ""
if applyICF:
    outputPrefix = outputPrefix+"_ICF"
if applyCWW:
    outputPrefix = outputPrefix + "_CWW"
start_time = time.time()
print("Dataset: ",dataset," , Decay:", decay, " , ICF = ", applyICF, " , CWW = ", applyCWW)
listOfObjects = []
with open(dataDir+dataset) as input:  #load all the objects in memory
    line = input.readline()
    while line:
        obj = json.loads(line)  # a line is a document represented in JSON
        listOfObjects.append(obj)
        line = input.readline()

printExecutionTime(start_time)
start_time = time.time()
indexOfAlpha = -1
indexOfBeta = -1
for a in alphas:
    indexOfAlpha += 1
    for b in betas:
        indexOfBeta += 1
        if indexOfAlpha!=indexOfBeta:
            continue
        if a == 0.0 or b == 0.0:
            continue
        ALPHA = a
        BETA = b

        output = outputFileNameFormatter(resultDir, dataset, outputPrefix, ALPHA, BETA, LAMDA, decay)

        output_active = outputFileNameFormatter_active(resultDir, dataset, outputPrefix, ALPHA, BETA, LAMDA, decay)

        output_delete = outputFileNameFormatter_delete(resultDir, dataset, outputPrefix, ALPHA, BETA, LAMDA, decay)

        output_active_word_wid_map= outputFileNameFormatter_active_word_wid_map(resultDir, dataset, outputPrefix, ALPHA, BETA, LAMDA, decay)

        output_active_cluster = outputFileNameFormatter_active_cluster(resultDir, dataset, outputPrefix, ALPHA, BETA, LAMDA, decay)
        
        output_delete_cluster = outputFileNameFormatter_delete_cluster(resultDir, dataset, outputPrefix, ALPHA, BETA, LAMDA, decay)

        output_delete_cluster_keyword = outputFileNameFormatter_delete_cluster_keyword(resultDir, dataset, outputPrefix, ALPHA, BETA, LAMDA, decay)
        
        output_active_cluster_keyword = outputFileNameFormatter_active_cluster_keyword(resultDir, dataset, outputPrefix, ALPHA, BETA, LAMDA, decay)

        output_word = outputFileNameFormatter_word(resultDir, dataset, outputPrefix, ALPHA, BETA, LAMDA, decay)
        
        model = Model(ALPHA, BETA, LAMDA, applyDecay=decay, applyICF = applyICF, applyCWW=applyCWW)
        iter = 1
        for obj in listOfObjects:
            document = Document(obj, model.word_wid_map, model.wid_word_map,
                                model.wid_docId, model.word_counter,model.word_)  # creating a document object which will spilt the text and update wordToIdMap, wordList
            if iter%1000 == 0:
                start_time=printExecutionTime(start_time,"Documents "+str(iter))
            model.processDocument(document)
            iter += 1

        # Printing (all) Clusters into File
        f = open(output, "w")
        for d in model.docIdClusId:
            st = ""+str(d)+" "+str(model.docIdClusId[d])+" \n"
            f.write(st)
        for d in model.deletedDocIdClusId:
            st = ""+str(d)+" "+str(model.deletedDocIdClusId[d])+" \n"
            f.write(st)
        f.close()
        print(output)
        printExecutionTime(start_time)

        #Printing Only Active cluster into file
        f = open(output_active, "w")
        for d in model.docIdClusId:
            st = ""+str(d)+" "+str(model.docIdClusId[d])+" \n"
            f.write(st)
        f.close()

        #Printing Only deleted cluster into file
        f = open(output_delete, "w")
        for d in model.deletedDocIdClusId:
            st = ""+str(d)+" "+str(model.deletedDocIdClusId[d])+" \n"
            f.write(st)
        f.close()

        #Printing active cluster wid_word
        f = open(output_active_word_wid_map, "w")
        for word,wid in model.word_wid_map.items():
            st = ""+str(word)+" "+str(wid)+" \n"
            # data=json.dumps(data)
            f.write(st)
        f.close()



        #Printing active cluster_Feature 
        f = open(output_active_cluster, "w")
        for cluster,features in model.clusters.items():
            data={cluster:features}
            data=json.dumps(data)
            # data=json.dumps(cluster)
            f.write(str(data)+"\n")
        f.close()
        
        #Printing delete cluster_Feature 
        f = open(output_delete_cluster, "w")
        for cluster,features in model.deleted_clusters.items():
            data={cluster:features}
            data=json.dumps(data)
            # data=json.dumps(cluster)
            # st = ""+str(word)+" "+str(wid)+" \n"
            f.write(str(data)+"\n")
        f.close()

        #Printing deleted keyword
        f = open(output_delete_cluster_keyword, "w")
        for clusterId,features in model.deleted_clusters_keyword.items():
            delete_keyword=sorted(features.items(), key=lambda z: z[1], reverse=True)
            data={clusterId:delete_keyword}
            data=json.dumps(data)
            f.write(str(data)+"\n")
        f.close()

        #Printing active cluster keyword
        active_cluster_keyword={}
        f = open(output_active_cluster_keyword, "w")
        for clusterId,features in model.clusters.items():
            list_word={}
            for wid , freq in features[1].items():
                word = model.wid_word_map[wid]
                list_word[word]=freq
            active_keyword=sorted(list_word.items(), key=lambda z: z[1], reverse=True)
            
            data={clusterId:active_keyword}
            data=json.dumps(data)
            f.write(str(data)+"\n")     
        f.close()

        #Printing total word
        # f=open(output_word,'w')
        # list_word={}
        # list_word['word']=list(model.word_)
        # data=json.dumps(list_word)
        # f.write(str(data))
        # f.close()

        #Printing 
        
        

    indexOfBeta = -1
    # end of beta loop
#end of alpha loop

printExecutionTime(start_time)

