def checkout_guest(guest_name):
    # ゲストのチェックアウト処理
    # 例えば、データベースからゲスト情報を削除するなどの処理を行う
    print(f"{guest_name}さんのチェックアウトが完了しました。")


def main():
    guest = input("ゲストの名前を入力してください: ")
    checkout_guest(guest)
    
# テストコード
if __name__ == "__main__":
    main()
    
    
