import toml  # 需要先安裝: pip install toml


def read_toml(file_path):
    try:
        data = toml.load(file_path)
        return data
    except Exception as e:
        raise ImportError(f"Error reading file: {file_path}. {e}")


# 使用範例
file_path = "bookmarks.toml"
bookmark_datas = read_toml(file_path)
counter = 0
if bookmark_datas:
    # 訪問資料
    for category in bookmark_datas:
        for section in bookmark_datas[category]:
            for item in bookmark_datas[category][section]:
                if (
                    item.get("url", None) is None
                    or item.get("icon", None) is None
                    or item.get("title", None) is None
                ):
                    raise ValueError(f"Invalid item: {item}")
                counter += 1

print(f"Total items: {counter}")
