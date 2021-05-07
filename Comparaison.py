# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
from io import StringIO

with open('C:\\Users\\Baptiste\\Desktop\\Travail\\Stage reverso\\testlogs.csv', 'r', encoding='utf8') as in_file:
    for i in range(32,123):
        contents = in_file.read().replace("\n"+chr(i),' ')
print(data)


punctuation = {' ',';',',',':','.','?','!',"\n",'/'}

def search_word(sentence,idx):
    if sentence[idx] not in punctuation :
        begin = idx
        end=idx
        while begin>0 and sentence[begin] not in punctuation :
            begin-=1
        while end<len(sentence)-1 and sentence[end] not in punctuation:
            end+=1
        if sentence[begin] in punctuation :
            if sentence[end] in punctuation :
                return sentence[begin+1:end], begin+1
            return sentence[begin+1:end+1], begin+1
        else :
            if sentence[end] in punctuation :
                return sentence[begin:end], begin
            return sentence[begin:end+1], begin
    else :
        if idx==0:
            return sentence[idx]+search_word(sentence[idx+1:],0)[0], 1+search_word(sentence[idx+1:],0)[1]
        if idx == len(sentence)-1 :
            return search_word(sentence[:idx],idx-1)[0]+sentence[idx], search_word(sentence[:idx],idx-1)[1]
        return search_word(sentence[:idx],idx-1)[0]+sentence[idx]+search_word(sentence[idx+1:],0)[0], search_word(sentence[:idx],idx-1)[1]
    

def comparaison(DataFrame):
    mistakes = pd.DataFrame(columns = ['mistake','correction', 'input_id'])
    for ind,row in DataFrame.iterrows() :
        index = int(row['id'])
        falt = row['initial_text']
        correct = row['corrected_text']
        i = 0
        j = 0 
        while i<len(correct) and j<len(falt):
            if(falt[j]!=correct[i]) :
                mist = search_word(falt,i)
                corr = search_word(correct,j)
                mistake = mist[0]
                correction = corr[0]
                mistakes = mistakes.append({'mistake': mistake,'correction': correction, 'input_id':index},ignore_index=True)
                i+=len(correction)-mist[1]
                j+=len(mistake)-corr[1]
            else :
                i+=1
                j+=1
    return mistakes.to_csv('mistakes.csv',index=False)
    
    
print(contents)
#comparaison(data)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    