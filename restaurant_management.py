import os
from prettytable import PrettyTable

class Order:
    def __init__(self, order_id, customer_name, items):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = items
        self.status = 'Sipariş Alındı'

    def __str__(self):
        return f"Order ID: {self.order_id}, Customer: {self.customer_name}, Items: {', '.join(self.items)}, Status: {self.status}"

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.orders = []
        self.next_order_id = 1

    def add_order(self, customer_name, items):
        order = Order(self.next_order_id, customer_name, items)
        self.orders.append(order)
        self.next_order_id += 1
        print(f"Sipariş Eklendi: {order}")

    def update_order_status(self, order_id, new_status):
        for order in self.orders:
            if order.order_id == order_id:
                order.status = new_status
                print(f"Sipariş Güncellendi: {order}")
                return
        print(f"Sipariş Bulunamadı: {order_id}")

    def list_orders(self):
        table = PrettyTable()
        table.field_names = ['Order ID', 'Customer', 'Items', 'Status']
        for order in self.orders:
            table.add_row([order.order_id, order.customer_name, ', '.join(order.items), order.status])
        print(table)

def main():
    restaurant = Restaurant("Ömer Hanem")

    while True:
        print("\n1. Sipariş Al\n2. Sipariş Durumunu Güncelle\n3. Siparişleri Listele\n4. Çıkış")
        choice = input("Seçiminizi Yapın: ")

        if choice == '1':
            customer_name = input("Müşteri Adı: ")
            items = input("Ürünler (virgülle ayırarak): ").split(',')
            restaurant.add_order(customer_name, [item.strip() for item in items])
        elif choice == '2':
            order_id = int(input("Sipariş ID: "))
            print("Yeni Durum: 1. Sipariş Hazırlanıyor, 2. Sipariş Tamamlandı")
            status_choice = input("Seçiminizi Yapın: ")
            if status_choice == '1':
                new_status = "Sipariş Hazırlanıyor"
            elif status_choice == '2':
                new_status = "Sipariş Tamamlandı"
            else:
                print("Geçersiz Seçim")
                continue
            restaurant.update_order_status(order_id, new_status)
        elif choice == '3':
            restaurant.list_orders()
        elif choice == '4':
            break
        else:
            print("Geçersiz Seçim")

if __name__ == "__main__":
    main()
