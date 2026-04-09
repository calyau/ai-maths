---
# === CORE IDENTIFICATION ===
concept: Minimal Polynomial
slug: minimal-polynomial

# === CLASSIFICATION ===
category: field-theory
subcategory: field-extensions
tier: advanced

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Fields"
chapter_number: 21
pdf_page: 274
section: "21.1 Extension Fields"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "irreducible polynomial of alpha"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - algebraic-element
  - irreducible-polynomial
extends: []
related:
  - degree-of-field-extension
  - simple-extension
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the minimal polynomial of an algebraic element?"
  - "How does the minimal polynomial determine a field extension?"
---

# Quick Definition

The minimal polynomial of an algebraic element $\alpha$ over $F$ is the unique monic irreducible polynomial $p(x) \in F[x]$ of smallest degree such that $p(\alpha) = 0$. Its degree equals $[F(\alpha):F]$.

# Core Definition

Let $E$ be an extension field of $F$ and $\alpha \in E$ be algebraic over $F$. The unique monic polynomial $p(x)$ of smallest degree such that $p(\alpha) = 0$ is called the **minimal polynomial** for $\alpha$ over $F$. The degree of $p(x)$ is the **degree of $\alpha$ over $F$** (Judson, p. 277).

By Theorem 21.10, this polynomial is irreducible, and if $f(x)$ is any other polynomial with $f(\alpha) = 0$, then $p(x)$ divides $f(x)$.

# Prerequisites

- **Algebraic element** — Only algebraic elements have minimal polynomials
- **Irreducible polynomial** — The minimal polynomial is always irreducible

# Key Properties

1. The minimal polynomial is unique, monic, and irreducible (Theorem 21.10)
2. It divides every polynomial that has $\alpha$ as a root
3. $F(\alpha) \cong F[x]/\langle p(x) \rangle$ (Proposition 21.12)
4. $[F(\alpha):F] = \deg p(x)$ (Theorem 21.13)
5. $\{1, \alpha, \alpha^2, \ldots, \alpha^{n-1}\}$ is a basis for $F(\alpha)$ over $F$ where $n = \deg p(x)$

# Construction / Recognition

## To Find:
1. Compute the kernel of the evaluation homomorphism $\phi_\alpha: F[x] \to E$
2. The generator of this kernel (made monic) is the minimal polynomial
3. Alternatively, find the monic polynomial of smallest degree in $F[x]$ having $\alpha$ as a root

# Context & Application

The minimal polynomial is the key tool for understanding simple algebraic extensions. It determines the degree of the extension, provides a basis, and controls the arithmetic in $F(\alpha)$.

# Examples

**Example 1** (p. 277): The minimal polynomial of $\sqrt{2}$ over $\mathbb{Q}$ is $x^2 - 2$.

**Example 2** (p. 277): The minimal polynomial of $\sqrt{2 + \sqrt{3}}$ over $\mathbb{Q}$ is $x^4 - 4x^2 + 1$.

**Example 3** (p. 278): The minimal polynomial of $i$ over $\mathbb{R}$ is $x^2 + 1$, giving $\mathbb{R}(i) = \mathbb{C}$.

# Relationships

## Builds Upon
- **Algebraic element** — Minimal polynomials exist only for algebraic elements
- **Irreducible polynomial** — The minimal polynomial is irreducible

## Enables
- **Degree of field extension** — $[F(\alpha):F] = \deg p(x)$
- **Simple extension** — The structure of $F(\alpha)$ is determined by the minimal polynomial

## Related
- **Conjugate elements** — Elements sharing the same minimal polynomial

# Common Errors

- **Error**: Finding a polynomial with $\alpha$ as a root and assuming it is the minimal polynomial
  **Correction**: The minimal polynomial is the one of smallest degree; larger-degree polynomials with $\alpha$ as a root are multiples of it

# Common Confusions

- **Confusion**: Thinking the minimal polynomial depends on the extension field $E$
  **Clarification**: The minimal polynomial depends only on $\alpha$ and the base field $F$, not on which extension $E$ contains $\alpha$

# Source Reference

Chapter 21: Fields, Section 21.1, pages 277–278. See Theorem 21.10, Proposition 21.12, Theorem 21.13.

# Verification Notes

- Definition source: Direct from p. 277
- Confidence: HIGH — explicit definition with theorems
- Cross-reference status: Verified
- Uncertainties: None
