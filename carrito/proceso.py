def total_pago(request):
    total = 0
    if request.user.is_authenticated:
        if request.session["carrito"]:
            for key, value in request.session["carrito"].items():
                total += int(value["precio"])
    return{"total_pago": total}