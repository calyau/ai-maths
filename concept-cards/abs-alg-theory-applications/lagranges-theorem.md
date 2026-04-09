---
# === CORE IDENTIFICATION ===
concept: Lagrange's Theorem
slug: lagranges-theorem

# === CLASSIFICATION ===
category: group-structure
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Cosets and Lagrange's Theorem"
chapter_number: 6
pdf_page: 89
section: "6.2 Lagrange's Theorem"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - left-coset
  - index-of-a-subgroup
extends: []
related:
  - eulers-theorem
  - fermats-little-theorem
  - alternating-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is Lagrange's theorem?"
  - "How do cosets relate to Lagrange's theorem?"
  - "How do I apply Lagrange's theorem?"
---

# Quick Definition

Lagrange's Theorem states that the order of any subgroup of a finite group divides the order of the group. Equivalently, $|G| = [G:H] \cdot |H|$ for any subgroup $H$ of a finite group $G$.

# Core Definition

**Theorem 6.10 (Lagrange):** "Let $G$ be a finite group and let $H$ be a subgroup of $G$. Then $|G|/|H| = [G:H]$ is the number of distinct left cosets of $H$ in $G$. In particular, the number of elements in $H$ must divide the number of elements in $G$" (Judson, p. 89).

# Prerequisites

- **Left Coset** — The proof partitions $G$ into left cosets
- **Index of a Subgroup** — $[G:H] = |G|/|H|$

# Key Properties

1. $|H|$ divides $|G|$ for any subgroup $H$ of finite group $G$
2. The order of any element divides $|G|$ (Corollary 6.11)
3. A group of prime order $p$ is cyclic and isomorphic to $\mathbb{Z}_p$ (Corollary 6.12)
4. The converse is false: not every divisor of $|G|$ corresponds to a subgroup order
5. $[G:K] = [G:H][H:K]$ for $G \supset H \supset K$ (Corollary 6.13)

# Construction / Recognition

## To Apply Lagrange's Theorem:
1. Determine $|G|$
2. The possible orders of subgroups are the divisors of $|G|$
3. The order of any element must divide $|G|$
4. If $|G| = p$ (prime), the only subgroups are $\{e\}$ and $G$ itself

# Context & Application

Lagrange's Theorem is "one of the most important results in finite group theory" (Judson, p. 87). It constrains which subgroups can exist and is the foundation for Euler's and Fermat's theorems. However, its converse fails: $A_4$ has order 12 but no subgroup of order 6 (Proposition 6.15).

# Examples

**Example 1** (p. 89): If $|G| = p$ (prime), then $G$ is cyclic. Any non-identity element generates $G$ since its order must divide $p$ and be greater than 1, so it must equal $p$.

**Example 2** (p. 89): The converse fails: $A_4$ has order 12, and 6 divides 12, but $A_4$ has no subgroup of order 6 (Proposition 6.15).

# Relationships

## Builds Upon
- **Left Coset** — Proof uses partition into cosets
- **Index of a Subgroup** — $|G| = [G:H] \cdot |H|$

## Enables
- **Euler's Theorem** — Applies Lagrange to $U(n)$
- **Fermat's Little Theorem** — Special case of Euler's Theorem
- **Groups of Prime Order are Cyclic** — Direct corollary

## Related
- **Alternating Group** — $A_4$ provides a counterexample to the converse

# Common Errors

- **Error**: Assuming the converse of Lagrange's Theorem holds (that every divisor of $|G|$ gives a subgroup of that order)
  **Correction**: The converse is false; $A_4$ has order 12 but no subgroup of order 6

# Common Confusions

- **Confusion**: Thinking Lagrange's Theorem tells us subgroups exist for every divisor
  **Clarification**: It only restricts which orders are *possible*; it does not guarantee existence

# Source Reference

Chapter 6: Cosets and Lagrange's Theorem, Section 6.2, Theorem 6.10, Corollaries 6.11-6.13, pages 89-90.

# Verification Notes

- Definition source: Direct from Theorem 6.10, p. 89
- Confidence rationale: Major named theorem with explicit statement
- Uncertainties: None
- Cross-reference status: Verified
