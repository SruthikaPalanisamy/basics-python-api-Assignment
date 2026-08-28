// Copyright (c) 2026, Me and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Task", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on("Task", {
    refresh(frm) {

        frm.add_custom_button("Create Task", function() {

            const dialog = new frappe.ui.Dialog({
                title: "Create Task",

                fields: [
                    {
                        fieldname: "task_subject",
                        label: "Task Subject",
                        fieldtype: "Data",
                        reqd: 1
                    }
                ],

                primary_action_label: "Create Task",

                primary_action(values) {

                    frappe.call({
                        method: "library_management.api.create_task",

                        args: {
                            task_subject: values.task_subject
                        },

                        callback: function(r) {

                            if (r.message) {

                                dialog.hide();

                                frappe.msgprint({
                                    title: "Success",
                                    message: `Task <b>${r.message}</b> created successfully.`,
                                    indicator: "green"
                                });

                            }
                        }
                    });
                }
            });

            dialog.show();
        });
    }
});
