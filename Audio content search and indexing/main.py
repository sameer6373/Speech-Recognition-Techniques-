from transcriber import transcribe_audio
from indexer import save_transcript
from searcher import search_in_transcripts

if __name__ == "__main__":
    file = "audio_files/sample1.wav"
    print("[INFO] Transcribing audio...")
    transcript = transcribe_audio(file)
    save_transcript(file, transcript)
    
    print("\n[INFO] Searching for a keyword...")
    keyword = input("Enter a keyword to search: ")
    results = search_in_transcripts(keyword)
    
    if results:
        print("\n[RESULTS]")
        for file, matches in results.items():
            print(f"- {file}:")
            for line in matches:
                print(f"  -> {line.strip()}")
    else:
        print("No matches found.")
