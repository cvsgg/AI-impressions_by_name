# AI-impressions_by_name
Functions using AI (openai library) to recognize Proper Names in a request text and return what comments there are about them.

![FlowchartAI](https://github.com/cvsgg/AI-impressions_by_name/assets/110683021/a8f53b5f-de08-49ce-be43-be81d2b80fde)

The functions can extracts a text in some website, using the BeautifulSoup library, identify the Proper Names was mentioned on there 
using the Spacy library, and requests to AI Openai to identify what comments is saying about the Name. Then it going to return us
a python dictionary with this data.

*Please, you'll need to get your api_key on Openai and put as a string on 'parameters.py'
*You can also put on 'parameters.py' the website url that you want to request the text

This is a start in a brainstorm to explore how a AI can help a Data Engineer to collect relevant data about anything, and put this
in a minimal structure level, making it possible to analyse.
