---
concept: Conjugacy Class
slug: conjugacy-class
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
  - "conjugacy class of an element"
prerequisites:
  - group-action
  - orbit
  - conjugation
  - centralizer
extends:
  - orbit
related:
  - class-equation
  - center
  - cycle-type
contrasts_with: []
answers_questions:
  - "What is a conjugacy class in a group?"
  - "When does a conjugacy class consist of a single element?"
---

# Quick Definition
Two elements a and b of G are conjugate if b = gag^{-1} for some g in G. The conjugacy classes of G are the orbits of G acting on itself by conjugation. An element's conjugacy class is a singleton {a} if and only if a is in the center Z(G).

# Core Definition
Two elements a and b of G are said to be conjugate in G if there is some g in G such that b = gag^{-1}, i.e., if and only if they are in the same orbit of G acting on itself by conjugation. The orbits of G acting on itself by conjugation are called the conjugacy classes of G (Dummit & Foote, p. 125). By Proposition 6, the number of conjugates of an element s equals |G : C_G(s)|, the index of the centralizer.

# Prerequisites
- **Group action** — Conjugacy classes are orbits of the conjugation action
- **Orbit** — Each class is an orbit
- **Conjugation** — The underlying action
- **Centralizer** — Determines the size of each class

# Key Properties
1. Conjugacy classes partition G
2. |conjugacy class of g| = |G : C_G(g)| (Proposition 6)
3. {a} is a conjugacy class iff a in Z(G)
4. Each conjugacy class size divides |G|
5. In S_n, two elements are conjugate iff they have the same cycle type (Proposition 11)
6. Normal subgroups are unions of conjugacy classes

# Examples
**Example 1** (p. 126): In S_3, the conjugacy classes are {1}, {(1 2), (1 3), (2 3)}, and {(1 2 3), (1 3 2)}.

**Example 2** (p. 127): In Q_8, the conjugacy classes are {1}, {-1}, {+/-i}, {+/-j}, {+/-k}.

**Example 3** (p. 127): In D_8, the conjugacy classes are {1}, {r^2}, {r, r^3}, {s, sr^2}, {sr, sr^3}.

# Relationships
## Builds Upon
- **Orbit** — Conjugacy classes are orbits under conjugation
## Enables
- **Class equation** — Sums conjugacy class sizes
- **Simplicity of A_n** — Uses conjugacy class analysis
## Related
- **Cycle type** — Determines conjugacy in S_n

# Common Confusions
- **Confusion**: Assuming conjugacy in a subgroup implies conjugacy in the larger group
  **Clarification**: Two elements conjugate in G may split into separate conjugacy classes in a subgroup H (e.g., 5-cycles split in A_5)

# Source Reference
Chapter 4: Group Actions, Section 4.3, pages 125-131.

# Verification Notes
- Definition source: Direct from p. 125
- Confidence: HIGH — explicit definition with extensive examples
- Uncertainties: None
