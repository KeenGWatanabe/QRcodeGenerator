I'll help you create a QR code generator app. Here are implementations in different programming languages:

## Python QR Code Generator (Console App)

```python
import qrcode
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import os

class QRCodeGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        
        self.setup_ui()
    
    def setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(main_frame, text="QR Code Generator", 
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Input field
        ttk.Label(main_frame, text="Enter text or URL:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.text_entry = tk.Text(main_frame, height=4, width=50, font=("Arial", 10))
        self.text_entry.grid(row=2, column=0, columnspan=2, pady=5, sticky=(tk.W, tk.E))
        
        # File name entry
        ttk.Label(main_frame, text="File name (without extension):").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.filename_entry = ttk.Entry(main_frame, width=50, font=("Arial", 10))
        self.filename_entry.grid(row=4, column=0, columnspan=2, pady=5, sticky=(tk.W, tk.E))
        self.filename_entry.insert(0, "qrcode")
        
        # Save location
        ttk.Label(main_frame, text="Save location:").grid(row=5, column=0, sticky=tk.W, pady=5)
        self.location_entry = ttk.Entry(main_frame, width=40, font=("Arial", 10))
        self.location_entry.grid(row=6, column=0, pady=5, sticky=(tk.W, tk.E))
        self.location_entry.insert(0, os.getcwd())
        
        browse_button = ttk.Button(main_frame, text="Browse", command=self.browse_location)
        browse_button.grid(row=6, column=1, padx=(5, 0), pady=5)
        
        # QR Code size
        ttk.Label(main_frame, text="QR Code size:").grid(row=7, column=0, sticky=tk.W, pady=5)
        self.size_var = tk.StringVar(value="Medium")
        size_combo = ttk.Combobox(main_frame, textvariable=self.size_var, 
                                 values=["Small", "Medium", "Large"], state="readonly")
        size_combo.grid(row=8, column=0, columnspan=2, sticky=tk.W, pady=5)
        
        # Generate button
        generate_btn = ttk.Button(main_frame, text="Generate QR Code", 
                                 command=self.generate_qr_code)
        generate_btn.grid(row=9, column=0, columnspan=2, pady=20)
        
        # QR Code display
        self.qr_label = ttk.Label(main_frame, text="QR Code will appear here", 
                                 background="white", relief="solid")
        self.qr_label.grid(row=10, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))
        
        # Configure grid weights
        main_frame.columnconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
    
    def browse_location(self):
        directory = filedialog.askdirectory()
        if directory:
            self.location_entry.delete(0, tk.END)
            self.location_entry.insert(0, directory)
    
    def generate_qr_code(self):
        text = self.text_entry.get("1.0", tk.END).strip()
        filename = self.filename_entry.get().strip()
        location = self.location_entry.get().strip()
        
        if not text:
            messagebox.showerror("Error", "Please enter some text or URL")
            return
        
        if not filename:
            messagebox.showerror("Error", "Please enter a file name")
            return
        
        if not location:
            messagebox.showerror("Error", "Please select a save location")
            return
        
        try:
            # Configure QR code based on size
            size_mapping = {
                "Small": (10, 4),
                "Medium": (15, 6),
                "Large": (20, 8)
            }
            box_size, border = size_mapping[self.size_var.get()]
            
            # Generate QR code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=box_size,
                border=border,
            )
            qr.add_data(text)
            qr.make(fit=True)
            
            # Create QR code image
            qr_image = qr.make_image(fill_color="black", back_color="white")
            
            # Save the image
            filepath = os.path.join(location, f"{filename}.png")
            qr_image.save(filepath)
            
            # Display the QR code in the app
            display_image = qr_image.resize((200, 200), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(display_image)
            self.qr_label.configure(image=photo, text="")
            self.qr_label.image = photo  # Keep a reference
            
            messagebox.showinfo("Success", f"QR Code generated successfully!\nSaved as: {filepath}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate QR code: {str(e)}")

def main():
    root = tk.Tk()
    app = QRCodeGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
```

