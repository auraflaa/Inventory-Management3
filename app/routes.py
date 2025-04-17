from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import (
    get_all_products, add_product, update_product, delete_product,
    get_all_order_statuses, get_all_companies, get_all_employees,
    get_all_customers, get_all_orders, get_order_details,
    get_all_purchase_orders, get_purchase_order_details,
    get_order_by_id, get_purchase_order_by_id, get_all_vendors,
    get_vendor_by_id, get_employee_by_id, get_customer_by_id,
    get_total_products, get_pending_orders, get_total_customers,
    get_product_by_id
)

main = Blueprint('main', __name__)

@main.route('/')
def dashboard():
    total_products = get_total_products()
    pending_orders = get_pending_orders()
    total_customers = get_total_customers()
    return render_template('dashboard/index.html', total_products=total_products, pending_orders=pending_orders, total_customers=total_customers)

@main.route('/inventory')
def inventory():
    products = get_all_products()
    return render_template('inventory/list.html', products=products)

@main.route('/add-item', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        # Handle adding a product
        pass
    return render_template('inventory/add.html')

@main.route('/edit-item/<int:product_id>', methods=['GET', 'POST'])
def edit_item(product_id):
    if request.method == 'POST':
        # Handle editing a product
        pass
    product = get_product_by_id(product_id)
    return render_template('inventory/edit.html', product=product)

@main.route('/orders')
def orders():
    orders = get_all_orders()
    return render_template('sales/orders/list.html', orders=orders)

@main.route('/order-details/<int:order_id>')
def order_details(order_id):
    order = get_order_by_id(order_id)
    return render_template('sales/orders/view.html', order=order)

@main.route('/customers')
def customers():
    customers = get_all_customers()
    return render_template('sales/customers/list.html', customers=customers)

@main.route('/customer-view/<int:customer_id>')
def customer_view(customer_id):
    customer = get_customer_by_id(customer_id)
    return render_template('sales/customers/view.html', customer=customer)

@main.route('/purchase-orders')
def purchase_orders():
    purchase_orders = get_all_purchase_orders()
    return render_template('purchasing/po/list.html', purchase_orders=purchase_orders)

@main.route('/purchase-order-details/<int:purchase_order_id>')
def purchase_order_details(purchase_order_id):
    po = get_purchase_order_by_id(purchase_order_id)
    return render_template('purchasing/po/view.html', po=po)

@main.route('/vendors')
def vendors():
    vendors = get_all_vendors()
    return render_template('purchasing/vendors/list.html', vendors=vendors)

@main.route('/vendor-view/<int:vendor_id>')
def vendor_view(vendor_id):
    vendor = get_vendor_by_id(vendor_id)
    return render_template('purchasing/vendors/view.html', vendor=vendor)

@main.route('/employees')
def employees():
    employees = get_all_employees()
    return render_template('people/employees/list.html', employees=employees)

@main.route('/employee-view/<int:employee_id>')
def employee_view(employee_id):
    employee = get_employee_by_id(employee_id)
    return render_template('people/employees/view.html', employee=employee)