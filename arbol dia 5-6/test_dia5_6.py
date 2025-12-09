import unittest
from main import FileTree   


class TestTrieArbol(unittest.TestCase):

    def setUp(self):
        self.tree = FileTree()

    def test_trie_insertar_y_buscar(self):
        self.tree.insertar("/root", "docs", "carpeta")
        self.tree.insertar("/root/docs", "archivo1", "archivo")

        ids = self.tree.buscar_nombre("docs")
        self.assertTrue(len(ids) == 1)
        self.assertIn("1", ids)


    def test_trie_autocompletar(self):
        self.tree.insertar("/root", "dog", "carpeta")
        self.tree.insertar("/root", "door", "carpeta")
        self.tree.insertar("/root", "cat", "carpeta")

        encontrados = self.tree.autocompletar("do")

        self.assertIn("1", encontrados)
        self.assertIn("2", encontrados)
        self.assertNotIn("3", encontrados)

    def test_trie_eliminar(self):
        self.tree.insertar("/root", "temp", "carpeta")
        node_id = list(self.tree.buscar_nombre("temp"))[0]

        self.tree.eliminar("/root/temp")

        # Ya no debería existir
        ids = self.tree.buscar_nombre("temp")
        self.assertEqual(len(ids), 0)

        # Y tampoco debe quedar el id en el map
        self.assertNotIn(node_id, self.tree.map)

    def test_renombrar(self):
        self.tree.insertar("/root", "old", "carpeta")
        node_id = list(self.tree.buscar_nombre("old"))[0]

        # renombrar
        self.tree.renombrar(node_id, "new")

        # old ya no debe estar
        self.assertEqual(len(self.tree.buscar_nombre("old")), 0)

        # new sí debe estar
        ids = self.tree.buscar_nombre("new")
        self.assertIn(node_id, ids)

    def test_mover(self):
        self.tree.insertar("/root", "folderA", "carpeta")
        self.tree.insertar("/root", "folderB", "carpeta")

        node_id = list(self.tree.buscar_nombre("folderA"))[0]

        self.tree.mover("/root/folderA", "/root/folderB")

        # El Trie no cambia porque no cambia el nombre
        ids = self.tree.buscar_nombre("folderA")
        self.assertIn(node_id, ids)

    def test_guardar_y_cargar(self):
        self.tree.insertar("/root", "carpetaX", "carpeta")
        id_insertado = list(self.tree.buscar_nombre("carpetaX"))[0]

        # Guardar
        self.tree.guardar("test_tree.json")

        # Nuevo árbol vacío
        nuevo = FileTree()
        nuevo.cargar("test_tree.json")

        ids = nuevo.buscar_nombre("carpetaX")
        self.assertIn(id_insertado, ids)

    def test_autocompletar_prefijo_corto(self):
        self.tree.insertar("/root", "alpha", "carpeta")
        self.tree.insertar("/root", "alpine", "carpeta")
        self.tree.insertar("/root", "beta", "carpeta")

        encontrados = self.tree.autocompletar("a")
        self.assertEqual(len(encontrados), 2)


    def test_buscar_inexistente(self):
        self.tree.insertar("/root", "hola", "carpeta")

        resultado = self.tree.buscar_nombre("adios")
        self.assertEqual(len(resultado), 0)


    def test_nombres_duplicados(self):
        self.tree.insertar("/root", "data", "carpeta")
        self.tree.insertar("/root", "data2", "carpeta")
        self.tree.insertar("/root/data", "data", "carpeta")  # subcarpeta con el mismo nombre

        encontrados = self.tree.buscar_nombre("data")

        # Deben existir 2 nodos con ese nombre
        self.assertEqual(len(encontrados), 2)


if __name__ == "__main__":
    unittest.main()
