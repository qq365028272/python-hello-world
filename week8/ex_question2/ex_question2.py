import urllib.request
url = "file:///Users/bohengwang/Desktop/VSCODEPROJECT/week8/ex_question2/textfile.txt"
response = urllib.request.urlopen(url)
data = response.read()
text = data.decode("utf-8")

with open("/Users/bohengwang/Desktop/VSCODEPROJECT/week8/ex_question2/blocked_words.txt", mode ='r') as blocked_words:
    block_word = []
    for words in blocked_words:
        if words in text:
            block_word.append(words)

print(block_word)


