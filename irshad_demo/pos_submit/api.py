import frappe
from frappe.utils import now_datetime

def handle_pos_submit(doc, method):

    if not doc.is_pos:
        return
    
    if doc.pos_profile == "Kitchen Service POS":
        create_kitchen_order(doc)

    elif doc.pos_profile == "Pharmacy POS":
        create_pharmacy_order(doc)

def create_kitchen_order(doc):       
    kitchen = frappe.get_doc({
        "doctype":"Kitchen Order",
        "pos_invoice":doc.name,
        "order_time": now_datetime(),
        "status": "Received",
        "customer": doc.customer
    })

    kitchen.insert()

    frappe.publish_realtime(
        event="new_kitchen_order",
        message={
            "name":kitchen.name,
            "status": kitchen.status,
            "pos_invoice": kitchen.pos_invoice
        },
        after_commit=True
    )
    frappe.msgprint("New Kitchen Order Listed")

def create_pharmacy_order(doc):
    pharmacy = frappe.get_doc({
        "doctype": "Pharmacy Order POS",
        "pharmacy_pos_invoice":doc.name,
        "status":"Received",
        "order_datetime": now_datetime(),
        "customer": doc.customer
    })

    pharmacy.insert()

    frappe.publish_realtime(
        event="new_pharmacy_order",
        message={
            "name":pharmacy.name,
            "status":pharmacy.status,
            "pharmacy_pos_invoice": pharmacy.pharmacy_pos_invoice
        },
        after_commit=True
    )
    frappe.msgprint("New Pharmacy Order Listed")


