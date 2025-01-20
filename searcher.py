import json

def load_json(file_path):
    """加载 JSON 文件"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def search_by_rhyme(data, rhyme):
    """通过韵脚查找字或词"""
    results = []
    for sentence_data in data:
        sentence = sentence_data["sentence"]
        for analysis in sentence_data["analysis"]:
            for pinyin, r in zip(analysis["pinyin"], analysis["rhyme"]):
                if r == rhyme:
                    results.append({
                        "sentence": sentence,
                        "phrase": analysis["phrase"],
                        "character": pinyin,
                        "rhyme": r
                    })
    return results

def select_word(data, target_word):
    """选中某个字词，返回其所有信息"""
    for sentence_data in data:
        sentence = sentence_data["sentence"]
        for analysis in sentence_data["analysis"]:
            if target_word in analysis["phrase"]:
                return {
                    "sentence": sentence,
                    "phrase": analysis["phrase"],
                    "pinyin": analysis["pinyin"],
                    "rhyme": analysis["rhyme"]
                }
    return None

def main():
    json_file = input("请输入 JSON 文件路径: ").strip()
    try:
        data = load_json(json_file)
    except FileNotFoundError:
        print("文件未找到，请确认路径是否正确。")
        return
    except json.JSONDecodeError:
        print("JSON 文件解析失败，请确认文件内容格式正确。")
        return

    while True:
        print("\n请选择操作: ")
        print("1. 通过韵脚查找字或词")
        print("2. 查找并选中某个字词")
        print("3. 退出")
        choice = input("输入 1、2 或 3: ").strip()

        if choice == "1":
            rhyme = input("请输入韵脚 (例如 'in', 'a' 等): ").strip()
            results = search_by_rhyme(data, rhyme)
            if results:
                print(f"\n找到以下结果包含韵脚 '{rhyme}':")
                for result in results:
                    print(f"句子: {result['sentence']}, 短语: {result['phrase']}, 字: {result['character']}, 韵脚: {result['rhyme']}")
            else:
                print(f"\n未找到包含韵脚 '{rhyme}' 的字或词。")
        
        elif choice == "2":
            word = input("请输入要查找的字词: ").strip()
            result = select_word(data, word)
            if result:
                print(f"\n找到字词 '{word}' 的信息:")
                print(json.dumps(result, ensure_ascii=False, indent=4))
            else:
                print(f"\n未找到字词 '{word}' 的相关信息。")
        
        elif choice == "3":
            print("自毁程序启动中……3……2……1……引爆！")
            break
        else:
            print("无效选项，请输入 1、2 或 3。")

if __name__ == "__main__":
    main()