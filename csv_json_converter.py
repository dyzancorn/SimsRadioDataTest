import csv
import json


def csv_to_json(csv_file_path: str, json_file_path: str):
    ''' Converts a CSV file to JSON file in the format required for the SimsRadio website '''

    with open(csv_file_path, mode='r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        data = []
        for row in csv_reader:
            song_object = {
                "description": row["Artist"],
                "filename": row["Name"],
                "mark": row["Icon"],
                "youtube": row["YouTube"][-11:],
                "songType": row["Song Type"],
                "originalSong": row["Original Song"][-11:],
                "pack": row["Pack"]
            }

            metadata = {
                "albumArtist": row["Game"],
                "artist": row["Artist"],
                "title": row["Name"],
                "year":  row["Release"][0:4]
            }
            source = {
                "client": row["Game"],
                "date": row["Release"],
                "structure": row["Radio Station"]
            }

            song_object["metadata"] = metadata
            song_object["source"] = source

            data.append(song_object)
        
    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file)
        
    print(f"CSV file '{csv_file_path}' successfully converted to JSON file '{json_file_path}'")

def main():
    csv_file_path = 'Sims Radio Music.csv'
    json_file_path = 'simsRadioData.json'
    csv_to_json(csv_file_path, json_file_path)

if __name__ == "__main__":
    main()