## Web-based QR Code Generator (HTML + JavaScript)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>QR Code Generator</title>
    <script src="https://cdn.jsdelivr.net/npm/qrcode@1.5.3/build/qrcode.min.js"></script>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }

        .container {
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
            padding: 40px;
            max-width: 500px;
            width: 100%;
        }

        h1 {
            text-align: center;
            color: #333;
            margin-bottom: 30px;
            font-size: 2.5em;
            font-weight: 300;
        }

        .input-group {
            margin-bottom: 20px;
        }

        label {
            display: block;
            margin-bottom: 8px;
            color: #555;
            font-weight: 500;
        }

        textarea, input, select {
            width: 100%;
            padding: 12px;
            border: 2px solid #e1e5e9;
            border-radius: 10px;
            font-size: 16px;
            transition: border-color 0.3s ease;
        }

        textarea:focus, input:focus, select:focus {
            outline: none;
            border-color: #667eea;
        }

        textarea {
            height: 100px;
            resize: vertical;
        }

        .size-options {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 10px;
            margin-bottom: 20px;
        }

        .size-option {
            text-align: center;
            padding: 15px;
            border: 2px solid #e1e5e9;
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .size-option:hover {
            border-color: #667eea;
        }

        .size-option.selected {
            border-color: #667eea;
            background-color: #f0f4ff;
        }

        .generate-btn {
            width: 100%;
            padding: 15px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 10px;
            font-size: 18px;
            font-weight: 600;
            cursor: pointer;
            transition: transform 0.2s ease;
        }

        .generate-btn:hover {
            transform: translateY(-2px);
        }

        .generate-btn:active {
            transform: translateY(0);
        }

        .qr-container {
            text-align: center;
            margin-top: 30px;
            padding: 20px;
            border: 2px dashed #e1e5e9;
            border-radius: 10px;
            min-height: 200px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }

        #qrcode {
            margin-bottom: 15px;
        }

        .download-btn {
            padding: 10px 20px;
            background: #28a745;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            display: none;
        }

        .download-btn:hover {
            background: #218838;
        }

        .error {
            color: #dc3545;
            text-align: center;
            margin-top: 10px;
            display: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>QR Code Generator</h1>
        
        <div class="input-group">
            <label for="qrText">Enter text or URL:</label>
            <textarea id="qrText" placeholder="Type your text, URL, or any content here..."></textarea>
        </div>

        <div class="input-group">
            <label for="fileName">File name:</label>
            <input type="text" id="fileName" placeholder="qrcode" value="qrcode">
        </div>

        <div class="input-group">
            <label>QR Code size:</label>
            <div class="size-options">
                <div class="size-option selected" data-size="128">Small</div>
                <div class="size-option" data-size="256">Medium</div>
                <div class="size-option" data-size="384">Large</div>
            </div>
        </div>

        <button class="generate-btn" onclick="generateQRCode()">Generate QR Code</button>

        <div class="error" id="errorMessage"></div>

        <div class="qr-container">
            <div id="qrcode"></div>
            <button class="download-btn" id="downloadBtn" onclick="downloadQRCode()">Download QR Code</button>
        </div>
    </div>

    <script>
        let currentQRCode = null;
        let selectedSize = 256;

        // Size selection
        document.querySelectorAll('.size-option').forEach(option => {
            option.addEventListener('click', function() {
                document.querySelectorAll('.size-option').forEach(opt => {
                    opt.classList.remove('selected');
                });
                this.classList.add('selected');
                selectedSize = parseInt(this.dataset.size);
            });
        });

        function generateQRCode() {
            const text = document.getElementById('qrText').value.trim();
            const errorElement = document.getElementById('errorMessage');
            const qrContainer = document.getElementById('qrcode');
            const downloadBtn = document.getElementById('downloadBtn');

            // Clear previous
            qrContainer.innerHTML = '';
            errorElement.style.display = 'none';
            downloadBtn.style.display = 'none';

            if (!text) {
                errorElement.textContent = 'Please enter some text or URL';
                errorElement.style.display = 'block';
                return;
            }

            try {
                // Generate QR code
                qrContainer.innerHTML = '';
                QRCode.toCanvas(qrContainer, text, {
                    width: selectedSize,
                    height: selectedSize,
                    margin: 2,
                    color: {
                        dark: '#000000',
                        light: '#FFFFFF'
                    }
                }, function(error) {
                    if (error) {
                        errorElement.textContent = 'Error generating QR code: ' + error;
                        errorElement.style.display = 'block';
                    } else {
                        downloadBtn.style.display = 'block';
                        currentQRCode = text;
                    }
                });
            } catch (error) {
                errorElement.textContent = 'Error generating QR code: ' + error.message;
                errorElement.style.display = 'block';
            }
        }

        function downloadQRCode() {
            const canvas = document.querySelector('#qrcode canvas');
            const fileName = document.getElementById('fileName').value.trim() || 'qrcode';
            
            if (canvas) {
                const link = document.createElement('a');
                link.download = fileName + '.png';
                link.href = canvas.toDataURL('image/png');
                link.click();
            }
        }

        // Generate QR code on Enter key press in textarea
        document.getElementById('qrText').addEventListener('keypress', function(e) {
            if (e.key === 'Enter' && e.ctrlKey) {
                generateQRCode();
            }
        });
    </script>
</body>
</html>
```

## Simple Python Console Version

```python
import qrcode
import os

def simple_qr_generator():
    print("=== Simple QR Code Generator ===")
    
    while True:
        print("\n1. Generate QR Code")
        print("2. Exit")
        
        choice = input("\nEnter your choice (1-2): ").strip()
        
        if choice == '1':
            text = input("Enter text or URL: ").strip()
            if not text:
                print("Error: Text cannot be empty!")
                continue
                
            filename = input("Enter filename (without extension): ").strip()
            if not filename:
                filename = "qrcode"
                
            try:
                # Generate QR code
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )
                qr.add_data(text)
                qr.make(fit=True)
                
                img = qr.make_image(fill_color="black", back_color="white")
                img.save(f"{filename}.png")
                
                print(f"✓ QR code generated successfully: {filename}.png")
                print(f"✓ File saved in: {os.getcwd()}")
                
            except Exception as e:
                print(f"Error generating QR code: {e}")
                
        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    simple_qr_generator()
```

## Installation Requirements

For the Python versions, you'll need to install the required packages:

```bash
pip install qrcode[pil] pillow
```

## Features

1. **Python GUI Version**:
   - Graphical user interface with Tkinter
   - Customizable QR code size
   - File browsing for save location
   - Preview of generated QR code

2. **Web Version**:
   - Responsive design
   - Real-time QR code generation
   - Download functionality
   - Size customization

3. **Console Version**:
   - Simple command-line interface
   - Basic QR code generation
   - Easy to use

## Usage

1. **Python GUI**: Run the script and use the graphical interface
2. **Web Version**: Open the HTML file in a web browser
3. **Console Version**: Run the script and follow the prompts

All versions allow you to generate QR codes from text, URLs, or any other content and save them as PNG images.