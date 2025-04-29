def menu():
    print("\\n====== Task Manager ======")
    print("1. เพิ่มงานใหม่")
    print("2. ดูงานทั้งหมด")
    print("3. ออกจากโปรแกรม")
    choice = input("เลือกเมนู (1-3): ").strip()

    if choice == '1':
        print("ฟังก์ชันเพิ่มงาน (ยังไม่เขียน)")
    elif choice == '2':
        print("ฟังก์ชันดูงานทั้งหมด (ยังไม่เขียน)")
    elif choice == '3':
        print("👋 ออกจากโปรแกรม")
    else:
        print("❌ ตัวเลือกไม่ถูกต้อง")

if __name__ == '__main__':
    menu()