---
# === CORE IDENTIFICATION ===
concept: Solvable by Radicals
slug: solvable-by-radicals

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
  - "solvability by radicals"
  - "solution by radicals"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - extension-by-radicals
  - splitting-field
  - galois-group
extends: []
related:
  - solvable-group
  - insolvability-of-quintic
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does it mean for a polynomial to be solvable by radicals?"
  - "How does solvability by radicals relate to the Galois group?"
---

# Quick Definition

A polynomial $f(x)$ is solvable by radicals over $F$ if its splitting field $K$ is contained in an extension of $F$ by radicals. Equivalently (in characteristic 0), $f(x)$ is solvable by radicals if and only if its Galois group is a solvable group.

# Core Definition

A polynomial $f(x)$ is **solvable by radicals** over $F$ if the splitting field $K$ of $f(x)$ over $F$ is contained in an extension of $F$ by radicals (Judson, p. 317).

**Theorem 23.30:** If $f(x)$ is solvable by radicals (and $\text{char } F = 0$), then the Galois group of $f(x)$ over $F$ is solvable (p. 319). The converse also holds.

# Prerequisites

- **Extension by radicals** — Solvability means the splitting field lies inside a radical extension
- **Splitting field** — The splitting field must be contained in the radical extension
- **Galois group** — Solvability is determined by the Galois group

# Key Properties

1. $f(x)$ is solvable by radicals if and only if its Galois group is a solvable group (Theorem 23.30 + converse)
2. Every polynomial of degree $\leq 4$ is solvable by radicals (since $S_n$ is solvable for $n \leq 4$)
3. The general polynomial of degree $\geq 5$ is not solvable by radicals (since $S_5$ is not solvable)
4. Specific polynomials of degree $\geq 5$ may still be solvable (e.g., $x^5 - 1$)
5. The Galois group of $x^n - a$ is always solvable (Lemma 23.28)

# Context & Application

This is the culmination of the text: the deep connection between solvability of polynomial equations (an ancient problem) and the solvability of the Galois group (a group-theoretic property). Galois discovered this connection, resolving a 300-year-old question about the solvability of the quintic.

# Examples

**Example 1** (p. 317): The quadratic $ax^2 + bx + c$ is solvable by radicals via $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$.

**Example 2** (p. 317): $x^n - 1$ is always solvable by radicals; its roots are the $n$th roots of unity.

# Relationships

## Builds Upon
- **Extension by radicals** — Defines what "solvable by radicals" means
- **Galois group** — Determines solvability
- **Solvable group** — The group-theoretic condition

## Enables
- **Insolvability of the quintic** — Specific quintics have Galois group $S_5$, which is not solvable

# Common Confusions

- **Confusion**: Thinking no degree-5 polynomial is solvable by radicals
  **Clarification**: Many quintics are solvable (e.g., $x^5 - 1$). The theorem says the general quintic is not, and specific quintics with Galois group $S_5$ are not.

# Source Reference

Chapter 23: Galois Theory, Section 23.3, pages 317–320. See Lemma 23.28, Theorem 23.30.

# Verification Notes

- Definition source: Direct from p. 317
- Confidence: HIGH — explicit definition and main theorem
- Cross-reference status: Verified
- Uncertainties: None
