---
# === CORE IDENTIFICATION ===
concept: Nil-Positive Subalgebra
slug: nil-positive-subalgebra

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
pdf_page: 111
section: "9.2 Highest-weight representations and Verma modules"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "n_+"
  - "n-plus"
  - "positive nilpotent subalgebra"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - root-decomposition
  - positive-roots
extends: []
related:
  - nil-negative-subalgebra
  - borel-subalgebra
  - highest-weight-vector
contrasts_with:
  - nil-negative-subalgebra

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is n_+?"
  - "What is the nil-positive subalgebra?"
---

# Quick Definition
The nil-positive subalgebra $\mathfrak{n}_+$ is the direct sum of all positive root spaces: $\mathfrak{n}_+ = \bigoplus_{\alpha \in R_+} \mathfrak{g}_\alpha$. It is a nilpotent Lie subalgebra of $\mathfrak{g}$.

# Core Definition
(Kirillov, p. 111-112): The subalgebra $\mathfrak{n}_+$ is defined as:

$$\mathfrak{n}_+ = \bigoplus_{\alpha \in R_+} \mathfrak{g}_\alpha$$

appearing in the conditions (9.4) that define a highest-weight vector: $xv_\lambda = 0$ for all $x \in \mathfrak{n}_+$.

# Prerequisites
- **Root decomposition** -- provides the root spaces $\mathfrak{g}_\alpha$
- **Positive roots** -- determines which root spaces are included

# Key Properties
1. $\mathfrak{n}_+$ is a nilpotent Lie subalgebra of $\mathfrak{g}$
2. $[\mathfrak{h}, \mathfrak{n}_+] \subset \mathfrak{n}_+$ (each root space is an $\mathfrak{h}$-eigenspace)
3. A highest-weight vector is precisely a vector annihilated by all of $\mathfrak{n}_+$
4. Together with $\mathfrak{h}$, forms the Borel subalgebra: $\mathfrak{b} = \mathfrak{h} \oplus \mathfrak{n}_+$
5. $\dim \mathfrak{n}_+ = |R_+|$

# Construction / Recognition
1. Choose positive roots $R_+$ in the root system
2. Take the direct sum of all root spaces for positive roots

# Context & Application
The nil-positive subalgebra is part of the triangular decomposition $\mathfrak{g} = \mathfrak{n}_- \oplus \mathfrak{h} \oplus \mathfrak{n}_+$, which is the Lie algebra analog of the decomposition of matrices into lower-triangular, diagonal, and upper-triangular parts. In the PBW theorem corollary, $U\mathfrak{g} \cong U\mathfrak{n}_- \otimes U\mathfrak{h} \otimes U\mathfrak{n}_+$.

# Examples
**Example**: For $\mathfrak{sl}(n+1, \mathbb{C})$ with standard positive roots, $\mathfrak{n}_+$ is the subalgebra of strictly upper-triangular matrices.

# Relationships
## Builds Upon
- **Root decomposition** -- provides the components

## Enables
- **Borel subalgebra** -- $\mathfrak{b} = \mathfrak{h} \oplus \mathfrak{n}_+$
- **Highest-weight vector** -- defined by annihilation by $\mathfrak{n}_+$

## Contrasts With
- **Nil-negative subalgebra** -- $\mathfrak{n}_- = \bigoplus_{R_-} \mathfrak{g}_\alpha$ uses negative roots

# Common Confusions
- **Confusion**: Thinking $\mathfrak{n}_+$ is the same as $\mathfrak{b}$
  **Clarification**: $\mathfrak{b} = \mathfrak{h} \oplus \mathfrak{n}_+$ includes the Cartan subalgebra; $\mathfrak{n}_+$ does not

# Source Reference
Chapter 9, Section 9.2, equation (9.4), pp. 111-112.

# Verification Notes
- Definition source: From equation (9.4) context
- Confidence rationale: Clearly stated in the text
- Uncertainties: None
- Cross-reference status: Verified
