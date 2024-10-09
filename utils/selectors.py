from tkinter import messagebox, filedialog
from constants import FORMATS_FOR_IMAGE

def file_selection(label_text, allowed_extensions=FORMATS_FOR_IMAGE):
    filename = filedialog.askopenfilename(title=f"Select {label_text}",
                                          filetypes=[("Allowed files", allowed_extensions)])
    if filename:
        # Update the appropriate global variable
        loaded_image = filename
        extension = filename.split(".")[-1] if "." in filename else ""
        if extension.lower() in [ext.replace(".", "") for ext in allowed_extensions]:
            print(f"Selected {label_text}: {filename}")
        else:
            messagebox.showerror("Invalid File",
                                 f"Selected file is not in allowed formats: {', '.join(allowed_extensions)}")
    else:
        print("No file was selected.")
