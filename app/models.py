from app import mysql

# -------------------- OrderStatus --------------------
def get_all_order_statuses():
    """Fetch all order statuses."""
    cursor = mysql.connection.cursor()
    query = "SELECT * FROM OrderStatus"
    cursor.execute(query)
    statuses = cursor.fetchall()
    cursor.close()
    return statuses

# -------------------- Companies --------------------
def get_all_companies():
    """Fetch all companies."""
    cursor = mysql.connection.cursor()
    query = "SELECT * FROM Companies"
    cursor.execute(query)
    companies = cursor.fetchall()
    cursor.close()
    return companies

def get_company_by_id(company_id):
    """Fetch a single company by its ID."""
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM Companies WHERE CompanyID = %s", (company_id,))
    company = cursor.fetchone()
    cursor.close()
    return company

def get_all_vendors():
    """Fetch all vendors."""
    cursor = mysql.connection.cursor()
    query = "SELECT * FROM Companies"
    cursor.execute(query)
    vendors = cursor.fetchall()
    cursor.close()
    return vendors

def get_vendor_by_id(vendor_id):
    """Fetch a single vendor by its ID."""
    cursor = mysql.connection.cursor()
    query = "SELECT * FROM Companies WHERE CompanyID = %s"
    cursor.execute(query, (vendor_id,))
    vendor = cursor.fetchone()
    cursor.close()
    return vendor

# -------------------- Employees --------------------
def get_all_employees():
    """Fetch all employees."""
    cursor = mysql.connection.cursor()
    query = "SELECT * FROM Employees"
    cursor.execute(query)
    employees = cursor.fetchall()
    cursor.close()
    return employees

def get_employee_by_id(employee_id):
    """Fetch a single employee by its ID."""
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM Employees WHERE EmployeeID = %s", (employee_id,))
    employee = cursor.fetchone()
    cursor.close()
    return employee

# -------------------- Customers --------------------
def get_all_customers():
    """Fetch all customers."""
    cursor = mysql.connection.cursor()
    query = "SELECT * FROM Customers"
    cursor.execute(query)
    customers = cursor.fetchall()
    cursor.close()
    return customers

def get_customer_by_id(customer_id):
    """Fetch a single customer by its ID."""
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM Customers WHERE CustomerID = %s", (customer_id,))
    customer = cursor.fetchone()
    cursor.close()
    return customer

def get_total_customers():
    """Fetch the total number of customers."""
    cursor = mysql.connection.cursor()
    query = "SELECT COUNT(*) FROM Customers"
    cursor.execute(query)
    total_customers = cursor.fetchone()[0]
    cursor.close()
    return total_customers

# -------------------- Products --------------------
def get_all_products(search_query=''):
    """Fetch all products, optionally filtered by a search query."""
    cursor = mysql.connection.cursor()
    if search_query:
        query = """
            SELECT ProductID, ProductName, ProductCode, UnitPrice, QuantityPerUnit
            FROM Products
            WHERE ProductName LIKE %s OR ProductCode LIKE %s
        """
        cursor.execute(query, (f'%{search_query}%', f'%{search_query}%'))
    else:
        query = "SELECT * FROM Products"
        cursor.execute(query)
    products = cursor.fetchall()
    cursor.close()
    return products

