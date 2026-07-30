import matplotlib.pyplot as plt
import os

os.makedirs("reports/plots", exist_ok=True)

def plot_studyHrs(data):
    plt.figure(figsize=(8,5))
    plt.hist(data[:,1], bins=10)
    plt.title("Study Hours Distribution")
    plt.xlabel("Hours")
    plt.ylabel("Students")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("reports/plots/study_hrs.png", dpi=300, bbox_inches="tight")
    plt.show()
    plt.close()
    #studyhrs vs final marks
    plt.figure(figsize=(8,5))
    plt.scatter(data[:,1], data[:,7])
    plt.xlabel('Study Hrs')
    plt.ylabel('Final Marks')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("reports/plots/studyVsfinalMarks.png", dpi=300, bbox_inches="tight")
    plt.show()
    plt.show()
    #attendance vs final marks
    plt.figure(figsize=(8,5))
    plt.scatter(data[:,1].astype(float), data[:,7].astype(float))
    plt.xlabel("Attendance(%)")
    plt.ylabel("Final Marks")
    plt.title("Attendance vs Final Marks")
    plt.tight_layout()
    plt.savefig("reports/plots/attendanceVsFinal.png", dpi=300, bbox_inches="tight")
    plt.show()
    plt.close()

    print("All plots saved successfully in reports/plots")