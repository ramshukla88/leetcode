from sklearn.metrics import precision_score, recall_score

y_true = [0, 1, 2, 0, 1, 2]
y_pred = [0, 1, 2, 0, 0, 1]

precision = precision_score(y_true, y_pred, average='macro')
recall = recall_score(y_true, y_pred, average='macro')

print(f'Precision: {precision:.2f}')
print(f'Recall: {recall:.2f}')