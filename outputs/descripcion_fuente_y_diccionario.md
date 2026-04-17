# Descripcion de la base de datos y diccionario de atributos

## 1) Tablas existentes en la fuente

Cada archivo anual se trata como una tabla independiente de origen (fuente denormalizada):

```text
                 tabla                                                     archivo  anio tipo_fuente                                            granularidad  filas columnas separador                                                                                               contenido
resumen_matricula_2022 20221013_Resumen_Matrícula_EE_Oficial_2022_20220430_WEB.csv  2022   principal 1 fila por establecimiento educacional (RBD) en el anio 16.601       59         ; Resumen anual de matricula y cursos por establecimiento, con atributos territoriales y administrativos.
resumen_matricula_2023 20230925_Resumen_Matricula_EE_Oficial_2023_20230430_WEB.csv  2023   principal 1 fila por establecimiento educacional (RBD) en el anio 16.659       60         ; Resumen anual de matricula y cursos por establecimiento, con atributos territoriales y administrativos.
resumen_matricula_2024   20240930_Resumen_Matricula_EE_Oficial_2024_20240430 1.csv  2024   principal 1 fila por establecimiento educacional (RBD) en el anio 16.694       74         ; Resumen anual de matricula y cursos por establecimiento, con atributos territoriales y administrativos.
resumen_matricula_2025     20251029_Resumen_Matricula_EE_Oficial_2025_20250430.csv  2025     soporte 1 fila por establecimiento educacional (RBD) en el anio 16.768       71         , Resumen anual de matricula y cursos por establecimiento, con atributos territoriales y administrativos.
```

## 2) Atributos por tabla (nombre, tipo y descripcion)

Nota: las descripciones se construyen a partir del nombre oficial de campo y se deben validar con metadata oficial de MINEDUC si el curso exige glosario institucional exacto.

