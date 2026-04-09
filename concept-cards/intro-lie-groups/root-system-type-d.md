---
# === CORE IDENTIFICATION ===
concept: Root System of Type D_n
slug: root-system-type-d

# === CLASSIFICATION ===
category: classification
subcategory: type-d
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Appendix C - Root Systems and Simple Lie Algebras"
chapter_number: null
pdf_page: 127
section: "C.4 D_n = so(2n,C)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "D_n root system"
  - "root system of so(2n)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - root-system
extends: []
related:
  - simple-roots-type-d
  - dynkin-diagram-type-d
contrasts_with:
  - root-system-type-a
  - root-system-type-b
  - root-system-type-c

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the root system of type D_n?"
  - "What distinguishes the root systems of types A, B, C, D?"
---

# Quick Definition
The root system of type $D_n$ consists of all vectors $\pm e_i \pm e_j$ ($i \neq j$) in $\mathbb{R}^n$. It is the root system of $\mathfrak{so}(2n, \mathbb{C})$, is simply laced (all roots have equal length), and has $2n(n-1)$ roots. Unlike $B_n$, there are no roots of the form $\pm e_i$.

# Core Definition
(Kirillov, p. 127-128): For $\mathfrak{g} = \mathfrak{so}(2n, \mathbb{C})$:

$$R = \{\pm e_i \pm e_j \mid i \neq j\}$$

with bilinear form $(e_i, e_j) = \delta_{ij}$. All roots have $(\alpha, \alpha) = 2$ (simply laced).

# Prerequisites
- **Root system** -- general theory

# Key Properties
1. $|R_+| = n(n-1)$, $|R| = 2n(n-1)$
2. Simply laced: all roots have equal length
3. $R_+ = \{e_i \pm e_j \mid i < j\}$
4. No roots of the form $\pm e_i$ (unlike $B_n$) or $\pm 2e_i$ (unlike $C_n$)
5. Highest root: $\theta = e_1 + e_2 = (1, 1, 0, \ldots, 0)$ (same as $B_n$)
6. $\rho = (n-1, n-2, \ldots, 0)$
7. Coxeter number: $h = h^\vee = 2n - 2$
8. Requires $n \geq 3$ (for $n \leq 2$, $D_n$ degenerates: $D_2 \cong A_1 \times A_1$, $D_3 \cong A_3$)

# Context & Application
Type $D_n$ corresponds to the even orthogonal group $\mathrm{SO}(2n)$. The key distinction from $B_n$ is the absence of short roots: $D_n$ is simply laced while $B_n$ is not. The branching at the end of the Dynkin diagram (two nodes at the fork) gives $D_n$ a richer structure, including the triality automorphism for $D_4$.

# Examples
**Example** (p. 127): For $D_3 \cong A_3$: the root system $\{\pm e_i \pm e_j\}$ in $\mathbb{R}^3$ is isomorphic to the $A_3$ root system.

# Relationships
## Contrasts With
- **Root system type B** -- $B_n$ has additional short roots $\pm e_i$; $D_n$ is simply laced
- **Root system type C** -- $C_n$ has additional long roots $\pm 2e_i$
- **Root system type A** -- both simply laced, but different combinatorial structure

# Source Reference
Appendix C, Section C.4, pp. 127-129.

# Verification Notes
- Definition source: Direct from pp. 127-128
- Confidence rationale: Fully explicit
- Uncertainties: None
- Cross-reference status: Verified