def add_product(product_name, product_code, unit_price, quantity):
    """Add a new product."""
    cursor = mysql.connection.cursor()
    query = """
        INSERT INTO Products (ProductName, ProductCode, UnitPrice, QuantityPerUnit)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (product_name, product_code, unit_price, quantity))
    mysql.connection.commit()
    cursor.close()

def get_product_by_id(product_id):
    """Fetch a single product by its ID."""
    cursor = mysql.connection.cursor()
    query = "SELECT ProductID, ProductName, ProductCode, UnitPrice, QuantityPerUnit FROM Products WHERE ProductID = %s"
    cursor.execute(query, (product_id,))
    product = cursor.fetchone()
    cursor.close()
    return product

def update_product(product_id, product_name, product_code, unit_price, quantity):
    """Update an existing product in the database."""
    cursor = mysql.connection.cursor()
    query = """
        UPDATE Products
        SET ProductName = %s, ProductCode = %s, UnitPrice = %s, QuantityPerUnit = %s
        WHERE ProductID = %s
    """
    cursor.execute(query, (product_name, product_code, unit_price, quantity, product_id))
    mysql.connection.commit()
    cursor.close()

def delete_product(product_id):
    """Delete a product from the database."""
    cursor = mysql.connection.cursor()
    query = "DELETE FROM Products WHERE ProductID = %s"
    cursor.execute(query, (product_id,))
    mysql.connection.commit()
    cursor.close()

def get_product_vendors(product_id):
    """Fetch vendors for a specific product."""
    cursor = mysql.connection.cursor()
    query = """
        SELECT Companies.CompanyName, Companies.BusinessPhone
        FROM ProductVendors
        JOIN Companies ON ProductVendors.VendorID = Companies.CompanyID
        WHERE ProductVendors.ProductID = %s
    """
    cursor.execute(query, (product_id,))
    vendors = cursor.fetchall()
    cursor.close()
    return vendors

def get_product_vendors_full(product_id):
    """Get full vendor details for a product."""
    cursor = mysql.connection.cursor()
    query = """
        SELECT Companies.* 
        FROM ProductVendors
        JOIN Companies ON ProductVendors.VendorID = Companies.CompanyID
        WHERE ProductVendors.ProductID = %s
    """
    cursor.execute(query, (product_id,))
    vendors = cursor.fetchall()
    cursor.close()
    return vendors

def get_total_products():
    """Fetch the total number of products."""
    cursor = mysql.connection.cursor()
    query = "SELECT COUNT(*) FROM Products"
    cursor.execute(query)
    total_products = cursor.fetchone()[0]
    cursor.close()
    return total_products

# -------------------- Orders --------------------
def get_all_orders():
    """Fetch all orders."""
    cursor = mysql.connection.cursor()
    query = """
        SELECT Orders.OrderID, Customers.FirstName, Customers.LastName, OrderDate, ShippedDate, OrderStatusName
        FROM Orders
        JOIN Customers ON Orders.CustomerID = Customers.CustomerID
        JOIN OrderStatus ON Orders.OrderStatusID = OrderStatus.OrderStatusID
    """
    cursor.execute(query)
    orders = cursor.fetchall()
    cursor.close()
    return orders

def get_order_by_id(order_id):
    """Fetch a single order by its ID."""
    cursor = mysql.connection.cursor()
    query = """
        SELECT Orders.OrderID, Customers.FirstName, Customers.LastName, OrderDate, ShippedDate, OrderStatusName
        FROM Orders
        JOIN Customers ON Orders.CustomerID = Customers.CustomerID
        JOIN OrderStatus ON Orders.OrderStatusID = OrderStatus.OrderStatusID
        WHERE Orders.OrderID = %s
    """
    cursor.execute(query, (order_id,))
    order = cursor.fetchone()
    cursor.close()
    return order

def create_order(customer_id, employee_id, payment_method):
    """Create a new order."""
    cursor = mysql.connection.cursor()
    query = """
        INSERT INTO Orders (CustomerID, EmployeeID, PaymentMethod, OrderStatusID)
        VALUES (%s, %s, %s, 1)  # Default status = 1 (Pending)
    """
    cursor.execute(query, (customer_id, employee_id, payment_method))
    mysql.connection.commit()
    order_id = cursor.lastrowid
    cursor.close()
    return order_id

def add_order_detail(order_id, product_id, quantity, unit_price):
    """Add details to an order."""
    cursor = mysql.connection.cursor()
    query = """
        INSERT INTO OrderDetails (OrderID, ProductID, Quantity, UnitPrice)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (order_id, product_id, quantity, unit_price))
    mysql.connection.commit()
    cursor.close()

def get_pending_orders():
    """Fetch the total number of pending orders."""
    cursor = mysql.connection.cursor()
    query = "SELECT COUNT(*) FROM Orders WHERE OrderStatusID = 1"  # Assuming 1 represents 'Pending'
    cursor.execute(query)
    pending_orders = cursor.fetchone()[0]
    cursor.close()
    return pending_orders

