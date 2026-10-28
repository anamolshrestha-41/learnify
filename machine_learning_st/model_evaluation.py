from sklearn.metrics import confusion_matrix, accuracy_score,  precision_score, recall_score, f1_score

y_true=(
    [1]*36 + [0]*64
)
y_pred=(
    [1]*24 + [0]*12+
    [1]*8 + [0]*56
)
confusion= confusion_matrix(y_true, y_pred)
accuracy= accuracy_score(y_true, y_pred)

print(f"Confusion Matrix: {confusion}")
print(f"Accuracy Score: {accuracy * 100}%")

y_true_1=(
    [1]*60 + [0]*140
)
y_pred_1=(
    [1]*42 + [0]*18+
    [1]*8 + [0]*132
)

print(f"Precision: {precision_score(y_true_1, y_pred_1)*100}%")
print(f"Recall: {recall_score(y_true_1, y_pred_1)*100}%")
print(f"f1_score: {f1_score(y_true_1, y_pred_1)*100}%")