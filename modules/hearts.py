from selenium.webdriver.support.ui      import WebDriverWait
from selenium.webdriver.common.by       import By
from selenium.webdriver.support         import expected_conditions as EC
import undetected_chromedriver          as uc
from colorama                           import Fore

import ctypes
import time
import os


class Rei:
    def __init__(self, video_link):
        self.video_link    = video_link
        self.hearts_sent   = 0
        self.hearts_failed = 0
        self.driver        = self.init_driver()
        self.update_title()
        self.run()

    def clear_terminal(self):
        os.system("cls" if os.name == "nt" else "clear")

    def init_driver(self):
        chrome_options = uc.ChromeOptions()
        driver         = uc.Chrome(options=chrome_options)
        driver.set_window_size(600, 900)
        return driver

    def update_title(self):
        title = f"TikTok HeartBot | Sent: {self.hearts_sent} | Failed: {self.hearts_failed} | github.com/@Froxxy1011"
        ctypes.windll.kernel32.SetConsoleTitleW(title)

    def solve_captcha(self):
        try:
            captcha_input = WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div[2]/form/div/div/div/input'))
            )
            captcha_code  = input(f"[{Fore.CYAN}?{Fore.RESET}] Enter CAPTCHA : ")
            captcha_input.send_keys(captcha_code)
            
            submit_button = self.driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/form/div/div/div/div/button')
            submit_button.click()
            
            print(f"[{Fore.GREEN}+{Fore.RESET}] CAPTCHA solved successfully!")
            time.sleep(5)
        except Exception as e:
            print(f"{Fore.RED}Error solving CAPTCHA: {e}{Fore.RESET}")

    def send_hearts(self):
        try:
            self.clear_terminal()
            send_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[8]/div/form/div/div/button'))
            )
            send_button.click()
            time.sleep(2)

            confirm_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[8]/div/div/div[1]/div/form/button'))
            )
            confirm_button.click()
            time.sleep(2)

            self.hearts_sent += 1000
            for i in range(10):
                print(f"{Fore.GREEN}+1 Heart Sent{Fore.RESET}")
                time.sleep(0.5)
            print(f"{Fore.GREEN}+10 Hearts Sent{Fore.RESET}")
        except Exception:
            self.hearts_failed += 1
            print(f"{Fore.RED}Failed to send hearts{Fore.RESET}")

        self.update_title()

    def run(self):
        try:
            self.driver.get("https://zefoy.com/")
            time.sleep(3)
            self.solve_captcha()

            category_button = WebDriverWait(self.driver, 45).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div/div[2]/div/div/div[3]/div/button'))
            )
            category_button.click()
            time.sleep(2)

            input_link = self.driver.find_element(By.XPATH, '/html/body/div[8]/div/form/div/input')
            input_link.send_keys(self.video_link)
            time.sleep(5)

            while True:
                self.send_hearts()
                time.sleep(20)
        except Exception as e:
            print(f"{Fore.RED}Error: {e}{Fore.RESET}")
        finally:
            self.driver.quit()


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    video_link = input(f"[{Fore.CYAN}?{Fore.RESET}] Video Link: ")
    print("")
    bot = Rei(video_link)
