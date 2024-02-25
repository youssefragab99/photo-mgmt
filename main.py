import os 
import datetime as dt
import sys

arg1 = sys.argv[1]

src = f"/Volumes/sandisk/Photography/{arg1}"

jpeg_src = f"{src}/Jpeg"
raw_src = f"{src}/Raw"


def main():
    today = dt.date.today()
    print(today)

    jpeg_files = [filename.strip(".JPG") for filename in os.listdir(jpeg_src)]
    jpeg_files = [filename for filename in jpeg_files if ".xmp" not in filename]

    raw_files = [filename.strip(".RAF") for filename in os.listdir(raw_src)]
    raw_files = [filename for filename in raw_files if ".xmp" not in filename]

    missing_files = [filename for filename in raw_files if filename not in jpeg_files]

    # Remove files containing ".xmp" in filename

    print(f"Missing files: {missing_files} ")
    for filename in missing_files:
        os.remove(os.path.join(raw_src, f"{filename}.RAF"))


if __name__ == "__main__":
    main()
