# Base de datos MySQL para un blog

Práctica de diseño de bases de datos con MySQL Workbench (noviembre de 2022). Armé la base de datos `platziblog`, el ejemplo de blog que usa Platzi, para una página de publicaciones.

## Qué hice

- Creé seis tablas relacionadas: `usuarios`, `posts`, `categorias`, `etiquetas`, `posts_etiquetas` y `comentarios`.
- Uní publicaciones y etiquetas con una tabla intermedia, porque una publicación puede tener varias etiquetas.
- Cargué datos de ejemplo y exporté todo como script en `platzi_blog.sql`.

## Cómo usarlo

1. En MySQL Workbench, crea una base de datos nueva y déjala como predeterminada.
2. Abre el script `platzi_blog.sql`.
3. Ejecútalo.
