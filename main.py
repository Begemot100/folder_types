import os
import shutil

def move_pdf():
    path_to_new_folder = os.path.join(os.getcwd(), 'PDFINHERE')
    os.makedirs(path_to_new_folder, exist_ok=True)
    for f in os.listdir():
        if f.endswith('.pdf'):
            current_file = os.path.join(os.getcwd(), f)
            shutil.move(current_file, path_to_new_folder)
            print("Success")

def find_all_extensions():
    extensions = set()
    for f in os.listdir():
        _, ext = os.path.splitext(f)
        if ext:
            extensions.add(ext[1:].lower())
    return extensions

def combine_files_by_extension(file_extensions, target_folder):
    new_folder_path = os.path.join(os.getcwd(), target_folder)
    os.makedirs(new_folder_path, exist_ok=True)
    for f in os.listdir():
        _, ext = os.path.splitext(f)
        if ext[1:].lower() in file_extensions:
            current_file = os.path.join(os.getcwd(), f)
            shutil.move(current_file, new_folder_path)
            print("Success")

if __name__ == '__main__':
    os.chdir('/Users/begemot')

    move_pdf()

    picture_extensions = {'jpeg', 'jpg', 'png'}
    combine_files_by_extension(picture_extensions, 'Photos')

    linux_windows_extensions = {'bin', 'deb', 'exe', 'zip', 'rpm', 'gz', 'xz'}
    combine_files_by_extension(linux_windows_extensions, 'Linux_And_Temp_Executable_Files')

    ppt_doc_extensions = {'doc', 'odt', 'ppt', 'pptx'}
    combine_files_by_extension(ppt_doc_extensions, 'PPTS_AND_DOCS')

    all_extensions = find_all_extensions()
    print(all_extensions)
