# Inteligencia-de-Negocios---Mineduc

Pipeline de Fase 0 para analizar el dataset de MINEDUC "Resumen de matricula por establecimiento".

## Requisitos
- Python 3.11+
- Paquetes: `pandas`, `matplotlib`, `seaborn`, `openpyxl`

Instalacion rapida:

```bash
python -m pip install -r requirements.txt
```

## Ejecucion
Desde la raiz del proyecto:

```bash
python analizar_matricula.py
```

## Salidas generadas
El pipeline crea la carpeta `outputs/` con:

- `outputs/tablas/inventario_fuentes.csv`
- `outputs/tablas/catalogo_tablas.csv`
- `outputs/tablas/columnas_disponibles_y_comparables.csv`
- `outputs/tablas/columnas_comparables_2022_2024.csv`
- `outputs/tablas/calidad_por_anio.csv`
- `outputs/tablas/base_integrada_2022_2024.csv`
- `outputs/tablas/matricula_total_por_anio.csv`
- `outputs/tablas/top10_regiones_por_anio.csv`
- `outputs/tablas/top20_comunas_2024.csv`
- `outputs/tablas/distribucion_dependencia_por_anio.csv`
- `outputs/tablas/distribucion_estado_por_anio.csv`
- `outputs/tablas/diccionario_datos_armonizado.csv`
- `outputs/tablas/diccionario_2022.csv`
- `outputs/tablas/diccionario_2023.csv`
- `outputs/tablas/diccionario_2024.csv`
- `outputs/tablas/diccionario_2025.csv`
- `outputs/tablas/diccionario_todas_las_tablas.csv`
- `outputs/tablas/soporte_2025_resumen.csv`
- `outputs/figuras/matricula_total_por_anio.png`
- `outputs/figuras/top10_regiones_2024.png`
- `outputs/figuras/matricula_por_dependencia_2024.png`
- `outputs/figuras/matriz_estado_establecimiento.png`
- `outputs/reporte_calidad.md`
- `outputs/descripcion_fuente_y_diccionario.md`
- `outputs/analisis_fase0.md`
- `outputs/preguntas_investigacion.md`
- `outputs/resumen_ejecutivo_fase0.md`
- `outputs/guia_presentacion_fase0.md`

## Cobertura
- Analisis principal: 2022, 2023, 2024.
- 2025 queda como soporte opcional.
