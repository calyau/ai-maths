---
# === CORE IDENTIFICATION ===
concept: Weight Space
slug: weight-space

# === CLASSIFICATION ===
category: representations
subcategory: highest-weight-theory
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Representations of Semisimple Lie Algebras"
chapter_number: 9
pdf_page: 110
section: "9.1 Weight decomposition"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "V[lambda]"
  - "eigenspace for weight lambda"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - weight-of-representation
  - cartan-subalgebra
extends: []
related:
  - weight-decomposition-theorem
  - weight-set
contrasts_with:
  - root-space

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a weight space?"
  - "What is the notation V[lambda]?"
---

# Quick Definition
The weight space $V[\lambda]$ is the subspace of a representation $V$ consisting of all vectors on which every element $h \in \mathfrak{h}$ acts by the scalar $\langle \lambda, h \rangle$. It is the simultaneous eigenspace for the Cartan subalgebra corresponding to the weight $\lambda$.

# Core Definition
**Definition 9.1** (Kirillov, p. 110): The space of all vectors of weight $\lambda$ is called the *weight space* and denoted $V[\lambda]$:

$$V[\lambda] = \{ v \in V \mid hv = \langle \lambda, h \rangle v \ \forall h \in \mathfrak{h} \}.$$

# Prerequisites
- **Weight of a representation** -- the weight space is the eigenspace corresponding to a weight
- **Cartan subalgebra** -- the simultaneous diagonalization is with respect to $\mathfrak{h}$

# Key Properties
1. $V[\lambda]$ is a vector subspace of $V$
2. $V[\lambda]$ is finite-dimensional when $V$ is finite-dimensional
3. Weight spaces for distinct weights have trivial intersection
4. Root vectors map between weight spaces: if $x \in \mathfrak{g}_\alpha$, then $x \cdot V[\lambda] \subset V[\lambda + \alpha]$ (Lemma 9.3)
5. $\dim V[\lambda] = 1$ for the highest weight of an irreducible representation

# Construction / Recognition
1. Fix a Cartan subalgebra $\mathfrak{h}$ and a weight $\lambda \in \mathfrak{h}^*$
2. The weight space is the joint kernel of operators $h - \langle \lambda, h \rangle \cdot \mathrm{id}$ for all $h \in \mathfrak{h}$
3. In practice, choose a basis $h_1, \ldots, h_r$ for $\mathfrak{h}$ and solve the simultaneous eigenvalue equations

# Context & Application
Weight spaces are the building blocks of the weight decomposition of representations. The dimension of a weight space is the *multiplicity* of that weight. Understanding weight multiplicities is central to representation theory; the Weyl character formula provides a tool for computing them.

# Examples
**Example** (p. 110): For $\mathfrak{sl}(2, \mathbb{C})$, the weight spaces are the eigenspaces of $h$, so $V[\lambda] = \{v \mid hv = \lambda v\}$ for $\lambda \in \mathbb{C}$.

# Relationships
## Builds Upon
- **Weight of a representation** -- defines which $\lambda$ have non-zero weight spaces

## Enables
- **Weight decomposition theorem** -- $V = \bigoplus V[\lambda]$
- **Highest weight vector** -- lives in a one-dimensional weight space

## Contrasts With
- **Root space** -- root spaces $\mathfrak{g}_\alpha$ are weight spaces of the adjoint representation specifically

# Common Errors
- **Error**: Assuming all weight spaces have dimension 1
  **Correction**: Only the highest weight space of an irreducible representation is guaranteed to be one-dimensional (Theorem 9.10(3))

# Common Confusions
- **Confusion**: Confusing weight spaces with root spaces
  **Clarification**: Root spaces are weight spaces of the adjoint representation; weight spaces exist for any representation

# Source Reference
Chapter 9: Representations of Semisimple Lie Algebras, Section 9.1, Definition 9.1, p. 110.

# Verification Notes
- Definition source: Direct from Definition 9.1
- Confidence rationale: Explicit definition in source
- Uncertainties: None
- Cross-reference status: Verified against planned cards
