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


def view_tasks(tasks):
    if not tasks:
        print("📭 ไม่มีงานในระบบ")
        return

    print("\n🕒 งานที่ยังไม่เสร็จ:")
    for task in tasks:
        if not task["completed"]:
            print(f"  [{task['id']}] {task['name']} (ครบกำหนด: {task['due_date']})")
            print(f"     📌 {task['description']}")

    print("\n✅ งานที่เสร็จแล้ว:")
    for task in tasks:
        if task["completed"]:
            print(f"  [{task['id']}] {task['name']} (ครบกำหนด: {task['due_date']})")

def mark_task_completed(tasks):
    try:
        task_id = int(input("🔸 ใส่ ID ของงานที่เสร็จแล้ว: "))
    except ValueError:
        print("❌ กรุณาใส่ตัวเลขเท่านั้น")
        return

    for task in tasks:
        if task['id'] == task_id:
            if task['completed']:
                print("ℹ️ งานนี้ทำเสร็จไปแล้ว")
            else:
                task['completed'] = True
                save_tasks(tasks)
                print("✅ ทำเครื่องหมายว่างานเสร็จเรียบร้อย")
            return

    print("❌ ไม่พบงานที่มี ID นี้")

def delete_task(tasks):
    try:
        task_id = int(input("🗑 ใส่ ID ของงานที่ต้องการลบ: "))
    except ValueError:
        print("❌ กรุณาใส่ตัวเลขเท่านั้น")
        return

    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print("✅ ลบงานเรียบร้อยแล้ว")
            return

    print("❌ ไม่พบงานที่มี ID นี้")

def search_tasks(tasks):
    keyword = input("🔍 ค้นหาจากคำ หรือวันที่ (YYYY-MM-DD): ").lower()

    results = []
    for task in tasks:
        if (keyword in task['name'].lower() or
            keyword in task['description'].lower() or
            keyword in task['due_date']):
            results.append(task)

    if results:
        print(f"\n🔎 พบ {len(results)} งานที่ตรงกับคำค้น:")
        for task in results:
            status = "✅ เสร็จแล้ว" if task['completed'] else "🕒 รอดำเนินการ"
            print(f"  [{task['id']}] {task['name']} - {status} (ครบกำหนด: {task['due_date']})")
    else:
        print("❌ ไม่พบงานที่ตรงกับคำค้น")

def menu():
    tasks = load_tasks()
    while True:
        print("\n====== Task Manager ======")
        print("1. เพิ่มงานใหม่")
        print("2. ดูงานทั้งหมด")
        print("3. ทำเครื่องหมายว่างานเสร็จสิ้น")
        print("4. ลบงาน") 
        print("5. ค้นหางาน") 
        print("6. ออกจากโปรแกรม") 
        choice = input("เลือกตัวเลือก (1-6): ").strip()

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_completed(tasks) 
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            search_tasks(tasks)
        elif choice == '6':
            print("👋 ออกจากโปรแกรม")
            break
        else:
            print("❌ ตัวเลือกไม่ถูกต้อง")

if __name__ == '__main__':
    menu()

