---
# === CORE IDENTIFICATION ===
concept: Admissible Composition Series
slug: admissible-composition-series

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
pdf_page: 96
section: "Groups with operators"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - a-group-operators
  - admissible-subgroup
  - composition-series
extends:
  - composition-series
related:
  - jordan-holder-for-a-groups
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an admissible composition series?"
  - "What are the quotients of an admissible composition series?"
---

# Quick Definition

An admissible composition series for an A-group G is a chain of admissible subgroups G = G_0 superset G_1 superset ... superset G_r = {1} with each G_i normal in G_{i-1}, having no proper admissible refinement. The quotients are simple A-groups (no normal admissible subgroups besides the trivial ones).

# Core Definition

An *admissible subnormal series* is a chain of admissible subgroups G superset G_1 superset ... superset G_r with each G_i normal in G_{i-1}. An *admissible composition series* is one with no proper admissible refinement. The quotients are A-groups that are simple as A-groups (they have no normal admissible subgroups apart from the obvious two).

(Milne, p. 96)

# Prerequisites

- **a-group-operators** -- the framework
- **admissible-subgroup** -- all terms must be admissible
- **composition-series** -- the concept being generalized

# Key Properties

1. Simple as an A-group is weaker than simple as a group: a group may have normal subgroups that are not admissible
2. When A = G (conjugation), admissible composition series correspond to normal composition series, and quotients are simple as G-groups
3. When A = Aut(G), the terms are characteristic subgroups

# Examples

**Example 1** (p. 97, 6.29a): A = G acting by conjugation. Admissible series = normal series. Quotients of admissible composition series are isomorphic as G-groups.

**Example 2** (p. 97, 6.29b): A = Aut(G). Admissible series = characteristic series. Quotients are isomorphic as Aut(G)-groups.

# Relationships

## Builds Upon
- **composition-series** -- generalized to include operator compatibility

## Enables
- **jordan-holder-for-a-groups** -- uniqueness of admissible composition factors

# Source Reference

Chapter 6, p. 96-97.

# Verification Notes

- Definition source: Direct from p. 96
- Confidence rationale: HIGH -- explicit definition
- Uncertainties: None
