import re, os, math

filePath = './train'
files = os.listdir(filePath)
files.sort()

ham_dic = {}
spam_dic = {}
ham_lines = ""
spam_lines = ""
ham_files_num = 0
spam_files_num = 0
for file in files:
    path = "./train/" + file
    try:
        with open(path, encoding="utf8", errors='ignore') as f:
        #with open(path, encoding='latin-1') as f:
            lines = f.read()
            if file.split("-")[1] == "ham":
                ham_lines += lines
                ham_files_num += 1
            else:
                spam_lines += lines
                spam_files_num += 1
                f.close()
    except:
        continue

ham_arr = re.split('[^a-zA-Z]', ham_lines.lower())
spam_arr = re.split('[^a-zA-Z]', spam_lines.lower())

vocabulary_set = set()
for word in ham_arr:
    if word not in ham_dic:
        ham_dic[word] = 1
    else:
        fre = ham_dic.get(word) + 1
        ham_dic[word] = fre
    vocabulary_set.add(word)

for word in spam_arr:
    if word not in spam_dic:
        spam_dic[word] = 1
    else:
        fre = spam_dic.get(word) + 1
        spam_dic[word] = fre
    vocabulary_set.add(word)

result = []
hamNum = ham_arr.__len__() - ham_dic['']
spamNum = spam_arr.__len__() - spam_dic['']

# Delete white space
vocabulary_set.remove('')

vocabularyNum = vocabulary_set.__len__()

print(hamNum)
print(spamNum)
print(vocabularyNum)

for word in vocabulary_set:
    if word not in ham_dic:
        ham_frequency = 0
        ham_probability = (ham_frequency + 0.5) / (hamNum + (0.5 * vocabularyNum))
    else:
        ham_frequency = ham_dic[word]
        ham_probability = (ham_frequency + 0.5) / (hamNum + (0.5 * vocabularyNum))
    if word not in spam_dic:
        spam_frequency = 0
        spam_probability = (spam_frequency + 0.5) / (spamNum + (0.5 * vocabularyNum))
    else:
        spam_frequency = spam_dic[word]
        spam_probability = (spam_frequency + 0.5) / (spamNum + (0.5 * vocabularyNum))

    result.append([word, ham_frequency, ham_probability, spam_frequency, spam_probability])

result.sort(key=(lambda x:x[0]))
with open("model.txt",mode='w',encoding='utf-8') as model:
    for i in range(0, result.__len__()):
        if i != result.__len__() - 1:
            model.write(str(i + 1) + "  " + result[i][0] + "  " + str(result[i][1]) + "  " + str(result[i][2]) + "  "
                        + str(result[i][3]) + "  " + str(result[i][4]) + "\n")
        else:
            model.write(str(i + 1) + "  " + result[i][0] + "  " + str(result[i][1]) + "  " + str(result[i][2]) + "  "
                        + str(result[i][3]) + "  " + str(result[i][4]))

with open("model.txt") as model:
    modelData = model.read()
modelLines = modelData.split("\n")
voc_dic = {}
for voc in modelLines:
    voc_arr = voc.split("  ")
    voc_dic[voc_arr[1]] = voc_arr

ham_evaluation = []
spam_evaluation = []

testfilePath = './test'
testfiles = os.listdir(testfilePath)
testfiles.sort()

for testfile in testfiles:
    path = "./test/" + testfile
    try:
        dic_test = {}
        with open(path, encoding="utf8", errors='ignore') as f:
            testdata = f.read()
            arr = (re.split('[^a-zA-Z]', testdata.lower()))

            ham_probability = math.log(ham_files_num / ham_files_num + spam_files_num, 10)
            spam_probability = math.log(spam_files_num / ham_files_num + spam_files_num, 10)

            for test_word in arr:
                if test_word in voc_dic:
                    value = voc_dic.get(test_word)
                    ham_probability += math.log(float(value[3]), 10)
                    spam_probability += math.log(float(value[5]), 10)
            if testfile.split("-")[1] == "ham":
                ham_evaluation.append([path, ham_probability, spam_probability])
            else:
                spam_evaluation.append([path, ham_probability, spam_probability])
    except:
        continue


with open("result.txt", mode='w', encoding='utf-8') as result:
    for i in range(0, ham_evaluation.__len__()):
        t_ham = ham_evaluation[i][0]
        ham_prob = ham_evaluation[i][1]
        spam_prob = ham_evaluation[i][2]
        if ham_prob > spam_prob:
            result.write(str(i + 1) + "  " + t_ham[7:] + "  " + "ham" + "  " + str(ham_prob)
                         + "  " + str(spam_prob) + "  " + "right" + "\n")
        else:
            result.write(str(i + 1) + "  " + t_ham[7:] + "  " + "spam" + "  " + str(ham_prob)
                        + "  " + str(spam_prob) + "  " + "wrong" + "\n")
    result.write("\n")
    for i in range(0, spam_evaluation.__len__()):
        t_spam = spam_evaluation[i][0]
        ham_prob = spam_evaluation[i][1]
        spam_prob = spam_evaluation[i][2]
        if ham_prob > spam_prob:
            result.write(str(i + 1 + ham_evaluation.__len__()) + "  " + t_spam[7:] + "  " + "ham" + "  " + str(ham_prob)
                         + "  " + str(spam_prob) + "  " + "wrong" + "\n")
        else:
            result.write(str(i + 1 + ham_evaluation.__len__()) + "  " + t_spam[7:] + "  " + "spam" + "  " + str(ham_prob)
                        + "  " + str(spam_prob) + "  " + "right" + "\n")