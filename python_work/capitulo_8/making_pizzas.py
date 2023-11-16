# import pizza
# pizza.make_pizza(16, 'pepperoni')
# pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

'''
Essa abordagem inicial de importação, em que simplesmente escrevemos import seguido pelo nome
do módulo, disponibiliza todas as funções do módulo no programa. Caso use esse tipo de instrução
import para importar um módulo inteiro chamado module_name.py, cada função no módulo estará disponivel
por meio da seguinte formula:
nome_modulo.nome_função()
'''

# Importando funções específicas
# from pizza import make_pizza

# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Podemos também colocar um apelido nas funções para caso tenha uma variável com o mesmo nome da função
from pizza import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

'''
Nesse programa, a instrução import mostrada aqui renomeia a função make_pizza() para mp().
Sempre que quisermos chamar make_pizza(), basta escrever mo(), e o Python executará o código em
make_pizza(), evitando qualqer confusão com outra função make_pizza() que possamos ter escrito no
arquivo de programa.

Vejamos a sintaxe:
from nome_modulo import nome_função as nf
'''