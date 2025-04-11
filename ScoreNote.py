# ScoreNote.py
import json

def load_scores():
    scores = {}
    try:
        with open("scores.json", "r", encoding="utf-8") as file:
            scores = json.load(file)  # JSONファイルを読み込む
    except FileNotFoundError:
        print("\nscores.json が見つかりません。")
    except json.JSONDecodeError:
        print("\nscores.json の形式が不正です。")
    return scores

def save_scores(scores):
    with open("scores.json", "w", encoding="utf-8") as file:
        json.dump(scores, file, ensure_ascii=False, indent=4)  # JSON形式で保存
    print("\nscores.json に保存しました。")

def main():
    # scores.json の内容を読み込む
    scores = load_scores()

    print("生徒の名前と点数を入力してください。（終了するには '終了' と入力）")

    while True:
        name = input("名前: ")
        if name == "終了":
            break
        score = input("点数: ")
        if score == "終了":
            break
        if name in scores:
            print(f"{name} は既に入力されています。")
            continue
        try:
            scores[name] = int(score)
        except ValueError:
            print("点数は整数で入力してください。")
            continue

    if not scores:
        print("データがありません。")
        return

    print("\n成績一覧:")
    for name, score in scores.items():
        print(f"{name}: {score} 点")

    # 平均点を計算して表示
    average = sum(scores.values()) / len(scores)
    print(f"\n平均点: {average:.2f} 点")

    # scores.json に保存
    save_scores(scores)

if __name__ == "__main__":
    main()