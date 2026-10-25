# Curso de Python: pip y entornos virtuales

Proyecto olvidado de un curso de Python sobre pip, entornos virtuales y librerías externas. Lo seguí junto a las clases y quedó casi terminado, como dice su último commit. El README del curso está en `README-original.md`.

## Qué hice

- `game/`: piedra, papel o tijera en la terminal.
- `charts/`: gráficos de torta con matplotlib.
- `app/`: lee `data.csv`, con la población mundial por país, usando pandas y genera gráficos. Trae su `requirements.txt`, un `Dockerfile` y un `docker-compose.yml` para correrlo en un contenedor.
- `web-server/`: un servidor con FastAPI y una consulta con requests a una API pública de ejemplo.
- `hello.py`: el primer saludo del curso.

## Cómo usarlo

Cada carpeta con `requirements.txt` va en su propio entorno virtual:

```sh
cd app
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
python3 main.py
```
