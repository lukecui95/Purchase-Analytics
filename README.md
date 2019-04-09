# Purchase-Analytics - Pengwei Cui

I used a top-approach for this problem.


## Approach

### Read csv files and extract each useful columns

Use functions **read_files**, **extract_order_products** and **extract_products** to achieve this goal.
Each of the useful columns will save in a list.

### Get department_id for each ordered product

Use functions **check_products** and **get_department_id** to achieve this goal.

When we call the **get_department_id** function, it will first check whether the product_ids in products.csv are documented in sequence. For example, product_ids are documented like 1,2,3,4,5,6,7,8....

If the product_ids are documented in sequence, we'll use a much faster method. Instead of searching the product_id in products.csv, we'll get the product_id from order_products.csv and get the department_id in products.csv by using index product_id. For example, if the product_id we get is 3456, then we can just get department_id[3456], since this product is documented in row 3456.

If the product_ids are not documented in sequence, we have to search each product_id in order to get the department_id for this product.

### Count the number of times a product was request and the number of times a product was requested for the first time.

Use the function **count_number_of_orders** to achieve this goal and save the result in a two-dimension list.

The function will go through each row in the list product_id(each row in order_product.csv) and count the number of orders in each department.

For the number of times a product was requested for the first time, the function will first check whether the reordered flag is 1 or not. If it's 1, then the product is definitely not ordered for the fisrt time. If not, we will check if the product_id is in the previous ordered product_ids. If still not, we will add one for this department. Moreover, we use **set** to record if a product is ordered before, since it's much faster to search in sets than lists.

### Calculate the percentage, sort the result by department_id and get our report.csv

Use functions **calculate_percentage**, **sort_department** and **get_report** to achieve this goal.


## Run instructions

1) cd to my files
2) type at the command prompt: sh run.sh

