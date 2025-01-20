import json
import re
from pypinyin import lazy_pinyin, Style

def split_into_phrases(text):
    """拆分文本为意群（按词语切分）。Split the text into meaning groups (by word segmentation)."""
    return re.findall(r'[\u4e00-\u9fff]+|[^\u4e00-\u9fff\s]+', text)

def extract_rhyme(pinyin):
    """提取拼音中的韵母部分。Extract the vowel part of pinyin."""
    vowels = re.findall(r"[aeiouü]+n?t?", pinyin)
    return vowels[-1] if vowels else ""

def process_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 按句号、感叹号、问号或换行符分句。Clause by period, exclamation point, question mark or line break
    sentences = re.split(r'[。！？\n]', content)
    result = []

    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue
        phrases = split_into_phrases(sentence)
        analyzed = []

        for phrase in phrases:
            pinyin = lazy_pinyin(phrase, style=Style.NORMAL)
            rhymes = [extract_rhyme(p) for p in pinyin]
            analyzed.append({
                "phrase": phrase,
                "pinyin": pinyin,
                "rhyme": rhymes
            })
        
        result.append({
            "sentence": sentence,
            "analysis": analyzed
        })
    
    return result

def save_as_json(data, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    input_file = "ALTERNATIVE"
    output_file = "output.json"

    data = process_text(input_file)
    save_as_json(data, output_file)
    print(f"处理完成，结果保存至 {output_file}The result has been output to {output_file}")