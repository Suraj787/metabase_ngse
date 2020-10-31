frappe.pages['metabase-dashboard'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Metabase Dashboard',
		single_column: true
	});
	$(frappe.render_template('metabase_dashboard')).appendTo(page.main);
}