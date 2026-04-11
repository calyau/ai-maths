---
concept: Class Equation
slug: class-equation
category: group-theory
subcategory: group-actions
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Group Actions"
chapter_number: 4
pdf_page: 126
section: "4.3 Groups Acting on Themselves by Conjugation"
extraction_confidence: high
aliases:
  - "conjugacy class equation"
prerequisites:
  - conjugacy-class
  - center
  - centralizer
  - orbit-stabilizer-theorem
extends:
  - orbit-stabilizer-theorem
related:
  - p-group
  - sylow-theorems
contrasts_with: []
answers_questions:
  - "What is the class equation of a finite group?"
  - "How does the class equation prove that p-groups have nontrivial centers?"
---

# Quick Definition
For a finite group G with representatives g_1, ..., g_r of the conjugacy classes not contained in the center Z(G), the class equation is: |G| = |Z(G)| + sum of |G : C_G(g_i)| for i = 1 to r.

# Core Definition
Theorem 7 (The Class Equation): Let G be a finite group and let g_1, g_2, ..., g_r be representatives of the distinct conjugacy classes of G not contained in the center Z(G). Then |G| = |Z(G)| + sum_{i=1}^{r} |G : C_G(g_i)| (Dummit & Foote, p. 126). Each summand on the right divides |G| since they are indices of subgroups. Each summand |G : C_G(g_i)| > 1.

# Prerequisites
- **Conjugacy class** — The equation counts elements by conjugacy class
- **Center** — Singleton conjugacy classes form the center
- **Centralizer** — Determines conjugacy class sizes
- **Orbit-stabilizer theorem** — The class equation is its application to conjugation

# Key Properties
1. |G| = |Z(G)| + sum of |G : C_G(g_i)| where the sum runs over non-central conjugacy classes
2. Each non-central conjugacy class has size > 1
3. Each conjugacy class size divides |G|
4. If |G| = p^a then p divides |Z(G)|, so Z(G) is nontrivial (Theorem 8)
5. Groups of order p^2 are abelian (Corollary 9)

# Context & Application
The class equation is a fundamental tool for proving structural results about finite groups. Its first application is showing p-groups have nontrivial centers (Theorem 8), which is the starting point for the theory of p-groups. It is also used in the proof of Sylow's Theorem and the proof of simplicity of A_5.

# Examples
**Example 1** (p. 127): For Q_8: |Q_8| = 8 = 2 + 2 + 2 + 2, with Z(Q_8) = {1, -1} having order 2.

**Example 2** (p. 127): For D_8: |D_8| = 8 = 2 + 2 + 2 + 2, with Z(D_8) = {1, r^2} having order 2.

# Relationships
## Builds Upon
- **Orbit-stabilizer theorem** — The class equation applies it to conjugation
## Enables
- **P-group properties** — Centers of p-groups are nontrivial
- **Sylow theorems** — Class equation used in the proof

# Common Errors
- **Error**: Including central elements in the summation
  **Correction**: The summation runs only over non-central conjugacy class representatives; central elements contribute to |Z(G)|

# Source Reference
Chapter 4: Group Actions, Section 4.3, Theorem 7, page 126. See also Theorem 8 and Corollary 9.

# Verification Notes
- Definition source: Direct from Theorem 7, p. 126
- Confidence: HIGH — stated and proved as a theorem
- Uncertainties: None
