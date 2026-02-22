import frappe
from frappe.utils import today

@frappe.whitelist()
def get_user_tasks():
    return frappe.get_all(
        "Task",
        filters={"assigned_to": frappe.session.user},
        fields=["name", "subject", "status"]
    )
def validate_task(doc, method):
    if doc.status == "Completed" and not doc.logs:
        frappe.throw("You must add at least one log before completing the task.")

def calculate_hours(doc, method):
    total = 0
    for log in doc.logs:
        total = total + log.hours

    doc.actual_hours = total    

# def update_project_demo_status(doc, method):
#     frappe.db.set_value("Project_demo", doc.project_demo, "status", "In Progress")

def auto_mark_overdue():
    tasks = frappe.get_all(
        "Task_demo",
        filters={ "status": "Open",
                 "due_date": ["<", today()]
                 },
        fields=["name"]         
    )

    for task in tasks:
        doc = frappe.get_doc("Task_demo", task.name)
        doc.status = "Overdue"
        doc.save()

    frappe.db.commit()      

def update_project_demo_status(doc, method):
    if not doc.project:
        return
    # Setting project to In progress when first task is submitted
    project = frappe.get_doc("Project_demo", doc.project)

    if project.status == "Open":
        project.status = "In Progress"
        project.save()

    # Checking if any incomplete tasks remain
    incomplete_tasks = frappe.get_all(
        "Task_demo",
        filters = {
            "project": doc.project,
            "status": ["!=", "Completed"]
        }
    )

    # If no incomplete task then set project as Compelted project 
    if not incomplete_tasks:
        project.status = "Completed"
        project.save()

def validate_stock_before_sale(doc, method):
    for item in doc.items:
        actual_qty = frappe.db.get_value("Bin",
                                         {"item_code": item.item_code, "warehouse": item.warehouse},
                                         "actual_qty")
        if item.qty > actual_qty:
            frappe.throw(f"Insufficient stock for {item.item_code}")        