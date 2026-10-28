from sklearn.metrics import confusion_matrix, accuracy_score

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