### resumen_matricula_2022
```text
      atributo tipo_dato                                                        descripcion nulos valores_distintos comparable_2022_2024
          AGNO     Int64                                                 Anio del registro.     0                 1                    1
   COD_COM_RBD     int64                              Codigo de comuna del establecimiento.     0               346                    1
      COD_DEPE     int64              Codigo de dependencia administrativa (nivel general).     0                 6                    1
     COD_DEPE2    string      Codigo de dependencia administrativa (clasificacion oficial).     0                 5                    1
COD_DEPROV_RBD     int64                   Codigo del departamento provincial de educacion.     0                42                    1
   COD_PRO_RBD     int64                           Codigo de provincia del establecimiento.     0                56                    1
   COD_REG_RBD     int64                              Codigo de region del establecimiento.     0                16                    1
   CUR_COMB_01     int64          Cantidad de cursos combinados en subcategoria especifica.     0                 3                    1
   CUR_COMB_02     int64          Cantidad de cursos combinados en subcategoria especifica.     0                 6                    1
  CUR_COMB_TOT     int64          Cantidad de cursos combinados en subcategoria especifica.     0                 7                    1
    CUR_SIM_01     int64             Cantidad de cursos simples en subcategoria especifica.     0                20                    1
    CUR_SIM_02     int64             Cantidad de cursos simples en subcategoria especifica.     0                55                    1
    CUR_SIM_03     int64             Cantidad de cursos simples en subcategoria especifica.     0                17                    1
    CUR_SIM_04     int64             Cantidad de cursos simples en subcategoria especifica.     0                33                    1
    CUR_SIM_05     int64             Cantidad de cursos simples en subcategoria especifica.     0                43                    1
    CUR_SIM_06     int64             Cantidad de cursos simples en subcategoria especifica.     0                28                    1
    CUR_SIM_07     int64             Cantidad de cursos simples en subcategoria especifica.     0                43                    1
    CUR_SIM_08     int64             Cantidad de cursos simples en subcategoria especifica.     0                17                    1
   CUR_SIM_TOT     int64             Cantidad de cursos simples en subcategoria especifica.     0                87                    1
       DGV_RBD    string                                        Digito verificador del RBD.     0                10                    1
  ESTADO_ESTAB    string Estado del establecimiento (funcionamiento/receso/cerrado u otro).     0                 4                    1
     MAT_ENS_1     int64       Metrica de matricula en subcategoria especifica del dataset.     0               296                    1
     MAT_ENS_2     int64       Metrica de matricula en subcategoria especifica del dataset.     0             1.012                    1
     MAT_ENS_3     int64       Metrica de matricula en subcategoria especifica del dataset.     0               109                    1
     MAT_ENS_4     int64       Metrica de matricula en subcategoria especifica del dataset.     0               245                    1
     MAT_ENS_5     int64       Metrica de matricula en subcategoria especifica del dataset.     0               659                    1
     MAT_ENS_6     int64       Metrica de matricula en subcategoria especifica del dataset.     0               280                    1
     MAT_ENS_7     int64       Metrica de matricula en subcategoria especifica del dataset.     0               471                    1
     MAT_ENS_8     int64       Metrica de matricula en subcategoria especifica del dataset.     0                67                    1
     MAT_HOM_1     int64       Metrica de matricula en subcategoria especifica del dataset.     0               173                    1
     MAT_HOM_2     int64       Metrica de matricula en subcategoria especifica del dataset.     0               636                    1
     MAT_HOM_3     int64       Metrica de matricula en subcategoria especifica del dataset.     0                79                    1
     MAT_HOM_4     int64       Metrica de matricula en subcategoria especifica del dataset.     0               162                    1
     MAT_HOM_5     int64       Metrica de matricula en subcategoria especifica del dataset.     0               413                    1
     MAT_HOM_6     int64       Metrica de matricula en subcategoria especifica del dataset.     0               187                    1
     MAT_HOM_7     int64       Metrica de matricula en subcategoria especifica del dataset.     0               338                    1
     MAT_HOM_8     int64       Metrica de matricula en subcategoria especifica del dataset.     0                58                    1
   MAT_HOM_TOT     int64       Metrica de matricula en subcategoria especifica del dataset.     0               918                    1
     MAT_MUJ_1     int64       Metrica de matricula en subcategoria especifica del dataset.     0               178                    1
     MAT_MUJ_2     int64       Metrica de matricula en subcategoria especifica del dataset.     0               623                    1
     MAT_MUJ_3     int64       Metrica de matricula en subcategoria especifica del dataset.     0                62                    1
     MAT_MUJ_4     int64       Metrica de matricula en subcategoria especifica del dataset.     0               128                    1
     MAT_MUJ_5     int64       Metrica de matricula en subcategoria especifica del dataset.     0               418                    1
     MAT_MUJ_6     int64       Metrica de matricula en subcategoria especifica del dataset.     0               182                    1
     MAT_MUJ_7     int64       Metrica de matricula en subcategoria especifica del dataset.     0               312                    1
     MAT_MUJ_8     int64       Metrica de matricula en subcategoria especifica del dataset.     0                50                    1
   MAT_MUJ_TOT     int64       Metrica de matricula en subcategoria especifica del dataset.     0               930                    1
      MAT_SI_1     int64       Metrica de matricula en subcategoria especifica del dataset.     0                 2                    1
      MAT_SI_2     int64       Metrica de matricula en subcategoria especifica del dataset.     0                 2                    1
      MAT_SI_4   float64       Metrica de matricula en subcategoria especifica del dataset. 5.381                 2                    1
      MAT_SI_5   float64       Metrica de matricula en subcategoria especifica del dataset. 5.381                 2                    1
    MAT_SI_TOT     int64       Metrica de matricula en subcategoria especifica del dataset.     0                 2                    1
     MAT_TOTAL     int64                Matricula total de estudiantes del establecimiento.     0             1.491                    1
   NOM_COM_RBD    string                              Nombre de comuna del establecimiento.     0               346                    1
NOM_DEPROV_RBD    string                   Nombre del departamento provincial de educacion.     0                42                    1
       NOM_RBD    string                            Nombre del establecimiento educacional.    30            15.193                    1
 NOM_REG_RBD_A    string                  Nombre/abreviatura de region del establecimiento.     0                16                    1
           RBD     int64                 Rol Base de Datos del establecimiento educacional.     0            16.601                    1
     RURAL_RBD    string                        Indicador de ruralidad del establecimiento.     0                 2                    1
```

