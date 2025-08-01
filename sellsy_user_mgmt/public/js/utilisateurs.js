 

frappe.ui.form.on('Utilisateurs', {
    refresh: function (frm) {
        // displays a specific set of roles.
        frm.fields_dict['role'].get_query = function () {
            return {
                filters: {
                    name: ["in", ["Responsable de vente", "Responsable Logistique", "Financier", "Administrateur"]]
                }
            };
        };
        if ($('[data-fieldname="password"] input').length) {
            $('[data-fieldname="password"] input').attr('type', 'password'); // Mask the input
        }
        // if the selected role is sales manager -> warehouse field is displayed.
        frm.trigger('role');
        console.log("user_id: ", frm.doc.user_id)
        console.log("password:", frm.doc.password)

        if (frm.doc.user_id && frm.doc.password) {
            frm.toggle_display('password', false); // Hide the field
        } else {
            frm.toggle_display('password', true); // Show the field
        }

        frm.add_custom_button(__('Change User Password'), function () {
            frappe.call({
                method: 'flexierp.flexierp.doctype.utilisateurs.utilisateurs.generate_password',
                args: {
                    user: frm.doc.user_id
                },
                callback: function (r) {
                    frappe.msgprint(r.message);
                }
            });
        });

        // button to update the user activation or not
        let activation_button_name;
        let updated_value;
        if (frm.doc.active === 0) {
            activation_button_name = __("Activate user")
            updated_value = 1;
        } else {
            activation_button_name = __('Deactivate user')
            updated_value = 0;
        }

        frm.add_custom_button(activation_button_name, function () {
            frappe.call({
                method: 'flexierp.flexierp.doctype.utilisateurs.utilisateurs.deactivate_user',
                args: {
                    docname: frm.doc.name,
                    updated_value: updated_value
                },
                callback: function (r) {
                    if (r.message == true) {
                        frappe.call({
                            method: "flexierp.utils.helpers.add_comment",
                            args: {
                                button_name: activation_button_name,
                                doctype_name: frm.doctype,
                                document_name: frm.docname
                            },
                            callback: function (r) {
                                location.reload();
                            }
                        })
                    } else {
                        frappe.msgprint(__("Something went wrong"))
                    }
                }
            });
        });
    },
    role: function (frm) {
        // display the warehouse name field if the role is sales manager.
        if (frm.doc.role === "Responsable de vente") {
            frm.toggle_display('warehouse_name', true);
        } else {
            frm.toggle_display('warehouse_name', false);
        }
    }
});