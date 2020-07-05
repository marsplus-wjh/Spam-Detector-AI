error = 0
total = 0
hamerror = 0
spamerror = 0
with open("./result.txt", encoding="utf8", errors='ignore') as f:
    data = f.read()
    f.close()

dataArr = data.split("\n")
for s in dataArr:
    arr = s.split("  ")
    if arr.__len__() != 1:
        total += 1
        if arr[5] == 'wrong':
            error += 1
        if "ham" in arr[1] and arr[2] == 'spam':
            hamerror += 1
        if "spam" in arr[1] and arr[2] == 'ham':
            spamerror += 1

print("Total Files: " + str(total))
print("Error: " + str(error))
print("Correct: " + str(total - error))
print("\nHam Confusion Matriix: ")
tp = 400 - hamerror
fp = spamerror
fn = hamerror
tn = 400 - spamerror
print("TP: " + str(tp)+ " FP: " + str(fp))
print("FN: " + str(fn) + "   TN: " + str(tn))
precision = round(tp / (tp + fp), 3)
recall = tp / (tp + fn)
f1 = round((2 * precision * recall) / (precision + recall), 3)
print("Accuracy: " + str((total - error) / total) + " Precision: " + str(precision)
      + " Recall: " + str(recall) + " F1: " + str(f1))

print("\nSpam Confusion Matriix: ")
tp = 400 - spamerror
fp = hamerror
fn = spamerror
tn = 400 - hamerror
print("TP: " + str(tp)+ " FP: " + str(fp))
print("FN: " + str(fn) + "   TN: " + str(tn))
precision = round(tp / (tp + fp), 3)
recall = tp / (tp + fn)
f1 = round((2 * precision * recall) / (precision + recall), 3)
print("Accuracy: " + str((total - error) / total) + " Precision: " + str(precision)
      + " Recall: " + str(recall) + " F1: " + str(f1))