---
# === CORE IDENTIFICATION ===
concept: Positive Weyl Chamber
slug: positive-weyl-chamber

# === CLASSIFICATION ===
category: lie-algebras
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Appendix C - Root Systems and Simple Lie Algebras"
chapter_number: null
pdf_page: 123
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "C_+"
  - "dominant chamber"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - positive-roots
  - simple-roots
extends: []
related:
  - dominant-integral-weight
  - dominant-weights-set
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the positive Weyl chamber?"
---

# Quick Definition
The positive Weyl chamber $C_+$ is the open cone in $E = \mathfrak{h}_\mathbb{R}^*$ consisting of elements $\lambda$ with $\langle \lambda, \alpha_i^\vee \rangle > 0$ for all simple roots $\alpha_i$. Its closure intersected with the weight lattice gives the dominant weights $P_+$.

# Core Definition
(Kirillov, pp. 123-129): For each classical type, $C_+$ is described explicitly:
- $A_n$: $C_+ = \{\lambda_1 > \lambda_2 > \cdots > \lambda_{n+1}\}/\mathbb{R}(1, \ldots, 1)$
- $B_n$: $C_+ = \{\lambda_1 > \lambda_2 > \cdots > \lambda_n > 0\}$
- $C_n$: $C_+ = \{\lambda_1 > \lambda_2 > \cdots > \lambda_n > 0\}$
- $D_n$: $C_+ = \{\lambda_1 > \cdots > \lambda_n, \lambda_{n-1} + \lambda_n > 0\}$

# Prerequisites
- **Positive roots** -- the chamber is defined by positivity with respect to simple roots
- **Simple roots** -- the walls are hyperplanes $\langle \lambda, \alpha_i^\vee \rangle = 0$

# Key Properties
1. $C_+$ is an open convex cone
2. $P_+ = P \cap \overline{C_+}$ (dominant integral weights are lattice points in the closure)
3. The Weyl group acts simply transitively on the set of Weyl chambers
4. For $D_n$: the condition $\lambda_{n-1} + \lambda_n > 0$ (not $\lambda_n > 0$) reflects the fork

# Relationships
## Enables
- **Dominant integral weight** -- $P_+ = P \cap \overline{C_+}$

# Source Reference
Appendix C, pp. 123-129.

# Verification Notes
- Definition source: Synthesized from explicit descriptions for each type
- Confidence rationale: Explicit for each type
- Uncertainties: None
- Cross-reference status: Verified
