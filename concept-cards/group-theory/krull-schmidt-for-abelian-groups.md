---
# === CORE IDENTIFICATION ===
concept: Krull-Schmidt for Abelian Groups
slug: krull-schmidt-for-abelian-groups

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
pdf_page: 98
section: "Krull-Schmidt theorem"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - krull-schmidt-theorem
  - indecomposable-group
extends:
  - krull-schmidt-theorem
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does Krull-Schmidt say for finite abelian groups?"
---

# Quick Definition

For finite abelian groups, the Krull-Schmidt theorem says that the cyclic groups of prime-power order in a decomposition G = C_{m_1} x ... x C_{m_r} are uniquely determined (up to ordering). This is because cyclic groups of prime-power order are the indecomposable finite abelian groups.

# Core Definition

**Remark 6.33(c).** When applied to a finite abelian group, the Krull-Schmidt theorem shows that the groups C_{m_i} in a decomposition G = C_{m_1} x ... x C_{m_r} with each m_i a prime power are uniquely determined up to isomorphism (and ordering).

(Milne, Remark 6.33c, p. 98)

# Prerequisites

- **krull-schmidt-theorem** -- the general theorem
- **indecomposable-group** -- C_{p^n} are the indecomposable abelian groups

# Key Properties

1. Indecomposable abelian groups = cyclic of prime-power order
2. Uniqueness of the prime-power decomposition follows from Krull-Schmidt
3. This gives an alternative route to the fundamental theorem of finite abelian groups

# Relationships

## Builds Upon
- **krull-schmidt-theorem** -- the general result specialized to abelian groups

# Source Reference

Chapter 6, Remark 6.33(c), p. 98.

# Verification Notes

- Definition source: Direct from Remark 6.33c
- Confidence rationale: HIGH -- explicit remark
- Uncertainties: None
