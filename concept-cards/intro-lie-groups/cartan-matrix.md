---
# === CORE IDENTIFICATION ===
concept: Cartan Matrix
slug: cartan-matrix

# === CLASSIFICATION ===
category: root-systems
subcategory: dynkin-diagrams
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Root Systems"
chapter_number: 8
pdf_page: 103
section: "8.8. Dynkin diagrams and classification of root systems"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "$A$"
  - "$a_{ij}$"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - simple-roots
  - coroot
extends: []
related:
  - dynkin-diagram
  - quotient-p-mod-q
  - serre-relations
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Cartan matrix?"
  - "How do I find the Cartan matrix from simple roots?"
  - "How does the Cartan matrix relate to the Dynkin diagram?"
---

# Quick Definition
The Cartan matrix $A$ of a root system is the $r \times r$ integer matrix with entries $a_{ij} = \langle\alpha_i^\vee, \alpha_j\rangle = 2(\alpha_i,\alpha_j)/(\alpha_i,\alpha_i)$, encoding all inner product information between simple roots up to isomorphism.

# Core Definition
The Cartan matrix $A$ of a set of simple roots $\Pi \subset R$ is the $r \times r$ matrix with entries (Definition 8.43, equation 8.23, p. 103):

$$a_{ij} = n_{\alpha_j\alpha_i} = \langle\alpha_i^\vee, \alpha_j\rangle = \frac{2(\alpha_i,\alpha_j)}{(\alpha_i,\alpha_i)}$$

# Prerequisites
- **simple-roots** -- the Cartan matrix encodes relationships between simple roots
- **coroot** -- the entries use the coroot pairing

# Key Properties
1. $a_{ii} = 2$ for all $i$ (Lemma 8.44(1))
2. $a_{ij} \leq 0$ and $a_{ij} \in \mathbb{Z}$ for $i \neq j$ (Lemma 8.44(2))
3. $a_{ij}a_{ji} = 4\cos^2\varphi$ where $\varphi$ is the angle between $\alpha_i,\alpha_j$ (Lemma 8.44(3))
4. If $\varphi \neq \pi/2$, then $|\alpha_i|^2/|\alpha_j|^2 = a_{ji}/a_{ij}$ (Lemma 8.44(3))
5. $|P/Q| = |\det A|$ (Exercise 8.4)
6. The Cartan matrix is determined by the Dynkin diagram (Theorem 8.48(2))

# Construction / Recognition
## To compute the Cartan matrix
1. Choose an ordering of simple roots $\alpha_1,\ldots,\alpha_r$
2. For each pair $(i,j)$, compute $a_{ij} = 2(\alpha_i,\alpha_j)/(\alpha_i,\alpha_i)$

## From the Dynkin diagram
1. $a_{ii} = 2$ always
2. No edge: $a_{ij} = a_{ji} = 0$
3. Single edge: $a_{ij} = a_{ji} = -1$
4. Double edge with arrow $i \to j$: $a_{ij} = -1$, $a_{ji} = -2$ (arrow points to shorter root)
5. Triple edge with arrow $i \to j$: $a_{ij} = -1$, $a_{ji} = -3$

# Context & Application
The Cartan matrix is the algebraic encoding of the root system geometry. It determines the root system up to isomorphism (via the Dynkin diagram). It also appears directly in the Serre relations (Section 8.9), which present the Lie algebra.

# Examples
**Example 8.45** (p. 103): For $A_n$, the Cartan matrix is:
$$A = \begin{pmatrix} 2 & -1 & 0 & \cdots \\ -1 & 2 & -1 & \cdots \\ 0 & -1 & 2 & \cdots \\ \vdots & & & \ddots \end{pmatrix}$$
(tridiagonal with 2's on diagonal and $-1$'s on sub/superdiagonal).

# Relationships
## Builds Upon
- **simple-roots** -- the Cartan matrix encodes their geometry
- **coroot** -- entries use the coroot pairing

## Enables
- **dynkin-diagram** -- equivalent graphical representation
- **serre-relations** -- use Cartan matrix entries $a_{ij}$

## Related
- **quotient-p-mod-q** -- $|P/Q| = |\det A|$

## Contrasts With
(none)

# Common Errors
- **Error**: Confusing $a_{ij}$ and $a_{ji}$ (they differ when roots have different lengths)
  **Correction**: $a_{ij} = 2(\alpha_i,\alpha_j)/(\alpha_i,\alpha_i)$ divides by $(\alpha_i,\alpha_i)$, not $(\alpha_j,\alpha_j)$

# Common Confusions
- **Confusion**: Thinking the Cartan matrix is symmetric
  **Clarification**: $A$ is symmetric only for simply-laced root systems (all roots equal length)

# Source Reference
Chapter 8: Root Systems, Section 8.8, pages 103--104. Definition 8.43, Lemma 8.44, Example 8.45.

# Verification Notes
- Definition source: Direct from Definition 8.43
- Confidence rationale: HIGH -- explicit definition with properties
- Uncertainties: None
- Cross-reference status: Verified
