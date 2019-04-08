import csv

#Read csv files
def read_files(csv_file):
    with open(csv_file, mode='r') as f:
        csv_reader = csv.reader(f)
        data = list(csv_reader)
    return data



#Use this function to extract each column in order_products
def extract_order_products(order_products):
    order_id = []
    product_id = []
    cart_order = []
    reordered = []
    for row in order_products:
        order_id.append(row[0])
        product_id.append(row[1])
        cart_order.append(row[2])
        reordered.append(row[3])
    return [order_id,product_id,cart_order,reordered]



#Use this function to extract each column in products
def extract_products(products):
    products_id = []
    department_id = []
    for row in products:
        products_id.append(row[0])
        department_id.append(row[3])
    return [products_id,department_id]


#Use this function to get department_id for each ordered product
def get_department_id(product_id,products_id,department_id):
    dep_product_id = ['department product']
    for i in range(1, len(product_id)):
        if products_id[int(product_id[i])] == product_id[i]:
            dep_product_id.append(department_id[int(product_id[i])])
        else:
            Print("This method doesn't apply to this dataset")
    return dep_product_id



# Count the number of times a product was request from each department
# And the number of times a product was requested for the first time
def count_number_of_orders(dep_product_id, product_id, reordered):
    w, h = 0, 4;
    department_num_orders = [[0 for x in range(w)] for y in range(h)]

    product_id_marker = set()
    tmp = dep_product_id[1:]
    product_id = product_id[1:]
    reordered = reordered[1:]

    for index, row in enumerate(tmp):
        if row not in department_num_orders[0]:
            department_num_orders[0].append(row)
            department_num_orders[1].append(1)
            #Use variable product_id_marker to record if a product has been requested before.
            product_id_marker.add(product_id[index])

            #If the reordered flag is 1, then the product is definitely not requested for the first time.
            if reordered[index] == '1':
                department_num_orders[2].append(0)
            else:
                if product_id[index] not in product_id[:index]:
                    department_num_orders[2].append(1)
                else:
                    department_num_orders[2].append(0)


        else:
            for index_dep, row_dep in enumerate(department_num_orders[0]):
                if row_dep == row:
                    department_num_orders[1][index_dep] += 1
                    if reordered[index] == '1':
                        pass
                    else:
                        if product_id[index] not in product_id_marker:
                            department_num_orders[2][index_dep] += 1
            product_id_marker.add(product_id[index])
    return department_num_orders


#Use this function to calculate the percentage
def calculate_percentage(department_num_orders):
    department_num_orders[3]= map(lambda x,y:x/y,department_num_orders[2],department_num_orders[1])
    department_num_orders[3] = list(department_num_orders[3])
    for i in range(len(department_num_orders[3])):
        department_num_orders[3][i] = round(department_num_orders[3][i],2)
    return department_num_orders



#Sort our data by department_id
def sort_department(department_num_orders):
    for i in range(len(department_num_orders[0])):
        department_num_orders[0][i]=int(department_num_orders[0][i])
    zipped = list(zip(department_num_orders[0],department_num_orders[1],department_num_orders[2],department_num_orders[3]))
    zipped.sort()
    return zipped

#Main function
def main():
    #Read csv files
    order_products = read_files('order_products__prior.csv')
    products = read_files('products.csv')

    #Extract columns
    order_id, product_id, cart_order, reordered = extract_order_products(order_products)
    products_id, department_id = extract_products(products)

    #Get the department_id for each ordered product
    dep_product_id = get_department_id(product_id,products_id,department_id)


    #Get results
    department_num_orders = count_number_of_orders(dep_product_id, product_id, reordered)
    department_num_orders = calculate_percentage(department_num_orders)

    #Sort the results by department id
    department_final = sort_department(department_num_orders)
    print(department_final)

if __name__ == "__main__":
    main()

