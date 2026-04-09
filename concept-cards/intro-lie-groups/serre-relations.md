---
# === CORE IDENTIFICATION ===
concept: Serre Relations
slug: serre-relations

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
pdf_page: 107
section: "8.9. Serre relations and classification of semisimple Lie algebras"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Chevalley-Serre relations"
  - "defining relations for semisimple Lie algebras"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cartan-matrix
  - simple-roots
extends: []
related:
  - serre-generators
  - classification-of-semisimple-lie-algebras
  - coxeter-relations
contrasts_with:
  - coxeter-relations

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the Serre relations?"
  - "How do the Serre relations present a semisimple Lie algebra?"
---

# Quick Definition
The Serre relations are a complete set of defining relations for a semisimple Lie algebra in terms of Chevalley generators $e_i, f_i, h_i$. They express all commutation relations using only the Cartan matrix entries $a_{ij}$.

# Core Definition
The Serre relations (Theorem 8.52(3), equations 8.27--8.31, pp. 107--108) are:

$$[h_i, h_j] = 0$$
$$[h_i, e_j] = a_{ij}e_j, \qquad [h_i, f_j] = -a_{ij}f_j$$
$$[e_i, f_j] = \delta_{ij}h_i$$
$$(\operatorname{ad} e_i)^{1-a_{ij}}e_j = 0 \qquad (i \neq j)$$
$$(\operatorname{ad} f_i)^{1-a_{ij}}f_j = 0 \qquad (i \neq j)$$

where $a_{ij}$ are entries of the Cartan matrix.

# Prerequisites
- **cartan-matrix** -- the entries $a_{ij}$ appear in all relations
- **simple-roots** -- the generators correspond to simple roots

# Key Properties
1. Relations (8.27)--(8.29) are the "easy" relations: Cartan subalgebra commutativity, root space eigenvalues, and $\mathfrak{sl}(2)$-triple structure
2. Relations (8.30)--(8.31) are the "hard" relations: they control the nilpotent parts
3. The exponent $1 - a_{ij}$ is a positive integer for $i \neq j$ (since $a_{ij} \leq 0$)
4. These relations are a complete set of defining relations (Theorem 8.54)
5. The proof of (8.30) uses $\mathfrak{sl}(2)$ representation theory: if $e_i f_j = 0$ and $h_i f_j = -a_{ij}f_j$, then $f_j$ is a highest-weight vector of weight $-a_{ij}$ for the $\mathfrak{sl}(2)$ triple $\{e_i, f_i, h_i\}$

# Construction / Recognition
To write the Serre relations for a specific root system:
1. Compute the Cartan matrix $A = (a_{ij})$
2. Write down the $3r$ generators $\{e_i, f_i, h_i\}_{i=1}^r$
3. Apply the five families of relations using the $a_{ij}$ values

# Context & Application
The Serre relations are the bridge between root systems and Lie algebras. They show that the Lie algebra is completely determined by the Cartan matrix (equivalently, the Dynkin diagram), which combines with the classification of root systems to give the classification of semisimple Lie algebras.

# Examples
**Example**: For $A_2$ with $a_{12} = a_{21} = -1$, the Serre relation $(\operatorname{ad} e_1)^2 e_2 = 0$ says $[e_1,[e_1,e_2]] = 0$, reflecting that $\alpha_1 + 2\alpha_2$ is not a root.

# Relationships
## Builds Upon
- **cartan-matrix** -- provides the $a_{ij}$

## Enables
- **classification-of-semisimple-lie-algebras** -- Serre relations + root system classification = Lie algebra classification

## Related
- **serre-generators** -- the generators appearing in the relations

## Contrasts With
- **coxeter-relations** -- present the Weyl group; Serre relations present the Lie algebra

# Common Errors
- **Error**: Forgetting the exponent is $1 - a_{ij}$ (not $-a_{ij}$ or $a_{ij}$)
  **Correction**: The exponent is $1 - a_{ij}$; since $a_{ij} \leq 0$ for $i \neq j$, this is $\geq 1$

# Common Confusions
- **Confusion**: Conflating Serre relations with Coxeter relations
  **Clarification**: Serre relations present the Lie algebra $\mathfrak{g}$; Coxeter relations present the Weyl group $W$. They involve different algebraic structures.

# Source Reference
Chapter 8: Root Systems, Section 8.9, pages 107--108. Theorem 8.52(3), equations (8.27)--(8.31).

# Verification Notes
- Definition source: Direct from Theorem 8.52(3)
- Confidence rationale: HIGH -- explicit equations
- Uncertainties: None
- Cross-reference status: Verified
