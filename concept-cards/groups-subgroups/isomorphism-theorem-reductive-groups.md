---
concept: Isomorphism Theorem for Split Reductive Groups
slug: isomorphism-theorem-reductive-groups
category: reductive-groups
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "The Structure of Reductive Groups: The Split Case"
chapter_number: 5
pdf_page: 348
section: "The main theorems"
extraction_confidence: high
aliases:
  - "isomorphism theorem"
prerequisites:
  - root-datum
  - split-reductive-group
extends: []
related:
  - existence-theorem-reductive-groups
  - isogeny-theorem
contrasts_with: []
answers_questions:
  - "How does a root datum determine a split reductive group?"
---

# Quick Definition

The isomorphism theorem states that every isomorphism of root data Ψ(G,T) → Ψ(G',T') arises from an isomorphism (G,T) → (G',T'). Thus root data classify split reductive groups up to isomorphism.

# Core Definition

**Theorem 2.22 (Isomorphism)**: Every isomorphism Ψ(G,T) → Ψ(G',T') of root data arises from an isomorphism (G,T) → (G',T') of split reductive groups (Milne, p. 348).

More precisely (Theorem 7.6): an isomorphism f: (G,T) → (G',T') defines an isomorphism of root data, and every isomorphism of root data arises from such an f, unique up to an inner automorphism by an element of T(k).

# Prerequisites

- **Root datum** — The classifying object
- **Split reductive group** — The objects being classified

# Key Properties

1. The root datum is a complete invariant (up to isomorphism)
2. The isomorphism is unique up to conjugation by T(k)
3. Combined with existence: bijection between split reductive groups and reduced root data

# Relationships

## Related
- **Existence theorem** — The existence complement
- **Isogeny theorem** — Generalizes to isogenies

# Source Reference

Chapter V, Section 2m, Theorem 2.22, page 348; Section 7, Theorem 7.6, page 378.

# Verification Notes

- Definition source: Direct from Theorem 2.22 and 7.6
- Confidence: HIGH
- Uncertainties: None
