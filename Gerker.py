import random
import string
from colorama import Fore, Style, init

# Initialize colorama
init()

# Print the text in yellow
print(Fore.YELLOW + """
                      ____           _             
                     / ___| ___ _ __| | _____ _ __ 
                    | |  _ / _ \ '__| |/ / _ \ '__|
                    | |_| |  __/ |  |   <  __/ |   
                     \____|\___|_|  |_|\_\___|_|
""" + Fore.RESET)

line = r""" ============================================================================ """

print(line)

# ANSI escape code for blue
blue = '\033[34m'
reset = '\033[0m'

# Print the text in blue
print(blue + """
[---]               The 3/4 User Generator (Gerker)             [---]
[---]                Created by: AKA_Sla7er (AKA)               [---]
[---]                      Version: 1.0.0                       [---]
[---]             Homepage: https://aka7-org.github.io/home/    [---]
                Welcome to the 3/4 User Generator Tool (SET)
""" + reset)

# Initialize colorama
init(autoreset=True)

def generate_usernames(length, count):
    """Generates a list of random usernames"""
    characters = string.ascii_letters + string.digits  # Letters and digits
    usernames = []

    for _ in range(count):
        username = ''.join(random.choice(characters) for _ in range(length))
        usernames.append(username)

    return usernames

def main():
    # Print the welcome message in red
    print(Fore.RED + "أهلاً بك في أداة توليد يوزرات للإختراق او الحسابات الوهمية !" + Style.RESET_ALL)
    
    while True:
        try:
            length = int(input("أدخل طول اليوزر (2, 3, 4, 5): "))
            if length not in [2, 3, 4, 5]:
                print("من فضلك أدخل رقماً صحيحاً (2, 3, 4, 5).")
                continue

            count = int(input("كم عدد اليوزرات التي ترغب في توليدها؟ "))

            if count <= 0:
                print("العدد يجب أن يكون أكبر من الصفر.")
                continue

            usernames = generate_usernames(length, count)
            print(f"تم توليد {count} يوزر بطول {length}:")
            for username in usernames:
                print(username)

        except ValueError:
            print("خطأ: من فضلك أدخل قيمة صحيحة.")
        
        cont = input("هل ترغب في توليد يوزرات أخرى؟ (نعم/لا): ").lower()
        if cont != "نعم":
            print("3/4 شكراً لاستخدامك أداة!")
            break

if __name__ == "__main__":
    main()
