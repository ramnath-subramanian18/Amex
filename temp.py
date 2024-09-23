from transformers import pipeline
print("temp")
classifier = pipeline("zero-shot-classification")

sentence = "WM SUPERCENTER #1117 6001 N CENTRAL EXPY PLANO 75023 TX USA"
labels = ["petrol", "grocery", "housing", "Dinning"]

result = classifier(sentence, candidate_labels=labels)
print((result))
