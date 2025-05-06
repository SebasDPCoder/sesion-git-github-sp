
import os
os.system('clear')

print("="*40)
print(f"{"☕ COFFEE SHOP ☕":^40}")
print("="*40)


print("=" * 40)
print(f"{'MENÚ DE LA CAFETERÍA':^40}")
print("=" * 40)


menu = {
    "Bebidas Calientes": {
        "Espresso": 2.00,
        "Cappuccino": 3.50,
        "Latte": 3.75,
        "Te": 2.50,
        "Chocolate caliente": 3.00
    },
    "Bebidas Frías": {
        "Cafe frio": 3.00,
        "Smoothie de frutas": 4.50,
        "Te helado": 2.75,
        "Limonada": 2.50
    },
    "Desayunos y Snacks": {
        "Croissant": 2.50,
        "Muffin": 2.75,
        "Tostada con aguacate": 4.00,
        "Yogur con granola": 3.50
    },
    "Postres": {
        "Pastel de chocolate": 4.00,
        "Cheesecake": 4.50,
        "Galletas": 1.50
    }
}


for category, items in menu.items():
    print(f"\n{category}")
    print("-" * 40)
    for product, price in items.items():
        print(f"- {product}: ${price:.2f}")

print("\nBienvenido a la cafetería. ¿Qué deseas pedir?")
order = []
total = 0

while True:
    product_order = input("\nIngresa el nombre del producto (o escribe 'salir' para finalizar): ").strip()
    if product_order.lower() == "salir":
        break

    found = False
    for categoria, items in menu.items():
        if product_order.capitalize() in items:
            found = True
            price = items[product_order] 
            while True:
                try:
                    quantity = int(input(f"¿Cuantos {product_order} deseas? "))
                    if quantity <= 0:
                        print("Por favor, ingresa una cantidad valida.")
                        continue
                    break
                except ValueError:
                    print("Por favor, ingresa un numero valido.")
            
            subtotal = price * quantity
            total += subtotal
            order.append((product_order, quantity, subtotal))
            print(f"Agregado {quantity} {product_order}(s) al pedido.")
            break

    if not found:
        print("El producto ingresado no esta en el menu. Por favor, intenta nuevamente.")

print("\nResumen de tu pedido:")
print("-" * 40)
for item in order:
    print(f"{item[1]}x {item[0]} - ${item[2]:.2f}")

if total > 50:
    discount = total * 0.10
    total -= discount
    print(f"\nSe ha aplicado un descuento del 10%: -${discount:.2f}")

print(f"\nTotal a pagar: ${total:.2f}")
print("Gracias por tu compra!")