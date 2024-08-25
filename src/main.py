import random
import subprocess

GREEN = '\033[32m'

def main() -> None:
    subprocess.run('title 数当てゲーム', shell=True)
    num = random.randrange(11)
    while True:
        try:
            answer = int(input("1～10の数を入力して下さい: "))
            if answer == num:
                print(f"{GREEN}正解!\n\n")
                subprocess.run('pause', shell=True)
                break
            elif answer < num:
                print("答えの数より小さい\n")
            elif answer > num:
                print("答えの数より大きい\n")
        except ValueError:
            print("数字を入力して下さい\n")

if __name__ == "__main__":
    main()