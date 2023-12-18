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

Analyse_Annotation.py creates statistics for the annotations. More specifically it creates two files, the first contains the frequency of each annotation and the second the frequency of each annotation per phrase. 
The code has 5 arguments:
1. Data path: The path to the folder with the CSV files, or a folder containing multiple subfolders with CSV files
2. Save path: The path where the export data will be saved
3. Translation (True/False)
4. Annotation Curation (True/False)
5. Phrases Curation (True/False)

To run the code execute:
```
python Codes\Analyse_Annotation.py <data path> <save path> <translation> <annot curation> <phrase curation>

```

The code will request a CSV file if any of the 3 arguments about the translation and curation are True. The CSV file must contain a column with the annotations values or the phrases and a second column with the translation or curations.

---
To create these files the code Extract_Unique_ValuesText.py can create 2 CSV with the unique annotation values and phrases.
The code has 2 arguments:
1. Data path: The path to the folder with the CSV files, or a folder containing multiple subfolders with CSV files
2. Save path: The path where the export data will be saved

To run the code execute:
```
python Codes\Extract_Unique_ValuesText.py <data path> <save path> 

```

Using these files you can manually add the curations or translations in the second column.

---
The code Count_Values_Per_Character.py categorised the annotation using a second annotation file. This file splits the entire text into labels. A use case is to label the phrases with the name of the character that speaks. In this use case, the final file has the annotated values for each character.
The code has 4 arguments:
1. Data path: The path to the folder with the CSV files, or a folder containing multiple subfolders with CSV files
2. Save path: The path where the export data will be saved
3. Translation (True/False)
4. Annotation Curation (True/False)

The code will request the CSV file containing the text annotation. This file can be created by annotating the text into the Ellegon exported and use the Ellegon_Json_to_Csv code.

---










