---
# === CORE IDENTIFICATION ===
concept: Root System of Type B_n
slug: root-system-type-b

# === CLASSIFICATION ===
category: classification
subcategory: type-b
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Appendix C - Root Systems and Simple Lie Algebras"
chapter_number: null
pdf_page: 124
section: "C.2 B_n = so(2n+1,C)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "B_n root system"
  - "root system of so(2n+1)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - root-system
extends: []
related:
  - cartan-subalgebra-type-b
  - simple-roots-type-b
  - dynkin-diagram-type-b
contrasts_with:
  - root-system-type-a
  - root-system-type-c
  - root-system-type-d

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the root system of type B_n?"
  - "What distinguishes the root systems of types A, B, C, D?"
---

# Quick Definition
The root system of type $B_n$ consists of all vectors $\pm e_i \pm e_j$ ($i \neq j$) and $\pm e_i$ in $\mathbb{R}^n$. It is the root system of $\mathfrak{so}(2n+1, \mathbb{C})$ and has roots of two different lengths (long: $\pm e_i \pm e_j$; short: $\pm e_i$).

# Core Definition
(Kirillov, p. 124-125): For $\mathfrak{g} = \mathfrak{so}(2n+1, \mathbb{C})$:

$$R = \{\pm e_i \pm e_j \ (i \neq j), \pm e_i\}$$

with bilinear form $(e_i, e_j) = \delta_{ij}$. Long roots have $(\alpha, \alpha) = 2$, short roots have $(\alpha, \alpha) = 1$.

# Prerequisites
- **Root system** -- general theory

# Key Properties
1. $|R_+| = n^2$, $|R| = 2n^2$
2. Two root lengths: long roots $\pm e_i \pm e_j$ with $(\alpha, \alpha) = 2$, short roots $\pm e_i$ with $(\alpha, \alpha) = 1$
3. Positive roots: $R_+ = \{e_i \pm e_j \ (i < j), e_i\}$
4. Root subspaces and coroots are explicitly given for each root type (p. 124-125)
5. Highest root: $\theta = e_1 + e_2 = (1, 1, 0, \ldots, 0)$
6. $\rho = (n - \frac{1}{2}, n - \frac{3}{2}, \ldots, \frac{1}{2})$
7. Coxeter number: $h = 2n$, dual Coxeter number: $h^\vee = 2n - 1$

# Context & Application
Type $B_n$ corresponds to the odd orthogonal group $\mathrm{SO}(2n+1)$. Unlike type A, it is not simply laced -- it has both long and short roots. The presence of short roots $\pm e_i$ distinguishes it from type D (which has only roots $\pm e_i \pm e_j$). Compared to type C, the roles of long and short roots are swapped.

# Examples
**Example** (p. 124): For $B_2 = \mathfrak{so}(5, \mathbb{C})$: $R = \{\pm e_1 \pm e_2, \pm e_1, \pm e_2\}$, 8 roots total, with 4 positive roots.

# Relationships
## Contrasts With
- **Root system type A** -- simply laced (one root length); B has two lengths
- **Root system type C** -- also has two lengths, but long roots are $\pm 2e_i$ (vs short $\pm e_i$ in B)
- **Root system type D** -- no short roots $\pm e_i$; only $\pm e_i \pm e_j$

# Source Reference
Appendix C, Section C.2, pp. 124-125.

# Verification Notes
- Definition source: Direct from pp. 124-125
- Confidence rationale: Fully explicit
- Uncertainties: None
- Cross-reference status: Verified
