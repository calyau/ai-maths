---
# === CORE IDENTIFICATION ===
concept: Borel Subalgebra
slug: borel-subalgebra

# === CLASSIFICATION ===
category: representations
subcategory: highest-weight-theory
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Representations of Semisimple Lie Algebras"
chapter_number: 9
pdf_page: 112
section: "9.2 Highest-weight representations and Verma modules"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "b"
  - "h + n_+"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cartan-subalgebra
  - nil-positive-subalgebra
  - root-decomposition
extends:
  - cartan-subalgebra
related:
  - verma-module
  - highest-weight-representation
  - nil-negative-subalgebra
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Borel subalgebra?"
  - "What must I know before studying representations of semisimple Lie algebras?"
---

# Quick Definition
The Borel subalgebra is $\mathfrak{b} = \mathfrak{h} \oplus \mathfrak{n}_+$, the sum of the Cartan subalgebra and the nilpotent subalgebra of positive root vectors. It is the largest solvable subalgebra of $\mathfrak{g}$.

# Core Definition
**Remark 9.6** (Kirillov, p. 112): The Borel subalgebra is defined as $\mathfrak{b} = \mathfrak{h} \oplus \mathfrak{n}_+$, where $\mathfrak{n}_+ = \bigoplus_{\alpha \in R_+} \mathfrak{g}_\alpha$. The Verma module $M_\lambda$ is the induced representation $M_\lambda = \mathrm{Ind}_{U\mathfrak{b}}^{U\mathfrak{g}} \mathbb{C}_\lambda$.

# Prerequisites
- **Cartan subalgebra** -- the $\mathfrak{h}$ summand
- **Nil-positive subalgebra** -- the $\mathfrak{n}_+$ summand
- **Root decomposition** -- provides the positive root spaces

# Key Properties
1. $\mathfrak{b} = \mathfrak{h} \oplus \mathfrak{n}_+$ as vector spaces
2. $\mathfrak{b}$ is a Lie subalgebra of $\mathfrak{g}$ (since $[\mathfrak{h}, \mathfrak{n}_+] \subset \mathfrak{n}_+$ and $[\mathfrak{n}_+, \mathfrak{n}_+] \subset \mathfrak{n}_+$)
3. $\mathfrak{b}$ is the largest solvable subalgebra (Borel's theorem)
4. One-dimensional representations of $\mathfrak{b}$ are parametrized by $\lambda \in \mathfrak{h}^*$ (since $\mathfrak{n}_+$ must act by zero)
5. $\dim \mathfrak{b} = r + |R_+|$ where $r = \mathrm{rank}(\mathfrak{g})$

# Construction / Recognition
1. Fix a Cartan subalgebra $\mathfrak{h}$ and a choice of positive roots $R_+$
2. Form $\mathfrak{n}_+ = \bigoplus_{\alpha \in R_+} \mathfrak{g}_\alpha$
3. The Borel subalgebra is $\mathfrak{b} = \mathfrak{h} \oplus \mathfrak{n}_+$

# Context & Application
The Borel subalgebra plays a central role in the construction of highest-weight representations via induction. A highest-weight vector with weight $\lambda$ is precisely a one-dimensional $\mathfrak{b}$-module $\mathbb{C}_\lambda$ on which $\mathfrak{h}$ acts by $\lambda$ and $\mathfrak{n}_+$ acts by zero. The Verma module is obtained by inducing this $\mathfrak{b}$-module to all of $\mathfrak{g}$.

# Examples
**Example** (p. 112): For $\mathfrak{g} = \mathfrak{sl}(2, \mathbb{C})$, the Borel subalgebra is $\mathfrak{b} = \mathbb{C}h \oplus \mathbb{C}e$, the subalgebra of upper-triangular matrices.

**Example**: For $\mathfrak{g} = \mathfrak{sl}(n+1, \mathbb{C})$, the Borel subalgebra (with standard choices) is the subalgebra of upper-triangular matrices.

# Relationships
## Builds Upon
- **Cartan subalgebra** -- the diagonal part of $\mathfrak{b}$
- **Nil-positive subalgebra** -- the nilpotent radical of $\mathfrak{b}$

## Enables
- **Verma module** -- constructed as $\mathrm{Ind}_{U\mathfrak{b}}^{U\mathfrak{g}} \mathbb{C}_\lambda$
- **Highest-weight representation** -- the highest-weight condition is "$\mathfrak{n}_+$ acts by zero on $v_\lambda$"

# Common Errors
- **Error**: Confusing the Borel subalgebra with the Cartan subalgebra
  **Correction**: $\mathfrak{b}$ contains $\mathfrak{h}$ as a proper subalgebra; it also includes all positive root spaces

# Common Confusions
- **Confusion**: Thinking there is only one Borel subalgebra
  **Clarification**: The choice of Borel subalgebra depends on the choice of positive roots $R_+$; different choices give conjugate Borel subalgebras

# Source Reference
Chapter 9, Section 9.2, Remark 9.6, p. 112.

# Verification Notes
- Definition source: From Remark 9.6; the Borel subalgebra is introduced functionally rather than with a formal definition
- Confidence rationale: Clear from context though not given a numbered definition
- Uncertainties: None
- Cross-reference status: Verified
