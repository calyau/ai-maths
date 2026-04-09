---
# === CORE IDENTIFICATION ===
concept: Classification of Semisimple Lie Algebras
slug: classification-of-semisimple-lie-algebras

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
  - "Theorem 8.56"
  - "Killing-Cartan classification"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - classification-of-root-systems
  - serre-relations
extends:
  - classification-of-root-systems
related:
  - dynkin-diagram
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How are semisimple Lie algebras classified?"
  - "What is the bijection between root systems and Lie algebras?"
---

# Quick Definition
Simple finite-dimensional complex Lie algebras are in bijection with connected Dynkin diagrams: $A_n, B_n, C_n, D_n, E_6, E_7, E_8, F_4, G_2$. The Lie algebra is recovered from the root system via the Serre relations.

# Core Definition
**Theorem 8.54** (p. 108): Let $R$ be a reduced irreducible root system. The Lie algebra $\mathfrak{g}(R)$ with generators $e_i, f_i, h_i$ and relations (8.27)--(8.31) (the Serre relations) is a finite-dimensional semisimple Lie algebra with root system $R$.

**Corollary 8.55** (p. 108):
1. If $\mathfrak{g}$ has root system $R$, then $\mathfrak{g} \simeq \mathfrak{g}(R)$.
2. There is a natural bijection between isomorphism classes of reduced root systems and isomorphism classes of finite-dimensional complex semisimple Lie algebras. The algebra is simple iff the root system is irreducible.

**Theorem 8.56** (p. 108): Simple finite-dimensional complex Lie algebras are classified by Dynkin diagrams $A_n,\ldots,G_2$ listed in Theorem 8.49.

# Prerequisites
- **classification-of-root-systems** -- classifies the Dynkin diagrams
- **serre-relations** -- allow recovery of the Lie algebra from the root system

# Key Properties
1. The bijection: root system $\leftrightarrow$ Lie algebra (up to isomorphism)
2. Simple algebra $\leftrightarrow$ irreducible root system $\leftrightarrow$ connected Dynkin diagram
3. Semisimple = direct sum of simples $\leftrightarrow$ union of irreducible root systems $\leftrightarrow$ disconnected diagram
4. $A_n \leftrightarrow \mathfrak{sl}(n+1,\mathbb{C})$
5. $B_n, C_n, D_n$ correspond to $\mathfrak{so}$ and $\mathfrak{sp}$ (classical types)
6. $E_6, E_7, E_8, F_4, G_2$ give the exceptional Lie algebras

# Construction / Recognition
Given a Dynkin diagram:
1. Write the Cartan matrix from the diagram
2. Define $\mathfrak{g}$ by the Serre generators and relations
3. The resulting Lie algebra is finite-dimensional and has the given root system

# Context & Application
This is one of the great classification results of 19th-20th century mathematics, originally due to Killing and Cartan. It shows that the "continuous symmetries" (semisimple Lie algebras) are completely determined by a combinatorial-geometric object (the Dynkin diagram). The classification governs much of modern physics (gauge theory, particle physics) and mathematics (algebraic geometry, number theory).

# Examples
**Example** (p. 108): $A_n \to \mathfrak{sl}(n+1,\mathbb{C})$. The Lie algebra of type $E_6$ is commonly referred to as "simple Lie algebra of type $E_6$" (p. 108).

# Relationships
## Builds Upon
- **classification-of-root-systems** -- provides the combinatorial classification
- **serre-relations** -- provide the algebra-from-diagram construction

## Enables
- Full structure theory and representation theory of semisimple Lie algebras

## Related
- **dynkin-diagram** -- the classifying object

## Contrasts With
(none)

# Common Errors
- **Error**: Thinking the classification is only for simple (not semisimple) algebras
  **Correction**: Semisimple = direct sum of simples, so classifying simples classifies all semisimples

# Common Confusions
- **Confusion**: Thinking different root systems might give isomorphic Lie algebras
  **Clarification**: The correspondence is a bijection (Corollary 8.55)

# Source Reference
Chapter 8: Root Systems, Section 8.9, page 108. Theorem 8.54, Corollary 8.55, Theorem 8.56.

# Verification Notes
- Definition source: Direct from Theorem 8.56 and Corollary 8.55
- Confidence rationale: HIGH -- the culminating theorem of the chapter
- Uncertainties: Proof of Theorem 8.54 is not given (referenced to [21], [12], [11])
- Cross-reference status: Verified
