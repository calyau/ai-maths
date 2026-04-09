---
# === CORE IDENTIFICATION ===
concept: "Poincare-Birkhoff-Witt Theorem"
slug: pbw-theorem

# === CLASSIFICATION ===
category: enveloping-algebras
subcategory: pbw-theorem
tier: advanced

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Representations of Lie Groups and Lie Algebras"
chapter_number: 4
pdf_page: 53
section: "4.9 Poincare-Birkhoff-Witt theorem"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "PBW theorem"
  - "PBW"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - universal-enveloping-algebra
  - filtered-algebra
extends: []
related:
  - graded-algebra
  - basis-of-enveloping-algebra
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the PBW theorem?"
  - "What is the structure of the universal enveloping algebra?"
---

# Quick Definition

The Poincare-Birkhoff-Witt (PBW) theorem states that ordered monomials $x_1^{k_1} \cdots x_n^{k_n}$ in any ordered basis of $\mathfrak{g}$ form a basis of $U\mathfrak{g}$, and that $\mathrm{Gr}\, U\mathfrak{g} \cong S\mathfrak{g}$ as graded algebras.

# Core Definition

**Theorem 4.60 (PBW)** (Kirillov, p. 53): Let $x_1, \ldots, x_n$ be an ordered basis of $\mathfrak{g}$. Then monomials of the form $x_1^{k_1} \cdots x_n^{k_n}$, $\sum k_i \leq p$, form a basis in $F^p U\mathfrak{g}$.

**Theorem 4.61** (coordinate-free form, p. 54): The graded algebra $\mathrm{Gr}\, U\mathfrak{g}$ is naturally isomorphic to the symmetric algebra $S\mathfrak{g}$.

# Prerequisites

- **Universal enveloping algebra** — The object whose structure is being described
- **Filtered algebra** — $U\mathfrak{g}$ is filtered, and PBW describes the associated graded

# Key Properties

1. Ordered monomials $x_1^{k_1} \cdots x_n^{k_n}$ form a basis of $U\mathfrak{g}$
2. $\mathrm{Gr}\, U\mathfrak{g} \cong S\mathfrak{g}$ (symmetric algebra)
3. The map $\mathfrak{g} \to U\mathfrak{g}$ is injective (Corollary 4.62)
4. If $\mathfrak{g} = \mathfrak{g}_1 \oplus \mathfrak{g}_2$ as vector spaces, then $U\mathfrak{g}_1 \otimes U\mathfrak{g}_2 \xrightarrow{\sim} U\mathfrak{g}$ (Corollary 4.63)
5. $U\mathfrak{g}$ has no zero divisors (Corollary 4.64)
6. The theorem would fail without the Jacobi identity

# Construction / Recognition

## Key Idea of Proof:
1. Proposition 4.57 shows ordered monomials span $F^p U\mathfrak{g}$
2. To show linear independence: construct a representation where the corresponding operators are independent
3. Take $V$ with basis given by ordered monomials, define $\rho(x_i)$ by left multiplication when $i \leq j_1$
4. The hard part: verify this is indeed a representation (uses Jacobi identity)

# Context & Application

PBW is fundamental for understanding the "size" of $U\mathfrak{g}$. It shows that as a vector space, $U\mathfrak{g}$ looks like a polynomial algebra (but with non-commutative multiplication). This is essential for constructing Verma modules and studying highest-weight representations.

# Examples

**Example** (p. 51): For commutative $\mathfrak{g}$, PBW reduces to the obvious fact that $U\mathfrak{g} = K[x_1, \ldots, x_n]$.

**Example**: For $\mathfrak{sl}(2,\mathbb{C})$ with ordered basis $\{e, f, h\}$, PBW says $\{e^a f^b h^c \mid a, b, c \geq 0\}$ is a basis of $U\mathfrak{sl}(2,\mathbb{C})$.

# Relationships

## Builds Upon
- **Universal enveloping algebra** — The object being analyzed
- **Filtered algebra** — $U\mathfrak{g}$ has a natural filtration

## Enables
- **Verma modules** — Use PBW to describe their structure
- **Injectivity of $\mathfrak{g} \to U\mathfrak{g}$** — A corollary of PBW

## Related
- **Graded algebra** — $\mathrm{Gr}\, U\mathfrak{g} \cong S\mathfrak{g}$

# Common Errors

- **Error**: Assuming $U\mathfrak{g}$ is graded (i.e., that degree is well-defined).
  **Correction**: $U\mathfrak{g}$ is only filtered, not graded. The relation $xy - yx = [x,y]$ mixes degrees ($\deg(xy) = 2$ but $\deg([x,y]) = 1$).

# Common Confusions

- **Confusion**: Thinking PBW means $U\mathfrak{g} \cong S\mathfrak{g}$ as algebras.
  **Clarification**: PBW says $\mathrm{Gr}\, U\mathfrak{g} \cong S\mathfrak{g}$. As algebras, $U\mathfrak{g}$ is non-commutative (for non-abelian $\mathfrak{g}$) while $S\mathfrak{g}$ is commutative. They are isomorphic only as vector spaces.

# Source Reference

Chapter 4, Section 4.9, Proposition 4.57, Theorems 4.60-4.61, Corollaries 4.62-4.64, pp. 52-54.

# Verification Notes

- Definition source: Direct from Theorems 4.60 and 4.61
- Confidence rationale: Explicit theorem (proof idea given, full proof referenced)
- Uncertainties: None
- Cross-reference status: Verified
