---
# === CORE IDENTIFICATION ===
concept: Insolvability of the Quintic
slug: insolvability-of-quintic

# === CLASSIFICATION ===
category: galois-theory
subcategory: solvability
tier: advanced

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Galois Theory"
chapter_number: 23
pdf_page: 307
section: "23.3 Applications"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Abel-Ruffini theorem"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - solvable-by-radicals
  - galois-group
  - solvable-group
extends: []
related:
  - fundamental-theorem-of-galois-theory
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Why can't the general quintic be solved by radicals?"
  - "Can you give a specific polynomial that is not solvable by radicals?"
---

# Quick Definition

There exist fifth-degree polynomials that cannot be solved by radicals. This is proven by exhibiting a quintic whose Galois group is $S_5$, which is not a solvable group.

# Core Definition

The **insolvability of the quintic** states that there exist polynomials of degree 5 that are not solvable by radicals. The proof exhibits a specific polynomial $f(x) = x^5 - 6x^3 - 27x - 3 \in \mathbb{Q}[x]$ whose Galois group is $S_5$ (Example 23.33, Judson, p. 320). Since $S_5$ is not solvable (by Theorem 10.11), the polynomial cannot be solved by radicals (by Theorem 23.30).

# Prerequisites

- **Solvable by radicals** — Solvability by radicals is equivalent to having a solvable Galois group
- **Galois group** — The Galois group must be computed
- **Solvable group** — $S_5$ is not solvable because $A_5$ is simple and nonabelian

# Key Properties

1. $f(x) = x^5 - 6x^3 - 27x - 3$ is irreducible over $\mathbb{Q}$ (by Eisenstein's Criterion with $p = 3$)
2. $f(x)$ has exactly three real roots and two complex conjugate roots
3. The Galois group contains a transposition (complex conjugation) and a 5-cycle (since $[\mathbb{Q}(\alpha):\mathbb{Q}] = 5$ divides $|G|$)
4. Any subgroup of $S_5$ containing a transposition and a 5-cycle is all of $S_5$ (Lemma 23.31)
5. $S_5$ is not solvable since $A_5$ is the smallest nonabelian simple group

# Context & Application

This result resolves one of the oldest problems in algebra. For over 300 years, mathematicians sought a formula for the roots of the general quintic analogous to the quadratic formula. Ruffini (1799) and Abel (1826) proved no such formula exists. Galois (1831) gave the complete characterization of which polynomials are solvable.

The insolvability of the quintic connects back to solvable groups from Chapter 13 and the simplicity of $A_5$ from Chapter 10.

# Examples

**Example 1** (p. 320): $f(x) = x^5 - 6x^3 - 27x - 3$ is not solvable by radicals. It is irreducible, has exactly 3 real roots, and its Galois group is $S_5$.

# Relationships

## Builds Upon
- **Solvable by radicals** — The criterion for solvability
- **Galois group** — Must equal $S_5$ for this argument
- **Solvable group** — $S_5$ is not solvable

## Related
- **Fundamental Theorem of Galois Theory** — The theoretical foundation

# Common Confusions

- **Confusion**: Thinking no quintic equation can be solved
  **Clarification**: Many specific quintics are solvable (e.g., $x^5 = 32$). The theorem says no single formula works for all quintics, and some specific quintics have no radical solution.

# Source Reference

Chapter 23: Galois Theory, Section 23.3, pages 319–321. See Lemma 23.31, Example 23.33.

# Verification Notes

- Definition source: Direct from Example 23.33, p. 320
- Confidence: HIGH — explicit example with full argument
- Cross-reference status: Verified against solvable groups from Ch. 10 and 13
- Uncertainties: None
