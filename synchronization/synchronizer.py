import os
import shutil
import argparse
import time


def sync_directories(src_dir, dst_dir):
    for root, dirs, files in os.walk(src_dir):
        for directory in dirs:
            src_dir_path = os.path.join(root, directory)
            rel_path = os.path.relpath(src_dir_path, src_dir)
            dst_dir_path = os.path.join(dst_dir, rel_path)
            if not os.path.exists(dst_dir_path):
                os.makedirs(dst_dir_path)  # Create directory
                print(f"Created directory: {dst_dir_path}")

        # Synchronize files
        for file in files:
            src_file_path = os.path.join(root, file)
            rel_path = os.path.relpath(src_file_path, src_dir)
            dst_file_path = os.path.join(dst_dir, rel_path)

            # Check if the file needs to be copied (doesn't exist or is newer)
            if not os.path.exists(dst_file_path) or os.path.getmtime(src_file_path) > os.path.getmtime(dst_file_path):
                # Ensure destination directory exists
                os.makedirs(os.path.dirname(dst_file_path), exist_ok=True)
                shutil.copy2(src_file_path, dst_file_path)  # Copy file
                print(f"Copied/Updated file: {src_file_path} -> {dst_file_path}")

    # Cleanup: Delete files/directories in destination that are not in source
    for root, dirs, files in os.walk(dst_dir):
        for file in files:
            dst_file_path = os.path.join(root, file)
            rel_path = os.path.relpath(dst_file_path, dst_dir)
            src_file_path = os.path.join(src_dir, rel_path)

            if not os.path.exists(src_file_path):
                os.remove(dst_file_path)
                print(f"Deleted file: {dst_file_path}")

        for directory in dirs:
            dst_dir_path = os.path.join(root, directory)
            rel_path = os.path.relpath(dst_dir_path, dst_dir)
            src_dir_path = os.path.join(src_dir, rel_path)

            if not os.path.exists(src_dir_path):
                shutil.rmtree(dst_dir_path)
                print(f"Deleted directory: {dst_dir_path}")


def periodic_sync(src_dir, dst_dir, interval):
    print(f"Starting periodic synchronization every {interval} seconds...")
    while True:
        sync_directories(src_dir, dst_dir)
        print("Synchronization complete. Waiting for the next interval...")
        time.sleep(interval)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Periodically synchronize directories.")
    parser.add_argument('source', help='Source directory path')
    parser.add_argument('check_path', help='Path to the replica directory')
    parser.add_argument('interval', type=int, help='Time interval in seconds for synchronization')

    args = parser.parse_args()

    source_folder = args.source
    check_path = args.check_path
    sync_interval = args.interval

    # Check and create destination directory if it doesn't exist
    if not os.path.exists(source_folder):
        print(f"Source directory '{source_folder}' does not exist.")
        exit(1)

    if not os.path.exists(check_path):
        os.makedirs(check_path)
        print(f"Created destination directory: {check_path}")

    periodic_sync(source_folder, check_path, sync_interval)
