frappe.pages['itam'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'IT Asset Management',
		single_column: true
	});
}