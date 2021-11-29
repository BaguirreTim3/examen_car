class Articulo:

      def __init__(self, codigo, valor_unitario, clase_articulo, agosto, 
                   septimbre, octubre, noviembre):
            self.codigo = codigo
            self.valor_unitariio = valor_unitario
            self.clase_articulo = clase_articulo
            self.agosto = agosto
            self.septimbre = septimbre
            self.octubre = octubre
            self.noviembre = noviembre


      def promedio(self):
             return  (self.agosto + self.septimbre + self.octubre + self.noviembre) / 4
       
      def ventas_esperadas(self, p):
            if self.clase_articulo == 1:
                  return (1 + 0.20) * p
            elif self.clase_articulo == 0:
                  return (1 + 0.10) * p  
            else:
                  print("Error")       

if __name__ == '__main__':

      articulo = Articulo(1, 15000, 1, 115, 45, 74, 85)
      articulo.promedio()
      print(articulo.valor_unitariio)
      print(articulo.promedio())
      print(articulo.ventas_esperadas(articulo.promedio()))
      
      articulo_2 = Articulo(2, 15800, 0, 74, 100, 78, 93)
      articulo_2.promedio()
      print(articulo_2.valor_unitariio)
      print(articulo_2.promedio())
      print(articulo_2.ventas_esperadas(articulo_2.promedio()))
      
     
