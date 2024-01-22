import subprocess

def run_croud_script():
    try:
        subprocess.run(["python", r"./Cloud_lecture/mysql/croud.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running croud.py: {e}")

if __name__ == "__main__":
    print("Running main.py")
    # 여기에 main.py의 나머지 코드 추가

    # croud.py 실행
    run_croud_script()
