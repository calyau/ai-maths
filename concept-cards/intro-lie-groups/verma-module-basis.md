---
# === CORE IDENTIFICATION ===
concept: Verma Module Basis Theorem
slug: verma-module-basis

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
  - "Theorem 9.9"
  - "PBW basis for Verma module"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - verma-module
  - nil-negative-subalgebra
  - universal-enveloping-algebra
extends:
  - verma-module
related:
  - pbw-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the structure of a Verma module as a vector space?"
  - "How do I compute the weight spaces of a Verma module?"
---

# Quick Definition
The Verma module $M_\lambda$ is isomorphic to $U\mathfrak{n}_-$ as a vector space via the map $u \mapsto uv_\lambda$. This gives an explicit PBW-type basis and determines the weight multiplicities of $M_\lambda$.

# Core Definition
**Theorem 9.9** (Kirillov, p. 112): Let $M_\lambda$ be the Verma module with highest weight $\lambda$.

(1) The map $U\mathfrak{n}_- \to M_\lambda$, $u \mapsto uv_\lambda$, is an isomorphism of vector spaces.

(2) $M_\lambda$ admits a weight decomposition with finite-dimensional weight spaces. The set of weights is $P(M_\lambda) = \lambda - Q_+$, where $Q_+ = \{\sum n_i \alpha_i \mid n_i \in \mathbb{Z}_+\}$.

(3) $\dim M_\lambda[\lambda] = 1$.

# Prerequisites
- **Verma module** -- this theorem describes its structure
- **Nil-negative subalgebra** -- $U\mathfrak{n}_-$ provides the basis
- **Universal enveloping algebra** -- via the PBW theorem

# Key Properties
1. The weight of $uv_\lambda$ for $u \in U\mathfrak{n}_-$ is determined by which negative root vectors appear in $u$
2. Weights of $M_\lambda$ form a "downward cone" from $\lambda$
3. Weight multiplicities equal the number of ways to write $\lambda - \mu$ as a sum of positive roots (Kostant's partition function)
4. The proof uses the PBW theorem corollary: $U\mathfrak{g} \cong U\mathfrak{n}_- \otimes U\mathfrak{h} \otimes U\mathfrak{n}_+$

# Construction / Recognition
A basis for $M_\lambda[\lambda - \sum n_i \alpha_i]$ consists of vectors $f_{\alpha_1}^{n_1} \cdots f_{\alpha_r}^{n_r} v_\lambda$ (using PBW ordering), where the weight is lowered by $\sum n_i \alpha_i$ from $\lambda$.

# Context & Application
This theorem makes the Verma module completely explicit as a vector space. While the $\mathfrak{g}$-module structure is more subtle (understanding submodules requires deeper analysis), the vector space structure and weight multiplicities are computable directly from the root system.

# Examples
**Example** (p. 112): For $\mathfrak{sl}(2, \mathbb{C})$, $U\mathfrak{n}_- = \mathbb{C}[f]$, so $M_\lambda$ has basis $\{v_\lambda, fv_\lambda, f^2 v_\lambda, \ldots\}$ with weights $\lambda, \lambda - 2, \lambda - 4, \ldots$, each of multiplicity 1.

# Relationships
## Builds Upon
- **Verma module** -- this describes its structure
- **PBW theorem** -- the key tool in the proof

## Enables
- **Weight multiplicity computations** -- for Verma modules and their quotients
- **Submodule analysis** -- understanding which elements generate submodules

# Common Errors
- **Error**: Applying this basis theorem to quotients of Verma modules (like $L_\lambda$)
  **Correction**: For quotients, the map $U\mathfrak{n}_- \to V$ is surjective but not injective (Theorem 9.10)

# Source Reference
Chapter 9, Section 9.2, Theorem 9.9, pp. 112-113.

# Verification Notes
- Definition source: Direct from Theorem 9.9
- Confidence rationale: Explicit theorem with proof sketch
- Uncertainties: None
- Cross-reference status: Verified
