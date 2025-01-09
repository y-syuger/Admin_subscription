
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
    monthly_cost = cost if payment_type == "月額" else round(cost / 12, 2)
    annual_cost = cost if payment_type == "年額" else cost * 12

    payment_date = input("支払い日 (YYYY-MM-DD): ")
    start_date = input("契約開始日 (YYYY-MM-DD): ")
    note = input("メモ (任意): ")

    subscription = {
        "service_name": service_name,
        "payment_type": payment_type,
        "cost": cost,
        "monthly_cost": monthly_cost,
        "annual_cost": annual_cost,
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
        print(f"   月額換算: {subscription['monthly_cost']} 円")
        print(f"   年額換算: {subscription['annual_cost']} 円")
        print(f"   支払い日: {subscription['payment_date']}")
        print(f"   契約開始日: {subscription['start_date']}")
        print(f"   メモ: {subscription['note']}\n")

# サブスクリプションを編集する
def edit_subscription():
    print("\n=== サブスクリプションを編集します ===")
    data = load_data()
    if not data:
        print("登録されているサブスクリプションはありません。")
        return
    
    list_subscriptions()
    while True:
        try:
            choice = int(input("編集するサブスクリプションの番号を入力してください (キャンセルは0): "))
            if choice == 0:
                print("編集をキャンセルしました。")
                return
            if 1 <= choice <= len(data):
                subscription = data[choice - 1]
                change_subscription(subscription, choice - 1)
            else:
                print("無効な番号です。もう一度入力してください。")
        except ValueError:
            print("数字を入力してください。")

# サブスクリプションの情報を変更する
def change_subscription(subscription, index):
    print(f"{subscription['service_name']} の情報を編集します。")
    service_name = input(f"サービス名 ({subscription['service_name']}): ")
    payment_type = input(f"支払いタイプ ({subscription['payment_type']}): ")
    cost = input(f"料金 ({subscription['cost']}): ")
    payment_date = input(f"支払い日 ({subscription['payment_date']}): ")
    start_date = input(f"契約開始日 ({subscription['start_date']}): ")
    note = input(f"メモ ({subscription['note']}): ")

    if payment_type and payment_type in ["月額", "年額"]:
        subscription["payment_type"] = payment_type
        subscription["cost"] = float(cost) if cost else subscription["cost"]
        subscription["monthly_cost"] = subscription["cost"] if payment_type == "月額" else round(subscription["cost"] / 12, 2)
        subscription["annual_cost"] = subscription["cost"] if payment_type == "年額" else subscription["cost"] * 12
    else:
        subscription["cost"] = float(cost) if cost else subscription["cost"]

    subscription["service_name"] = service_name if service_name else subscription["service_name"]
    subscription["payment_date"] = payment_date if payment_date else subscription["payment_date"]
    subscription["start_date"] = start_date if start_date else subscription["start_date"]
    subscription["note"] = note if note else subscription["note"]

    print("本当に更新しますか？更新したら、元に戻すことはできません。y/n")
    choice = input("選択: ")
    if choice.lower() == "y":
        data = load_data()
        data[index] = subscription
        save_data(data)
        print(f"{service_name or subscription['service_name']} の情報を更新しました！")
    else:
        print("更新をキャンセルしました。")

# サブスクリプションを削除する
def delete_subscription():
    print("\n=== サブスクリプションを削除します ===")
    data = load_data()
    if not data:
        print("登録されているサブスクリプションはありません。")
        return

    list_subscriptions()
    while True:
        try:
            choice = int(input("削除するサブスクリプションの番号を入力してください (キャンセルは0): "))
            if choice == 0:
                print("削除をキャンセルしました。")
                return
            if 1 <= choice <= len(data):
                removed = data.pop(choice - 1)
                save_data(data)
                print(f"{removed['service_name']} を削除しました！")
                return
            else:
                print("無効な番号です。もう一度入力してください。")
        except ValueError:
            print("数字を入力してください。")

# メインメニュー
def main():
    while True:
        print("\n=== サブスクリプション管理ツール ===")
        print("1. 登録")
        print("2. 一覧表示")
        print("3. 編集")
        print("4. 削除")
        print("5. 終了")
        choice = input("選択肢を入力してください: ")

        if choice == "1":
            add_subscription()
        elif choice == "2":
            list_subscriptions()
        elif choice == "3":
            edit_subscription()    
        elif choice == "4":
            delete_subscription()
        elif choice == "5":
            print("終了します。")
            break
        else:
            print("無効な選択肢です。")

if __name__ == "__main__":
    main()
