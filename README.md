# Spam Detector AI
This is a instance of Bayesian.
Totally, 800 files divided 400 ham and 400 spam files. There are 6 errors in ham class and 64 errors in spam class in our programme.
 
Ham Confusion Matrix:
 
Accuracy	(394 + 336) / 800	0.9125
Precision	TP / (TP + FP) = 394 / (394 + 64)	0.86
Recall	TP / (TP + FN) = 394 / (394 + 6)	0.985
F1-measure	2 * Precision * Recall / (Precision + Recall)	0.918


Spam Confusion Matrix:
 
Accuracy	(394 + 336) / 800	0.9125
Precision	TP / (TP + FP) = 336 / (336 + 6)	0.982
Recall	TP / (TP + FN) = 336 / (336 + 64)	0.84
F1-measure	2 * Precision * Recall / (Precision + Recall)	0.905
In the result.txt which we generated, we collected predicted results are “ham” file in ham class as TP for ham class, “spam” predicted results which are in ham class as FN, “ham” predicted results are in the not ham class (spam) as FP and “not ham” (spam) predicted results are in the “not ham” (spam) class as TN.

Then, we collected predicted results are “spam” file in spam class as TP for spam class, predicted “ham” in spam class as FN, predicted “spam” in ham class as FP, and finally, “ham” predicted results in ham class as TN.

Finally, we applied several formulas to get accuracy, precision, recall and F1-measure for each class, ham and spam.

