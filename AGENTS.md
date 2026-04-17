# AGENTS.md

## Project Overview
- Course: Inteligencia de Negocios (MINEDUC), Fase 0.
- Goal of this phase: understand, profile, and explore the selected open dataset before DW implementation.
- Focus dataset: "Resumen de matrícula por establecimiento" (MINEDUC Datos Abiertos).
- Main analysis window: 2022, 2023, 2024.
- 2025 can be used only as optional support if structure is comparable.

## Main Objective
Analyze and integrate MINEDUC open data (2022-2024) to identify patterns, trends, and relevant variables as input for future data warehouse design.

## Scope (Phase 0)
### In scope
- Source understanding and justification.
- Dataset structure and attributes review.
- Data quality and consistency checks across years.
- Exploratory analysis with Python/Pandas.
- Identification of candidate dimensions for DW.
- Formulation of research questions for next phases.

### Out of scope
- Full DW implementation.
- Final multidimensional model implementation.
- Full ETL production pipeline.
- OLAP deployment.

## Data Inventory (current workspace)
Files in `data/`:
- `20221013_Resumen_Matrícula_EE_Oficial_2022_20220430_WEB.csv`
- `20230925_Resumen_Matricula_EE_Oficial_2023_20230430_WEB.csv`
- `20240930_Resumen_Matricula_EE_Oficial_2024_20240430 1.csv`
- `20251029_Resumen_Matricula_EE_Oficial_2025_20250430.csv`

## Known Technical Differences
- 2022: semicolon separator (`;`), 59 columns.
- 2023: semicolon separator (`;`), 61 columns, includes an extra empty first column.
- 2024: semicolon separator (`;`), 74 columns.
- 2025: comma separator (`,`), 71 columns.
- Conclusion: schema harmonization is required before cross-year comparisons.

## Analytical Priorities
1. Harmonize schemas for 2022-2024.
2. Normalize column names/types and remove technical artifacts.
3. Validate key fields (`AGNO`, `RBD`, region/comuna/dependency fields, `MAT_TOTAL`, `ESTADO_ESTAB`).
4. Check data quality: nulls, duplicates, domain consistency.
5. Build integrated base table (append by year).
6. Produce initial EDA (time, region, comuna, dependency, establishment status).

## Candidate Dimensions (for future DW)
- Time (`AGNO`)
- Establishment (`RBD`, name, status)
- Territory (region, province, comuna)
- Administrative dependency (`COD_DEPE`, `COD_DEPE2`)
- Education level / modality fields (where comparable)
- Inclusion / special indicators (if stable across years)

## Research Questions (initial)
- How does total enrollment evolve from 2022 to 2024?
- Which regions concentrate most enrollment?
- How does enrollment distribution vary by administrative dependency?
- Are there meaningful territorial differences by comuna?
- Which variables are stable and useful for dimensional modeling?

## Quality Rules (minimum)
- No cross-year analysis without schema harmonization.
- Keep raw files unchanged; work on transformed copies/dataframes.
- Track every transformation step for reproducibility.
- Explicitly document dropped or recoded columns.
- Prefer comparable metrics across all analyzed years.

## Deliverables for Phase 0
- Source description and justification.
- Data dictionary (working version, harmonized columns).
- Data quality report (issues + handling decisions).
- EDA outputs (tables/plots + concise interpretation).
- Prioritized research questions for next phase.

## Working Conventions for AI Agents
- Language for outputs: Spanish.
- Be concise and reproducible.
- Do not invent fields; infer only from actual data.
- Flag assumptions explicitly.
- Prefer pandas-based workflows and clear, auditable steps.
- If ambiguity affects conclusions, propose default + alternative.
