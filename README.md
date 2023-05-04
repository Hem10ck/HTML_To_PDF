# HTML_To_PDF
This code is a Python script that uses the tkinter library to create a graphical user interface (GUI) for an HTML to PDF converter. It also uses the Selenium WebDriver library to automate the conversion process.

The script defines several functions:

send_devtools: a helper function that sends a command to the DevTools API of the Chrome browser and returns the result
get_pdf_from_html: a function that takes a URL of an HTML page and converts it to a PDF using the Chrome browser and the DevTools API
convert_html_to_pdf: a function that retrieves the URL from a GUI input field, calls get_pdf_from_html, and saves the resulting PDF to a file
The tkinter library is used to create the GUI with the following widgets:

ttk.Label: a label widget to display the text "Enter URL to convert to PDF:"
ttk.Entry: an entry widget to allow the user to input the URL to convert
ttk.Button: a button widget to trigger the conversion process
When the "Convert" button is clicked, the convert_html_to_pdf function is called, which retrieves the URL from the input field, converts the HTML to a PDF using the get_pdf_from_html function, and saves the PDF to a file using the filedialog.asksaveasfilename method. If the conversion process fails, an error message is displayed using the messagebox.showerror method, and if successful, a success message is displayed using the messagebox.showinfo method.
