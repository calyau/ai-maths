---
# === CORE IDENTIFICATION ===
concept: Coroots of Type A_n
slug: coroot-type-a

# === CLASSIFICATION ===
category: classification
subcategory: type-a
tier: intermediate

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
  - "h_alpha for type A"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - root-system-type-a
  - coroot
extends: []
related:
  - cartan-subalgebra-type-a
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the coroots of type A_n?"
---

# Quick Definition
For type $A_n$, the coroot corresponding to $\alpha = e_i - e_j$ is $h_\alpha = \alpha^\vee = E_{ii} - E_{jj} \in \mathfrak{h}$, where $E_{ii}$ are diagonal matrix units.

# Core Definition
(Kirillov, p. 123): Root subspace corresponding to root $\alpha = e_i - e_j$ is $\mathfrak{g}_\alpha = \mathbb{C}E_{ij}$, and the corresponding coroot $h_\alpha = \alpha^\vee \in \mathfrak{h}$ is $h_\alpha = E_{ii} - E_{jj}$.

# Prerequisites
- **Root system type A** -- the roots
- **Coroot** -- general concept

# Key Properties
1. $h_{e_i - e_j} = E_{ii} - E_{jj}$
2. Since $A_n$ is simply laced, $\alpha^\vee = \alpha$ under the identification $\mathfrak{h}^* \cong \mathfrak{h}$ via the bilinear form
3. $\langle e_k, h_{e_i - e_j} \rangle = \delta_{ki} - \delta_{kj}$

# Examples
**Example** (p. 123): For $A_2$: simple coroots are $h_{\alpha_1} = E_{11} - E_{22}$ and $h_{\alpha_2} = E_{22} - E_{33}$.

# Source Reference
Appendix C, Section C.1, p. 123.

# Verification Notes
- Definition source: Direct from p. 123
- Confidence rationale: Explicit
- Uncertainties: None
- Cross-reference status: Verified
