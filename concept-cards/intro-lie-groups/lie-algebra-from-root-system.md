---
# === CORE IDENTIFICATION ===
concept: Lie Algebra from Root System
slug: lie-algebra-from-root-system

# === CLASSIFICATION ===
category: root-systems
subcategory: dynkin-diagrams
tier: advanced

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Root Systems"
chapter_number: 8
pdf_page: 108
section: "8.9. Serre relations and classification of semisimple Lie algebras"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "$\\mathfrak{g}(R)$"
  - "Theorem 8.54"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - serre-relations
  - serre-generators
  - classification-of-root-systems
extends: []
related:
  - classification-of-semisimple-lie-algebras
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Can you recover a Lie algebra from its root system?"
  - "Is the Lie algebra uniquely determined by the root system?"
---

# Quick Definition
Given a reduced irreducible root system $R$, the Lie algebra $\mathfrak{g}(R)$ defined by Serre generators and relations is a finite-dimensional semisimple Lie algebra with root system $R$, and any semisimple Lie algebra with root system $R$ is isomorphic to $\mathfrak{g}(R)$.

# Core Definition
**Theorem 8.54** (p. 108): Let $R$ be a reduced irreducible root system with simple roots $\Pi = \{\alpha_1,\ldots,\alpha_r\}$. Let $\mathfrak{g}(R)$ be the complex Lie algebra with generators $e_i, f_i, h_i$ ($i = 1,\ldots,r$) and relations (8.27)--(8.31). Then $\mathfrak{g}(R)$ is a finite-dimensional semisimple Lie algebra with root system $R$.

**Corollary 8.55(1)**: If $\mathfrak{g}$ has root system $R$, then $\mathfrak{g} \simeq \mathfrak{g}(R)$.

# Prerequisites
- **serre-relations** -- the defining relations of $\mathfrak{g}(R)$
- **serre-generators** -- the generating set
- **classification-of-root-systems** -- provides the input data $R$

# Key Properties
1. $\mathfrak{g}(R)$ is finite-dimensional (the key nontrivial step of the proof)
2. $\mathfrak{g}(R)$ is semisimple with root system $R$
3. Any other semisimple Lie algebra with root system $R$ is isomorphic to $\mathfrak{g}(R)$ (uniqueness)
4. The construction provides a bijection: root systems $\leftrightarrow$ semisimple Lie algebras

# Construction / Recognition
1. Start with a reduced irreducible root system $R$ (equivalently, a connected Dynkin diagram)
2. Compute the Cartan matrix $A$
3. Define $\mathfrak{g}(R)$ by generators $\{e_i, f_i, h_i\}$ and Serre relations using $A$
4. The result is the unique (up to isomorphism) simple Lie algebra with root system $R$

# Context & Application
This theorem closes the loop: Chapter 7 showed Lie algebra $\to$ root system; Theorem 8.54 shows root system $\to$ Lie algebra. Together with the classification of root systems (Theorem 8.49), this yields the complete classification of simple Lie algebras (Theorem 8.56).

# Examples
**Example** (p. 108): The Lie algebra $\mathfrak{g}(A_n) = \mathfrak{sl}(n+1,\mathbb{C})$.

# Relationships
## Builds Upon
- **serre-relations**, **serre-generators**

## Enables
- **classification-of-semisimple-lie-algebras**

## Related
(none)

## Contrasts With
(none)

# Common Errors
(none)

# Common Confusions
- **Confusion**: Thinking finite-dimensionality of $\mathfrak{g}(R)$ is obvious
  **Clarification**: It is highly nontrivial that the algebra defined by Serre relations is finite-dimensional; this is the key step in the proof (p. 108)

# Source Reference
Chapter 8: Root Systems, Section 8.9, page 108. Theorem 8.54, Corollary 8.55.

# Verification Notes
- Definition source: Direct from Theorem 8.54
- Confidence rationale: HIGH -- explicit theorem
- Uncertainties: Proof not given in text (referenced to [21], [12], [11])
- Cross-reference status: Verified
