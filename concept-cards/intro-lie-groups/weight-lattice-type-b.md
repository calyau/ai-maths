---
# === CORE IDENTIFICATION ===
concept: Weight and Root Lattices of Type B_n
slug: weight-lattice-type-b

# === CLASSIFICATION ===
category: classification
subcategory: type-b
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Appendix C - Root Systems and Simple Lie Algebras"
chapter_number: null
pdf_page: 125
section: "C.2 B_n = so(2n+1,C)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - root-system-type-b
  - weight-lattice
extends: []
related:
  - dominant-weights-set
contrasts_with:
  - weight-lattice-type-a
  - weight-lattice-type-d

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the weight and root lattices of type B_n?"
---

# Quick Definition
For $B_n$, the weight lattice is $P = \{(\lambda_1, \ldots, \lambda_n) \mid \lambda_i \in \frac{1}{2}\mathbb{Z}, \lambda_i - \lambda_j \in \mathbb{Z}\}$ (integer or all half-integer coordinates), and the root lattice is $Q = \mathbb{Z}^n$, with $P/Q \cong \mathbb{Z}_2$.

# Core Definition
(Kirillov, p. 125):

$$P = \{(\lambda_1, \ldots, \lambda_n) \mid \lambda_i \in \tfrac{1}{2}\mathbb{Z}, \lambda_i - \lambda_j \in \mathbb{Z}\}$$

$$Q = \mathbb{Z}^n$$

$$P/Q \cong \mathbb{Z}_2$$

Dominant weights: $P_+ = \{(\lambda_1, \ldots, \lambda_n) \mid \lambda_1 \geq \cdots \geq \lambda_n \geq 0, \lambda_i \in \frac{1}{2}\mathbb{Z}, \lambda_i - \lambda_j \in \mathbb{Z}\}$.

# Prerequisites
- **Root system type B** -- determines the lattices
- **Weight lattice** -- general concept

# Key Properties
1. $P/Q \cong \mathbb{Z}_2$ -- the weight lattice is an index-2 extension of the root lattice
2. Weights can be all integers or all half-integers (but not mixed)
3. The half-integer weights correspond to spinor representations
4. $C_+ = \{\lambda_1 > \lambda_2 > \cdots > \lambda_n > 0\}$

# Context & Application
The existence of half-integer weights in $B_n$ reflects the fact that $\mathrm{Spin}(2n+1) \to \mathrm{SO}(2n+1)$ is a double cover. The half-integer weights correspond to representations that do not descend to $\mathrm{SO}(2n+1)$ but are genuine representations of $\mathrm{Spin}(2n+1)$.

# Examples
**Example** (p. 125): For $B_1 = A_1$: $P = \frac{1}{2}\mathbb{Z}$, $Q = \mathbb{Z}$.

# Source Reference
Appendix C, Section C.2, p. 125.

# Verification Notes
- Definition source: Direct from p. 125
- Confidence rationale: Explicit formulas
- Uncertainties: None
- Cross-reference status: Verified
