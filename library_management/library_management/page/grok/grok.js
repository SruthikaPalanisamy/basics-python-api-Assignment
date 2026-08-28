frappe.pages['grok'].on_page_load = function(wrapper) {

    let page = frappe.ui.make_app_page({
        title: 'Pagee',
        parent: wrapper,
        single_column: true
    });



    page.add_inner_button('Update Posts', () => {

        frappe.msgprint('Update Posts clicked');

    });


	// page.remove_inner_button('Update Posts');

    page.add_inner_button('Remove Update Button', () => {

        page.remove_inner_button('Update Posts');

    });


	let name = page.add_field({
		label:'Name',
		fieldtype:'Data',
		feildname:'name1',
		change() {

            console.log(
                'Selected:',
                name.get_value()
            );

        }
		
	})
    let status_field = page.add_field({

        label: 'Status',

        fieldtype: 'Select',

        fieldname: 'status',

        options: [
            'Open',
            'Closed',
            'Cancelled'
        ],

        change() {

            console.log(
                'Selected:',
                status_field.get_value()
            );

        }

    });


    page.add_inner_button('Get Values', () => {

        let values = page.get_form_values();

        console.log(values);

        frappe.msgprint(
            'Status: ' + values.status
        );

    });

    page.add_inner_button('Clear Fields', () => {

        page.clear_fields();

    });


	//page.clear_inner_toolbar();

    page.add_menu_item('Clear Toolbar', () => {

        page.clear_inner_toolbar();

    });
	//page.clear_inner_toolbar(); //page.clear_inner_toolbar() does not remove Menu items because the inner toolbar and the Menu are two different UI areas.

	page.add_menu_item('Clear Toolbar', () => {
    	page.clear_inner_toolbar();
	});

	page.add_menu_item('Remove Menu', () => {
		page.clear_menu();
	});
	//page.clear_inner_toolbar();
};