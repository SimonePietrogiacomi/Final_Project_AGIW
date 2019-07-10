#!/usr/bin/env python3

import csv

# TODO aggiorna queste due stringhe con i nomi dei file corretti
output_jedai_file_name = "file_output_jedai.csv"
gt_file_name = "file_gt.csv"

output_file_list = []
output_file_list_evaluation = {}

counter_TP = 0
counter_FP = 0
counter_TN = 0
counter_FN = 0

with open(output_jedai_file_name, mode="r") as output_file:
    output_reader = csv.reader(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    # skip first 3 rows where is located precision, recall and f-measure
    for _ in range(3):
        next(output_reader)
    for output_row in output_reader:
        output_file_list.append((output_row[0], output_row[1]))
        output_file_list_evaluation[(output_row[0], output_row[1])] = output_row[2]

        if output_row[2] == "TP":
            counter_TP += 1
        if output_row[2] == "FP":
            counter_FP += 1
        if output_row[2] == "TN":
            counter_TN += 1
        if output_row[2] == "FN":
            counter_FN += 1

output_file_length = len(output_file_list)

print("Lettura file di output di JedAI completata, sono state trovate " + str(output_file_length) + " righe")

with open(gt_file_name, mode="r") as gt:
    gt_reader = csv.reader(gt, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    gt_row_count = sum(1 for row in gt_reader) - 1

print("Numero di righe della GT pari a " + str(gt_row_count))

pair_in_match = 0
pair_in_match_tp = 0
gt_length = 0

with open(gt_file_name, mode="r") as gt:
    gt_reader = csv.reader(gt, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    # Skip first line, the one with the meaning of the column
    next(gt_reader)
    for gt_row in gt_reader:
        if gt_length % 500 == 0:
            print("-.-.-.-.-.-.-")
            print("Lettura riga " + str(gt_length) + " di " + str(gt_row_count))
            print("Coppie in match trovate finora: " + str(pair_in_match))
        gt_length += 1
        if (gt_row[0], gt_row[1]) in output_file_list:
            # output_file_list.remove(gt_row)
            pair_in_match += 1
            if output_file_list_evaluation[(gt_row[0], gt_row[1])] == "TP":
                pair_in_match_tp += 1
            # print(pair_in_match)

print("\n")

print("Esecuzione completata, il numero di coppie in match è " + str(pair_in_match))

precision = pair_in_match / output_file_length
recall = pair_in_match / gt_length

print("\n")

print("Precision: " + str(precision) + "\nRecall: " + str(recall))

print("\n")

print("Il numero di coppie IN MATCH con la ground truth segnate come TP è " + str(pair_in_match_tp))

print("\n")

print("Di seguito il numero di coppie su tutto il file, quindi NON NECESSARIAMENTE IN MATCH con la ground truth "
      "segnate come True Positive, False Positive, True Negative e False Negative")

print("TP: " + str(counter_TP) + "\nFP: " + str(counter_FP) + "\nTN: " + str(counter_TN) + "\nFN: " + str(counter_FN))
# print("Total: " + str(counter_FN + counter_TN + counter_FP + counter_TP))
