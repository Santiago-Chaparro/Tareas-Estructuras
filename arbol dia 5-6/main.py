import json
import os


class TrieNode:
    def __init__(self):
        self.hijos = {}
        self.ids = set()  # IDs de nodos con este nombre


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insertar(self, palabra, node_id):
        nodo = self.root
        for c in palabra:
            if c not in nodo.hijos:
                nodo.hijos[c] = TrieNode()
            nodo = nodo.hijos[c]
        nodo.ids.add(node_id)

    def buscar(self, palabra):
        nodo = self.root
        for c in palabra:
            if c not in nodo.hijos:
                return set()
            nodo = nodo.hijos[c]
        return nodo.ids.copy()

    def autocompletar(self, prefijo):
        nodo = self.root
        for c in prefijo:
            if c not in nodo.hijos:
                return []
            nodo = nodo.hijos[c]

        resultados = set()

        def dfs(n):
            for i in n.ids:
                resultados.add(i)
            for h in n.hijos.values():
                dfs(h)

        dfs(nodo)
        return list(resultados)

    def eliminar(self, palabra, node_id):
        nodo = self.root
        stack = []

        for c in palabra:
            if c not in nodo.hijos:
                return
            stack.append((nodo, c))
            nodo = nodo.hijos[c]

        if node_id in nodo.ids:
            nodo.ids.remove(node_id)

        if len(nodo.ids) == 0 and len(nodo.hijos) == 0:
            for padre, caracter in reversed(stack):
                del padre.hijos[caracter]
                if len(padre.ids) > 0 or len(padre.hijos) > 0:
                    break

class Node:
    def __init__(self, node_id, name, tipo, content=None):
        self.id = node_id
        self.name = name
        self.tipo = tipo
        self.content = content
        self.children = []

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "tipo": self.tipo,
            "content": self.content,
            "children": [child.to_dict() for child in self.children]
        }

    @staticmethod
    def from_dict(data):
        node = Node(data["id"], data["name"], data["tipo"], data["content"])
        node.children = [Node.from_dict(c) for c in data["children"]]
        return node



