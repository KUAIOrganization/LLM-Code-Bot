n = int(input())
total_faces = 0
polyhedron_faces = {
    "Tetrahedron": 4,
    "Cube": 6,
    "Octahedron": 8,
    "Dodecahedron": 12,
    "Icosahedron": 20
}
for _ in range(n):
    polyhedron_name = input()
    total_faces += polyhedron_faces[polyhedron_name]
print(total_faces)
