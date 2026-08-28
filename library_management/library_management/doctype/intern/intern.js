// Copyright (c) 2026, Me and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Intern", {
// 	refresh(frm) {

// 	},
// });


// frappe.ui.form.on("Intern", {
//     refresh(frm) {
//         frappe.show_alert({
//             message: "Task saved successfully!",
//             indicator: "orange"
//         }, 5);
//     }
// });

// frappe.ui.form.on("Intern", {
//     refresh(frm) {
//         frappe.show_progress(
//             'Loading..',
//             70,
//             100,
//             'Please wait'
//         );
//     }
// });

// 
// frappe.ui.form.on("Intern", {
//     refresh(frm) {
//         new frappe.ui.form.MultiSelectDialog({
//             doctype: "Intern",
//             target: this.cur_frm,
//             setters: {
//                 status:"null",
//                 college:"KEC"
//             },
//             add_filters_group: 1,
//             date_field: "creation_date",

//             get_query() {
//                 return {
//                     filters: {
//                         docstatus: ["!=", 2]
//                     }
//                 };
//             },

//             action(selections) {
//                 console.log(selections);
//             }
//         });
//             }
// });

// frappe.ui.form.on("Intern", {
//     refresh(frm) {

//         frm.add_custom_button("Create Logs", () => {

//             const dialog = new frappe.ui.Dialog({
//                 title: __("Create Logs"),

//                 fields: [
//                     {
//                         fieldname: "logs",
//                         fieldtype: "Table",
//                         label: __("Logs"),
//                         in_place_edit: true,
//                         reqd: 1,

//                         fields: [
//                             {
//                                 fieldname: "log_type",
//                                 label: __("Log Type"),
//                                 fieldtype: "Select",
//                                 options: "IN\nOUT",
//                                 in_list_view: 1,
//                                 reqd: 1
//                             },
//                             {
//                                 fieldname: "time",
//                                 label: __("Time"),
//                                 fieldtype: "Time",
//                                 in_list_view: 1,
//                                 reqd: 1
//                             }
//                         ],

//                         on_add_row: (idx) => {

//                             let data_id = idx - 1;

//                             let logs = dialog.fields_dict.logs;

//                             let log_type =
//                                 (data_id % 2) === 0
//                                     ? "IN"
//                                     : "OUT";

//                             logs.df.data[data_id].log_type = log_type;

//                             logs.grid.refresh();
//                         }
//                     }
//                 ],

//                 primary_action: (values) => {

//                     console.log("Selected logs:", values.logs);

//                     dialog.hide();
//                 },

//                 primary_action_label: __("Create")
//             });

//             dialog.show();
//         });
//     }
// });




frappe.db.set_value(
    "Intern",
    'Alice',
    "status",
    "Inactive"
).then(r => {

    console.log("Database updated:", r.message);

    frm.set_value("status", "Inactive");

    frappe.show_alert({
        message: "Task marked as completed",
        indicator: "green"
    });
});
    
