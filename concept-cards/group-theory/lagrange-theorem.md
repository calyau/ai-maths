---
# === CORE IDENTIFICATION ===
concept: Lagrange's Theorem
slug: lagrange-theorem

# === CLASSIFICATION ===
category: subgroup-theory
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Basic Definitions and Results"
chapter_number: 1
pdf_page: 17
section: "Cosets"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - left-coset
  - index-of-subgroup
extends: []
related:
  - normal-subgroup
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Why must the order of a subgroup divide the order of a finite group?"
  - "Does every divisor of the group order correspond to a subgroup?"
---

# Quick Definition

If $G$ is a finite group and $H$ is a subgroup, then $|G| = (G : H) \cdot |H|$. In particular, both $|H|$ and $(G : H)$ divide $|G|$.

# Core Definition

"If $G$ is finite, then $(G:1) = (G:H)(H:1)$. In particular, the order of every subgroup of a finite group divides the order of the group." (Milne, Theorem 1.26, p. 17)

# Prerequisites

- **Left coset** — The proof uses the coset partition
- **Index of a subgroup** — Lagrange's theorem relates index to orders

# Key Properties

1. $|H|$ divides $|G|$ for any subgroup $H$ of finite $G$
2. The order of every element divides $|G|$ (Corollary 1.27)
3. Multiplicativity: $(G : K) = (G : H)(H : K)$ for $H \supset K$ (Proposition 1.31)
4. Partial converse: if prime $p$ divides $|G|$, then $G$ has an element of order $p$ (Cauchy's theorem, 4.13)
5. The converse fails: not every divisor of $|G|$ gives a subgroup (e.g., $A_4$ has no subgroup of order 6)

# Construction / Recognition

## Proof Idea:
1. The left cosets of $H$ partition $G$
2. There are $(G:H)$ cosets
3. Each coset has $|H|$ elements
4. Therefore $|G| = (G:H) \cdot |H|$

# Context & Application

Lagrange's theorem is one of the most fundamental results in finite group theory. It immediately implies that any group of prime order $p$ is cyclic ($\cong C_p$), since the only subgroups have order 1 or $p$.

# Examples

**Example 1** (p. 17): If $|G| = p$ (prime), then every non-identity element has order $p$, so $G$ is cyclic. Hence $G \approx C_p$ (Example 1.28).

**Example 2** (p. 18): The 4-group $C_2 \times C_2$ has order 4 but no element of order 4 — the converse of Lagrange fails.

# Relationships

## Builds Upon
- **left-coset** — cosets partition $G$
- **index-of-subgroup** — the number of cosets

## Enables
- Recognition that groups of prime order are cyclic

## Related
- **normal-subgroup** — subgroups of index 2 are normal

# Common Errors

- **Error**: Assuming the converse: "if $d$ divides $|G|$, then $G$ has a subgroup of order $d$"
  **Correction**: This is false in general ($A_4$ has order 12 but no subgroup of order 6). Partial converses exist (Cauchy, Sylow)

# Source Reference

Chapter 1, Theorem 1.26, Corollary 1.27, Proposition 1.31, pages 17-18.

# Verification Notes

- Definition source: Direct from Theorem 1.26
- Confidence: HIGH — explicit theorem with proof
- Uncertainties: None
