---
# === CORE IDENTIFICATION ===
concept: Root System of Type A_n
slug: root-system-type-a

# === CLASSIFICATION ===
category: classification
subcategory: type-a
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Appendix C - Root Systems and Simple Lie Algebras"
chapter_number: null
pdf_page: 123
section: "C.1 A_n = sl(n+1,C)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "A_n root system"
  - "root system of sl(n+1)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - root-system
  - root-decomposition
extends: []
related:
  - cartan-subalgebra-type-a
  - simple-roots-type-a
  - dynkin-diagram-type-a
contrasts_with:
  - root-system-type-b
  - root-system-type-c
  - root-system-type-d

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the root system of type A_n?"
  - "What distinguishes the root systems of types A, B, C, D?"
---

# Quick Definition
The root system of type $A_n$ consists of all vectors $e_i - e_j$ ($i \neq j$) in the quotient space $\bigoplus \mathbb{R}e_i / \mathbb{R}(e_1 + \cdots + e_{n+1})$. It is the root system of $\mathfrak{sl}(n+1, \mathbb{C})$ and has $n(n+1)$ roots.

# Core Definition
(Kirillov, p. 123): For $\mathfrak{g} = \mathfrak{sl}(n+1, \mathbb{C})$ with Cartan subalgebra $\mathfrak{h} = \{\text{diagonal matrices with trace } 0\}$:

$$R = \{e_i - e_j \mid i \neq j\}$$

where $e_i \in \mathfrak{h}^*$ extracts the $i$-th diagonal entry. The inner product is $(\lambda, \mu) = \sum \lambda_i \mu_i$ when representatives satisfy $\sum \lambda_i = \sum \mu_i = 0$. All roots have the same length (simply laced), normalized so $(\alpha, \alpha) = 2$.

# Prerequisites
- **Root system** -- general theory
- **Root decomposition** -- the root system arises from the root decomposition

# Key Properties
1. $|R| = n(n+1)$, $|R_+| = \frac{n(n+1)}{2}$
2. All roots have the same length: $(\alpha, \alpha) = 2$ (simply laced)
3. Root subspace: $\mathfrak{g}_{e_i - e_j} = \mathbb{C}E_{ij}$ (matrix units)
4. Coroot: $h_{e_i - e_j} = E_{ii} - E_{jj}$
5. The ambient space $E = \mathfrak{h}_\mathbb{R}^*$ has dimension $n$
6. Highest root: $\theta = e_1 - e_{n+1}$
7. $\rho = (n, n-1, \ldots, 1, 0)$
8. Coxeter number: $h = h^\vee = n + 1$

# Construction / Recognition
1. Start with $\mathfrak{sl}(n+1, \mathbb{C})$ and diagonal Cartan subalgebra
2. Compute the adjoint action on each matrix unit $E_{ij}$ ($i \neq j$)
3. $[H, E_{ij}] = (h_i - h_j)E_{ij}$ for $H = \mathrm{diag}(h_1, \ldots, h_{n+1})$
4. Read off roots as $e_i - e_j$

# Context & Application
Type $A_n$ is the most fundamental root system, corresponding to the special linear group $\mathrm{SL}(n+1)$. Its representation theory connects to symmetric group representations via Schur-Weyl duality. The key distinguishing feature of type A is that it is simply laced (all roots equal length) and its Weyl group is the symmetric group $S_{n+1}$.

# Examples
**Example** (p. 123): For $A_1 = \mathfrak{sl}(2, \mathbb{C})$: $R = \{\alpha, -\alpha\}$ where $\alpha = e_1 - e_2$.

**Example** (p. 123): For $A_2 = \mathfrak{sl}(3, \mathbb{C})$: $R = \{\pm(e_1 - e_2), \pm(e_2 - e_3), \pm(e_1 - e_3)\}$, six roots.

# Relationships
## Builds Upon
- **Root system** -- $A_n$ is a specific root system

## Enables
- **Simple roots type A** -- $\alpha_i = e_i - e_{i+1}$
- **Representations of sl(n,C)** -- built on this root system

## Contrasts With
- **Root system type B** -- has two root lengths ($\pm e_i \pm e_j$ and $\pm e_i$)
- **Root system type C** -- has two root lengths ($\pm e_i \pm e_j$ and $\pm 2e_i$)
- **Root system type D** -- simply laced like A, but only $\pm e_i \pm e_j$ (no short roots)

# Source Reference
Appendix C, Section C.1, p. 123.

# Verification Notes
- Definition source: Direct from p. 123
- Confidence rationale: Fully explicit description
- Uncertainties: None
- Cross-reference status: Verified
