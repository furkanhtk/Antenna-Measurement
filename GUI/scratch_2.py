import os,sys

sys.path.append(r'C:\Users\Furkan\Desktop\ANTENNA MEASUREMENT SYSTEM\csv')
csv_path = os.path.realpath(".\.\csv")
csvs = os.listdir(csv_path)

print(csvs)