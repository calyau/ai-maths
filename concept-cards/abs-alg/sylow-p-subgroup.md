---
concept: Sylow p-Subgroup
slug: sylow-p-subgroup
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
  - "Sylow subgroup"
  - "Sylow p-group"
prerequisites:
  - p-group
  - subgroup
  - order-of-group
  - lagranges-theorem
extends:
  - p-group
related:
  - first-sylow-theorem
  - second-sylow-theorem
  - third-sylow-theorem
  - normal-subgroup
contrasts_with:
  - p-group
answers_questions:
  - "What is a Sylow p-subgroup?"
  - "How large can a p-subgroup be in a finite group?"
---

# Quick Definition
If |G| = p^a * m where p does not divide m, then a Sylow p-subgroup of G is a subgroup of order p^a, the largest possible p-power dividing |G|. The set of Sylow p-subgroups is denoted Syl_p(G) and their number is denoted n_p(G).

# Core Definition
If G is a group of order p^a * m, where p does not divide m, then a subgroup of order p^a is called a Sylow p-subgroup of G. The set of Sylow p-subgroups of G is denoted Syl_p(G) and the number of Sylow p-subgroups is denoted n_p(G) (Dummit & Foote, p. 142). Sylow's Theorem guarantees existence, conjugacy, and a congruence condition on n_p.

# Prerequisites
- **p-group** — A Sylow p-subgroup is a maximal p-subgroup
- **Subgroup** — It is a subgroup of G
- **Order of group** — Its order is the largest p-power dividing |G|
- **Lagrange's theorem** — Its order divides |G|

# Key Properties
1. Order equals p^a where p^a is the largest power of p dividing |G|
2. Existence guaranteed by the First Sylow Theorem
3. Any two Sylow p-subgroups are conjugate (Second Sylow Theorem)
4. n_p divides m and n_p is congruent to 1 mod p (Third Sylow Theorem)
5. P is the unique Sylow p-subgroup iff P is normal in G (Corollary 20)
6. n_p = 1 iff P is normal iff P is characteristic (Corollary 20)
7. Any two Sylow p-subgroups (for the same prime) are isomorphic

# Construction / Recognition
## To Find Sylow p-Subgroups:
1. Factor |G| = p^a * m with gcd(p, m) = 1
2. Look for subgroups of order p^a
3. Use the congruence n_p equiv 1 mod p and n_p | m to constrain possibilities
4. If n_p = 1, the Sylow p-subgroup is normal (and unique)

# Examples
**Example 1** (p. 146): S_3 has three Sylow 2-subgroups: <(1 2)>, <(2 3)>, <(1 3)>. It has a unique Sylow 3-subgroup: <(1 2 3)>.

**Example 2** (p. 146): A_4 has a unique Sylow 2-subgroup (V_4) and four Sylow 3-subgroups.

**Example 3** (p. 146): S_4 has n_2 = 3 and n_3 = 4. Each Sylow 2-subgroup is isomorphic to D_8.

# Relationships
## Builds Upon
- **p-group** — A Sylow p-subgroup IS a p-group (of maximal order in G)
## Enables
- **First Sylow theorem** — Guarantees existence
- **Second Sylow theorem** — All are conjugate
- **Third Sylow theorem** — Constrains their number
## Contrasts With
- **p-group** — A p-group is any group of prime-power order; a Sylow p-subgroup specifically has the largest p-power order within G

# Common Errors
- **Error**: Assuming Sylow p-subgroups are always normal
  **Correction**: They are normal only when n_p = 1

# Common Confusions
- **Confusion**: Thinking there must be subgroups of every prime-power order dividing |G|
  **Clarification**: Sylow's Theorem guarantees subgroups of order p^a (the full prime power), not necessarily of intermediate orders in general (though Theorem 6.1 shows p-groups do have subgroups of all orders)

# Source Reference
Chapter 4: Group Actions, Section 4.5, page 142. Theorem 18 (Sylow's Theorem) and Corollary 20.

# Verification Notes
- Definition source: Direct from p. 142
- Confidence: HIGH — explicit definition
- Uncertainties: None
