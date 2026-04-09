---
# === CORE IDENTIFICATION ===
concept: Solvable Groups and Radical Extensions
slug: solvable-group-galois-connection

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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - solvable-by-radicals
  - galois-group
  - solvable-group
extends: []
related:
  - fundamental-theorem-of-galois-theory
  - insolvability-of-quintic
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does solvability by radicals connect to solvable groups?"
  - "Why are 'solvable' groups so named?"
---

# Quick Definition

A polynomial $f(x)$ over a field of characteristic 0 is solvable by radicals if and only if its Galois group is a solvable group. This is the deep connection Galois discovered between group theory and polynomial equations.

# Core Definition

**Theorem 23.30.** Let $f(x)$ be in $F[x]$, where $\text{char } F = 0$. If $f(x)$ is solvable by radicals, then the Galois group of $f(x)$ over $F$ is solvable (Judson, p. 319).

The converse also holds (stated without proof, p. 320).

The key ingredient is **Lemma 23.28**: the Galois group of $x^n - a$ over $F$ is solvable (p. 318). This is because the Galois group of a pure radical extension is abelian when $F$ contains the $n$th roots of unity.

# Prerequisites

- **Solvable by radicals** — The polynomial-theoretic concept
- **Galois group** — The Galois group determines solvability
- **Solvable group** — The group-theoretic concept (from Chapter 13)

# Key Properties

1. The Galois group of $x^n - a$ is always solvable (Lemma 23.28)
2. The subnormal series $\{id\} \subset G(E/F_{n-1}) \subset \cdots \subset G(E/F)$ has abelian factors
3. $S_n$ is solvable for $n \leq 4$ but not for $n \geq 5$
4. Therefore, every polynomial of degree $\leq 4$ is solvable by radicals

# Context & Application

This theorem explains why "solvable groups" are so named: they are precisely the groups that arise as Galois groups of polynomials that can be solved by radicals. The connection between polynomial solvability and group solvability is Galois's greatest achievement.

# Examples

**Example 1** (p. 319): The polynomial $x^5 - 6x^3 - 27x - 3$ has Galois group $S_5$, which is not solvable, so it is not solvable by radicals.

**Example 2**: The polynomial $x^4 - 2$ has Galois group $D_4$, which is solvable ($D_4 \supset \{1, \sigma^2\} \supset \{1\}$ with abelian quotients), so it is solvable by radicals.

# Relationships

## Builds Upon
- **Solvable by radicals** — One side of the equivalence
- **Solvable group** — The other side (from Chapter 13)
- **Galois group** — The bridge between the two

## Related
- **Insolvability of the quintic** — $S_5$ is not solvable
- **Fundamental Theorem of Galois Theory** — Underlies the proof

# Source Reference

Chapter 23: Galois Theory, Section 23.3, pages 317–320. See Lemma 23.28, Theorem 23.30.

# Verification Notes

- Definition source: Direct from Theorem 23.30, p. 319
- Confidence: HIGH — explicit theorem
- Cross-reference status: Verified against solvable groups from Ch. 13
- Uncertainties: None
