---
# === CORE IDENTIFICATION ===
concept: Root System of Type C_n
slug: root-system-type-c

# === CLASSIFICATION ===
category: classification
subcategory: type-c
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Appendix C - Root Systems and Simple Lie Algebras"
chapter_number: null
pdf_page: 126
section: "C.3 C_n = sp(n,C)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "C_n root system"
  - "root system of sp(n)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - root-system
extends: []
related:
  - simple-roots-type-c
  - dynkin-diagram-type-c
contrasts_with:
  - root-system-type-a
  - root-system-type-b
  - root-system-type-d

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the root system of type C_n?"
  - "What distinguishes the root systems of types A, B, C, D?"
---

# Quick Definition
The root system of type $C_n$ consists of all vectors $\pm e_i \pm e_j$ ($i \neq j$) and $\pm 2e_i$ in $\mathbb{R}^n$. It is the root system of $\mathfrak{sp}(n, \mathbb{C})$ and has two root lengths (short: $\pm e_i \pm e_j$; long: $\pm 2e_i$).

# Core Definition
(Kirillov, p. 126): For $\mathfrak{g} = \mathfrak{sp}(n, \mathbb{C})$:

$$R = \{\pm e_i \pm e_j \ (i \neq j), \pm 2e_i\}$$

with bilinear form $(e_i, e_j) = \frac{1}{2}\delta_{ij}$. Short roots $\pm e_i \pm e_j$ have $(\alpha, \alpha) = 1$, long roots $\pm 2e_i$ have $(\alpha, \alpha) = 2$ (normalized so long roots have length squared 2).

# Prerequisites
- **Root system** -- general theory

# Key Properties
1. $|R_+| = n^2$, same as $B_n$
2. Two root lengths: short $\pm e_i \pm e_j$ and long $\pm 2e_i$
3. $R_+ = \{e_i \pm e_j \ (i < j), 2e_i\}$
4. Highest root: $\theta = 2e_1 = (2, 0, \ldots, 0)$
5. $\rho = (n, n-1, \ldots, 1)$
6. Coxeter number: $h = 2n$, dual Coxeter number: $h^\vee = n + 1$
7. $C_n$ is dual to $B_n$: $C_n^\vee = B_n$

# Context & Application
Type $C_n$ corresponds to the symplectic group $\mathrm{Sp}(n)$. It is the "dual" of type $B_n$ in the sense that the roles of long and short roots are swapped. While $B_n$ has short roots $\pm e_i$ and long roots $\pm e_i \pm e_j$, type $C_n$ has short roots $\pm e_i \pm e_j$ and long roots $\pm 2e_i$.

# Examples
**Example** (p. 126): For $C_2 = \mathfrak{sp}(2, \mathbb{C}) \cong B_2 = \mathfrak{so}(5, \mathbb{C})$: the root systems $B_2$ and $C_2$ are isomorphic (this only happens for $n = 2$).

# Relationships
## Contrasts With
- **Root system type B** -- $B_n$ has short roots $\pm e_i$, long roots $\pm e_i \pm e_j$; $C_n$ swaps these roles
- **Root system type A** -- simply laced
- **Root system type D** -- no roots of the form $\pm 2e_i$ or $\pm e_i$

# Source Reference
Appendix C, Section C.3, pp. 126-127.

# Verification Notes
- Definition source: Direct from p. 126
- Confidence rationale: Fully explicit
- Uncertainties: None
- Cross-reference status: Verified
