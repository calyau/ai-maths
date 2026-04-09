---
# === CORE IDENTIFICATION ===
concept: Normal Composition Series (G-Composition Series)
slug: normal-composition-series

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
  - G-composition series

# === TYPED RELATIONSHIPS ===
prerequisites:
  - normal-series
  - a-group-operators
  - admissible-composition-series
extends:
  - admissible-composition-series
related:
  - jordan-holder-for-a-groups
contrasts_with:
  - composition-series

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a normal composition series?"
  - "How does Jordan-Holder apply to normal series?"
---

# Quick Definition

When G acts on itself by conjugation, an admissible composition series is a normal series (each G_i normal in G) that cannot be refined by inserting more normal subgroups. The quotients of two such series are isomorphic as G-groups (not just as abstract groups).

# Core Definition

**Example 6.29(a).** Consider G with G acting by conjugation. An admissible subnormal series is a sequence G = G_0 superset G_1 superset ... superset G_s = {1} with each G_i normal in G, i.e., a normal series. The action of G on G_i by conjugation passes to the quotient, giving an action of G on G_i/G_{i+1}. The quotients of two admissible composition series are isomorphic as G-groups.

(Milne, Example 6.29a, p. 97)

# Prerequisites

- **normal-series** -- a normal composition series is a maximal normal series
- **a-group-operators** -- the framework with A = G acting by conjugation
- **admissible-composition-series** -- the general notion specialized

# Key Properties

1. Each term is normal in G (not just in the preceding term)
2. The quotients carry a G-action by conjugation
3. The isomorphisms in the Jordan-Holder theorem respect the G-action
4. This is strictly finer than the ordinary composition series (which only requires subnormality)

# Relationships

## Builds Upon
- **admissible-composition-series** -- specialization to A = G

## Related
- **jordan-holder-for-a-groups** -- provides the stronger uniqueness

## Contrasts With
- **composition-series** -- ordinary composition series need not have all terms normal in G

# Source Reference

Chapter 6, Example 6.29(a), p. 97.

# Verification Notes

- Definition source: Direct from Example 6.29a
- Confidence rationale: HIGH -- explicit example
- Uncertainties: None
