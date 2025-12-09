import unittest
import os
import json
from main import FileTree, Node   


class TestFileTree(unittest.TestCase):

    def setUp(self):
        self.tree = FileTree()

    def test_insertar(self):
        self.tree.insertar("/root", "carpeta1", "carpeta")
        nodo = self.tree.buscar_por_ruta("/root/carpeta1")

        self.assertIsNotNone(nodo)
        self.assertEqual(nodo.name, "carpeta1")
        self.assertEqual(nodo.tipo, "carpeta")

    def test_buscar_por_ruta(self):
        self.tree.insertar("/root", "docs", "carpeta")
        self.assertIsNotNone(self.tree.buscar_por_ruta("/root/docs"))
        self.assertIsNone(self.tree.buscar_por_ruta("/root/inexistente"))

    def test_eliminar(self):
        self.tree.insertar("/root", "tmp", "carpeta")
        self.tree.eliminar("/root/tmp")

        self.assertIsNone(self.tree.buscar_por_ruta("/root/tmp"))
        self.assertNotIn("1", self.tree.map)

    def test_renombrar(self):
        self.tree.insertar("/root", "oldname", "carpeta")
        nodo = self.tree.buscar_por_ruta("/root/oldname")
        self.tree.renombrar(nodo.id, "newname")

        nuevo = self.tree.buscar_por_ruta("/root/newname")
        self.assertIsNotNone(nuevo)
        self.assertEqual(nuevo.name, "newname")

    def test_mover(self):
        self.tree.insertar("/root", "a", "carpeta")
        self.tree.insertar("/root/a", "b", "carpeta")

        self.tree.insertar("/root", "c", "carpeta")

        self.tree.mover("/root/a/b", "/root/c")

        movido = self.tree.buscar_por_ruta("/root/c/b")
        self.assertIsNotNone(movido)

    def test_altura(self):
        self.tree.insertar("/root", "a", "carpeta")
        self.tree.insertar("/root/a", "b", "carpeta")
        self.tree.insertar("/root/a/b", "c", "carpeta")

        self.assertEqual(self.tree.altura(), 4)

    def test_tamaño(self):
        self.tree.insertar("/root", "a", "carpeta")
        self.tree.insertar("/root", "b", "carpeta")
        self.tree.insertar("/root/a", "c", "carpeta")

        # root + a + b + c = 4
        self.assertEqual(self.tree.tamaño(), 4)

    def test_guardar_y_cargar(self):
        archivo = "test_tree.json"

        self.tree.insertar("/root", "carpetaX", "carpeta")
        self.tree.insertar("/root/carpetaX", "archivoY", "archivo", "hola")

        self.tree.guardar(archivo)

        nuevo_arbol = FileTree()
        nuevo_arbol.cargar(archivo)

        ruta_archivo = nuevo_arbol.buscar_por_ruta("/root/carpetaX/archivoY")
        self.assertIsNotNone(ruta_archivo)
        self.assertEqual(ruta_archivo.content, "hola")

        os.remove(archivo)  # limpiar archivo temporal

