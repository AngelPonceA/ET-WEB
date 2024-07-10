class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        else:
            self.carrito = carrito

    def agregar(self, auto):
        if str(auto.id) not in self.carrito.keys():
            self.carrito[auto.id] = {
                
            }
