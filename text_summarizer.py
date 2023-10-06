import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
from transformers import T5Tokenizer, TFT5ForConditionalGeneration
from summarizer import Summarizer,TransformerSummarizer

tokenizer = T5Tokenizer.from_pretrained('SJ-Ray/Re-Punctuate')
model = TFT5ForConditionalGeneration.from_pretrained('SJ-Ray/Re-Punctuate')

test = ""

def punctuator(input_text):
  inputs = tokenizer.encode("punctuate: " + input_text, return_tensors="tf") 
  result = model.generate(inputs)
  decoded_output = tokenizer.decode(result[0], skip_special_tokens=True)
  return decoded_output

def summarizer_extractive(test):
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
  final_summary= [word.text for word in summary]
  summary = ' '.join(final_summary)
  return summary

def summarizer_abstractive(test):
    GPT2_model = TransformerSummarizer(transformer_type="GPT2",transformer_model_key="gpt2-medium")
    summary = ''.join(GPT2_model(test))
    return summary