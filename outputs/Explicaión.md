### ¿Qué va a ir aquí?

Resultados generados por los notebooks o scripts, pensados para el informe
final y las presentaciones — no para que la app de Streamlit los use en
vivo (eso lo hace directo desde `models/` y `src/`).

### Subcarpetas

- `figures/` — Gráficos exportados como imagen (`.png`, `.jpg`). Útil para
  pegar en el informe o en una presentación, fuera de la app.
- `reports/` — Resultados en texto: comparativa de los 3 algoritmos del
  Módulo 2 (cuál funcionó mejor y por qué), comparación modelo tradicional
  vs red neuronal del Módulo 4, y el resultado del p-value del notebook de
  SciPy.

### Reglas

- Nombra los archivos con el módulo al que pertenecen, ej.
  `modulo2_comparacion_algoritmos.png`, `modulo4_reporte_comparacion.md` —
  evita nombres genéricos como `grafico1.png` que no dicen de qué módulo son.
- Estos archivos se regeneran cada vez que corres el notebook — no importa
  si los sobrescribes, no es información "original" como `data/raw/`.
- No se edita el contenido de un reporte a mano después de generado — si
  el resultado cambió, vuelve a correr el notebook y regenera el archivo.