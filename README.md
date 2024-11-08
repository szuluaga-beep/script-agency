1. Crear el ambiente virtual
`python -m venv .venv`
2. Activar el ambiente
`.venv\Scripts\Activate.ps1`
3. Instalar FastAPI
`pip install "fastapi[standard]"`
4. Crear archivo requirements.txt
`pip freeze > requirements.txt`
5. Iniciar en modo desarrollo
`fastapi dev main.py`
6. Instalando libreria de peticiones
`python -m pip install requests`

7. Intalando pandas y matplotlib
`pip install pandas`
`pip install matplotlib`

## Estamos consumiendo el api de Rick and morty y con esta información vamos a poder visualizar en un grafico los personajes vivos, muertos o no se sabe
![alt text](image.png)