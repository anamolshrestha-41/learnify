from sklearn.metrics import confusion_matrix, accuracy_score,  precision_score, recall_score, f1_score, classification_report, precision_recall_curve, average_precision_score
import matplotlib.pyplot as plt
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

import numpy as np
y_true_2=np.array([
    1,1,1,1,1,
    0,0,0,0,0
])
y_prob=np.array([
    0.95, 0.85, 0.70, 0.45, 0.25,
    0.90, 0.60, 0.35, 0.20, 0.10
])
thresh=0.5
y_pred_2=(y_prob>=thresh).astype(int)
classification= classification_report(y_true_2, y_pred_2)
print(classification)

for threshold in [0.3, 0.5, 0.7]:
    y_pred_3=(y_prob>=threshold).astype(int)
    precision, recall, thresholds= precision_recall_curve(y_true_2, y_pred_3)
    average_precision= average_precision_score(y_true_2, y_pred_3)
    plt.plot(recall, precision, marker=".")
    plt.title(f"Futsal Goal Prediction - PR Curve {average_precision:.2f}")
    plt.xlabel("Recall")
    plt.ylabel("Precision")
    plt.grid(True)
    plt.show()
    plt.close()
    print(f"Average Precision: ", round(average_precision,3))