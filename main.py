import json
from datetime import datetime

# JSONファイルへの保存
DATA_FILE = "subscriptions.json"

# データを読み込む
def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# データを保存する
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# サブスクリプションを登録する
def add_subscription():
    print("新しいサブスクリプションを登録します")
    service_name = input("サービス名: ")
    while True:
        payment_type = input("支払いタイプ（月額または年額）: ").strip()
        if payment_type in ["月額", "年額"]:
            break
        print("「月額」または「年額」を選んでください")
    
    cost = float(input(f"{payment_type}料金(円): "))
    payment_date = input("支払い日 (YYYY-MM-DD): ")
    start_date = input("契約開始日 (YYYY-MM-DD): ")
    note = input("メモ (任意): ")

    subscription = {
        "service_name": service_name,
        "payment_type": payment_type,
        "cost": cost,
        "payment_date": payment_date,
        "start_date": start_date,
        "note": note
    }

    data = load_data()
    data.append(subscription)
    save_data(data)

    print(f"{service_name}を登録しました！")

# サブスクリプションの一覧を表示する
def list_subscriptions():
    print("\n=== 登録されているサブスクリプション一覧 ===")
    data = load_data()
    if not data:
        print("登録されているサブスクリプションはありません。")
        return

    for index, subscription in enumerate(data, start=1):
        print(f"{index}. サービス名: {subscription['service_name']}")
        print(f"   支払いタイプ: {subscription['payment_type']} ")
        print(f"   費用: {subscription['cost']} 円")
        print(f"   支払い日: {subscription['payment_date']}")
        print(f"   契約開始日: {subscription['start_date']}")
        print(f"   メモ: {subscription['note']}\n")

# メインメニュー
def main():
    while True:
        print("\n=== サブスクリプション管理ツール ===")
        print("1. 登録")
        print("2. 一覧表示")
        print("3. 終了")
        choice = input("選択肢を入力してください: ")

        if choice == "1":
            add_subscription()
        elif choice == "2":
            list_subscriptions()
        elif choice == "3":
            print("終了します。")
            break
        else:
            print("無効な選択肢です。")

if __name__ == "__main__":
    main()