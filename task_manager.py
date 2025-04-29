import json
import os

FILENAME = 'tasks.json'

def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, 'r') as f:
        return json.load(f)

def save_tasks(data):
    with open(FILENAME, 'w') as f:
        json.dump(data, f, indent=4)


def add_task(tasks):
    name = input("🔹 ชื่องาน: ").strip()
    if not name:
        print("❌ ห้ามเว้นชื่อว่าง")
        return
    description = input("🔹 คำอธิบาย: ").strip()
    due_date = input("🔹 วันที่ครบกำหนด (YYYY-MM-DD): ").strip()

    task_id = max([t['id'] for t in tasks], default=0) + 1
    task = {
        'id': task_id,
        'name': name,
        'description': description,
        'due_date': due_date,
        'completed': False
    }

    tasks.append(task)
    save_tasks(tasks)
    print("✅ เพิ่มงานเรียบร้อย")

def menu():
    tasks = load_tasks()
    while True:
        print("\n====== Task Manager ======")
        print("1. เพิ่มงานใหม่")
        print("2. ดูงานทั้งหมด (ยังไม่ทำ)")
        print("3. ออกจากโปรแกรม")
        choice = input("เลือกเมนู (1-3): ").strip()

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            print("🔧 ฟังก์ชันนี้อยู่ระหว่างพัฒนา")
        elif choice == '3':
            print("👋 ออกจากโปรแกรม")
            break
        else:
            print("❌ ตัวเลือกไม่ถูกต้อง")

if __name__ == '__main__':
    menu()
