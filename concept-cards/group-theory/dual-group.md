---
# === CORE IDENTIFICATION ===
concept: Dual Group
slug: dual-group

# === CLASSIFICATION ===
category: subgroup-theory
subcategory: commutative-groups
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Basic Definitions and Results"
chapter_number: 1
pdf_page: 27
section: "The linear characters of a commutative group"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - character group
  - Pontryagin dual

# === TYPED RELATIONSHIPS ===
prerequisites:
  - linear-character
extends: []
related:
  - orthogonality-relations
  - fundamental-theorem-finitely-generated-abelian-groups
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the dual group of a commutative group?"
  - "Is the dual group isomorphic to the original group?"
---

# Quick Definition

The dual group $G^\vee$ of a group $G$ is the group of all linear characters $\chi: G \to \mu(\mathbb{C})$, with pointwise multiplication $(\chi + \chi')(g) = \chi(g)\chi'(g)$.

# Core Definition

"The set of characters of a group $G$ becomes a group $G^\vee$ under the addition, $(\chi + \chi')(g) = \chi(g)\chi'(g)$, called the *dual group* of $G$." (Milne, p. 27)

# Prerequisites

- **Linear character** — the elements of $G^\vee$ are characters

# Key Properties

1. For finite commutative $G$: $G^\vee \approx G$ (non-canonically) (Theorem 1.60a)
2. The canonical map $G \to G^{\vee\vee}$, $a \mapsto (\chi \mapsto \chi(a))$, is an isomorphism (Theorem 1.60b)
3. $G \approx G^\vee$ but $G \simeq G^{\vee\vee}$ (the double dual is canonically isomorphic)
4. $\mathbb{Z}^\vee \cong \mu(\mathbb{C})$
5. $(G \times H)^\vee \simeq G^\vee \times H^\vee$

# Context & Application

Pontryagin duality generalizes this to locally compact abelian groups with topologies. The canonical isomorphism $G \simeq G^{\vee\vee}$ is a prototype for duality in algebra and analysis.

# Examples

**Example 1** (p. 27): $\mathbb{Z}^\vee \cong \mu(\mathbb{C})$ via $\chi \mapsto \chi(1)$.

**Example 2**: $C_n^\vee \cong C_n$, since characters are determined by $\chi(1) \in \mu_n(\mathbb{C})$.

# Relationships

## Builds Upon
- **linear-character**

## Related
- **orthogonality-relations** — characters from $G^\vee$ satisfy orthogonality
- **fundamental-theorem-finitely-generated-abelian-groups** — $G^\vee \approx G$ uses the structure theorem

# Source Reference

Chapter 1, Theorem 1.60, Aside 1.61, pages 27-28.

# Verification Notes

- Definition source: Direct from p. 27
- Confidence: HIGH
- Uncertainties: None
