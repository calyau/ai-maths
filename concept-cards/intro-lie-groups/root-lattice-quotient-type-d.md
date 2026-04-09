---
# === CORE IDENTIFICATION ===
concept: Root Lattice Quotient P/Q for Type D_n
slug: root-lattice-quotient-type-d

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
  - weight-lattice-type-d
extends: []
related:
  - root-lattice-quotient-type-b
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is P/Q for type D_n?"
  - "Why does P/Q depend on the parity of n for type D?"
---

# Quick Definition
For type $D_n$, the quotient $P/Q$ depends on the parity of $n$: $P/Q \cong \mathbb{Z}_2 \times \mathbb{Z}_2$ for even $n$, and $P/Q \cong \mathbb{Z}_4$ for odd $n$.

# Core Definition
(Kirillov, p. 128):

$$P/Q \cong \begin{cases} \mathbb{Z}_2 \times \mathbb{Z}_2 & n \text{ even} \\ \mathbb{Z}_4 & n \text{ odd} \end{cases}$$

# Prerequisites
- **Weight lattice type D** -- provides $P$ and $Q$

# Key Properties
1. $|P/Q| = 4$ in both cases
2. For even $n$: the four cosets correspond to vector representation, two half-spin representations, and the root lattice itself
3. For odd $n$: the cosets form a cyclic group
4. This reflects the structure of the center of $\mathrm{Spin}(2n)$

# Context & Application
The parity-dependent structure of $P/Q$ for $D_n$ is unique among classical types. It reflects the more complex topology of $\mathrm{SO}(2n)$ compared to $\mathrm{SO}(2n+1)$: the fundamental group of $\mathrm{SO}(2n)/\mathrm{center}$ depends on the parity of $n$.

# Source Reference
Appendix C, Section C.4, p. 128.

# Verification Notes
- Definition source: Direct from p. 128
- Confidence rationale: Explicit
- Uncertainties: None
- Cross-reference status: Verified
