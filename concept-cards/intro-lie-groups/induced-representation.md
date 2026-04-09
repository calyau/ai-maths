---
# === CORE IDENTIFICATION ===
concept: Induced Representation
slug: induced-representation

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
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - "Ind"
  - "induction from subalgebra"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - universal-enveloping-algebra
  - borel-subalgebra
extends: []
related:
  - verma-module
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an induced representation in the Lie algebra context?"
  - "How is the Verma module constructed as an induced representation?"
---

# Quick Definition
An induced representation extends a module over a subalgebra to a module over the full algebra by tensoring with the universal enveloping algebra. For Lie algebras, $\mathrm{Ind}_{U\mathfrak{b}}^{U\mathfrak{g}} V = U\mathfrak{g} \otimes_{U\mathfrak{b}} V$.

# Core Definition
**Remark 9.6** (Kirillov, p. 112): The Verma module can be naturally described as an induced representation:

$$M_\lambda = \mathrm{Ind}_{U\mathfrak{b}}^{U\mathfrak{g}} \mathbb{C}_\lambda = U\mathfrak{g} \otimes_{U\mathfrak{b}} \mathbb{C}_\lambda$$

where $\mathfrak{b} = \mathfrak{h} \oplus \mathfrak{n}_+$ is the Borel subalgebra, and $\mathbb{C}_\lambda$ is the one-dimensional representation of $\mathfrak{b}$ defined by the highest-weight conditions.

# Prerequisites
- **Universal enveloping algebra** -- the tensor product is over $U\mathfrak{b}$
- **Borel subalgebra** -- the subalgebra from which we induce

# Key Properties
1. $\mathrm{Ind}_{U\mathfrak{b}}^{U\mathfrak{g}} V = U\mathfrak{g} \otimes_{U\mathfrak{b}} V$ where the tensor product identifies $ub \otimes v$ with $u \otimes bv$
2. The induced module is a left $U\mathfrak{g}$-module via left multiplication on the first factor
3. Induction is left adjoint to restriction (Frobenius reciprocity)
4. The Verma module is the fundamental example in semisimple Lie algebra theory

# Context & Application
Induction provides a systematic way to construct representations of a larger algebra from representations of a subalgebra. In the context of semisimple Lie algebras, inducing from the Borel subalgebra produces Verma modules, which are the universal highest-weight modules.

# Examples
**Example** (p. 112): $M_\lambda = \mathrm{Ind}_{U\mathfrak{b}}^{U\mathfrak{g}} \mathbb{C}_\lambda$ where $\mathbb{C}_\lambda$ is the one-dimensional $\mathfrak{b}$-module on which $\mathfrak{h}$ acts by $\lambda$ and $\mathfrak{n}_+$ acts by zero.

# Relationships
## Enables
- **Verma module** -- the primary example of induction in this context

## Related
- **Borel subalgebra** -- the subalgebra from which one induces

# Common Confusions
- **Confusion**: Thinking induction always produces finite-dimensional modules
  **Clarification**: Inducing from a finite-dimensional module over a proper subalgebra typically produces an infinite-dimensional module

# Source Reference
Chapter 9, Section 9.2, Remark 9.6, p. 112.

# Verification Notes
- Definition source: Synthesized from Remark 9.6; source notes this is "for readers familiar with the notion"
- Confidence rationale: Medium -- mentioned briefly, not fully developed in this source
- Uncertainties: Full development of induction theory is not in this text
- Cross-reference status: Verified
