import argparse
import os
import shutil

N = 3


def move_files(abs_dirname):
    """Move files into subdirectories."""

    files = [os.path.join(abs_dirname, f) for f in os.listdir(abs_dirname)]

    i = 0
    curr_subdir = None

    for f in files:
        # create new subdir if necessary
        if i % N == 0:
            subdir_name = os.path.join(abs_dirname, '{0:03d}'.format(i // N + 1))
            os.mkdir(subdir_name)
            curr_subdir = subdir_name

        # move file to current dir
        f_base = os.path.basename(f)
        shutil.move(f, os.path.join(subdir_name, f_base))
        i += 1


def parse_args():
    """Parse command line arguments passed to script invocation."""
    parser = argparse.ArgumentParser(
        description='Split files into multiple subfolders.')

    parser.add_argument('src_dir', help='source directory')

    return parser.parse_args()


def main():
    """Module's main entry point (zopectl.command)."""
    args = parse_args()
    src_dir = args.src_dir

    if not os.path.exists(src_dir):
        raise Exception('Directory does not exist ({0}).'.format(src_dir))

    move_files(os.path.abspath(src_dir))

    chunk_folders = os.listdir(src_dir)
    chunk_folders = [p for p in chunk_folders if os.path.isdir(os.path.join(src_dir, p))]
    print("Created Chunk Folder(s) ", chunk_folders)

    for chunk in chunk_folders:
        content_folder = os.listdir(f"{src_dir}/{chunk}")
        content_folder = [p for p in content_folder if os.path.isdir(os.path.join(f"{src_dir}/{chunk}", p))]
        print(f"Content in Chunk Folder #{chunk}", content_folder)


if __name__ == '__main__':
    main()
