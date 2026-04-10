---
concept: Split Maximal Torus
slug: split-maximal-torus
category: reductive-groups
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "The Structure of Reductive Groups: The Split Case"
chapter_number: 5
pdf_page: 336
section: "Split reductive groups"
extraction_confidence: high
aliases: []
prerequisites:
  - split-torus
  - reductive-algebraic-group
extends:
  - split-torus
related:
  - split-reductive-group
  - cartan-subalgebra
contrasts_with: []
answers_questions:
  - "What is a split maximal torus?"
  - "What distinguishes a split torus from a non-split torus?"
---

# Quick Definition

A split maximal torus in an algebraic group G is a split torus T ⊂ G that is maximal among all tori in G (over a separable closure). All split maximal tori are conjugate by elements of G(k).

# Core Definition

A torus T ⊂ G is **maximal** if T_{k^{sep}} is maximal in G_{k^{sep}} (i.e., not properly contained in any other torus). A torus T is maximal if and only if T = C_G(T) (it equals its own centralizer) (Milne, §1c, p. 336; Theorem 2.7c).

A **split maximal torus** is a maximal torus that is split (diagonalizable over k). All split maximal tori are conjugate by elements of G(k) (Theorem 2.19, proved in 3.22–3.23).

# Prerequisites

- **Split torus** — A split maximal torus is a split torus that is maximal
- **Reductive algebraic group** — The ambient group

# Key Properties

1. T is maximal iff T = C_G(T) (Theorem 2.7c)
2. All maximal tori in G_{k^{al}} are conjugate (Theorem 3.22)
3. All split maximal tori in G are conjugate by G(k) (Theorem 2.19)
4. 𝔻_n is a split maximal torus in GL_n (its own centralizer)
5. Not to be confused with "maximal split torus" (which may not be maximal among all tori)

# Examples

**Example 1** (p. 336): 𝔻_n is a split maximal torus in GL_n.

**Example 2** (p. 337): The diagonal matrices of determinant 1 form a split maximal torus in SL_{n+1}.

# Common Confusions

- **Confusion**: "Split maximal torus" vs "maximal split torus"
  **Clarification**: A split maximal torus is maximal among ALL tori and happens to be split. A maximal split torus is maximal among SPLIT tori but may not be maximal among all tori. (footnote 3, p. 337)

# Source Reference

Chapter V, Sections 1c, 2h–2i, pages 336, 342–343.

# Verification Notes

- Definition source: Direct from §1c
- Confidence: HIGH
- Uncertainties: None
