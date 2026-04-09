---
# === CORE IDENTIFICATION ===
concept: Irreducible Highest-Weight Module
slug: irreducible-highest-weight-module

# === CLASSIFICATION ===
category: representations
subcategory: highest-weight-theory
tier: advanced

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Representations of Semisimple Lie Algebras"
chapter_number: 9
pdf_page: 113
section: "9.3 Classification of irreducible finite-dimensional representations"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "L_lambda"
  - "irreducible highest weight representation"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - verma-module
  - highest-weight-representation
  - maximal-proper-submodule
extends:
  - highest-weight-representation
related:
  - dominant-integral-weight
  - finite-dimensional-criterion
  - bgg-resolution
contrasts_with:
  - verma-module

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes a Verma module from an irreducible highest-weight module?"
  - "How do I classify irreducible representations using highest weights?"
---

# Quick Definition
The irreducible highest-weight module $L_\lambda$ is the unique (up to isomorphism) irreducible highest-weight representation with highest weight $\lambda$. It is obtained as the quotient $L_\lambda = M_\lambda / J_\lambda$, where $J_\lambda$ is the unique maximal proper submodule of the Verma module.

# Core Definition
**Theorem 9.13** (Kirillov, p. 113): For any $\lambda \in \mathfrak{h}^*$, there exists a unique up to isomorphism irreducible highest weight representation with highest weight $\lambda$. This representation is denoted $L_\lambda$.

The construction: $L_\lambda = M_\lambda / J_\lambda$ where $J_\lambda$ is the sum of all submodules $W \subset M_\lambda$ satisfying $W[\lambda] = 0$. Since $J_\lambda[\lambda] = 0$, it is a proper submodule; since it contains every other proper submodule, it is the unique maximal proper submodule.

# Prerequisites
- **Verma module** -- $L_\lambda$ is a quotient of $M_\lambda$
- **Highest-weight representation** -- $L_\lambda$ is the irreducible one
- **Maximal proper submodule** -- $J_\lambda$ is used in the construction

# Key Properties
1. **Uniqueness**: For each $\lambda$, there is exactly one irreducible highest-weight module (up to isomorphism)
2. **Construction**: $L_\lambda = M_\lambda / J_\lambda$
3. **Finite-dimensional iff $\lambda \in P_+$** (Theorem 9.17)
4. **Every irreducible finite-dimensional representation is some $L_\lambda$** (Corollary 9.15)
5. For generic $\lambda$, $L_\lambda = M_\lambda$ (the Verma module is already irreducible)
6. $L_\lambda$ inherits the weight decomposition from $M_\lambda$, with $P(L_\lambda) \subset \lambda - Q_+$

# Construction / Recognition
## To construct $L_\lambda$
1. Form the Verma module $M_\lambda$
2. Find the unique maximal proper submodule $J_\lambda$ (the sum of all proper submodules)
3. Take the quotient: $L_\lambda = M_\lambda / J_\lambda$

## To recognize $L_\lambda$
1. Check that the module is irreducible
2. Check that it has a highest-weight vector of weight $\lambda$

# Context & Application
The modules $L_\lambda$ are the atoms of representation theory for semisimple Lie algebras. By complete reducibility (Section 6.9), every finite-dimensional representation decomposes as $V = \bigoplus n_i L_{\lambda_i}$. The classification theorem (Theorem 9.17) identifies exactly which $L_\lambda$ are finite-dimensional: precisely those with $\lambda \in P_+$.

# Examples
**Example 9.14** (p. 114): For $\mathfrak{g} = \mathfrak{sl}(2, \mathbb{C})$:
- If $\lambda \in \mathbb{Z}_+$, then $L_\lambda = V_\lambda$ is the $((\lambda+1))$-dimensional irreducible module
- If $\lambda \notin \mathbb{Z}_+$, then $L_\lambda = M_\lambda$ (the Verma module is already irreducible)

# Relationships
## Builds Upon
- **Verma module** -- $L_\lambda$ is a quotient of $M_\lambda$
- **Highest-weight representation** -- $L_\lambda$ is the irreducible one

## Enables
- **Classification of irreducible representations** -- every irreducible is some $L_\lambda$
- **BGG resolution** -- resolves $L_\lambda$ in terms of Verma modules
- **Weyl character formula** -- computes the character of $L_\lambda$

## Contrasts With
- **Verma module** -- $M_\lambda$ is typically reducible and always infinite-dimensional; $L_\lambda$ is irreducible and may be finite-dimensional

# Common Errors
- **Error**: Assuming $L_\lambda$ is always finite-dimensional
  **Correction**: $L_\lambda$ is finite-dimensional if and only if $\lambda \in P_+$ (Theorem 9.17)

# Common Confusions
- **Confusion**: Thinking $L_\lambda$ and $M_\lambda$ are always different
  **Clarification**: For generic $\lambda$ (specifically $\lambda \notin P_+$ in many cases), $M_\lambda$ has no proper submodules, so $L_\lambda = M_\lambda$

# Source Reference
Chapter 9, Section 9.3, Theorem 9.13 and Corollary 9.15, pp. 113-114.

# Verification Notes
- Definition source: Direct from Theorem 9.13
- Confidence rationale: Central theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
