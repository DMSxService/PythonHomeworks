class Product:
    def __init__(self, name='Potato', weight=50.0, category='Vagetables'):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file_op = open(self.__file_name, 'r')
        file_cont = file_op.read()
        file_op.close()
        return file_cont

    def add(self, *products):

        for i in products:
            pr = self.get_products()
            pr_list = str(i).split(",")
            if pr_list[0] in pr:
                print(f'Продукт {pr_list[0]} уже есть в магазине')
            else:
                file_op = open(self.__file_name, 'a')
                file_op.write(str(i)+"\n")
                file_op.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
