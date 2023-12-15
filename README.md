# Ellegon-annotation-Analysis
This repository focuses on the extraction and analysis of the annotation data from the Ellegon annotation tool.
This analysis is used on the findings of >>>

---

To run the scripts first install the required Python packages
```
pip install requirements.txt
```
---

The Ellegon_Json_to_Csv.py generates CSV files of the annotations using the JSON file extracted from a collection in Ellegon. If the collection includes multiple annotated files the code will create a CSV file for each, if the name is the same to all a number will be added to prevent overwrites. If in a file in the collection there are multiple annotators, a single file will be created with all the annotations. 

To run the code there are 2 arguments:
1. Data path: The path to the JSON file or folder with  multiple JSON files
2. Save path: The path where the export data will be saved

To run the code execute: 

```
python Codes\Ellegon_Json_to_Csv.py <path to JSON/Folder> <path to save folder>
```
The export files for each annotation have the following format:

|text |start point |end point |annotation|
|---|---|---|---|
---






