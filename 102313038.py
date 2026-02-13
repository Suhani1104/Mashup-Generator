import sys
from mashup_core import create_mashup, MashupError

def main():
    if len(sys.argv) != 5:
        print("Usage: python 102313038.py <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>")
        sys.exit(1)

    singer = sys.argv[1]

    try:
        n = int(sys.argv[2])
        duration = int(sys.argv[3])
    except ValueError:
        print("Error: NumberOfVideos and AudioDuration must be integers.")
        sys.exit(1)

    output_file = sys.argv[4]

    if n <= 10:
        print("Error: NumberOfVideos must be greater than 10.")
        sys.exit(1)

    if duration <= 20:
        print("Error: AudioDuration must be greater than 20 seconds.")
        sys.exit(1)

    try:
        create_mashup(singer, n, duration, output_file)
        print("Mashup created successfully:", output_file)

    except MashupError as e:
        print("Mashup Error:", e)
        sys.exit(1)

    except Exception as e:
        print("Unexpected Error:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
