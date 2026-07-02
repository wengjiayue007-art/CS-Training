#文件信息统计

from pathlib import Path

def get_file_info(path):
    """
    Analyze a file.

    Args:
        path:(Path):file path

    Returns:
        dict:file statistics
    """
    file_info={}
    file_info['filename']=path.name
    file_info['Extension']=path.suffix
    file_info['Size']=path.stat().st_size
    line_count=0
    word_count=0
    character_count=0
    with open(path) as file:
        for line in file:
            line_count+=1
            for word in line.split():
                word_count+=1
                character_count+=len(word)
    file_info['Lines']=line_count
    file_info['Words']=word_count
    file_info['Characters']=character_count
    return file_info
    
def get_dir_info(path):
    """
    Analyze all files in a directory.

    Args:
        path(Path):directory path

    Returns:
        dict:file type statistics
    """
    dir_info={}
    for item in path.rglob('*'):
        #if item.is_dir():
        #    dir_info['{directory}'] = dir_info.get('{directory}', 0) + 1
        if item.is_file():
            suffix=item.suffix
            if suffix:
                dir_info[suffix] = dir_info.get(suffix, 0) + 1
            else:
                dir_info['{no extension}'] = dir_info.get('{no extension}', 0) + 1
    return dir_info

def main():
    path_str=input("Please enter a path:")
    path=Path(path_str)
    if not path.exists():
        raise FileNotFoundError(f"路径或文件不存在: {path_str}")
    if path.is_dir():
        print("Start analyzing directory...")
        info=get_dir_info(path)
    elif path.is_file():
        print("Start analyzing file...")
        info=get_dir_info(path)
    print(info)


if __name__ == "__main__":
    main()