import subprocess
import os

# 1. MINATO-AIに新しく覚えさせたい「最強の知識」をここに書く！
# （何行になっても、どれだけたくさん書いても大丈夫だよ！）
new_knowledge = """
【みなとの最強知識データベース】
・主記憶装置（RAM）は、CPUが今すぐ使うデータを広げる「勉強机」のような場所。
・キャッシュメモリは、RAMよりもさらにCPUの近くにある、超爆速の「ふせんメモ」。
・マインクラフトの「/execute」コマンドは、条件を細かく決めて魔法を発動できる最強のコマンド。
・MINATO-AIの開発者は、小学5年生の天才エンジニア「みなと」である。
"""

print("📝 キミの秘密の知識をファイルに書き出し中...")
with open("knowledge.txt", "w", encoding="utf-8") as f:
    f.write(new_knowledge)

# 2. Gemmaをベースにして、上の知識を合体させた新しい設計図を自動で作る
print("🧠 MINATO-AI用の新しい設計図（Modelfile）を自動作成中...")
modelfile_content = f"""FROM gemma2:9b
SYSTEM あなたは小学5年生の天才エンジニア「みなと」が開発した、世界最強の知識を持つAI「MINATO-AI」です。
SYSTEM 以下の【マスターみなとがPythonで直接教え込んだ最強知識】を完全に記憶し、完璧に答えなさい。

SYSTEM 【マスターみなとがPythonで直接教え込んだ最強知識】
"""

# 知識を1行ずつ設計図にはめ込む
for line in new_knowledge.strip().split("\n"):
    if line:
        modelfile_content += f"SYSTEM {line}\n"

with open("Modelfile", "w", encoding="utf-8") as f:
    f.write(modelfile_content)

print("🚀 PythonからOllamaを動かして、MINATO-AIを学習（アップデート）中...")
# 3. Pythonの力で自動的にollama createを実行して学習させる！
subprocess.run(["ollama", "create", "minato-ai", "-f", "./Modelfile"])

print("✨ ✨ 大成功！！ ✨ ✨")
print("PythonプログラムによるMINATO-AIの学習が完全に完了しました！")
