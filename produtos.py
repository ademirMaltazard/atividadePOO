class Produtos:
    def __init__(self, cod, nome, preco, quantEstoque):
        self.__cod = cod
        self.__nome = nome
        self.__preco = preco
        self.__quantEstoque = quantEstoque

    def getCod(self):
        return self.__cod

    def getNome(self):
        return self.__nome

    def getPreco(self):
        return self.__preco

    def getQuantidade(self):
        return self.__quantEstoque

    def setCod(self, newCod):
        self.__cod = newCod

    def setNome(self, newNome):
        self.__nome = newNome

    def setPreco(self, newPreco):
        self.__preco = newPreco

    def entrada(self, quantidade):
        self.__quantEstoque += quantidade

    def saida(self, quantidade):
        if self.__quantEstoque == 0:
            return
        elif self.__quantEstoque > 0:
            self.__quantEstoque -= quantidade

        if self.__quantEstoque < 0:
            self.__quantEstoque = 0

    def MostrarDescricao(self):
        return f"Código: {f'{self.getCod()}:>8'} Nome: {f'{self.getNome()}':>15}\n Preço: {self.getPreco():.2f}\n Quantidade em estoque: {self.getQuantidade()}"


class Alimentos(Produtos):
    def __init__(self, cod, nome, preco, quantEstoque):
        super().__init__(cod, nome, preco, quantEstoque)

    def MostrarDescricao(self):
        if self.getQuantidade() <= 0:
            quantEstoque = 'Produto indisponível'
        else:
            quantEstoque = self.getQuantidade()
        return f"{'Produto tipo Alimento:':<23} Código: {f'{self.getCod()}':>5} Nome: {f'{self.getNome()}':<20} Preço: {f'{self.getPreco():.2f}':>8} Quantidade em estoque: {quantEstoque}"

class Bebidas(Produtos):
    def __init__(self, cod, nome, preco, quantEstoque):
        super().__init__(cod, nome, preco, quantEstoque)

    def MostrarDescricao(self):
        if self.getQuantidade() <= 0:
            quantEstoque = 'Produto indisponível'
        else:
            quantEstoque = self.getQuantidade()
        return f"{'Produto tipo Bebida:':<23} Código: {f'{self.getCod()}':>5} Nome: {f'{self.getNome()}':<20} Preço: {f'{self.getPreco():.2f}':>8} Quantidade em estoque: {quantEstoque}"


class Loja:
    def __init__(self):
        self.__estoque = []

    def AdicionarProduto(self, produto):
        self.__estoque.append(produto)
        return print('Produto adicionado com sucesso!')
    def RemoverProduto(self, cod):
        for produto in self.__estoque:
            if produto.getCod() == cod:
                self.__estoque.remove(produto)
                return print(f'Produto removido com sucesso!')
        return print('Produto não encontrado.')

    def MostrarTodosProdutos(self):
        for produto in self.__estoque:
            print(produto.MostrarDescricao())


### TESTES

# INSTANCIA DA LOJA
dieguinhoSupermercados = Loja()

# DEFINIÇÃO DOS PRODUTOS
produto1 = Alimentos('LT01', 'Leite liquido', 5.30, 4)
produto2 = Bebidas('RF01', 'Coca-cola', 8.30, 12)
produto3 = Alimentos('LT02', 'Leite desnatado', 6.30, 24)
produto4 = Bebidas('SC01', 'Del vale kappo', 2.30, 20)
produto5 = Alimentos('BC01', 'Biscoito recheado', 3.50, 50)

print(produto1.MostrarDescricao())
produto1.entrada(2)
print(produto1.MostrarDescricao())
produto1.saida(8)
print(produto1.MostrarDescricao())

# ADIONANDO PRODUTOS A LOJA
dieguinhoSupermercados.AdicionarProduto(produto1)
dieguinhoSupermercados.AdicionarProduto(produto2)
dieguinhoSupermercados.AdicionarProduto(produto3)
dieguinhoSupermercados.AdicionarProduto(produto4)
dieguinhoSupermercados.AdicionarProduto(produto5)

#mostrar lista de produtos na loja
dieguinhoSupermercados.MostrarTodosProdutos()

# alterar quantidade e mostrar produtos
print('-'*100)
produto1.entrada(2)
produto4.saida(28)
dieguinhoSupermercados.MostrarTodosProdutos()

# REMOVENDO COCA-COLA
print('-'*100)
dieguinhoSupermercados.RemoverProduto('LT01')
dieguinhoSupermercados.MostrarTodosProdutos()

dieguinhoSupermercados.RemoverProduto('LT01')
