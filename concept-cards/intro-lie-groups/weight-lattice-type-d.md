---
# === CORE IDENTIFICATION ===
concept: Weight and Root Lattices of Type D_n
slug: weight-lattice-type-d

# === CLASSIFICATION ===
category: classification
subcategory: type-d
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Appendix C - Root Systems and Simple Lie Algebras"
chapter_number: null
pdf_page: 128
section: "C.4 D_n = so(2n,C)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - root-system-type-d
  - weight-lattice
extends: []
related:
  - dominant-weights-set
contrasts_with:
  - weight-lattice-type-b

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the weight and root lattices of type D_n?"
---

# Quick Definition
For $D_n$, the weight lattice $P = \{(\lambda_1, \ldots, \lambda_n) \mid \lambda_i \in \frac{1}{2}\mathbb{Z}, \lambda_i - \lambda_j \in \mathbb{Z}\}$ and root lattice $Q = \{(\lambda_1, \ldots, \lambda_n) \mid \lambda_i \in \mathbb{Z}, \sum \lambda_i \in 2\mathbb{Z}\}$, with $P/Q \cong \mathbb{Z}_2 \times \mathbb{Z}_2$ (even $n$) or $\mathbb{Z}_4$ (odd $n$).

# Core Definition
(Kirillov, pp. 128-129):

$$P = \{(\lambda_1, \ldots, \lambda_n) \mid \lambda_i \in \tfrac{1}{2}\mathbb{Z}, \lambda_i - \lambda_j \in \mathbb{Z}\}$$

$$Q = \{(\lambda_1, \ldots, \lambda_n) \mid \lambda_i \in \mathbb{Z}, \sum \lambda_i \in 2\mathbb{Z}\}$$

$$P/Q \cong \begin{cases} \mathbb{Z}_2 \times \mathbb{Z}_2 & \text{for even } n \\ \mathbb{Z}_4 & \text{for odd } n \end{cases}$$

$P_+ = \{(\lambda_1, \ldots, \lambda_n) \mid \lambda_1 \geq \cdots \geq \lambda_n, \lambda_{n-1} + \lambda_n \geq 0, \lambda_i \in \frac{1}{2}\mathbb{Z}, \lambda_i - \lambda_j \in \mathbb{Z}\}$.

# Prerequisites
- **Root system type D** -- determines the lattices
- **Weight lattice** -- general concept

# Key Properties
1. Same weight lattice as $B_n$ (both have half-integer weights)
2. The root lattice requires even coordinate sum (more restrictive than $B_n$ where $Q = \mathbb{Z}^n$)
3. $P/Q$ depends on the parity of $n$
4. Dominance condition includes $\lambda_{n-1} + \lambda_n \geq 0$ (not just $\lambda_n \geq 0$), reflecting the fork
5. $C_+ = \{\lambda_1 > \cdots > \lambda_n, \lambda_{n-1} + \lambda_n > 0\}$

# Context & Application
The condition $\lambda_{n-1} + \lambda_n \geq 0$ (rather than $\lambda_n \geq 0$) for dominant weights reflects the fork in the Dynkin diagram. The last coordinate $\lambda_n$ can be negative as long as $\lambda_{n-1} + \lambda_n \geq 0$. This is related to the two types of spinor representations of $\mathrm{so}(2n)$.

# Examples
**Example** (pp. 128-129): For $D_4$: $P/Q \cong \mathbb{Z}_2 \times \mathbb{Z}_2$ (even $n = 4$). The three non-trivial cosets correspond to the vector representation and the two half-spin representations.

# Relationships
## Contrasts With
- **Weight lattice type B** -- same $P$ but different $Q$ ($\mathbb{Z}^n$ for $B_n$ vs. even-sum lattice for $D_n$)

# Source Reference
Appendix C, Section C.4, pp. 128-129.

# Verification Notes
- Definition source: Direct from pp. 128-129
- Confidence rationale: Explicit formulas
- Uncertainties: None
- Cross-reference status: Verified
