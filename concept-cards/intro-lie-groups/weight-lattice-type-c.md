---
# === CORE IDENTIFICATION ===
concept: Weight and Root Lattices of Type C_n
slug: weight-lattice-type-c

# === CLASSIFICATION ===
category: classification
subcategory: type-c
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Appendix C - Root Systems and Simple Lie Algebras"
chapter_number: null
pdf_page: 127
section: "C.3 C_n = sp(n,C)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - root-system-type-c
  - weight-lattice
extends: []
related:
  - dominant-weights-set
contrasts_with:
  - weight-lattice-type-b

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the weight and root lattices of type C_n?"
---

# Quick Definition
For $C_n$, the weight lattice is $P = \mathbb{Z}^n$ and the root lattice is $Q = \{(\lambda_1, \ldots, \lambda_n) \mid \lambda_i \in \mathbb{Z}, \sum \lambda_i \in 2\mathbb{Z}\}$, with $P/Q \cong \mathbb{Z}_2$.

# Core Definition
(Kirillov, p. 127):

$$P = \mathbb{Z}^n$$

$$Q = \{(\lambda_1, \ldots, \lambda_n) \mid \lambda_i \in \mathbb{Z}, \sum \lambda_i \in 2\mathbb{Z}\}$$

$$P/Q \cong \mathbb{Z}_2$$

$P_+ = \{(\lambda_1, \ldots, \lambda_n) \mid \lambda_1 \geq \cdots \geq \lambda_n \geq 0, \lambda_i \in \mathbb{Z}\}$.

# Prerequisites
- **Root system type C** -- determines the lattices
- **Weight lattice** -- general concept

# Key Properties
1. $P = \mathbb{Z}^n$ -- all integer coordinates (simpler than $B_n$)
2. $Q$ requires the sum of coordinates to be even
3. $P/Q \cong \mathbb{Z}_2$
4. No half-integer weights (unlike $B_n$ and $D_n$)
5. $C_+ = \{\lambda_1 > \cdots > \lambda_n > 0\}$

# Context & Application
The weight lattice of $C_n$ is notably simpler than that of $B_n$ or $D_n$ -- it is just $\mathbb{Z}^n$. This reflects the fact that $\mathrm{Sp}(n)$ is simply connected, so all representations of the Lie algebra integrate to the group.

# Relationships
## Contrasts With
- **Weight lattice type B** -- $B_n$ has half-integer weights; $C_n$ does not

# Source Reference
Appendix C, Section C.3, p. 127.

# Verification Notes
- Definition source: Direct from p. 127
- Confidence rationale: Explicit formulas
- Uncertainties: None
- Cross-reference status: Verified
