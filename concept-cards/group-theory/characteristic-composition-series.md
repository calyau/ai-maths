---
# === CORE IDENTIFICATION ===
concept: Characteristic Composition Series
slug: characteristic-composition-series

# === CLASSIFICATION ===
category: groups-with-operators
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Subnormal Series; Solvable and Nilpotent Groups"
chapter_number: 6
pdf_page: 97
section: "Groups with operators"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - Aut(G)-composition series

# === TYPED RELATIONSHIPS ===
prerequisites:
  - characteristic-subgroup
  - a-group-operators
  - admissible-composition-series
extends:
  - admissible-composition-series
related:
  - jordan-holder-for-a-groups
  - normal-composition-series
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a characteristic composition series?"
---

# Quick Definition

When A = Aut(G) acts as operator group, an admissible composition series consists of characteristic subgroups. The quotients of two such series are isomorphic as Aut(G)-groups.

# Core Definition

**Example 6.29(b).** Consider G with A = Aut(G) as operator group. An admissible subnormal series is a sequence G = G_0 superset G_1 superset ... superset G_s = {1} with each G_i a characteristic subgroup of G. The quotients of two admissible composition series are isomorphic as Aut(G)-groups.

(Milne, Example 6.29b, p. 97)

# Prerequisites

- **characteristic-subgroup** -- the terms are characteristic
- **a-group-operators** -- the framework with A = Aut(G)
- **admissible-composition-series** -- the general notion specialized

# Key Properties

1. Each term is characteristic in G (invariant under all automorphisms)
2. This is a strictly stronger condition than being a normal composition series
3. The quotient isomorphisms respect the full automorphism group

# Relationships

## Builds Upon
- **admissible-composition-series** -- specialization to A = Aut(G)

## Related
- **jordan-holder-for-a-groups** -- provides the uniqueness
- **normal-composition-series** -- the A = G (conjugation) case is weaker

# Source Reference

Chapter 6, Example 6.29(b), p. 97.

# Verification Notes

- Definition source: Direct from Example 6.29b
- Confidence rationale: HIGH -- explicit example
- Uncertainties: None
