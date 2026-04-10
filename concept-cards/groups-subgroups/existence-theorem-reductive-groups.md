---
concept: Existence Theorem for Split Reductive Groups
slug: existence-theorem-reductive-groups
category: reductive-groups
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "The Structure of Reductive Groups: The Split Case"
chapter_number: 5
pdf_page: 347
section: "The main theorems"
extraction_confidence: high
aliases:
  - "existence theorem"
prerequisites:
  - root-datum
  - split-reductive-group
extends: []
related:
  - isomorphism-theorem-reductive-groups
  - isogeny-theorem
contrasts_with: []
answers_questions:
  - "How do I construct a split reductive group from a root datum?"
---

# Quick Definition

The existence theorem states that every reduced root datum arises from a split reductive group (G,T). Combined with the isomorphism theorem, this gives a bijection between isomorphism classes of split reductive groups and reduced root data.

# Core Definition

**Theorem 2.21 (Existence)**: Every reduced root datum arises from a split reductive group (G, T) (Milne, p. 348).

The proof (sketched in §6) proceeds by:
1. Showing it suffices to handle semisimple root data
2. For each indecomposable Dynkin diagram, constructing the simply connected group (e.g., SL_{n+1} for A_n, Sp_{2n} for C_n)
3. Obtaining other groups as quotients by subgroups of the centre

# Prerequisites

- **Root datum** — The classifying object
- **Split reductive group** — The objects being classified

# Key Properties

1. Every reduced root datum is realized (no "exotic" root data)
2. The root datum is field-independent: the same construction works over any field
3. For characteristic zero, can construct via Lie algebras and Tannakian categories (Theorem 3.20 in Ch. III)

# Relationships

## Related
- **Isomorphism theorem** — Uniqueness complement to existence
- **Isogeny theorem** — Isogenies correspond to isogenies of root data

# Source Reference

Chapter V, Section 2m, Theorem 2.21, page 348; Section 6, pages 374–377.

# Verification Notes

- Definition source: Direct from Theorem 2.21
- Confidence: HIGH — major named theorem
- Uncertainties: None
