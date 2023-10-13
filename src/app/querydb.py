

def query_get_supplier(company_id, query_string):
    limit = query_string['limit']
    offset = query_string['offset']
    search_text = query_string['search_text']
    supplier_id = query_string['supplier_id']

    query = '''
        SELECT *, COUNT(id) OVER() total 
        FROM app_supplier
        WHERE "company_id" = {} 
    '''.format(company_id)

    if supplier_id:
        query += '''
            AND "id" = '{}' LIMIT 1
        '''.format(supplier_id)
    else:
        if search_text:
            query += '''
                AND ("name" ILIKE '%%{}%%' OR "sku" ILIKE '%%{}%%' OR "phone" ILIKE '%%{}%%')
            '''.format(search_text, search_text, search_text)
        query += '''
            ORDER BY "updated_at" DESC
            LIMIT {} OFFSET {}
        '''.format(limit, offset)

    return query

def query_get_customer(company_id, query_string):
    limit = query_string['limit']
    offset = query_string['offset']
    search_text = query_string['search_text']
    customer_id = query_string['customer_id']

    query = '''
        SELECT *, COUNT(id) OVER() total 
        FROM app_customer
        WHERE "company_id" = {} 
    '''.format(company_id)

    if customer_id:
        query += '''
            AND "id" = '{}' LIMIT 1
        '''.format(customer_id)
    else:
        if search_text:
            query += '''
                AND ("name" ILIKE '%%{}%%' OR "sku" ILIKE '%%{}%%' OR "phone" ILIKE '%%{}%%')
            '''.format(search_text, search_text, search_text)
        query += '''
            ORDER BY "updated_at" DESC
            LIMIT {} OFFSET {}
        '''.format(limit, offset)

    return query

def query_get_warehouse(company_id, query_string):
    limit = query_string['limit']
    offset = query_string['offset']
    search_text = query_string['search_text']
    warehouse_id = query_string['warehouse_id']
    start_date = query_string['start_date']
    end_date = query_string['end_date']

    query = '''
        SELECT *, COUNT(id) OVER() total 
        FROM app_warehouse
        WHERE "company_id" = {} 
    '''.format(company_id)

    if warehouse_id:
        query += '''
            AND "id" = '{}' LIMIT 1
        '''.format(warehouse_id)
    else:
        if search_text:
            query += '''
                AND ("name" ILIKE '%%{}%%' OR "sku" ILIKE '%%{}%%')
            '''.format(search_text, search_text)
        if start_date and end_date:
            query += '''
                AND DATE(created_at) BETWEEN '{}' AND '{}'
            '''.format(start_date, end_date)
        query += '''
            ORDER BY "updated_at" DESC
            LIMIT {} OFFSET {}
        '''.format(limit, offset)

    return query

def query_get_warranty(company_id, query_string):
    warranty_id = query_string['warranty_id']

    query = '''
        SELECT * FROM app_warranty
        WHERE "company_id" = {} 
    '''.format(company_id)

    if warranty_id:
        query += '''
            AND "id" = '{}' LIMIT 1
        '''.format(warranty_id)
    else:
        query += '''
            ORDER BY "updated_at" DESC
        '''
    return query


def query_get_category(company_id, query_string):
    parent_id = query_string['parent_id']
    search_text = query_string['search_text']
    limit = query_string['limit']
    offset = query_string['offset']
    
    query = '''
        SELECT *, COUNT(id) OVER() total  
        FROM app_category
        WHERE "company_id" = {}
    '''.format(company_id)
    if parent_id:
        query += '''
            AND "id" = {} LIMIT 1
        '''.format(parent_id)
    else:
        if search_text:
            query += '''
                AND ("name" ILIKE '%%{}%%')
            '''.format(search_text)
        query += '''
            ORDER BY "updated_at" DESC
            LIMIT {} OFFSET {}
        '''.format(limit, offset)
    return query

def query_get_brand(company_id, query_string):
    brand_id = query_string['brand_id']
    search_text = query_string['search_text']
    limit = query_string['limit']
    offset = query_string['offset']

    query = '''
        SELECT *, COUNT(id) OVER() total  
        FROM app_brand
        WHERE "company_id" = {} 
    '''.format(company_id)

    if brand_id:
        query += '''
            AND "id" = '{}' LIMIT 1
        '''.format(brand_id)
    else:
        if search_text:
            query += '''
                AND ("name" ILIKE '%%{}%%')
            '''.format(search_text)
        query += '''
            ORDER BY "updated_at" DESC
            LIMIT {} OFFSET {}
        '''.format(limit, offset)
    return query

def query_get_product(company_id, query_string):
    limit = query_string['limit']
    offset = query_string['offset']
    search_text = query_string['search_text']
    product_id = query_string['product_id']
    start_date = query_string['start_date']
    end_date = query_string['end_date']
    sortDate = query_string['sortDate']

    query = '''
        SELECT *, COUNT(id) OVER() total 
        FROM app_product
        WHERE "company_id" = {} 
    '''.format(company_id, limit, offset)

    if product_id:
        query += '''
            AND "id" = '{}' LIMIT 1
        '''.format(product_id)
    else:
        if search_text:
            query += '''
                AND ("name" ILIKE '%%{}%%' OR "sku" ILIKE '%%{}%%')
            '''.format(search_text, search_text)
        if start_date and end_date:
            query += '''
                AND DATE(created_at) BETWEEN '{}' AND '{}'
            '''.format(start_date, end_date)
        if sortDate:
            query += '''
                ORDER BY "created_at" {}
            '''.format(sortDate)
        else:  
            query += '''
                ORDER BY "updated_at" DESC
            '''
        query += '''
                LIMIT {} OFFSET {}
            '''.format(limit, offset)

    return query

