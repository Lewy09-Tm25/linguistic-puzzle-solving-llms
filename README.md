
# Multilingual problem solving abilities and reasoning of Large Language Models

#### Aim
The aim of this work is to understand how good the LLMs are at solving school-level linguistic olympiad puzzles, like [UKLO](https://www.uklo.org/past-exam-papers/).

#### Web scraping
The first and foremost task is to scrape the questions and answers that are part of one single pdf for each round in an year. The website has details of all the rounds like the difficulty level, subjects, question formats, theme, language family, authors, and a link for the pdf of that round.
```
web_scraping.py
```

#### Splitting
After scraping the data and ingesting it into a dataframe, the next task was to split one pdf into the questions and their corresponding answers. Each pdf has the answers followed by the questions.
```
pdf_Q_and_A_splitting.ipynb
```

#### Experiments
There were 3 different versions of experiments conducted. Direct prompting to GPT 4o mini with text and images as inputs. GPT 3.5 was also used by creating a RAG (Retrieval-Augmented Generation) framework with LlamaIndex.
```
pdf_ques_to_imgs.ipynb
search_and_RAG/UKLO_GPT4o_mini.ipynb
search_and_RAG/UKLO_GPT3_5_GPT4_text.ipynb
```
