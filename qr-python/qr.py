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