---
# === CORE IDENTIFICATION ===
concept: Nil-Negative Subalgebra
slug: nil-negative-subalgebra

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
  - "n_-"
  - "n-minus"
  - "negative nilpotent subalgebra"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - root-decomposition
  - positive-roots
extends: []
related:
  - nil-positive-subalgebra
  - verma-module
contrasts_with:
  - nil-positive-subalgebra

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is n_-?"
  - "What role does n_- play in constructing representations?"
---

# Quick Definition
The nil-negative subalgebra $\mathfrak{n}_-$ is the direct sum of all negative root spaces: $\mathfrak{n}_- = \bigoplus_{\alpha \in R_-} \mathfrak{g}_\alpha$. It is the "lowering" part of the triangular decomposition and generates the Verma module from the highest-weight vector.

# Core Definition
(Kirillov, p. 112): The subalgebra $\mathfrak{n}_- = \bigoplus_{R_-} \mathfrak{g}_\alpha$ appears in Theorem 9.9, which states that every vector in the Verma module $M_\lambda$ can be uniquely written as $v = uv_\lambda$ with $u \in U\mathfrak{n}_-$.

# Prerequisites
- **Root decomposition** -- provides the negative root spaces
- **Positive roots** -- negative roots are $R_- = -R_+$

# Key Properties
1. $\mathfrak{n}_-$ is a nilpotent Lie subalgebra of $\mathfrak{g}$
2. $U\mathfrak{n}_- \to M_\lambda$ via $u \mapsto uv_\lambda$ is an isomorphism of vector spaces (Theorem 9.9)
3. Elements of $\mathfrak{n}_-$ lower weights: if $x \in \mathfrak{g}_{-\alpha}$ with $\alpha \in R_+$, then $x \cdot V[\lambda] \subset V[\lambda - \alpha]$
4. The triangular decomposition gives $U\mathfrak{g} \cong U\mathfrak{n}_- \otimes U\mathfrak{h} \otimes U\mathfrak{n}_+$ (Corollary 4.63)

# Context & Application
While $\mathfrak{n}_+$ annihilates the highest-weight vector, $\mathfrak{n}_-$ generates the rest of the representation. The Verma module $M_\lambda$ is isomorphic to $U\mathfrak{n}_-$ as a vector space (Theorem 9.9), making $U\mathfrak{n}_-$ the "template" for the weight structure of highest-weight modules.

# Examples
**Example**: For $\mathfrak{sl}(n+1, \mathbb{C})$, $\mathfrak{n}_-$ is the subalgebra of strictly lower-triangular matrices.

**Example** (p. 112): For $\mathfrak{sl}(2, \mathbb{C})$, $\mathfrak{n}_- = \mathbb{C}f$, and $U\mathfrak{n}_- = \mathbb{C}[f]$, so the Verma module has basis $\{f^k v_\lambda \mid k \geq 0\}$.

# Relationships
## Builds Upon
- **Root decomposition** -- provides the components

## Enables
- **Verma module** -- $M_\lambda \cong U\mathfrak{n}_-$ as vector spaces

## Contrasts With
- **Nil-positive subalgebra** -- $\mathfrak{n}_+$ raises weights; $\mathfrak{n}_-$ lowers them

# Source Reference
Chapter 9, Section 9.2, Theorem 9.9, p. 112.

# Verification Notes
- Definition source: Synthesized from Theorem 9.9 context
- Confidence rationale: Clearly defined in the text
- Uncertainties: None
- Cross-reference status: Verified
