// Copyright (c) 2018, Gaurav Naik and contributors
// For license information, please see license.txt
cur_frm.cscript.tax_table = "Sales Taxes and Charges";
{% include 'erpnext/accounts/doctype/sales_taxes_and_charges_template/sales_taxes_and_charges_template.js' %}

frappe.ui.form.on('Consignment Note', {
	refresh: function(frm) {

	}
});
