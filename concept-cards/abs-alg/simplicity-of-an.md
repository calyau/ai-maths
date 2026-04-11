---
concept: Simplicity of A_n
slug: simplicity-of-an
category: group-theory
subcategory: group-actions
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Group Actions"
chapter_number: 4
pdf_page: 152
section: "4.6 The Simplicity of A_n"
extraction_confidence: high
aliases:
  - "A_n is simple"
prerequisites:
  - conjugacy-class
  - normal-subgroup
  - sylow-p-subgroup
  - class-equation
extends:
  - simple-group
related:
  - cycle-type
contrasts_with: []
answers_questions:
  - "For which n is the alternating group A_n simple?"
  - "Why is A_4 not simple?"
---

# Quick Definition
The alternating group A_n is simple for all n >= 5. The proof for n = 5 uses conjugacy class sizes; the proof for n >= 6 uses induction and the structure of stabilizers.

# Core Definition
Theorem 24: A_n is simple for all n >= 5 (Dummit & Foote, p. 153). The base case A_5 (Theorem 12, p. 131) is proved by computing that the conjugacy classes of A_5 have sizes 1, 15, 20, 12, 12, and no proper nontrivial union of these (including 1) divides 60. The inductive step for n >= 6 uses the stabilizers G_i (isomorphic to A_{n-1}) and shows that any normal subgroup H must contain all stabilizers or consist only of fixed-point-free elements, then derives contradictions in both cases.

# Prerequisites
- **Conjugacy class** — The proof analyzes conjugacy class sizes
- **Normal subgroup** — Simplicity means no proper nontrivial normal subgroups
- **Sylow p-subgroup** — Used in the A_5 proof
- **Class equation** — Conjugacy class analysis relies on this

# Key Properties
1. A_3 is cyclic of order 3, hence simple (abelian)
2. A_4 is NOT simple: it has a normal Sylow 2-subgroup V_4
3. A_5 is simple (the smallest non-abelian simple group, order 60)
4. A_n is simple for all n >= 5
5. A_5 is the unique simple group of order 60 (Proposition 23)

# Examples
**Example 1** (p. 131): A_5 has conjugacy classes of sizes 1, 15, 20, 12, 12. No proper nontrivial sum of these (including 1) divides 60, so A_5 is simple.

**Example 2** (p. 152): A_4 has n_2 = 1, so its Sylow 2-subgroup V_4 is normal, hence A_4 is not simple.

# Relationships
## Builds Upon
- **Conjugacy class** — Proof depends on class analysis
## Enables
- Understanding of finite simple groups

# Source Reference
Chapter 4: Group Actions, Section 4.6, Theorem 24, pages 152-155. Also Theorem 12 for A_5, pages 131-132.

# Verification Notes
- Definition source: Direct from Theorem 24, p. 153
- Confidence: HIGH — major theorem, fully proved
- Uncertainties: None
