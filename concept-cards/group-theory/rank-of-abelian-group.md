---
# === CORE IDENTIFICATION ===
concept: Rank of a Finitely Generated Abelian Group
slug: rank-of-abelian-group

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
pdf_page: 26
section: "Commutative groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - free rank
  - torsion-free rank

# === TYPED RELATIONSHIPS ===
prerequisites:
  - fundamental-theorem-finitely-generated-abelian-groups
extends: []
related:
  - torsion-subgroup
  - rank-of-free-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the rank of a finitely generated abelian group?"
  - "How is rank determined?"
---

# Quick Definition

The rank of a finitely generated commutative group $M \cong C_{n_1} \times \cdots \times C_{n_s} \times C_\infty^r$ is the integer $r$, the number of infinite cyclic summands.

# Core Definition

"The number $r$ is called the rank of $M$." In any decomposition of $M$ of the form $C_{n_1} \times \cdots \times C_{n_s} \times C_\infty^r$, the number of copies of $C_\infty$ is the same. (Milne, Theorem 1.57, p. 26)

# Prerequisites

- **Fundamental theorem of finitely generated abelian groups** — provides the decomposition

# Key Properties

1. $r$ is uniquely determined by $M$
2. For a prime $p$ not dividing any $n_i$: $M/pM \cong (\mathbb{Z}/p\mathbb{Z})^r$, so $r = \dim_{\mathbb{F}_p}(M/pM)$
3. $r = 0$ iff $M$ is a torsion group (finite if finitely generated)
4. $M/M_{\mathrm{tors}} \cong \mathbb{Z}^r$

# Context & Application

The rank counts the "free" part of a finitely generated abelian group. It is the analogue of the dimension of a vector space.

# Examples

**Example 1**: $\mathbb{Z}^n$ has rank $n$.

**Example 2**: Any finite abelian group has rank 0.

# Relationships

## Builds Upon
- **fundamental-theorem-finitely-generated-abelian-groups**

## Related
- **torsion-subgroup** — the rank is the rank of $M/M_{\mathrm{tors}}$
- **rank-of-free-group** — distinct concept for non-abelian free groups

# Source Reference

Chapter 1, Theorem 1.57, page 26.

# Verification Notes

- Definition source: Direct from Theorem 1.57
- Confidence: HIGH
- Uncertainties: None
