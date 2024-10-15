from UTN_Heroes_Dataset.utn_pp import get_original_matrix
from main import app
matriz_concesionaria = get_original_matrix()

if __name__ == "__main__":
    app(matriz_concesionaria)