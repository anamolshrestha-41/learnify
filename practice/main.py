from src.generateData import generate_data
from src.loadData import load_dataset
from src.preprocessing import preprocess
from src.featureEngineering import feature_engineering
from src.statistics import statistics_data
from src.visualization import plot_studyHrs
from src.analysis import analysis_data
from src.saveData import save_dataset

def main():
    generate_data()
    data= load_dataset()
    data= preprocess(data)
    statistics_data(data)
    data=feature_engineering(data)
    plot_studyHrs(data)
    analysis_data(data)
    save_dataset(data)

if __name__=='__main__':
    main()