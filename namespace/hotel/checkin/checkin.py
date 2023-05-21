def checkin_guest(guest_name):
    # ゲストのチェックイン処理
    # 例えば、データベースにゲスト情報を登録するなどの処理を行う
    print(f"{guest_name}さんのチェックインが完了しました。")

# テストコード
def main():
    guest = input("ゲストの名前を入力してください: ")
    checkin_guest(guest)

if __name__ == "__main__":
    main()