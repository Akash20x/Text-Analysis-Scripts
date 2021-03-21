from wordhoard import synonyms
from nltk.corpus import wordnet as wn
import random
def get_synonyms(word):
    synonyms=[]
    for synset in wn.synsets(word):
        for lemma in synset.lemmas():
            if lemma:
                synonyms.append(lemma.name())
    return list(set(synonyms))

def get_example(word):
    synset=wn.synsets(word)
    if synset:
        return synset[0].examples()
    else:
        return None

word_to_find="book"
try:	
	synonym_01 = synonyms.query_synonym_com(word_to_find)
	synonym_02 = synonyms.query_thesaurus_com(word_to_find)
	synonym_03 = synonyms.query_thesaurus_plus(word_to_find)		
	synonym_04=get_synonyms(word_to_find)

	synonym_results = sorted(set([y for x in [ synonym_01, synonym_02, synonym_03,synonym_04] for y in x]))
    
	synonyms1=""
	for w in synonym_results:
		synonyms1+=w+" "
	words = list(map(str, synonyms1.split()))
	synonyms2=random.sample(words,4)

	final=""
	for f in synonyms2:
		final+=f+","

	example=get_example(word_to_find)
	ex=""
	for x in example:
		ex=x+""

	synonyms=final+ex

except:
	final="Not Found"
print(synonyms)

#Sample Output:compendium,album,record,book,I am reading a good book on economics