### resumen_matricula_2023
```text
      atributo tipo_dato                                                        descripcion nulos valores_distintos comparable_2022_2024
          AGNO     Int64                                                 Anio del registro.     0                 1                    1
   COD_COM_RBD     int64                              Codigo de comuna del establecimiento.     0               346                    1
      COD_DEPE     int64              Codigo de dependencia administrativa (nivel general).     0                 6                    1
     COD_DEPE2    string      Codigo de dependencia administrativa (clasificacion oficial).     0                 5                    1
COD_DEPROV_RBD     int64                   Codigo del departamento provincial de educacion.     0                42                    1
   COD_PRO_RBD     int64                           Codigo de provincia del establecimiento.     0                56                    1
   COD_REG_RBD     int64                              Codigo de region del establecimiento.     0                16                    1
   CUR_COMB_01     int64          Cantidad de cursos combinados en subcategoria especifica.     0                 3                    1
   CUR_COMB_02     int64          Cantidad de cursos combinados en subcategoria especifica.     0                 6                    1
  CUR_COMB_TOT     int64          Cantidad de cursos combinados en subcategoria especifica.     0                 7                    1
    CUR_SIM_01     int64             Cantidad de cursos simples en subcategoria especifica.     0                19                    1
    CUR_SIM_02     int64             Cantidad de cursos simples en subcategoria especifica.     0                52                    1
    CUR_SIM_03     int64             Cantidad de cursos simples en subcategoria especifica.     0                16                    1
    CUR_SIM_04     int64             Cantidad de cursos simples en subcategoria especifica.     0                35                    1
    CUR_SIM_05     int64             Cantidad de cursos simples en subcategoria especifica.     0                45                    1
    CUR_SIM_06     int64             Cantidad de cursos simples en subcategoria especifica.     0                30                    1
    CUR_SIM_07     int64             Cantidad de cursos simples en subcategoria especifica.     0                41                    1
    CUR_SIM_08     int64             Cantidad de cursos simples en subcategoria especifica.     0                17                    1
   CUR_SIM_TOT     int64             Cantidad de cursos simples en subcategoria especifica.     0                90                    1
       DGV_RBD    string                                        Digito verificador del RBD.     0                10                    1
  ESTADO_ESTAB    string Estado del establecimiento (funcionamiento/receso/cerrado u otro).     0                 4                    1
     MAT_ENS_1     int64       Metrica de matricula en subcategoria especifica del dataset.     0               288                    1
     MAT_ENS_2     int64       Metrica de matricula en subcategoria especifica del dataset.     0             1.021                    1
     MAT_ENS_3     int64       Metrica de matricula en subcategoria especifica del dataset.     0               111                    1
     MAT_ENS_4     int64       Metrica de matricula en subcategoria especifica del dataset.     0               244                    1
     MAT_ENS_5     int64       Metrica de matricula en subcategoria especifica del dataset.     0               664                    1
     MAT_ENS_6     int64       Metrica de matricula en subcategoria especifica del dataset.     0               267                    1
     MAT_ENS_7     int64       Metrica de matricula en subcategoria especifica del dataset.     0               470                    1
     MAT_ENS_8     int64       Metrica de matricula en subcategoria especifica del dataset.     0                66                    1
     MAT_HOM_1     int64       Metrica de matricula en subcategoria especifica del dataset.     0               167                    1
     MAT_HOM_2     int64       Metrica de matricula en subcategoria especifica del dataset.     0               627                    1
     MAT_HOM_3     int64       Metrica de matricula en subcategoria especifica del dataset.     0                76                    1
     MAT_HOM_4     int64       Metrica de matricula en subcategoria especifica del dataset.     0               168                    1
     MAT_HOM_5     int64       Metrica de matricula en subcategoria especifica del dataset.     0               418                    1
     MAT_HOM_6     int64       Metrica de matricula en subcategoria especifica del dataset.     0               187                    1
     MAT_HOM_7     int64       Metrica de matricula en subcategoria especifica del dataset.     0               339                    1
     MAT_HOM_8     int64       Metrica de matricula en subcategoria especifica del dataset.     0                54                    1
   MAT_HOM_TOT     int64       Metrica de matricula en subcategoria especifica del dataset.     0               897                    1
     MAT_MUJ_1     int64       Metrica de matricula en subcategoria especifica del dataset.     0               172                    1
     MAT_MUJ_2     int64       Metrica de matricula en subcategoria especifica del dataset.     0               610                    1
     MAT_MUJ_3     int64       Metrica de matricula en subcategoria especifica del dataset.     0                64                    1
     MAT_MUJ_4     int64       Metrica de matricula en subcategoria especifica del dataset.     0               123                    1
     MAT_MUJ_5     int64       Metrica de matricula en subcategoria especifica del dataset.     0               423                    1
     MAT_MUJ_6     int64       Metrica de matricula en subcategoria especifica del dataset.     0               178                    1
     MAT_MUJ_7     int64       Metrica de matricula en subcategoria especifica del dataset.     0               301                    1
     MAT_MUJ_8     int64       Metrica de matricula en subcategoria especifica del dataset.     0                50                    1
   MAT_MUJ_TOT     int64       Metrica de matricula en subcategoria especifica del dataset.     0               912                    1
      MAT_SI_1     int64       Metrica de matricula en subcategoria especifica del dataset.     0                 2                    1
      MAT_SI_2     int64       Metrica de matricula en subcategoria especifica del dataset.     0                 2                    1
      MAT_SI_3     int64       Metrica de matricula en subcategoria especifica del dataset.     0                 2                    0
      MAT_SI_4     int64       Metrica de matricula en subcategoria especifica del dataset.     0                 2                    1
      MAT_SI_5     int64       Metrica de matricula en subcategoria especifica del dataset.     0                 2                    1
    MAT_SI_TOT     int64       Metrica de matricula en subcategoria especifica del dataset.     0                 2                    1
     MAT_TOTAL     int64                Matricula total de estudiantes del establecimiento.     0             1.478                    1
   NOM_COM_RBD    string                              Nombre de comuna del establecimiento.     0               346                    1
NOM_DEPROV_RBD    string                   Nombre del departamento provincial de educacion.     0                42                    1
       NOM_RBD    string                            Nombre del establecimiento educacional.     0            15.257                    1
 NOM_REG_RBD_A    string                  Nombre/abreviatura de region del establecimiento.     0                16                    1
           RBD     int64                 Rol Base de Datos del establecimiento educacional.     0            16.659                    1
     RURAL_RBD    string                        Indicador de ruralidad del establecimiento.     0                 2                    1
```

