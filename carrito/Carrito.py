class carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get["carrito"]
        if not carrito:
            carrito = self.session["carrito"] = {}
        else:
            self.carrito = carrito

    def agregar(self, auto):
        id = str(auto.id_auto)
        if id not in self.carrito.keys():
            self.carrito[auto.id] = {
                "auto ID": auto.id_auto,
                "modelo": auto.modelo,
                "precio": auto.precio,
                "cantidad": 1,
                'imagen': auto.img
            }
        else:
            for key, value in self.carrito.items():
                if key == str(id):
                    value["cantidad"] = value["cantidad"] + 1
                    break
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True
    
    def eliminar(self, auto):
        id = str(auto.id_auto)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()
    
    def restar(self, auto):
        for key, value in self.carrito.item(): 
            id = str(auto.id_auto)
            if id in self.carrito.keys():
                self.carrito[id]["cantidad"] -= 1
                if self.carrito[id]["cantidad"] < 1:
                    self.eliminar(auto)
                else:
                    self.guardar_carrito()
                break
            else:
                print("XD")

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True
