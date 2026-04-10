# 🌺 Tuta Wayta – Sitio Web

Proyecto Flask para el sitio web de **Tuta Wayta**, empresa de pitahaya orgánica peruana.

## Estructura

```
tuta_wayta/
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── main.js
│   └── img/
│       ├── Mermelada.png
│       ├── Nectar_Natural.png
│       └── ... (todas las imágenes)
├── templates/
│   ├── base.html        ← nav + footer compartido
│   ├── index.html       ← página de inicio
│   ├── productos.html   ← catálogo completo
│   ├── nosotros.html    ← página institucional
│   └── detalles.html    ← detalle de producto
├── app.py
├── package.json
├── package-lock.json
├── .gitignore
└── README.md
```

## Instalación y uso

1. Instala Flask:
```bash
pip install flask
```

2. Ejecuta el servidor:
```bash
python app.py
```

3. Abre en el navegador:
```
http://localhost:5000
```

## Rutas

| Ruta         | Template          |
|--------------|-------------------|
| `/`          | index.html        |
| `/productos` | productos.html    |
| `/nosotros`  | nosotros.html     |
| `/detalles`  | detalles.html     |
