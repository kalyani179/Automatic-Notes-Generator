import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

test = """A black hole is a fascinating and enigmatic celestial object in the universe. It's formed from the remnants of massive stars that have undergone a supernova explosion. What makes black holes unique is their incredibly strong gravitational pull, so intense that nothing, not even light, can escape from their grasp. This property is often described as an "event horizon," a boundary beyond which anything is inexorably drawn into the black hole.

Black holes come in different sizes, ranging from stellar-mass black holes, which are several times the mass of our Sun, to supermassive black holes found at the centers of galaxies, which can be millions or even billions of times the mass of the Sun. These supermassive black holes play a crucial role in the formation and evolution of galaxies.

The study of black holes has opened up new avenues for understanding the fundamental principles of physics, particularly in the realms of general relativity and quantum mechanics. Black holes have been the subject of intense scientific research and have captured the public's imagination, leading to numerous depictions in popular culture.

Recent advancements in astrophysical observations, such as the detection of gravitational waves from merging black holes, have provided unprecedented insights into these cosmic enigmas. They continue to be a subject of great intrigue and exploration in the field of astrophysics."""

def summarizer():
  stopwords = list(STOP_WORDS)
  # print(stopwords)
  # print(punctuation)
  nlp = spacy.load("en_core_web_sm")
  doc = nlp(test)
  word_freq={}
  for token in doc:
    word = token.text
    if(word.lower() not in stopwords and word.lower() not in punctuation):
      # print(word,end=" ")
      if word in word_freq.keys():
        word_freq[word]+=1
      else:
        word_freq[word]=1
  # print(word_freq)
  max_freq = max(word_freq.values())
  # print(max_freq)

  # Noramlizing the frequencies (dividing the frequencies with the maxFrequency)
  for word in word_freq.keys():
    word_freq[word] = word_freq[word]/max_freq
  # print(word_freq)


  #sentences
  sent_tokens = [sent for sent in doc.sents]
  sent_scores = {}
  for sent in doc.sents:
    for token in sent:
      word = token.text
      if(word in word_freq.keys()):
        if sent not in sent_scores.keys():
          sent_scores[sent] = word_freq[word]
        else:
          sent_scores[sent] += word_freq[word]

  #print(sent_scores)


  select_len = int(len(sent_tokens) * 0.3)
  summary = nlargest(select_len,sent_scores,key=sent_scores.get)
  res = ""
  for word in summary:
    res+=word.text
  print(res)
  return res


