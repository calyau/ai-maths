---
concept: First Sylow Theorem
slug: first-sylow-theorem
category: group-theory
subcategory: group-actions
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Group Actions"
chapter_number: 4
pdf_page: 142
section: "4.5 Sylow's Theorem"
extraction_confidence: high
aliases:
  - "Sylow existence theorem"
  - "Sylow I"
prerequisites:
  - sylow-p-subgroup
  - class-equation
  - lagranges-theorem
  - cauchys-theorem
extends:
  - cauchys-theorem
related:
  - second-sylow-theorem
  - third-sylow-theorem
contrasts_with: []
answers_questions:
  - "Do Sylow p-subgroups always exist?"
  - "What must I know before learning the Sylow theorems?"
  - "How do I apply the Sylow theorems to analyze group structure?"
---

# Quick Definition
For any finite group G and any prime p dividing |G|, Sylow p-subgroups of G exist. That is, if |G| = p^a * m with gcd(p, m) = 1, then G has a subgroup of order p^a.

# Core Definition
Theorem 18(1) (Sylow's Theorem, Part 1): Let G be a group of order p^a * m, where p is a prime not dividing m. Sylow p-subgroups of G exist, i.e., Syl_p(G) is nonempty (Dummit & Foote, p. 142). The proof uses induction on |G|, applying the class equation. If p divides |Z(G)|, Cauchy's Theorem for abelian groups provides a normal subgroup of order p, and induction on G/N completes the argument. Otherwise, some centralizer C_G(g_i) has order divisible by p^a but |C_G(g_i)| < |G|, and induction applies.

# Prerequisites
- **Sylow p-subgroup** — The objects whose existence is being proved
- **Class equation** — Key tool in the proof
- **Lagrange's theorem** — Subgroup orders divide group order
- **Cauchy's theorem** — Used for the base case with abelian groups

# Key Properties
1. Syl_p(G) is nonempty for every prime p dividing |G|
2. This is a partial converse to Lagrange's Theorem
3. The proof is constructive via induction using the class equation
4. Combined with Cauchy's Theorem, this gives existence of subgroups of all prime-power orders dividing |G|

# Context & Application
The First Sylow Theorem is fundamental to the analysis of finite group structure. It guarantees that the "largest" p-subgroups always exist, providing leverage for structural analysis. It is the starting point for most classification arguments for groups of specific orders.

# Examples
**Example 1**: For |G| = 12 = 2^2 * 3, there exist subgroups of order 4 (Sylow 2-subgroups) and order 3 (Sylow 3-subgroups).

**Example 2**: For |G| = 60 = 2^2 * 3 * 5, there exist Sylow 2-subgroups (order 4), Sylow 3-subgroups (order 3), and Sylow 5-subgroups (order 5).

# Relationships
## Builds Upon
- **Cauchy's theorem** — The First Sylow Theorem extends Cauchy's result
- **Class equation** — Used in the proof
## Enables
- **Second Sylow theorem** — Proved after establishing existence
- **Third Sylow theorem** — Constrains the number of Sylow subgroups

# Common Errors
- **Error**: Claiming the First Sylow Theorem guarantees subgroups of every order dividing |G|
  **Correction**: It only guarantees subgroups of the maximal prime-power orders p^a. For example, A_4 has no subgroup of order 6.

# Source Reference
Chapter 4: Group Actions, Section 4.5, Theorem 18(1), pages 142-144.

# Verification Notes
- Definition source: Direct from Theorem 18(1), p. 142
- Confidence: HIGH — stated and proved
- Uncertainties: None
