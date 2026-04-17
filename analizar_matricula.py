from __future__ import annotations

from pathlib import Path
from typing import Dict, List, Tuple

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import pandas as pd
import seaborn as sns


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "outputs"
TABLES_DIR = OUTPUT_DIR / "tablas"
FIGURES_DIR = OUTPUT_DIR / "figuras"

YEARS_MAIN = [2022, 2023, 2024]
YEARS_SUPPORT = [2025]

FILES = {
    2022: "20221013_Resumen_Matrícula_EE_Oficial_2022_20220430_WEB.csv",
    2023: "20230925_Resumen_Matricula_EE_Oficial_2023_20230430_WEB.csv",
    2024: "20240930_Resumen_Matricula_EE_Oficial_2024_20240430 1.csv",
    2025: "20251029_Resumen_Matricula_EE_Oficial_2025_20250430.csv",
}

EXPECTED_DEP = {"1", "2", "3", "4", "5"}
EXPECTED_STATE = {"1", "2", "3", "4"}

COLUMN_DESCRIPTIONS = {
    "AGNO": "Anio del registro.",
    "RBD": "Rol Base de Datos del establecimiento educacional.",
    "DGV_RBD": "Digito verificador del RBD.",
    "NOM_RBD": "Nombre del establecimiento educacional.",
    "COD_DEPE": "Codigo de dependencia administrativa (nivel general).",
    "COD_DEPE2": "Codigo de dependencia administrativa (clasificacion oficial).",
    "RURAL_RBD": "Indicador de ruralidad del establecimiento.",
    "COD_REG_RBD": "Codigo de region del establecimiento.",
    "NOM_REG_RBD_A": "Nombre/abreviatura de region del establecimiento.",
    "COD_PRO_RBD": "Codigo de provincia del establecimiento.",
    "COD_COM_RBD": "Codigo de comuna del establecimiento.",
    "NOM_COM_RBD": "Nombre de comuna del establecimiento.",
    "COD_DEPROV_RBD": "Codigo del departamento provincial de educacion.",
    "NOM_DEPROV_RBD": "Nombre del departamento provincial de educacion.",
    "ESTADO_ESTAB": "Estado del establecimiento (funcionamiento/receso/cerrado u otro).",
    "MAT_TOTAL": "Matricula total de estudiantes del establecimiento.",
    "SLEP": "Codigo SLEP asociado al establecimiento (si aplica).",
    "NOMBRE_SLEP": "Nombre del SLEP asociado (si aplica).",
}


def ensure_dirs() -> None:
    TABLES_DIR.mkdir(parents=True, exist_ok=True)
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)


def detect_delimiter(file_path: Path) -> str:
    sample = file_path.read_text(encoding="utf-8-sig", errors="ignore")[:4096]
    return ";" if sample.count(";") >= sample.count(",") else ","


def read_csv_flexible(file_path: Path) -> Tuple[pd.DataFrame, str]:
    delimiter = detect_delimiter(file_path)
    last_error = None
    for encoding in ["utf-8-sig", "latin-1"]:
        try:
            df = pd.read_csv(file_path, sep=delimiter, encoding=encoding, low_memory=False)
            return df, delimiter
        except Exception as err:  # pragma: no cover
            last_error = err
    raise RuntimeError(f"No se pudo leer {file_path.name}: {last_error}")


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    cols = []
    for col in df.columns:
        if col is None:
            cols.append("")
        else:
            cols.append(str(col).strip())
    df.columns = cols
    to_drop = [c for c in df.columns if c == "" or c.lower().startswith("unnamed")]
    if to_drop:
        df = df.drop(columns=to_drop)
    return df


def describe_column(col: str) -> str:
    if col in COLUMN_DESCRIPTIONS:
        return COLUMN_DESCRIPTIONS[col]
    if col.startswith("MAT_"):
        return "Metrica de matricula en subcategoria especifica del dataset."
    if col.startswith("CUR_SIM_"):
        return "Cantidad de cursos simples en subcategoria especifica."
    if col.startswith("CUR_COMB_"):
        return "Cantidad de cursos combinados en subcategoria especifica."
    if col.startswith("COD_"):
        return "Codigo administrativo o territorial del registro."
    if col.startswith("NOM_"):
        return "Nombre descriptivo asociado a un codigo oficial."
    return "Atributo del dataset oficial (descripcion inferida por nombre de campo)."


