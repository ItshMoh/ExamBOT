# qa_pairs = []
# with open("/home/kayden/Desktop/python_projects/ExamBOT/rust_qa.txt", "r") as f:
#     content = f.read()
    
# # Split by double newlines to separate QA pairs
# raw_pairs = content.split("\n\n")
    
# for pair in raw_pairs:
#     lines = pair.split("\n", 1)  # Split only at the first newline
#     if len(lines) == 2:
#         question = lines[0]
#         answer = lines[1]
#         qa_pairs.append({"question": question, "answer": answer})


import csv

qa_pairs = []

with open("/home/kayden/Desktop/python_projects/ExamBOT/dataset/kubernetes_qa.csv", "r", encoding="utf-8") as f:
    csv_reader = csv.DictReader(f)
    
    for row in csv_reader:
        qa_pairs.append({
            "question": row["question"],
            "answer": row["answer"],
            "topic": row["topic"],
            "type": row["type"],
            "difficulty": row["difficulty"]
        })