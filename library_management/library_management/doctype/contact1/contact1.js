// Copyright (c) 2026, Me and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Contact1", {
// 	refresh(frm) {

// 	},

const dialog = new frappe.ui.Dialog({
    title: "Create Contact",

    fields: [
        {
            fieldname: "first_name",
            label: "First Name",
            fieldtype: "Data",
            reqd: 1
        }
    ],

    primary_action_label: "Create Contact",

    primary_action(values) {
        const first_name = values.first_name;

        dialog.hide();

        frappe.route_options = {
            first_name: first_name
        };

        frappe.new_doc("Contact1");
    }
});

dialog.show();
