---
# === CORE IDENTIFICATION ===
concept: Lagrange's Theorem
slug: lagrange-theorem

# === CLASSIFICATION ===
category: subgroup-theory
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Lagrange's Theorem"
chapter_number: 11
pdf_page: 64
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - subgroup
  - left-coset
  - group
extends: []
related:
  - index-of-subgroup
  - cauchy-theorem
  - euler-theorem
  - fermat-little-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do subgroups relate to the parent group's order (Lagrange's theorem)?"
  - "What constraints does the order of a group place on its subgroups?"
---

# Quick Definition

Lagrange's theorem states that the order of a subgroup of a finite group always divides the order of the group.

# Core Definition

**(11.1) Lagrange's Theorem.** The order of a subgroup of a finite group is always a divisor of the order of the group (Armstrong, p. 64).

The proof proceeds by partitioning $G$ into left cosets of $H$. Each coset has the same size as $H$, and distinct cosets are disjoint, so $|G| = (k+1)|H|$ where there are $k+1$ cosets.

# Prerequisites

- **Subgroup** — The theorem concerns the relationship between a subgroup and its parent group
- **Left coset** — The proof uses the partition of $G$ into left cosets of $H$
- **Group** — The ambient finite group whose order is being divided

# Key Properties

1. If $H$ is a subgroup of finite group $G$, then $|H|$ divides $|G|$
2. The quotient $|G|/|H|$ equals the number of distinct left cosets (the index)
3. The converse is false: a divisor of $|G|$ need not correspond to a subgroup (e.g., $A_4$ has no subgroup of order 6)
4. For prime divisors, Cauchy's theorem provides a partial converse

# Construction / Recognition

## To Apply Lagrange's Theorem:
1. Identify the finite group $G$ and compute $|G|$
2. Identify the subgroup $H$
3. Conclude that $|H|$ divides $|G|$
4. The number of distinct cosets is $|G|/|H|$

# Context & Application

Lagrange's theorem is one of the most fundamental results in finite group theory. Armstrong uses it to derive Euler's theorem and Fermat's little theorem in number theory, to classify subgroups of $A_4$, and as a stepping stone to Cauchy's theorem. The theorem constrains what subgroups can exist but does not guarantee their existence.

**Caution** (p. 64): Armstrong warns that the converse fails. If $m$ divides $|G|$, there is no guarantee that $G$ contains a subgroup of order $m$. The group $A_4$ (order 12) has no subgroup of order 6.

# Examples

**Example 1** (p. 64): $G = S_3$, $H = \{\varepsilon, (13)\}$. The three cosets $H$, $(123)H$, $(12)H$ partition $S_3$. Since $|S_3| = 6$ and $|H| = 2$, we get $6 = 3 \cdot 2$.

**Example 2** (pp. 65-66): The subgroups of $A_4$ (order 12). By Lagrange's theorem, subgroup orders must divide 12. Armstrong finds subgroups of orders 1, 2, 3, 4, and 12, but proves no subgroup of order 6 exists.

# Relationships

## Builds Upon
- **Left coset** — The proof partitions $G$ into left cosets of $H$

## Enables
- **Euler's theorem** — Derived as a corollary via $R_n$
- **Fermat's little theorem** — Special case of Euler's theorem
- **Order of element divides group order** — Corollary (11.2)
- **Groups of prime order are cyclic** — Corollary (11.3)
- **Cauchy's theorem** — Provides partial converse for prime divisors

## Related
- **Index of a subgroup** — The number $|G|/|H|$

# Common Errors

- **Error**: Applying the converse — assuming every divisor of $|G|$ gives a subgroup order
  **Correction**: $A_4$ has order 12 but no subgroup of order 6. The converse holds only for prime divisors (Cauchy's theorem) and prime-power divisors (Sylow's theorems)

# Common Confusions

- **Confusion**: Thinking Lagrange's theorem applies to infinite groups
  **Clarification**: The theorem as stated requires $G$ to be finite. For infinite groups, the concept of index still applies but the divisibility statement does not

# Source Reference

Chapter 11: Lagrange's Theorem, pp. 64-67 (pdf). Theorem (11.1) with proof, Corollaries (11.2)-(11.4), and the analysis of $A_4$ subgroups.

# Verification Notes

- Definition source: Direct from Theorem (11.1), p. 64
- Proof: Explicitly given via coset partition argument
- Confidence rationale: HIGH — central theorem with explicit statement and proof
- Cross-references: All slugs verified against planned extractions
- Uncertainties: None