def query_get_product_variant(company_id, query_string):
    limit = query_string['limit']
    offset = query_string['offset']
    product_id = query_string['product_id']

    query = '''
        SELECT *, COUNT(id) OVER() total 
        FROM app_productvariant
        WHERE "company_id" = {} 
    '''.format(company_id)

    if product_id:
        query += '''
            AND "product_id" = '{}'
        '''.format(product_id)
    query += '''
        ORDER BY "updated_at" DESC
        LIMIT {} OFFSET {}
    '''.format(limit, offset)

    return query

def query_get_inventory(company_id, query_string):
    limit = query_string['limit']
    offset = query_string['offset']
    variant_id = query_string['variant_id']
    warehouse_id = query_string['warehouse_id']
    start_date = query_string['start_date']
    end_date = query_string['end_date']

    query = '''
        SELECT a1.id, COUNT(a1.id) OVER() total 
        FROM app_inventory a1
        INNER JOIN app_productvariant a2 ON a1.variant_id = a2.id
        WHERE a1.company_id = {} 
    '''.format(company_id)

    if variant_id:
        query += '''
            AND a2.id = '{}'
        '''.format(variant_id)
    if warehouse_id:
        query += '''
            AND a2.warehouse_id = '{}'
        '''.format(warehouse_id)
    if start_date and end_date:
        query += '''
            AND DATE(a2.created_at) BETWEEN '{}' AND '{}'
        '''.format(start_date, end_date)
    
    query += '''
        ORDER BY a1.id DESC
        LIMIT {} OFFSET {}
    '''.format(limit, offset)

    return query

def query_get_inventory_report(company_id, query_string):
    limit = query_string['limit']
    offset = query_string['offset']
    start_date = query_string['start_date']
    end_date = query_string['end_date']

    query = '''
        SELECT *, COUNT(id) OVER() total 
        FROM app_inventoryreport
        WHERE "company_id" = {} 
    '''.format(company_id)

    if start_date and end_date:
        query += '''
            AND DATE(onhand_date) BETWEEN '{}' AND '{}'
        '''.format(start_date, end_date)
    query += '''
        ORDER BY "onhand_date" DESC
        LIMIT {} OFFSET {}
    '''.format(limit, offset)

    return query

def query_get_purchase_order(company_id, query_string):
    limit = query_string['limit']
    offset = query_string['offset']
    search_text = query_string['search_text']
    purchase_id = query_string['purchase_id']
    sortDate = query_string['sortDate']
    warehouse_id = query_string['warehouse_id']
    start_date = query_string['start_date']
    end_date = query_string['end_date']

    query = '''
        SELECT a1.id, COUNT(a1.id) OVER() total 
        FROM app_purchaseorder a1
        LEFT JOIN app_supplier a2 ON a1.supplier_id = a2.id
        WHERE a1.company_id = {}
    '''.format(company_id, limit, offset)

    if purchase_id:
        query += '''
            AND a1.id = '{}' LIMIT 1
        '''.format(purchase_id)
    else:
        if search_text:
            query += '''
                AND (a2.phone ILIKE '%%{}%%' OR a2.sku ILIKE '%%{}%%' OR a1.sku ILIKE '%%{}%%')
            '''.format(search_text, search_text, search_text)
        if warehouse_id:
            query += '''
                AND a1.warehouse_id = '{}'
            '''.format(warehouse_id)
        if start_date and end_date:
            query += '''
                AND DATE(a1.created_at) BETWEEN '{}' AND '{}'
            '''.format(start_date, end_date)
        if sortDate:
            query += '''
                ORDER BY a1.created_at {}
            '''.format(sortDate)
        else:  
            query += '''
                ORDER BY a1.updated_at DESC
            '''
        query += '''
                LIMIT {} OFFSET {}
            '''.format(limit, offset)

    return query

def query_get_sale_order(company_id, query_string):
    limit = query_string['limit']
    offset = query_string['offset']
    search_text = query_string['search_text']
    sale_id = query_string['sale_id']
    sortDate = query_string['sortDate']
    warehouse_id = query_string['warehouse_id']
    start_date = query_string['start_date']
    end_date = query_string['end_date']

    query = '''
        SELECT a1.id, COUNT(a1.id) OVER() total 
        FROM app_saleorder a1
        LEFT JOIN app_customer a2 ON a1.customer_id = a2.id
        INNER JOIN app_saledetail a3 ON a3.order_id = a1.id
        INNER JOIN app_productvariant a4 ON a3.variant_id = a4.id
        WHERE a1.company_id = {}
    '''.format(company_id, limit, offset)

    if sale_id:
        query += '''
            AND a1.id = '{}' LIMIT 1
        '''.format(sale_id)
    else:
        if search_text:
            query += '''
                AND (a2.phone ILIKE '%%{}%%' OR a2.sku ILIKE '%%{}%%' OR a1.sku ILIKE '%%{}%%')
            '''.format(search_text, search_text, search_text)
        if warehouse_id:
            query += '''
                AND a4.warehouse_id = '{}'
            '''.format(warehouse_id)
        if start_date and end_date:
            query += '''
                AND DATE(a1.created_at) BETWEEN '{}' AND '{}'
            '''.format(start_date, end_date)
        if sortDate:
            query += '''
                ORDER BY a1.created_at {}
            '''.format(sortDate)
        else:  
            query += '''
                ORDER BY a1.updated_at DESC
            '''
        query += '''
                LIMIT {} OFFSET {}
            '''.format(limit, offset)

    return query