### resumen_matricula_2024
```text
      atributo tipo_dato                                                        descripcion  nulos valores_distintos comparable_2022_2024
          AGNO     Int64                                                 Anio del registro.      0                 1                    1
   COD_COM_RBD     int64                              Codigo de comuna del establecimiento.      0               346                    1
      COD_DEPE     int64              Codigo de dependencia administrativa (nivel general).      0                 6                    1
     COD_DEPE2    string      Codigo de dependencia administrativa (clasificacion oficial).      0                 5                    1
COD_DEPROV_RBD     int64                   Codigo del departamento provincial de educacion.      0                42                    1
   COD_PRO_RBD     int64                           Codigo de provincia del establecimiento.      0                56                    1
   COD_REG_RBD     int64                              Codigo de region del establecimiento.      0                16                    1
   CUR_COMB_01     int64          Cantidad de cursos combinados en subcategoria especifica.      0                 3                    1
   CUR_COMB_02     int64          Cantidad de cursos combinados en subcategoria especifica.      0                 6                    1
  CUR_COMB_TOT     int64          Cantidad de cursos combinados en subcategoria especifica.      0                 7                    1
    CUR_SIM_01     int64             Cantidad de cursos simples en subcategoria especifica.      0                18                    1
    CUR_SIM_02     int64             Cantidad de cursos simples en subcategoria especifica.      0                52                    1
    CUR_SIM_03     int64             Cantidad de cursos simples en subcategoria especifica.      0                15                    1
    CUR_SIM_04     int64             Cantidad de cursos simples en subcategoria especifica.      0                33                    1
    CUR_SIM_05     int64             Cantidad de cursos simples en subcategoria especifica.      0                42                    1
    CUR_SIM_06     int64             Cantidad de cursos simples en subcategoria especifica.      0                28                    1
    CUR_SIM_07     int64             Cantidad de cursos simples en subcategoria especifica.      0                40                    1
    CUR_SIM_08     int64             Cantidad de cursos simples en subcategoria especifica.      0                16                    1
   CUR_SIM_TOT     int64             Cantidad de cursos simples en subcategoria especifica.      0                88                    1
       DGV_RBD    string                                        Digito verificador del RBD.      0                10                    1
  ESTADO_ESTAB    string Estado del establecimiento (funcionamiento/receso/cerrado u otro).      0                 4                    1
       MAT_CHI     int64       Metrica de matricula en subcategoria especifica del dataset.      0             1.404                    0
     MAT_ENS_1     int64       Metrica de matricula en subcategoria especifica del dataset.      0               281                    1
     MAT_ENS_2     int64       Metrica de matricula en subcategoria especifica del dataset.      0               993                    1
     MAT_ENS_3     int64       Metrica de matricula en subcategoria especifica del dataset.      0               107                    1
     MAT_ENS_4     int64       Metrica de matricula en subcategoria especifica del dataset.      0               238                    1
     MAT_ENS_5     int64       Metrica de matricula en subcategoria especifica del dataset.      0               670                    1
     MAT_ENS_6     int64       Metrica de matricula en subcategoria especifica del dataset.      0               264                    1
     MAT_ENS_7     int64       Metrica de matricula en subcategoria especifica del dataset.      0               473                    1
     MAT_ENS_8     int64       Metrica de matricula en subcategoria especifica del dataset.      0                67                    1
     MAT_ETNIA     int64       Metrica de matricula en subcategoria especifica del dataset.      0               301                    0
       MAT_EXT     int64       Metrica de matricula en subcategoria especifica del dataset.      0               375                    0
     MAT_HOM_1     int64       Metrica de matricula en subcategoria especifica del dataset.      0               162                    1
     MAT_HOM_2     int64       Metrica de matricula en subcategoria especifica del dataset.      0               620                    1
     MAT_HOM_3     int64       Metrica de matricula en subcategoria especifica del dataset.      0                77                    1
     MAT_HOM_4     int64       Metrica de matricula en subcategoria especifica del dataset.      0               159                    1
     MAT_HOM_5     int64       Metrica de matricula en subcategoria especifica del dataset.      0               412                    1
     MAT_HOM_6     int64       Metrica de matricula en subcategoria especifica del dataset.      0               182                    1
     MAT_HOM_7     int64       Metrica de matricula en subcategoria especifica del dataset.      0               338                    1
     MAT_HOM_8     int64       Metrica de matricula en subcategoria especifica del dataset.      0                54                    1
   MAT_HOM_INT     int64       Metrica de matricula en subcategoria especifica del dataset.      0               212                    0
   MAT_HOM_TOT     int64       Metrica de matricula en subcategoria especifica del dataset.      0               896                    1
 MAT_INT_TOTAL     int64       Metrica de matricula en subcategoria especifica del dataset.      0               303                    0
     MAT_MUJ_1     int64       Metrica de matricula en subcategoria especifica del dataset.      0               166                    1
     MAT_MUJ_2     int64       Metrica de matricula en subcategoria especifica del dataset.      0               604                    1
     MAT_MUJ_3     int64       Metrica de matricula en subcategoria especifica del dataset.      0                61                    1
     MAT_MUJ_4     int64       Metrica de matricula en subcategoria especifica del dataset.      0               125                    1
     MAT_MUJ_5     int64       Metrica de matricula en subcategoria especifica del dataset.      0               419                    1
     MAT_MUJ_6     int64       Metrica de matricula en subcategoria especifica del dataset.      0               163                    1
     MAT_MUJ_7     int64       Metrica de matricula en subcategoria especifica del dataset.      0               307                    1
     MAT_MUJ_8     int64       Metrica de matricula en subcategoria especifica del dataset.      0                46                    1
   MAT_MUJ_INT     int64       Metrica de matricula en subcategoria especifica del dataset.      0               163                    0
   MAT_MUJ_TOT     int64       Metrica de matricula en subcategoria especifica del dataset.      0               910                    1
       MAT_NAC     int64       Metrica de matricula en subcategoria especifica del dataset.      0                 5                    0
      MAT_NB_5     int64       Metrica de matricula en subcategoria especifica del dataset.      0                 2                    0
    MAT_NB_INT     int64       Metrica de matricula en subcategoria especifica del dataset.      0                 1                    0
    MAT_NB_TOT     int64       Metrica de matricula en subcategoria especifica del dataset.      0                 2                    0
  MAT_NO_ETNIA     int64       Metrica de matricula en subcategoria especifica del dataset.      0             1.429                    0
      MAT_SI_1     int64       Metrica de matricula en subcategoria especifica del dataset.      0                 2                    1
      MAT_SI_2     int64       Metrica de matricula en subcategoria especifica del dataset.      0                 2                    1
      MAT_SI_4     int64       Metrica de matricula en subcategoria especifica del dataset.      0                 2                    1
      MAT_SI_5     int64       Metrica de matricula en subcategoria especifica del dataset.      0                 2                    1
      MAT_SI_6     int64       Metrica de matricula en subcategoria especifica del dataset.      0                 2                    0
    MAT_SI_INT     int64       Metrica de matricula en subcategoria especifica del dataset.      0                 2                    0
    MAT_SI_TOT     int64       Metrica de matricula en subcategoria especifica del dataset.      0                 2                    1
     MAT_TOTAL     int64                Matricula total de estudiantes del establecimiento.      0             1.487                    1
   NOMBRE_SLEP       str                              Nombre del SLEP asociado (si aplica). 15.550                15                    0
   NOM_COM_RBD    string                              Nombre de comuna del establecimiento.      0               346                    1
NOM_DEPROV_RBD    string                   Nombre del departamento provincial de educacion.      0                42                    1
       NOM_RBD    string                            Nombre del establecimiento educacional.      0            15.320                    1
 NOM_REG_RBD_A    string                  Nombre/abreviatura de region del establecimiento.      0                16                    1
           RBD     int64                 Rol Base de Datos del establecimiento educacional.      0            16.694                    1
     RURAL_RBD    string                        Indicador de ruralidad del establecimiento.      0                 2                    1
          SLEP   float64               Codigo SLEP asociado al establecimiento (si aplica). 15.550                15                    0
```

