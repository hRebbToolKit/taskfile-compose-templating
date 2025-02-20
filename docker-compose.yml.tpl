services:
  web:
    image: "nginx:{{ nginx_version }}"
    environment:
      - APP_ENV={{ app_env }}
  database:
    image: "postgres:{{ postgres_version }}"
    environment:
      - POSTGRES_USER={{ db_user }}
      - POSTGRES_PASSWORD={{ db_password }}