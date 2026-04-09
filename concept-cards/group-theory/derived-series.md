---
# === CORE IDENTIFICATION ===
concept: Derived Series
slug: derived-series

# === CLASSIFICATION ===
category: series-solvability
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Subnormal Series; Solvable and Nilpotent Groups"
chapter_number: 6
pdf_page: 91
section: "Solvable groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - commutator-subgroup
extends: []
related:
  - solvable-group
  - solvable-length
  - upper-central-series
contrasts_with:
  - upper-central-series

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the derived series relate to solvability?"
  - "What is the canonical solvable series of a group?"
---

# Quick Definition

The derived series is G superset G' superset G'' superset ..., where each term is the commutator subgroup of the previous one: G^(n+1) = (G^(n))'. A group is solvable if and only if this series reaches {1}.

# Core Definition

The *second derived subgroup* of G is (G')' = G''; the third is G^(3) = (G'')', and so on. Since a characteristic subgroup of a characteristic subgroup is characteristic, each derived group G^(n) is a characteristic subgroup of G. This gives a normal series

G superset G^(1) superset G^(2) superset ...,

called the *derived series* of G.

**Proposition 6.10.** A group G is solvable if and only if G^(k) = 1 for some k.

(Milne, p. 91, Proposition 6.10)

# Prerequisites

- **commutator-subgroup** -- each term is the commutator subgroup of the previous

# Key Properties

1. Each G^(n) is characteristic (hence normal) in G
2. The derived series is a *normal* series (not just subnormal)
3. G is solvable iff G^(k) = {1} for some k
4. The derived series is the shortest solvable series: if G > G_1 > ... > G_s = 1 is any solvable series, then G^(i) subset G_i for all i
5. The quotients G^(i)/G^(i+1) are abelian (since G^(i+1) = (G^(i))')

# Context & Application

The derived series provides the canonical solvable series. Its length (when it terminates) is the solvable length, which is an important invariant. For S_n (n >= 5), the derived series is S_n > A_n > A_n > A_n > ..., which never reaches {1} since A_n is simple and nonabelian.

# Examples

**Example 1** (p. 91): For S_n with n >= 5, the derived series is S_n > A_n > A_n > A_n > ... (does not terminate, so S_n is not solvable).

**Example 2**: For S_4, the derived series is S_4 > A_4 > V > {1} where V = {1, (12)(34), (13)(24), (14)(23)}, showing S_4 is solvable of length 3.

**Example 3**: For S_3, the derived series is S_3 > A_3 > {1}, so S_3 is solvable of length 2.

# Relationships

## Builds Upon
- **commutator-subgroup** -- each term is a commutator subgroup

## Enables
- **solvable-group** -- solvable iff derived series reaches {1}
- **solvable-length** -- the length of the derived series

## Contrasts With
- **upper-central-series** -- ascending series related to nilpotency; derived series is descending and related to solvability

# Source Reference

Chapter 6, pp. 91-92, Proposition 6.10.

# Verification Notes

- Definition source: Direct from p. 91
- Confidence rationale: HIGH -- explicit definition and characterization
- Uncertainties: None
