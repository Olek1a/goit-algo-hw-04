from pprint import pprint  # хотів, щоб список був більше чительним

def get_cats_info(path):
    cats_list = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line:
                    part = line.split(",")
                    
                    cat_data = {
                        "id": part[0],
                        "name": part[1],
                        "age": part[2]
                    }
                    cats_list.append(cat_data)
        return cats_list
    except FileNotFoundError:
        print(f"Помилка: Файл за шляхом {path} не знайдено.")
        return [] 
    except Exception as e:
        print(f"Сталася непередбачувана помилка: {e}")
        return []

cats_info = get_cats_info("cats_file.txt")
pprint(cats_info, width=50)