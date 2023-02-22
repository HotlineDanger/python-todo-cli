import zipfile


def make_archive(filepaths, dest_dir):
    with zipfile.ZipFile(dest_dir + "/" + "compressed_zip", "w") as archive:
        for filepath in filepaths:
            archive.write(filepath)


if __name__ == "__main__":
    make_archive(filepaths=["gui.py", "cli.py"], dest_dir="dest")

