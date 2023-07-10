import random
import time

def generate_random_focus_time():
    # 生成随机时间（秒）：2小时到18小时之间
    random_seconds = random.randint(2 * 60 * 60, 18 * 60 * 60)
    return random_seconds

def focus_timer():
    focus_seconds = generate_random_focus_time()
    print(f"专注时钟设定时间为：{focus_seconds // 3600}小时{(focus_seconds % 3600) // 60}分钟")
    time.sleep(focus_seconds)
    print("专注时钟结束，休息一下吧！")

focus_timer()
