import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json, base64


def send_devtools(driver, cmd, params={}):
    resource = "/session/%s/chromium/send_command_and_get_result" % driver.session_id
    url = driver.command_executor._url + resource
    body = json.dumps({'cmd': cmd, 'params': params})
    response = driver.command_executor._request('POST', url, body)
    if response.get('status'):
        raise Exception(response.get('value'))
    return response.get('value')

def get_pdf_from_html(url, chromedriver='./chromedriver', print_options = {}):
    webdriver_options = Options()
    webdriver_options.add_argument('--headless')
    webdriver_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chromedriver, options=webdriver_options)
    driver.get(url)
    calculated_print_options = {
        'landscape': False,
        'displayHeaderFooter': False,
        'printBackground': True,
        'preferCSSPageSize': True,
    }
    calculated_print_options.update(print_options)
    result = send_devtools(driver, "Page.printToPDF", calculated_print_options)
    driver.quit()
    return base64.b64decode(result['data'])

def convert_html_to_pdf():
    url = url_entry.get()
    filename = filedialog.asksaveasfilename(defaultextension=".pdf")
    if filename:
        try:
            pdf_data = get_pdf_from_html(url)
            with open(filename, 'wb') as f:
                f.write(pdf_data)
            messagebox.showinfo("Success", f"PDF file saved to {filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to convert HTML to PDF: {str(e)}")

root = tk.Tk()
root.geometry("400x200")
root.title("HTML to PDF Converter")
root.config(background="dark grey")
# create style object
style = ttk.Style()

# set style theme to "dark"
style.theme_use("clam")
style.configure("TButton", foreground="white", background="#4CAF50", font=("Helvetica", 10, "bold"))

# create label for URL input
url_label = ttk.Label(root, text="Enter URL to convert to PDF:")
url_label.pack(pady=(10,5))

# create URL input
url_entry = ttk.Entry(root, width=50)
url_entry.pack()

# create convert button
convert_button = ttk.Button(root, text="Convert", command=convert_html_to_pdf)
convert_button.pack(pady=10)

root.mainloop()
