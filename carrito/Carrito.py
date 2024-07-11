class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session["carrito"]
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar(self, auto):
        id = str(auto.id_auto)
        if id not in self.carrito.keys():
            self.carrito[id] = {
                "auto ID": auto.id_auto,
                "modelo": auto.modelo,
                "precio": auto.precio,
                "cantidad": 1
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["precio"] += auto.precio
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True
    
    def eliminar(self, auto):
        id = str(auto.id_auto)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito
    
    def restar(self, auto):
        id = str(auto.id_auto)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["precio"] -= auto.precio
            if self.carrito[id]["cantidad"] <= 0: self.eliminar(auto)
            self.guardar_carrito()
    
    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True
