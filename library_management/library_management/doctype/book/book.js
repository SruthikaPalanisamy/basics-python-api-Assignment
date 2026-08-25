// Copyright (c) 2026, Me and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Book", {
// 	refresh(frm) {

// 	},
// });
//import frappe;


// frappe.ui.form.on("Book", {
//     refresh(frm) {

//         frappe.realtime.emit(
//             "book_subscribe",
//             frm.doc.name
//         );

//         if (!frm.book_realtime_listener_added) {

//             frappe.realtime.on("book_updated", (data) => {
//                 console.log("BOOK UPDATED:", data);
//             });

//             frm.book_realtime_listener_added = true;
//         }
//     }
// });

frappe.ui.form.on("Book", {
    refresh(frm) {

        frappe.realtime.on("book_updated", (data) => {
            console.log("Book updated:", data);
        });

    }
});