import os

def save_transcript(filepath, text):
    base = os.path.basename(filepath).replace(".wav", "")
    out_path = f"transcripts/{base}.txt"
    with open(out_path, "w") as f:
        f.write(text)
