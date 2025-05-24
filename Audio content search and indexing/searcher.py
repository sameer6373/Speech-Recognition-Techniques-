import os

def search_in_transcripts(keyword):
    results = {}
    for file in os.listdir("transcripts"):
        with open(f"transcripts/{file}", "r") as f:
            lines = f.readlines()
            matches = [line for line in lines if keyword.lower() in line.lower()]
            if matches:
                results[file] = matches
    return results
