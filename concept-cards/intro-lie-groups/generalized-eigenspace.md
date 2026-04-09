---
# === CORE IDENTIFICATION ===
concept: Generalized Eigenspace
slug: generalized-eigenspace

# === CLASSIFICATION ===
category: lie-algebras
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Appendix B - Jordan Decomposition"
chapter_number: null
pdf_page: 120
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "V_(lambda)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - nilpotent-operator
extends: []
related:
  - jordan-decomposition
  - weight-space
contrasts_with:
  - weight-space

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a generalized eigenspace?"
  - "How does the generalized eigenspace decomposition work?"
---

# Quick Definition
The generalized eigenspace $V_{(\lambda)}$ of an operator $A$ with eigenvalue $\lambda$ consists of all vectors $v$ such that $(A - \lambda I)^n v = 0$ for some $n$. The restriction of $A - \lambda I$ to $V_{(\lambda)}$ is nilpotent.

# Core Definition
(Kirillov, p. 120): The generalized eigenspace with eigenvalue $\lambda$ is defined by the condition that the restriction of $A - \lambda \cdot \mathrm{id}$ to $V_{(\lambda)}$ is nilpotent. The space $V$ decomposes as $V = \bigoplus V_{(\lambda)}$ where $\lambda$ runs over the distinct eigenvalues of $A$.

# Prerequisites
- **Nilpotent operator** -- the restriction $A - \lambda I$ to $V_{(\lambda)}$ is nilpotent

# Key Properties
1. $V = \bigoplus V_{(\lambda)}$ (direct sum over eigenvalues)
2. $(A - \lambda I)|_{V_{(\lambda)}}$ is nilpotent
3. $\dim V_{(\lambda)}$ equals the algebraic multiplicity of $\lambda$
4. $V_{(\lambda)}$ contains the ordinary eigenspace $\ker(A - \lambda I)$
5. Each $V_{(\lambda)}$ is $A$-invariant

# Context & Application
The generalized eigenspace decomposition is the foundation for Jordan decomposition. It is also the motivation for the weight decomposition in representation theory: weight spaces are ordinary eigenspaces, while generalized weight spaces would be generalized eigenspaces. For semisimple Lie algebras acting on finite-dimensional representations, the generalized eigenspaces equal the ordinary eigenspaces (i.e., $\mathfrak{h}$ acts semisimply).

# Examples
**Example** (p. 120): For $A = \begin{pmatrix} \lambda & 1 \\ 0 & \lambda \end{pmatrix}$, the entire space $\mathbb{C}^2$ is the generalized eigenspace $V_{(\lambda)}$, while the ordinary eigenspace is one-dimensional.

# Relationships
## Enables
- **Jordan decomposition** -- constructed using generalized eigenspace decomposition

## Contrasts With
- **Weight space** -- an ordinary eigenspace; the generalized eigenspace is larger when the operator is not semisimple

# Source Reference
Appendix B: Jordan Decomposition, proof of Theorem B.2, p. 120.

# Verification Notes
- Definition source: From the proof of Theorem B.2
- Confidence rationale: Standard concept clearly used in the proof
- Uncertainties: None
- Cross-reference status: Verified
