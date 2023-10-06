# Import the warnings module
import warnings

# Suppress the FutureWarning for the n_init parameter
warnings.filterwarnings("ignore", category=FutureWarning)

from summarizer import Summarizer,TransformerSummarizer
from transformers import T5Tokenizer, TFT5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained('SJ-Ray/Re-Punctuate')
model = TFT5ForConditionalGeneration.from_pretrained('SJ-Ray/Re-Punctuate')

input_text = """what is time dilation will according to Einstein special theory of relativity the difference in the ellipse time as measured by two clocks is called time dilation simply remember that time dilation is the slowing down of time in different frame of reference time dilation occurs due to difference in relative velocity and difference in gravitational field for example consider a man standing on the earth and another man travelling in the space shape let the time on the earth is 5 and the time in the space ship is also 5 o'clock in physics the man standing on the earth is one frame of reference and the main travelling in the space ship is another frame of reference the time appears normal for both men and their respective frame of reference I mean for the man standing on the earth the time is 5:00"""
inputs = tokenizer.encode("punctuate: " + input_text, return_tensors="tf") 
result = model.generate(inputs)

decoded_output = tokenizer.decode(result[0], skip_special_tokens=True)

body = decoded_output
def  summarizer():
    GPT2_model = TransformerSummarizer(transformer_type="GPT2",transformer_model_key="gpt2-medium")
    full = ''.join(GPT2_model(body))
    return full

print(summarizer())