class FileTree:
    def __init__(self):
        self.root = Node("0", "root", "carpeta")
        self.map = {"0": self.root}

        # Trie para búsquedas
        self.trie = Trie()
        self.trie.insertar("root", "0")

    # Buscar nodo por ruta tipo /root/carpeta
    def buscar_por_ruta(self, ruta):
        partes = [p for p in ruta.split("/") if p]

        if len(partes) == 0:
            return self.root

        actual = self.root

        for p in partes[1:]:
            encontrado = None
            for hijo in actual.children:
                if hijo.name == p:
                    encontrado = hijo
                    break
            if not encontrado:
                return None
            actual = encontrado

        return actual

    # Búsqueda por nombre (usado en pruebas)
    def buscar_nombre(self, nombre):
        return self.trie.buscar(nombre)

    def autocompletar(self, prefijo):
        return self.trie.autocompletar(prefijo)

    # Crear archivo/carpeta
    def insertar(self, ruta_padre, nombre, tipo, contenido=None):
        padre = self.buscar_por_ruta(ruta_padre)
        if padre is None:
            return

        nuevo_id = str(len(self.map))
        nuevo = Node(nuevo_id, nombre, tipo, contenido)

        padre.children.append(nuevo)
        self.map[nuevo_id] = nuevo

        # Guardar en trie
        self.trie.insertar(nombre, nuevo_id)

    # Listar hijos
    def listar_hijos(self, ruta):
        nodo = self.buscar_por_ruta(ruta)
        if nodo is None:
            return
        print(f"Hijos de {ruta}:")
        for h in nodo.children:
            print(f"- ({h.tipo}) {h.name}")

    # Obtener ruta completa por ID
    def obtener_ruta_id(self, node_id):
        if node_id not in self.map:
            return None

        nodo = self.map[node_id]

        def buscar_padre(actual, target):
            if actual == target:
                return []
            for hijo in actual.children:
                if hijo == target:
                    return [actual]
                resto = buscar_padre(hijo, target)
                if resto is not None:
                    return [actual] + resto
            return None

        ruta = buscar_padre(self.root, nodo)
        if ruta is None:
            return "/root"

        nombres = [n.name for n in ruta] + [nodo.name]
        return "/" + "/".join(nombres)

    # Eliminar nodo
    def eliminar(self, ruta):
        nodo = self.buscar_por_ruta(ruta)
        if nodo is None or nodo == self.root:
            return

        # Buscar padre
        def buscar_padre(actual, target):
            for hijo in actual.children:
                if hijo == target:
                    return actual
                res = buscar_padre(hijo, target)
                if res:
                    return res
            return None

        padre = buscar_padre(self.root, nodo)
        padre.children.remove(nodo)

        # Eliminar del trie
        def borrar_rec(n):
            self.trie.eliminar(n.name, n.id)
            del self.map[n.id]
            for c in n.children:
                borrar_rec(c)

        borrar_rec(nodo)

    # Renombrar
    def renombrar(self, node_id, nuevo_nombre):
        if node_id not in self.map:
            return
        nodo = self.map[node_id]

        # quitar nombre viejo
        self.trie.eliminar(nodo.name, node_id)

        nodo.name = nuevo_nombre

        # agregar nombre nuevo
        self.trie.insertar(nuevo_nombre, node_id)

    # Mover nodo
    def mover(self, ruta_origen, ruta_destino):
        nodo = self.buscar_por_ruta(ruta_origen)
        destino = self.buscar_por_ruta(ruta_destino)

        if nodo is None or destino is None or nodo == self.root:
            return

        def buscar_padre(actual, target):
            for hijo in actual.children:
                if hijo == target:
                    return actual
                res = buscar_padre(hijo, target)
                if res:
                    return res
            return None

        padre = buscar_padre(self.root, nodo)
        padre.children.remove(nodo)
        destino.children.append(nodo)

    # Altura
    def altura(self):
        def calc(nodo):
            if len(nodo.children) == 0:
                return 1
            return 1 + max(calc(c) for c in nodo.children)
        return calc(self.root)

    # Tamaño
    def tamaño(self):
        def contar(nodo):
            total = 1
            for c in nodo.children:
                total += contar(c)
            return total
        return contar(self.root)

    # Guardar JSON
    def guardar(self, archivo="tree.json"):
        data = self.root.to_dict()
        with open(archivo, "w") as f:
            json.dump(data, f, indent=4)

    # Cargar JSON
    def cargar(self, archivo="tree.json"):
        if not os.path.exists(archivo):
            return

        with open(archivo, "r") as f:
            data = json.load(f)

        self.root = Node.from_dict(data)
        self.map = {}
        self.trie = Trie()

        def registrar(nodo):
            self.map[nodo.id] = nodo
            self.trie.insertar(nodo.name, nodo.id)
            for c in nodo.children:
                registrar(c)

        registrar(self.root)

def menu():
    tree = FileTree()
    tree.cargar()

    while True:
        print("\n=== MENU ===")
        print("1. Crear carpeta")
        print("2. Crear archivo")
        print("3. Listar hijos")
        print("4. Obtener ruta por ID")
        print("5. Eliminar")
        print("6. Renombrar")
        print("7. Mover")
        print("8. Altura")
        print("9. Tamaño")
        print("10. Guardar")
        print("11. Cargar")
        print("12. Buscar nombre")
        print("13. Autocompletar")
        print("14. Salir")

        op = input("Opción: ")

        if op == "1":
            ruta = input("Ruta padre: ")
            nombre = input("Nombre carpeta: ")
            tree.insertar(ruta, nombre, "carpeta")

        elif op == "2":
            ruta = input("Ruta padre: ")
            nombre = input("Nombre archivo: ")
            contenido = input("Contenido: ")
            tree.insertar(ruta, nombre, "archivo", contenido)

        elif op == "3":
            ruta = input("Ruta: ")
            tree.listar_hijos(ruta)

        elif op == "4":
            node_id = input("ID: ")
            print(tree.obtener_ruta_id(node_id))

        elif op == "5":
            ruta = input("Ruta a eliminar: ")
            tree.eliminar(ruta)

        elif op == "6":
            node_id = input("ID: ")
            nuevo = input("Nuevo nombre: ")
            tree.renombrar(node_id, nuevo)

        elif op == "7":
            o = input("Origen: ")
            d = input("Destino: ")
            tree.mover(o, d)

        elif op == "8":
            print("Altura:", tree.altura())

        elif op == "9":
            print("Tamaño:", tree.tamaño())

        elif op == "10":
            tree.guardar()

        elif op == "11":
            tree.cargar()

        elif op == "12":
            n = input("Nombre: ")
            print(tree.buscar_nombre(n))

        elif op == "13":
            p = input("Prefijo: ")
            print(tree.autocompletar(p))

        elif op == "14":
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    menu()
