# Reporte de calidad de datos - Fase 0

## Alcance
- Analisis principal: 2022, 2023 y 2024.
- 2025 se usa solo como soporte.

## Inventario de fuentes
```text
 agno                                                     archivo separador  filas  columnas
 2022 20221013_Resumen_Matrícula_EE_Oficial_2022_20220430_WEB.csv         ;  16601        59
 2023 20230925_Resumen_Matricula_EE_Oficial_2023_20230430_WEB.csv         ;  16659        60
 2024   20240930_Resumen_Matricula_EE_Oficial_2024_20240430 1.csv         ;  16694        74
 2025     20251029_Resumen_Matricula_EE_Oficial_2025_20250430.csv         ,  16768        71
```

## Hallazgos de calidad
- Duplicados por AGNO+RBD (2022-2024): 0.
- Registros con AGNO distinto al anio del archivo (2022-2024): 0.
- 2023 trae una columna tecnica vacia al inicio; se elimina en la estandarizacion.
- Hay diferencias de esquema entre anios, por lo que la comparacion longitudinal usa solo columnas comunes.

## Reglas aplicadas
- No se modifica ningun archivo raw.
- Se normalizan tipos para campos clave.
- Se comparan 2022-2024 con la interseccion de columnas.

## Riesgos
- Variables nuevas en 2024 no son comparables hacia atras.
- 2025 usa separador distinto (coma), por lo que requiere carga diferenciada.