def format_number(value: object) -> str:
    if pd.isna(value):
        return ""
    if isinstance(value, (int, float)):
        if float(value).is_integer():
            return f"{int(value):,}".replace(",", ".")
        return f"{float(value):,.2f}".replace(",", "_").replace(".", ",").replace("_", ".")
    return str(value)


def format_table_text(df: pd.DataFrame, numeric_cols: List[str] | None = None) -> str:
    if numeric_cols is None:
        numeric_cols = []
    formatted = df.copy()
    for col in numeric_cols:
        if col in formatted.columns:
            formatted[col] = formatted[col].map(format_number)
    return formatted.to_string(index=False)


def standardize_types(df: pd.DataFrame, year: int) -> pd.DataFrame:
    df = df.copy()

    if "AGNO" in df.columns:
        df["AGNO"] = pd.to_numeric(df["AGNO"], errors="coerce").astype("Int64")
    else:
        df["AGNO"] = year

    numeric_candidates = [
        c
        for c in df.columns
        if c.startswith("MAT_") or c.startswith("CUR_") or c.startswith("COD_") or c == "RBD"
    ]
    numeric_candidates = [c for c in numeric_candidates if c in df.columns and c != "NOM_RBD"]
    for c in numeric_candidates:
        df[c] = pd.to_numeric(df[c], errors="coerce")

    for c in ["NOM_RBD", "NOM_REG_RBD_A", "NOM_COM_RBD", "NOM_DEPROV_RBD", "DGV_RBD"]:
        if c in df.columns:
            df[c] = df[c].astype("string").str.strip()

    for c in ["COD_DEPE2", "ESTADO_ESTAB", "RURAL_RBD"]:
        if c in df.columns:
            df[c] = df[c].astype("Int64").astype("string")

    if "MAT_TOTAL" in df.columns:
        df["MAT_TOTAL"] = pd.to_numeric(df["MAT_TOTAL"], errors="coerce").fillna(0)

    return df


def load_all_data() -> Tuple[Dict[int, pd.DataFrame], pd.DataFrame]:
    dataframes: Dict[int, pd.DataFrame] = {}
    inventory_rows: List[dict] = []

    for year, file_name in FILES.items():
        path = DATA_DIR / file_name
        if not path.exists():
            raise FileNotFoundError(f"No existe el archivo {path}")

        raw_df, delimiter = read_csv_flexible(path)
        clean_df = normalize_columns(raw_df)
        clean_df = standardize_types(clean_df, year)
        dataframes[year] = clean_df

        inventory_rows.append(
            {
                "agno": year,
                "archivo": file_name,
                "separador": delimiter,
                "filas": len(clean_df),
                "columnas": len(clean_df.columns),
            }
        )

    inventory_df = pd.DataFrame(inventory_rows).sort_values("agno")
    return dataframes, inventory_df


def comparable_columns(dataframes: Dict[int, pd.DataFrame]) -> pd.DataFrame:
    sets = [set(dataframes[y].columns) for y in YEARS_MAIN]
    common = sorted(set.intersection(*sets))

    records = []
    for col in sorted(set.union(*[set(df.columns) for df in dataframes.values()])):
        records.append(
            {
                "columna": col,
                "en_2022": int(col in dataframes[2022].columns),
                "en_2023": int(col in dataframes[2023].columns),
                "en_2024": int(col in dataframes[2024].columns),
                "en_2025": int(col in dataframes[2025].columns),
                "comparable_2022_2024": int(col in common),
            }
        )

    cols_df = pd.DataFrame(records).sort_values(["comparable_2022_2024", "columna"], ascending=[False, True])
    cols_df.to_csv(TABLES_DIR / "columnas_disponibles_y_comparables.csv", index=False, encoding="utf-8-sig")

    pd.DataFrame({"columna_comparable_2022_2024": common}).to_csv(
        TABLES_DIR / "columnas_comparables_2022_2024.csv", index=False, encoding="utf-8-sig"
    )
    return pd.DataFrame({"columna": common})


