import frappe
from frappe.model.document import Document

class Utilisateurs(Document):
    def on_submit(self):
        create_or_update_user(self)

def create_or_update_user(doc):
    if not doc.email:
        frappe.throw("Email is required")

    if frappe.db.exists("User", {"email": doc.email}):
        user = frappe.get_doc("User", {"email": doc.email})
    else:
        user = frappe.new_doc("User")
        user.email = doc.email
        user.first_name = doc.full_name
        user.enabled = 1

    user.first_name = doc.full_name
    user.phone = doc.telephone

    if doc.password:
        user.new_password = doc.password

    user.roles = []
    if isinstance(doc.role, str):
        # Support single role selection
        user.append("roles", {"role": doc.role})
    elif isinstance(doc.role, list):
        # Support multi-select roles
        for role in doc.role:
            user.append("roles", {"role": role})

    user.save(ignore_permissions=True)
