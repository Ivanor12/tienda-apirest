from flask import Flask, jsonify, request

app = Flask(__name__)

from products import products


@app.route('/products')
def getProducts():
    return jsonify({"products": products, "message": "Product´s List"})

@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if (len(productsFound) > 0):
        return jsonify({"product": productsFound[0]})
    return jsonify({"message": "Producto no encontrado"}) 

@app.route('/products', methods=['POST'])
def addProduct():
    nuevo_producto = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }
    products.append(nuevo_producto)
    return jsonify({"message": "Producto añadido correctamente", "products": products})

@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if (len(productFound) > 0):
        productFound[0]['name'] == request.json['name']
        productFound[0]['price'] == request.json['price']
        productFound[0]['quantity'] == request.json['quantity']
        return jsonify({
            "message": "Producto actualizado",
            "product": productFound[0]
        })
    return jsonify({"message": "Producto no encontrado"})

@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if len(productsFound) > 0:
        products.remove(productsFound[0])
        return jsonify({
           "message": "Producto borrado",
           "products": products 
        })
    return jsonify({"message: Producto no encontrado"})

if __name__ == '__main__':
    app.run(debug=True, port=4000)