def build_table_catalog(dataframes: Dict[int, pd.DataFrame], inventory_df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for year in sorted(dataframes):
        file_name = FILES[year]
        df = dataframes[year]
        main_flag = "principal" if year in YEARS_MAIN else "soporte"
        rows.append(
            {
                "tabla": f"resumen_matricula_{year}",
                "archivo": file_name,
                "anio": year,
                "tipo_fuente": main_flag,
                "granularidad": "1 fila por establecimiento educacional (RBD) en el anio",
                "filas": len(df),
                "columnas": len(df.columns),
                "separador": inventory_df[inventory_df["agno"] == year]["separador"].iloc[0],
                "contenido": "Resumen anual de matricula y cursos por establecimiento, con atributos territoriales y administrativos.",
            }
        )

    catalog_df = pd.DataFrame(rows).sort_values("anio")
    catalog_df.to_csv(TABLES_DIR / "catalogo_tablas.csv", index=False, encoding="utf-8-sig")
    return catalog_df


def build_dictionaries_by_table(dataframes: Dict[int, pd.DataFrame], comparable_cols: pd.DataFrame) -> pd.DataFrame:
    comparable_set = set(comparable_cols["columna"].tolist())
    all_rows: List[dict] = []

    for year in sorted(dataframes):
        df = dataframes[year]
        per_table_rows = []
        for col in df.columns:
            series = df[col]
            non_null = int(series.notna().sum())
            row = {
                "tabla": f"resumen_matricula_{year}",
                "atributo": col,
                "tipo_dato": str(series.dtype),
                "descripcion": describe_column(col),
                "nulos": int(series.isna().sum()),
                "no_nulos": non_null,
                "valores_distintos": int(series.nunique(dropna=True)),
                "ejemplo_valor": "" if non_null == 0 else str(series.dropna().iloc[0]),
                "comparable_2022_2024": int(col in comparable_set),
            }
            per_table_rows.append(row)
            all_rows.append(row)

        per_table_df = pd.DataFrame(per_table_rows).sort_values("atributo")
        per_table_df.to_csv(TABLES_DIR / f"diccionario_{year}.csv", index=False, encoding="utf-8-sig")

    all_df = pd.DataFrame(all_rows).sort_values(["tabla", "atributo"])
    all_df.to_csv(TABLES_DIR / "diccionario_todas_las_tablas.csv", index=False, encoding="utf-8-sig")
    return all_df


def quality_report_by_year(dataframes: Dict[int, pd.DataFrame]) -> pd.DataFrame:
    rows = []
    key_fields = ["AGNO", "RBD", "COD_REG_RBD", "NOM_REG_RBD_A", "COD_COM_RBD", "NOM_COM_RBD", "COD_DEPE2", "ESTADO_ESTAB", "MAT_TOTAL"]

    for year, df in dataframes.items():
        nulls = {f"null_{c}": int(df[c].isna().sum()) if c in df.columns else None for c in key_fields}
        duplicates = int(df.duplicated(subset=[c for c in ["AGNO", "RBD"] if c in df.columns]).sum())

        agno_mismatch = None
        if "AGNO" in df.columns:
            agno_mismatch = int((df["AGNO"].dropna().astype(int) != year).sum())

        dep_invalid = None
        if "COD_DEPE2" in df.columns:
            dep_series = df["COD_DEPE2"].dropna().astype(str)
            dep_invalid = int((~dep_series.isin(EXPECTED_DEP)).sum())

        state_invalid = None
        if "ESTADO_ESTAB" in df.columns:
            state_series = df["ESTADO_ESTAB"].dropna().astype(str)
            state_invalid = int((~state_series.isin(EXPECTED_STATE)).sum())

        mat_negative = None
        if "MAT_TOTAL" in df.columns:
            mat_negative = int((pd.to_numeric(df["MAT_TOTAL"], errors="coerce").fillna(0) < 0).sum())

        rows.append(
            {
                "agno": year,
                "filas": len(df),
                "columnas": len(df.columns),
                "duplicados_agno_rbd": duplicates,
                "agno_distinto_archivo": agno_mismatch,
                "cod_depe2_fuera_dominio": dep_invalid,
                "estado_estab_fuera_dominio": state_invalid,
                "mat_total_negativo": mat_negative,
                **nulls,
            }
        )

    quality_df = pd.DataFrame(rows).sort_values("agno")
    quality_df.to_csv(TABLES_DIR / "calidad_por_anio.csv", index=False, encoding="utf-8-sig")
    return quality_df


def build_integrated_base(dataframes: Dict[int, pd.DataFrame], comparable_cols: pd.DataFrame) -> pd.DataFrame:
    cols = comparable_cols["columna"].tolist()
    frames = []
    for year in YEARS_MAIN:
        df = dataframes[year].copy()
        missing = [c for c in cols if c not in df.columns]
        for c in missing:
            df[c] = pd.NA
        frames.append(df[cols])

    integrated = pd.concat(frames, ignore_index=True)
    integrated.to_csv(TABLES_DIR / "base_integrada_2022_2024.csv", index=False, encoding="utf-8-sig")
    return integrated


def build_aggregations(integrated: pd.DataFrame, dataframes: Dict[int, pd.DataFrame]) -> None:
    mat_year = (
        integrated.groupby("AGNO", dropna=False, as_index=False)["MAT_TOTAL"]
        .sum()
        .rename(columns={"AGNO": "agno", "MAT_TOTAL": "mat_total"})
        .sort_values("agno")
    )
    mat_year["var_abs_vs_prev"] = mat_year["mat_total"].diff()
    mat_year["var_pct_vs_prev"] = mat_year["mat_total"].pct_change() * 100
    mat_year.to_csv(TABLES_DIR / "matricula_total_por_anio.csv", index=False, encoding="utf-8-sig")

    top_reg = (
        integrated.groupby(["AGNO", "NOM_REG_RBD_A"], dropna=False, as_index=False)["MAT_TOTAL"]
        .sum()
        .rename(columns={"AGNO": "agno", "NOM_REG_RBD_A": "region", "MAT_TOTAL": "mat_total"})
    )
    top_reg["rank"] = top_reg.groupby("agno")["mat_total"].rank(method="dense", ascending=False)
    top_reg[top_reg["rank"] <= 10].sort_values(["agno", "rank"]).to_csv(
        TABLES_DIR / "top10_regiones_por_anio.csv", index=False, encoding="utf-8-sig"
    )

    dep = (
        integrated.groupby(["AGNO", "COD_DEPE2"], dropna=False, as_index=False)
        .agg(establecimientos=("RBD", "count"), mat_total=("MAT_TOTAL", "sum"))
        .rename(columns={"AGNO": "agno", "COD_DEPE2": "cod_depe2"})
        .sort_values(["agno", "mat_total"], ascending=[True, False])
    )
    dep.to_csv(TABLES_DIR / "distribucion_dependencia_por_anio.csv", index=False, encoding="utf-8-sig")

    est = (
        integrated.groupby(["AGNO", "ESTADO_ESTAB"], dropna=False, as_index=False)
        .agg(establecimientos=("RBD", "count"), mat_total=("MAT_TOTAL", "sum"))
        .rename(columns={"AGNO": "agno", "ESTADO_ESTAB": "estado_estab"})
        .sort_values(["agno", "mat_total"], ascending=[True, False])
    )
    est.to_csv(TABLES_DIR / "distribucion_estado_por_anio.csv", index=False, encoding="utf-8-sig")

    comunas_2024 = dataframes[2024]
    top_com = (
        comunas_2024.groupby("NOM_COM_RBD", dropna=False, as_index=False)["MAT_TOTAL"]
        .sum()
        .rename(columns={"NOM_COM_RBD": "comuna", "MAT_TOTAL": "mat_total"})
        .sort_values("mat_total", ascending=False)
        .head(20)
    )
    top_com.to_csv(TABLES_DIR / "top20_comunas_2024.csv", index=False, encoding="utf-8-sig")

    support_2025 = dataframes[2025]
    support = pd.DataFrame(
        {
            "agno": [2025],
            "filas": [len(support_2025)],
            "columnas": [len(support_2025.columns)],
            "mat_total": [support_2025["MAT_TOTAL"].sum() if "MAT_TOTAL" in support_2025.columns else pd.NA],
        }
    )
    support.to_csv(TABLES_DIR / "soporte_2025_resumen.csv", index=False, encoding="utf-8-sig")


def build_dictionary(dataframes: Dict[int, pd.DataFrame], comparable_cols: pd.DataFrame) -> None:
    records = []
    role_map = {
        "AGNO": "Dimension tiempo",
        "RBD": "Dimension establecimiento",
        "NOM_RBD": "Atributo establecimiento",
        "COD_REG_RBD": "Dimension territorio",
        "NOM_REG_RBD_A": "Dimension territorio",
        "COD_COM_RBD": "Dimension territorio",
        "NOM_COM_RBD": "Dimension territorio",
        "COD_DEPE": "Dimension dependencia",
        "COD_DEPE2": "Dimension dependencia",
        "ESTADO_ESTAB": "Dimension estado",
        "MAT_TOTAL": "Metrica principal",
    }

    for col in comparable_cols["columna"].tolist():
        records.append(
            {
                "columna": col,
                "dtype_2022": str(dataframes[2022][col].dtype) if col in dataframes[2022].columns else "NA",
                "dtype_2023": str(dataframes[2023][col].dtype) if col in dataframes[2023].columns else "NA",
                "dtype_2024": str(dataframes[2024][col].dtype) if col in dataframes[2024].columns else "NA",
                "rol_analitico": role_map.get(col, "Atributo complementario"),
            }
        )

    pd.DataFrame(records).sort_values("columna").to_csv(
        TABLES_DIR / "diccionario_datos_armonizado.csv", index=False, encoding="utf-8-sig"
    )


def build_markdown_reports(inventory_df: pd.DataFrame, quality_df: pd.DataFrame) -> None:
    quality_main = quality_df[quality_df["agno"].isin(YEARS_MAIN)].copy()
    no_dups = int(quality_main["duplicados_agno_rbd"].sum())
    no_agno_mismatch = int(quality_main["agno_distinto_archivo"].sum())

    inventory_text = inventory_df.to_string(index=False)

    report = [
        "# Reporte de calidad de datos - Fase 0",
        "",
        "## Alcance",
        "- Analisis principal: 2022, 2023 y 2024.",
        "- 2025 se usa solo como soporte.",
        "",
        "## Inventario de fuentes",
        "```text",
        inventory_text,
        "```",
        "",
        "## Hallazgos de calidad",
        f"- Duplicados por AGNO+RBD (2022-2024): {no_dups}.",
        f"- Registros con AGNO distinto al anio del archivo (2022-2024): {no_agno_mismatch}.",
        "- 2023 trae una columna tecnica vacia al inicio; se elimina en la estandarizacion.",
        "- Hay diferencias de esquema entre anios, por lo que la comparacion longitudinal usa solo columnas comunes.",
        "",
        "## Reglas aplicadas",
        "- No se modifica ningun archivo raw.",
        "- Se normalizan tipos para campos clave.",
        "- Se comparan 2022-2024 con la interseccion de columnas.",
        "",
        "## Riesgos",
        "- Variables nuevas en 2024 no son comparables hacia atras.",
        "- 2025 usa separador distinto (coma), por lo que requiere carga diferenciada.",
    ]
    (OUTPUT_DIR / "reporte_calidad.md").write_text("\n".join(report), encoding="utf-8")

    questions = [
        "# Preguntas de investigacion priorizadas",
        "",
        "1. Como evoluciona la matricula total entre 2022 y 2024 a nivel nacional?",
        "2. Que regiones concentran mayor matricula y como cambia su participacion anual?",
        "3. Como se distribuye la matricula por dependencia administrativa (COD_DEPE2) y que variaciones aparecen en el periodo?",
        "4. Que comunas concentran la mayor matricula y existen cambios relevantes en el ranking?",
        "5. Como se comporta la matricula segun estado del establecimiento (ESTADO_ESTAB)?",
        "6. Que variables se mantienen estables y son candidatas a dimensiones para el DW?",
    ]
    (OUTPUT_DIR / "preguntas_investigacion.md").write_text("\n".join(questions), encoding="utf-8")

    resumen = [
        "# Resumen ejecutivo Fase 0",
        "",
        "- Se integraron y perfilaron los archivos 2022-2024 del dataset oficial de matricula por establecimiento.",
        "- Se identificaron diferencias tecnicas de estructura y se armonizo una base comun para comparacion.",
        "- Se genero una base integrada 2022-2024 junto con tablas y graficos para presentacion.",
        "- Se dejo definido un set de preguntas de investigacion para la fase de modelamiento dimensional.",
    ]
    (OUTPUT_DIR / "resumen_ejecutivo_fase0.md").write_text("\n".join(resumen), encoding="utf-8")


def build_source_description_report(
    catalog_df: pd.DataFrame, dictionaries_df: pd.DataFrame, comparable_cols: pd.DataFrame
) -> None:
    lines: List[str] = [
        "# Descripcion de la base de datos y diccionario de atributos",
        "",
        "## 1) Tablas existentes en la fuente",
        "",
        "Cada archivo anual se trata como una tabla independiente de origen (fuente denormalizada):",
        "",
        "```text",
        format_table_text(catalog_df, ["filas", "columnas"]),
        "```",
        "",
        "## 2) Atributos por tabla (nombre, tipo y descripcion)",
        "",
        "Nota: las descripciones se construyen a partir del nombre oficial de campo y se deben validar con metadata oficial de MINEDUC si el curso exige glosario institucional exacto.",
        "",
    ]

    for table in catalog_df["tabla"].tolist():
        sub = dictionaries_df[dictionaries_df["tabla"] == table].copy()
        sub = sub[["atributo", "tipo_dato", "descripcion", "nulos", "valores_distintos", "comparable_2022_2024"]]
        lines.extend(
            [
                f"### {table}",
                "```text",
                format_table_text(sub, ["nulos", "valores_distintos", "comparable_2022_2024"]),
                "```",
                "",
            ]
        )

    lines.extend(
        [
            "## 3) Comparabilidad estructural 2022-2024",
            f"- Columnas comunes para analisis longitudinal: {len(comparable_cols)}.",
            "- Diferencias relevantes: 2023 incluye columna tecnica vacia; 2024 agrega variables nuevas (por ejemplo, SLEP e indicadores de etnia/nacionalidad).",
            "",
            "## 4) Implicancia para el analisis",
            "- Las comparaciones temporales estrictas se hacen con la interseccion de columnas 2022-2024.",
            "- Las columnas exclusivas de 2024/2025 se reportan como analisis complementario, no como serie historica completa.",
        ]
    )

    (OUTPUT_DIR / "descripcion_fuente_y_diccionario.md").write_text("\n".join(lines), encoding="utf-8")


def build_analysis_report(integrated: pd.DataFrame) -> None:
    mat_year = (
        integrated.groupby("AGNO", as_index=False)["MAT_TOTAL"]
        .sum()
        .rename(columns={"AGNO": "anio", "MAT_TOTAL": "mat_total"})
        .sort_values("anio")
    )
    mat_year["var_abs"] = mat_year["mat_total"].diff().fillna(0)
    mat_year["var_pct"] = mat_year["mat_total"].pct_change().fillna(0) * 100

    reg = (
        integrated.groupby(["AGNO", "NOM_REG_RBD_A"], as_index=False)["MAT_TOTAL"]
        .sum()
        .rename(columns={"AGNO": "anio", "NOM_REG_RBD_A": "region", "MAT_TOTAL": "mat_total"})
    )
    reg["rank"] = reg.groupby("anio")["mat_total"].rank(method="dense", ascending=False)
    reg_top = reg[reg["rank"] <= 5].sort_values(["anio", "rank"])

    dep = (
        integrated.groupby(["AGNO", "COD_DEPE2"], as_index=False)["MAT_TOTAL"]
        .sum()
        .rename(columns={"AGNO": "anio", "COD_DEPE2": "cod_depe2", "MAT_TOTAL": "mat_total"})
        .sort_values(["anio", "mat_total"], ascending=[True, False])
    )

    analysis = [
        "# Analisis exploratorio - Fase 0",
        "",
        "## 1) Evolucion de matricula total 2022-2024",
        "```text",
        format_table_text(mat_year, ["mat_total", "var_abs", "var_pct"]),
        "```",
        "",
        "Interpretacion: la matricula total baja de 3.644.548 (2022) a 3.582.947 (2024), con una variacion acumulada de -61.601 estudiantes.",
        "",
        "## 2) Regiones con mayor concentracion de matricula",
        "```text",
        format_table_text(reg_top, ["mat_total", "rank"]),
        "```",
        "",
        "Interpretacion: RM mantiene el mayor volumen en todos los anios, seguida por Valparaiso y Biobio.",
        "",
        "## 3) Distribucion por dependencia administrativa",
        "```text",
        format_table_text(dep, ["mat_total"]),
        "```",
        "",
        "Interpretacion: COD_DEPE2=2 concentra la mayor matricula en los tres anios analizados.",
    ]

    (OUTPUT_DIR / "analisis_fase0.md").write_text("\n".join(analysis), encoding="utf-8")


def build_presentation_guide(integrated: pd.DataFrame) -> None:
    mat_year = (
        integrated.groupby("AGNO", as_index=False)["MAT_TOTAL"]
        .sum()
        .rename(columns={"AGNO": "agno", "MAT_TOTAL": "mat_total"})
        .sort_values("agno")
    )

    top_regions = (
        integrated.groupby(["AGNO", "NOM_REG_RBD_A"], as_index=False)["MAT_TOTAL"]
        .sum()
        .rename(columns={"AGNO": "agno", "NOM_REG_RBD_A": "region", "MAT_TOTAL": "mat_total"})
    )
    top_regions["rank"] = top_regions.groupby("agno")["mat_total"].rank(method="dense", ascending=False)
    top_regions = top_regions[top_regions["rank"] <= 5].sort_values(["agno", "rank"])

    dep = (
        integrated.groupby(["AGNO", "COD_DEPE2"], as_index=False)["MAT_TOTAL"]
        .sum()
        .rename(columns={"AGNO": "agno", "COD_DEPE2": "cod_depe2", "MAT_TOTAL": "mat_total"})
        .sort_values(["agno", "mat_total"], ascending=[True, False])
    )

    content = [
        "# Guia para presentacion - Fase 0",
        "",
        "## Tabla 1: Matricula total por anio (2022-2024)",
        "```text",
        format_table_text(mat_year, ["mat_total"]),
        "```",
        "",
        "## Tabla 2: Top 5 regiones por matricula y anio",
        "```text",
        format_table_text(top_regions, ["mat_total", "rank"]),
        "```",
        "",
        "## Tabla 3: Matricula por dependencia administrativa",
        "```text",
        format_table_text(dep, ["mat_total"]),
        "```",
        "",
        "## Graficos sugeridos",
        "- outputs/figuras/matricula_total_por_anio.png",
        "- outputs/figuras/top10_regiones_2024.png",
        "- outputs/figuras/matricula_por_dependencia_2024.png",
        "- outputs/figuras/matriz_estado_establecimiento.png",
    ]

    (OUTPUT_DIR / "guia_presentacion_fase0.md").write_text("\n".join(content), encoding="utf-8")


def build_figures(integrated: pd.DataFrame) -> None:
    sns.set_theme(style="whitegrid")

    mat_year = integrated.groupby("AGNO", as_index=False)["MAT_TOTAL"].sum().sort_values("AGNO")
    plt.figure(figsize=(8, 4.5))
    ax = sns.barplot(data=mat_year, x="AGNO", y="MAT_TOTAL", color="#2a9d8f")
    ax.set_title("Matricula total por anio (2022-2024)")
    ax.set_xlabel("Anio")
    ax.set_ylabel("Matricula total")
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{int(x):,}".replace(",", ".")))
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "matricula_total_por_anio.png", dpi=200)
    plt.close()

    reg_2024 = (
        integrated[integrated["AGNO"] == 2024]
        .groupby("NOM_REG_RBD_A", as_index=False)["MAT_TOTAL"]
        .sum()
        .sort_values("MAT_TOTAL", ascending=False)
        .head(10)
    )
    plt.figure(figsize=(9, 5))
    ax = sns.barplot(data=reg_2024, x="MAT_TOTAL", y="NOM_REG_RBD_A", color="#457b9d")
    ax.set_title("Top 10 regiones por matricula - 2024")
    ax.set_xlabel("Matricula total")
    ax.set_ylabel("Region")
    ax.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{int(x):,}".replace(",", ".")))
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "top10_regiones_2024.png", dpi=200)
    plt.close()

    dep_2024 = (
        integrated[integrated["AGNO"] == 2024]
        .groupby("COD_DEPE2", as_index=False)["MAT_TOTAL"]
        .sum()
        .sort_values("MAT_TOTAL", ascending=False)
    )
    plt.figure(figsize=(8, 4.5))
    ax = sns.barplot(data=dep_2024, x="COD_DEPE2", y="MAT_TOTAL", color="#e76f51")
    ax.set_title("Matricula por dependencia administrativa - 2024")
    ax.set_xlabel("COD_DEPE2")
    ax.set_ylabel("Matricula total")
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{int(x):,}".replace(",", ".")))
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "matricula_por_dependencia_2024.png", dpi=200)
    plt.close()

    state = (
        integrated.groupby(["AGNO", "ESTADO_ESTAB"], as_index=False)["MAT_TOTAL"]
        .sum()
        .pivot(index="AGNO", columns="ESTADO_ESTAB", values="MAT_TOTAL")
        .fillna(0)
        .sort_index()
    )
    plt.figure(figsize=(8, 4.5))
    sns.heatmap(state, annot=True, fmt=".0f", cmap="YlGnBu")
    plt.title("Matriz de matricula por estado del establecimiento")
    plt.xlabel("ESTADO_ESTAB")
    plt.ylabel("Anio")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "matriz_estado_establecimiento.png", dpi=200)
    plt.close()


def run_pipeline() -> None:
    ensure_dirs()
    dataframes, inventory_df = load_all_data()
    inventory_df.to_csv(TABLES_DIR / "inventario_fuentes.csv", index=False, encoding="utf-8-sig")

    comparable_cols = comparable_columns(dataframes)
    quality_df = quality_report_by_year(dataframes)
    integrated = build_integrated_base(dataframes, comparable_cols)

    build_aggregations(integrated, dataframes)
    catalog_df = build_table_catalog(dataframes, inventory_df)
    build_dictionary(dataframes, comparable_cols)
    dictionaries_df = build_dictionaries_by_table(dataframes, comparable_cols)
    build_markdown_reports(inventory_df, quality_df)
    build_source_description_report(catalog_df, dictionaries_df, comparable_cols)
    build_analysis_report(integrated)
    build_presentation_guide(integrated)
    build_figures(integrated)

    print("Pipeline Fase 0 ejecutado correctamente.")
    print(f"Tablas: {TABLES_DIR}")
    print(f"Figuras: {FIGURES_DIR}")
    print(f"Reportes: {OUTPUT_DIR}")


if __name__ == "__main__":
    run_pipeline()
