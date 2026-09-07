# import os
import pandas as pd
import matplotlib.pyplot as plt

def main():
    # Load the dataset
    file_path= "data/dataset.csv"
    df= pd.read_csv(file_path)

    months=df["Month"]
    attendance=df["Attendance"]
    grade=df["Average_Grade"]
    
    #Attendance line chart
    fig= plt.figure(figsize=(10, 5))
    ax= fig.add_subplot(111)
#     111
# ││└── position
# │└─── number of columns
# └──── number of rows
    ax.plot(months, attendance, label="Attendance", linewidth=2)
    ax.set_title("Monthly Attendance")
    ax.set_xlabel("Months")
    ax.set_ylabel("Attendance (%)")
    ax.legend()
    plt.tight_layout()
    plt.savefig("graphs/attendance_line.png")
    plt.show()
    plt.close()

    #Grade line chart
    fig= plt.figure(figsize=(10, 5))
    ax= fig.add_subplot(111)
    ax.plot(months, grade, label="Average Grade")
    ax.set_title("Monthly Average Grade")
    ax.set_xlabel("Months")
    ax.set_ylabel("Average Grade")
    ax.legend()
    plt.tight_layout()
    plt.savefig("graphs/grade_line.png")
    plt.show()
    plt.close()

    #Combined line  chart
    fig= plt.figure(figsize=(10, 5))
    ax= fig.add_subplot(111)
    ax.plot(months, attendance, label="Attendance")
    ax.plot(months, grade, label="Average Grade")
    ax.set_title("Monthly Attendance and Average Grade")
    ax.set_xlabel("Months")
    ax.set_ylabel("Values")
    ax.legend()
    plt.tight_layout()
    plt.savefig("graphs/combined_line.png")
    plt.show()
    plt.close()

    #Twinx Axis chart
    fig, ax1= plt.subplots(figsize=(10, 5))
    ax2=ax1.twinx()
    ax1.plot(months, attendance, label="Attendance")
    ax1.set_xlabel("Months")
    ax1.set_ylabel("Attendance (%)", color="blue")
    ax2.plot(months, grade, label="Average Grade", color="orange")    
    ax2.set_ylabel("Average Grade", color="orange")
    ax2.set_title("Attendance and Average Grade with Twin Axes")

    #combine legends from both axes
    lines1, labels1= ax1.get_legend_handles_labels()
    lines2, labels2= ax2.get_legend_handles_labels()

    ax1.legend(lines1+ lines2, labels1+ labels2, loc="upper left")

    plt.tight_layout()
    plt.savefig("graphs/twinx_chart.png")
    plt.show()
    plt.close()


if __name__ == "__main__":
    main()