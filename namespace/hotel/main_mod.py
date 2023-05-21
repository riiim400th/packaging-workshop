from checkin.checkin import checkin_guest
from checkout.checkout import checkout_guest

def main():
    # メインの実行ロジックを記述する
    guest_name = input("ゲストの名前を入力してください: ")
    
    # チェックイン処理を実行
    checkin_guest(guest_name)
    
    # チェックアウト処理を実行
    checkout_guest(guest_name)

if __name__ == "__main__":
    main()
