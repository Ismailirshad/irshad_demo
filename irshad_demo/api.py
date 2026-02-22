import frappe
from frappe.utils import nowdate, now, today, add_days


@frappe.whitelist()
def get_emoji():
    return "🚀"

def item_after_insert(doc, method):
    frappe.msgprint("New item added to list") 

def new_supplier_added(doc, method):
    frappe.msgprint("New supplier added")

def ticket_issued(doc, method):
    if not doc.priority:
       frappe.throw("Priority shold be selected?")

def sales_order_recieved(doc, method):
    frappe.msgprint(f"Sales order recieved from {doc.customer}")

def new_customer_created(doc, method):
    frappe.msgprint("New customer added")

def block_delete(doc, method):
    frappe.throw("You cannot delete the customer")

def after_customer_delete(doc, method):
    frappe.msgprint("Customer deleted successfully")

def send_issue_reminders():
    issues = frappe.get_all("Issue", filters={"status": "Open"})

    if issues == 0:
        return 
    
    frappe.sendmail(
            recipients=["admin@gmail.com"],
            subject="pending issues",
            message="There are open issues"
        )
    frappe.log_error("Pending issue reminders mail sent", "Scheduler Test")

def auto_close_issue():
    cutoff = add_days(nowdate(), -7)

    frappe.db.sql("""
                  UPDATE `tabIssue`
                  SET status = 'Closed'
                  WHERE status = 'Open'
                  AND creation < %s
                  """, cutoff)
    frappe.db.commit()

    frappe.log_error(
        f"Issues older than {cutoff} auto closed",
        "Weekly Issue auto closed"
    )

def validate_web_form(doc, method):
    if doc.title and len(doc.title) < 3:
        frappe.throw("Title must be more than 3 characters")  


# API call Demo
@frappe.whitelist()
def print_hello():
    return "Hello Irshad I am API" 
        
@frappe.whitelist()
def greet(name):
    return f"HEllo{name}"  

@frappe.whitelist()
def get_kitchen_orders():
    return frappe.get_all(
        "Kitchen Order",
        fields= ["name", "status", "customer"]
    ) 

@frappe.whitelist()
def add_description(title):
    doc = frappe.get_doc({
        "doctype": "ToDo",
        "description": title
    }) 
    doc.insert()
    return "description added"        

@frappe.whitelist()
def update_pharmacy_order_status(name, new_status):
    doc = frappe.get_doc(
        "Pharmacy Order POS", name
    )
    doc.status = new_status
    doc.save()
    return "Updated"    