### resumen_matricula_2025
```text
      atributo tipo_dato                                                        descripcion  nulos valores_distintos comparable_2022_2024
          AGNO     Int64                                                 Anio del registro.      0                 1                    1
   COD_COM_RBD     int64                              Codigo de comuna del establecimiento.      0               346                    1
      COD_DEPE     int64              Codigo de dependencia administrativa (nivel general).      0                 6                    1
     COD_DEPE2    string      Codigo de dependencia administrativa (clasificacion oficial).      0                 5                    1
COD_DEPROV_RBD     int64                   Codigo del departamento provincial de educacion.      0                42                    1
   COD_PRO_RBD     int64                           Codigo de provincia del establecimiento.      0                56                    1
   COD_REG_RBD     int64                              Codigo de region del establecimiento.      0                16                    1
   CUR_COMB_01     int64          Cantidad de cursos combinados en subcategoria especifica.      0                 3                    1
   CUR_COMB_02     int64          Cantidad de cursos combinados en subcategoria especifica.      0                 6                    1
  CUR_COMB_TOT     int64          Cantidad de cursos combinados en subcategoria especifica.      0                 7                    1
    CUR_SIM_01     int64             Cantidad de cursos simples en subcategoria especifica.      0                19                    1
    CUR_SIM_02     int64             Cantidad de cursos simples en subcategoria especifica.      0                53                    1
    CUR_SIM_03     int64             Cantidad de cursos simples en subcategoria especifica.      0                14                    1
    CUR_SIM_04     int64             Cantidad de cursos simples en subcategoria especifica.      0                34                    1
    CUR_SIM_05     int64             Cantidad de cursos simples en subcategoria especifica.      0                43                    1
    CUR_SIM_06     int64             Cantidad de cursos simples en subcategoria especifica.      0                26                    1
    CUR_SIM_07     int64             Cantidad de cursos simples en subcategoria especifica.      0                41                    1
    CUR_SIM_08     int64             Cantidad de cursos simples en subcategoria especifica.      0                14                    1
   CUR_SIM_TOT     int64             Cantidad de cursos simples en subcategoria especifica.      0                88                    1
       DGV_RBD    string                                        Digito verificador del RBD.      0                10                    1
  ESTADO_ESTAB    string Estado del establecimiento (funcionamiento/receso/cerrado u otro).      0                 4                    1
       MAT_CHI     int64       Metrica de matricula en subcategoria especifica del dataset.      0             1.403                    0
     MAT_ENS_1     int64       Metrica de matricula en subcategoria especifica del dataset.      0               274                    1
     MAT_ENS_2     int64       Metrica de matricula en subcategoria especifica del dataset.      0             1.003                    1
     MAT_ENS_3     int64       Metrica de matricula en subcategoria especifica del dataset.      0               106                    1
     MAT_ENS_4     int64       Metrica de matricula en subcategoria especifica del dataset.      0               245                    1
     MAT_ENS_5     int64       Metrica de matricula en subcategoria especifica del dataset.      0               676                    1
     MAT_ENS_6     int64       Metrica de matricula en subcategoria especifica del dataset.      0               255                    1
     MAT_ENS_7     int64       Metrica de matricula en subcategoria especifica del dataset.      0               471                    1
     MAT_ENS_8     int64       Metrica de matricula en subcategoria especifica del dataset.      0                63                    1
     MAT_ETNIA     int64       Metrica de matricula en subcategoria especifica del dataset.      0               362                    0
       MAT_EXT     int64       Metrica de matricula en subcategoria especifica del dataset.      0               382                    0
     MAT_HOM_1     int64       Metrica de matricula en subcategoria especifica del dataset.      0               162                    1
     MAT_HOM_2     int64       Metrica de matricula en subcategoria especifica del dataset.      0               608                    1
     MAT_HOM_3     int64       Metrica de matricula en subcategoria especifica del dataset.      0                81                    1
     MAT_HOM_4     int64       Metrica de matricula en subcategoria especifica del dataset.      0               160                    1
     MAT_HOM_5     int64       Metrica de matricula en subcategoria especifica del dataset.      0               418                    1
     MAT_HOM_6     int64       Metrica de matricula en subcategoria especifica del dataset.      0               183                    1
     MAT_HOM_7     int64       Metrica de matricula en subcategoria especifica del dataset.      0               342                    1
     MAT_HOM_8     int64       Metrica de matricula en subcategoria especifica del dataset.      0                57                    1
   MAT_HOM_INT     int64       Metrica de matricula en subcategoria especifica del dataset.      0               213                    0
   MAT_HOM_TOT     int64       Metrica de matricula en subcategoria especifica del dataset.      0               893                    1
 MAT_INT_TOTAL     int64       Metrica de matricula en subcategoria especifica del dataset.      0               315                    0
     MAT_MUJ_1     int64       Metrica de matricula en subcategoria especifica del dataset.      0               160                    1
     MAT_MUJ_2     int64       Metrica de matricula en subcategoria especifica del dataset.      0               598                    1
     MAT_MUJ_3     int64       Metrica de matricula en subcategoria especifica del dataset.      0                67                    1
     MAT_MUJ_4     int64       Metrica de matricula en subcategoria especifica del dataset.      0               124                    1
     MAT_MUJ_5     int64       Metrica de matricula en subcategoria especifica del dataset.      0               432                    1
     MAT_MUJ_6     int64       Metrica de matricula en subcategoria especifica del dataset.      0               158                    1
     MAT_MUJ_7     int64       Metrica de matricula en subcategoria especifica del dataset.      0               309                    1
     MAT_MUJ_8     int64       Metrica de matricula en subcategoria especifica del dataset.      0                48                    1
   MAT_MUJ_INT     int64       Metrica de matricula en subcategoria especifica del dataset.      0               168                    0
   MAT_MUJ_TOT     int64       Metrica de matricula en subcategoria especifica del dataset.      0               894                    1
       MAT_NAC     int64       Metrica de matricula en subcategoria especifica del dataset.      0                 4                    0
  MAT_NO_ETNIA     int64       Metrica de matricula en subcategoria especifica del dataset.      0             1.361                    0
      MAT_SI_1     int64       Metrica de matricula en subcategoria especifica del dataset.      0                 2                    1
      MAT_SI_2     int64       Metrica de matricula en subcategoria especifica del dataset.      0                 2                    1
      MAT_SI_4     int64       Metrica de matricula en subcategoria especifica del dataset.      0                 2                    1
      MAT_SI_5     int64       Metrica de matricula en subcategoria especifica del dataset.      0                 2                    1
      MAT_SI_6     int64       Metrica de matricula en subcategoria especifica del dataset.      0                 1                    0
    MAT_SI_INT     int64       Metrica de matricula en subcategoria especifica del dataset.      0                 2                    0
    MAT_SI_TOT     int64       Metrica de matricula en subcategoria especifica del dataset.      0                 2                    1
     MAT_TOTAL     int64                Matricula total de estudiantes del establecimiento.      0             1.479                    1
   NOMBRE_SLEP       str                              Nombre del SLEP asociado (si aplica). 10.281                26                    0
   NOM_COM_RBD    string                              Nombre de comuna del establecimiento.      0               346                    1
NOM_DEPROV_RBD    string                   Nombre del departamento provincial de educacion.      0                42                    1
       NOM_RBD    string                            Nombre del establecimiento educacional.      0            15.392                    1
 NOM_REG_RBD_A    string                  Nombre/abreviatura de region del establecimiento.      0                16                    1
           RBD     int64                 Rol Base de Datos del establecimiento educacional.      0            16.768                    1
     RURAL_RBD    string                        Indicador de ruralidad del establecimiento.      0                 2                    1
          SLEP   float64               Codigo SLEP asociado al establecimiento (si aplica). 10.281                26                    0
```

## 3) Comparabilidad estructural 2022-2024
- Columnas comunes para analisis longitudinal: 59.
- Diferencias relevantes: 2023 incluye columna tecnica vacia; 2024 agrega variables nuevas (por ejemplo, SLEP e indicadores de etnia/nacionalidad).

## 4) Implicancia para el analisis
- Las comparaciones temporales estrictas se hacen con la interseccion de columnas 2022-2024.
- Las columnas exclusivas de 2024/2025 se reportan como analisis complementario, no como serie historica completa.