import tkinter as tk
from tkinter import messagebox
import threading
import asyncio
from playwright.async_api import async_playwright
import json
from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env
user_id = os.getenv("USER_ID")
password = os.getenv("PASSWORD")
print(user_id, password)

# Placeholder functions for each action
def login():
    async def do_login_async():
        try:
            async with async_playwright() as p:
                browser = await p.chromium.launch(headless=False)
                page = await browser.new_page()
                await page.goto("https://www.click-sec.com/")
                await page.wait_for_timeout(30000)
                await page.fill('input[name="j_username"]', user_id)
                await page.fill('input[name="j_password"]', password)
                # await asyncio.sleep(random.uniform(0.2, 0.5))
                await page.click('button[type="submit"][name="LoginForm"][value="Login"]')
                await page.wait_for_timeout(3000)
                # content = await page.content()
                # if "ログアウト" in content:
                #     messagebox.showinfo("Login", "Login successful!")
                # else:
                #     messagebox.showerror("Login", "Login failed. Please check credentials or selectors.")
                # await browser.close()
        except Exception as e:
            messagebox.showerror("Login", f"Login error: {e}")

    def run_async_login():
        asyncio.run(do_login_async())

    threading.Thread(target=run_async_login).start()

def fetch_rate():
    messagebox.showinfo("Fetch Rate", "Fetch Rate function called.")

def place_order():
    messagebox.showinfo("Place Order", "Place Order function called.")

def fetch_execution():
    messagebox.showinfo("Fetch Execution", "Fetch Execution function called.")

def get_positions():
    messagebox.showinfo("Get Positions", "Get Positions function called.")

def close_order():
    messagebox.showinfo("Close Order", "Close Order function called.")

# Main Tkinter window
root = tk.Tk()
root.title("GMO FX Automation")
root.geometry("300x350")

# Create buttons for each function
tk.Button(root, text="Login", width=25, command=login).pack(pady=10)
tk.Button(root, text="Fetch Rate", width=25, command=fetch_rate).pack(pady=10)
tk.Button(root, text="Place Order", width=25, command=place_order).pack(pady=10)
tk.Button(root, text="Fetch Execution", width=25, command=fetch_execution).pack(pady=10)
tk.Button(root, text="Get Positions", width=25, command=get_positions).pack(pady=10)
tk.Button(root, text="Close Order", width=25, command=close_order).pack(pady=10)

root.mainloop() 