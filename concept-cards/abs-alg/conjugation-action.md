---
concept: Conjugation Action
slug: conjugation-action
category: group-theory
subcategory: group-actions
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Group Actions"
chapter_number: 4
pdf_page: 125
section: "4.3 Groups Acting on Themselves by Conjugation"
extraction_confidence: high
aliases:
  - "action by conjugation"
prerequisites:
  - group-action
  - conjugation
extends:
  - group-action
related:
  - conjugacy-class
  - class-equation
  - centralizer
  - normalizer
contrasts_with:
  - left-regular-representation
answers_questions:
  - "How does a group act on itself by conjugation?"
  - "How does conjugation on subsets relate to normalizers?"
---

# Quick Definition
The conjugation action of G on itself is g . a = gag^{-1}. Orbits are conjugacy classes; the stabilizer of a is its centralizer C_G(a). G also acts on its subsets by g . S = gSg^{-1}; the stabilizer of a subset S is the normalizer N_G(S).

# Core Definition
G acts on itself by conjugation: g . a = gag^{-1} for all g, a in G (Dummit & Foote, p. 125). This extends to G acting on the power set P(G) by g . S = gSg^{-1}. For elements: the orbits are conjugacy classes, the stabilizer of a is C_G(a). For subsets: the orbits are conjugacy classes of subsets, the stabilizer of S is N_G(S). The number of conjugates of S equals |G : N_G(S)| (Proposition 6).

# Prerequisites
- **Group action** — Conjugation defines a group action
- **Conjugation** — The underlying operation

# Key Properties
1. g . a = gag^{-1} (action on elements)
2. g . S = gSg^{-1} (action on subsets)
3. Orbits on elements = conjugacy classes
4. Stabilizer of a = centralizer C_G(a)
5. Stabilizer of S = normalizer N_G(S)
6. Number of conjugates of S = |G : N_G(S)| (Proposition 6)
7. Number of conjugates of a = |G : C_G(a)| (Proposition 6)

# Relationships
## Builds Upon
- **Group action** — Conjugation is a specific action
## Enables
- **Conjugacy class** — Orbits of the conjugation action
- **Class equation** — Counts elements by conjugacy class
- **Normalizer** — Stabilizer of subsets under conjugation
- **Centralizer** — Stabilizer of elements under conjugation

# Source Reference
Chapter 4, Section 4.3, pages 125-132.

# Verification Notes
- Definition source: Direct from p. 125
- Confidence: HIGH
- Uncertainties: None