# -------------------- OrderDetails --------------------
def get_order_details(order_id):
    """Fetch details of a specific order."""
    cursor = mysql.connection.cursor()
    query = """
        SELECT OrderDetails.OrderDetailID, Products.ProductName, OrderDetails.Quantity, OrderDetails.UnitPrice, OrderDetails.Discount
        FROM OrderDetails
        JOIN Products ON OrderDetails.ProductID = Products.ProductID
        WHERE OrderDetails.OrderID = %s
    """
    cursor.execute(query, (order_id,))
    details = cursor.fetchall()
    cursor.close()
    return details

# -------------------- PurchaseOrders --------------------
def get_all_purchase_orders():
    """Fetch all purchase orders."""
    cursor = mysql.connection.cursor()
    query = """
        SELECT PurchaseOrders.PurchaseOrderID, Companies.CompanyName, Employees.FirstName, Employees.LastName, OrderDate, OrderStatusName
        FROM PurchaseOrders
        JOIN Companies ON PurchaseOrders.VendorID = Companies.CompanyID
        JOIN Employees ON PurchaseOrders.SubmittedBy = Employees.EmployeeID
        JOIN OrderStatus ON PurchaseOrders.StatusID = OrderStatus.OrderStatusID
    """
    cursor.execute(query)
    purchase_orders = cursor.fetchall()
    cursor.close()
    return purchase_orders

def get_purchase_order_by_id(purchase_order_id):
    """Fetch a single purchase order by its ID."""
    cursor = mysql.connection.cursor()
    query = """
        SELECT PurchaseOrders.PurchaseOrderID, Companies.CompanyName, Employees.FirstName, Employees.LastName, OrderDate, OrderStatusName
        FROM PurchaseOrders
        JOIN Companies ON PurchaseOrders.VendorID = Companies.CompanyID
        JOIN Employees ON PurchaseOrders.SubmittedBy = Employees.EmployeeID
        JOIN OrderStatus ON PurchaseOrders.StatusID = OrderStatus.OrderStatusID
        WHERE PurchaseOrders.PurchaseOrderID = %s
    """
    cursor.execute(query, (purchase_order_id,))
    purchase_order = cursor.fetchone()
    cursor.close()
    return purchase_order

def create_purchase_order(vendor_id, submitted_by, product_list):
    """Create a new purchase order."""
    cursor = mysql.connection.cursor()
    try:
        # Create PO header
        query = """
            INSERT INTO PurchaseOrders (VendorID, SubmittedBy, StatusID)
            VALUES (%s, %s, 1)  # Default status = 1 (Pending)
        """
        cursor.execute(query, (vendor_id, submitted_by))
        po_id = cursor.lastrowid

        # Add PO details
        for product in product_list:
            query = """
                INSERT INTO PurchaseOrderDetails 
                (PurchaseOrderID, ProductID, Quantity, UnitCost)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (
                po_id,
                product['product_id'],
                product['quantity'],
                product['unit_cost']
            ))

        mysql.connection.commit()
        return po_id
    except Exception as e:
        mysql.connection.rollback()
        raise e
    finally:
        cursor.close()

# -------------------- PurchaseOrderDetails --------------------
def get_purchase_order_details(purchase_order_id):
    """Fetch details of a specific purchase order."""
    cursor = mysql.connection.cursor()
    query = """
        SELECT Products.ProductName, PurchaseOrderDetails.Quantity, PurchaseOrderDetails.UnitCost, PurchaseOrderDetails.ReceivedDate
        FROM PurchaseOrderDetails
        JOIN Products ON PurchaseOrderDetails.ProductID = Products.ProductID
        WHERE PurchaseOrderDetails.PurchaseOrderID = %s
    """
    cursor.execute(query, (purchase_order_id,))
    details = cursor.fetchall()
    cursor.close()
    return details

# -------------------- Unified Changes --------------------
def update_order_status(order_id, new_status_id):
    """Update the status of an order."""
    cursor = mysql.connection.cursor()
    cursor.execute(
        "UPDATE Orders SET OrderStatusID = %s WHERE OrderID = %s",
        (new_status_id, order_id)
    )
    mysql.connection.commit()
    cursor.close()

def update_purchase_order_status(po_id, new_status_id):
    """Update the status of a purchase order."""
    cursor = mysql.connection.cursor()
    cursor.execute(
        "UPDATE PurchaseOrders SET StatusID = %s WHERE PurchaseOrderID = %s",
        (new_status_id, po_id)
    )
    mysql.connection.commit()
    cursor.close()