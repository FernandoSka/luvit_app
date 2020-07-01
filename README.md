# luvit_app

Esta es una aplicacion de ejemplo que muestra una insercion en bulk y una consulta de objetos basica bajo el esquema de trabajo del framework Django


* Especificaciones:

Para este ejemplo se utilizo Heroku, un PaaS parecido a beanstalk que por cuestiones de tiempo para la reparacion de dependencias de Beanstalk cli para ubuntu, se utilizo para hacer desplegar nuestra aplicacion

* Tecnologias:
  
  + Heroku
  + Django
  + Django Rest framework
  + Postman (API debbug)

* API:

  - Creacion de objetos nuevos (POST)
    + url: https://luvit-app.herokuapp.com/api/Product_bulk
    + Json dict: 
    ```
    {
        "products": [
            {
                "name": "Producto 5",
                "value": 3,
                "stock": 1,
                "discount_value":2
            },
            {
                "name": "Producto 6",
                "value": -1,
                "stock": -1
            },
            {
                "name": "Producto 7",
                "value": -1,
                "stock": -1
            }
        ]
    }
    ```
    + Expected json response (Beautify):
    ```
    {
        "status": "ERROR",
        "products_report": [
            {
                "product_id": 2,
                "errors": {
                    "value": [
                        "The value should be up to 0"
                    ],
                    "stock": [
                        "The value should be up to 0"
                    ]
                }
            },
            {
                "product_id": 3,
                "errors": {
                    "value": [
                        "The value should be up to 0"
                    ],
                    "stock": [
                        "The value should be up to 0"
                    ]
                }
            }
        ],
        "number_of_products_unable_to_parse": 2
    }
    ```
    
    
    + Curl test: 
    ```
    curl -H "Content-Type: application/json" -d '{"products":[{"name":"Producto 5","value":3,"stock":1,"discount_value":2},{"name":"Producto 6","value":-1,"stock":-1},{"name":"Producto 7","value":-1,"stock":-1}]}' -X POST https://luvit-app.herokuapp.com/api/Product_bulk
    ```
    + Response test: 
    ```
    {"status":"ERROR","products_report":[{"product_id":2,"errors":{"value":["The value should be up to 0"],"stock":["The value should be up to 0"]}},{"product_id":3,"errors":{"value":["The value should be up to 0"],"stock":["The value should be up to 0"]}}],"number_of_products_unable_to_parse":2}
    ```
  - Obtencion de objetos (GET)
    + Url: https://luvit-app.herokuapp.com/api/Product
    + Expected json response (Beautify):
    ```
    [
        {
            "name": "Producto 5",
            "value": 3,
            "stock": 1,
            "discount_value": 2
        }
    ]
    ```
    + Curl test:
    ```
    curl https://luvit-app.herokuapp.com/api/Product
    ```
    + Response test:
    ```
    [{"name":"Producto 5","value":3.0,"stock":1,"discount_value":2.0}]
    ```
