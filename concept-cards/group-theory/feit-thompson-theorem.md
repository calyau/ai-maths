---
# === CORE IDENTIFICATION ===
concept: Feit-Thompson Theorem
slug: feit-thompson-theorem

# === CLASSIFICATION ===
category: series-solvability
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Subnormal Series; Solvable and Nilpotent Groups"
chapter_number: 6
pdf_page: 89
section: "Solvable groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - odd order theorem

# === TYPED RELATIONSHIPS ===
prerequisites:
  - solvable-group
extends: []
related:
  - non-simplicity-criteria
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Are all groups of odd order solvable?"
  - "Must every finite group contain an element of order 2 or be solvable?"
---

# Quick Definition

Every finite group of odd order is solvable. Equivalently, every finite non-solvable group contains an element of order 2. The proof occupies an entire journal issue (Feit and Thompson, 1963).

# Core Definition

**Theorem 6.4 (Feit-Thompson).** Every finite group of odd order is solvable.

(Milne, Theorem 6.4, p. 89)

# Prerequisites

- **solvable-group** -- the conclusion of the theorem

# Key Properties

1. The contrapositive: every non-solvable finite group has even order (hence contains an involution by Cauchy's theorem)
2. The proof is 255 pages long (Pacific Journal of Mathematics, 1963)
3. This was a key step in the classification of finite simple groups
4. Burnside conjectured this result in 1897

# Context & Application

The Feit-Thompson theorem dramatically limits where non-solvable (and hence simple) groups can occur: only at even orders. Combined with other results, it was instrumental in the classification of finite simple groups. It implies that every finite group is either solvable or contains an element of order 2.

# Relationships

## Builds Upon
- **solvable-group** -- the property being established

## Related
- **non-simplicity-criteria** -- complements Sylow-theoretic non-simplicity arguments

# Source Reference

Chapter 6, Theorem 6.4, p. 89. References to Feit-Thompson 1963 and Glauberman 1999.

# Verification Notes

- Definition source: Direct from Theorem 6.4
- Confidence rationale: HIGH -- explicitly stated theorem (proof by reference)
- Uncertainties: None
