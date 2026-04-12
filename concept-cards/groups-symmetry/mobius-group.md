---
# === CORE IDENTIFICATION ===
concept: "Mobius Group"
slug: mobius-group

# === CLASSIFICATION ===
category: homomorphisms
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Homomorphisms"
chapter_number: 16
pdf_page: 93
section: null

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - "Moebius group"
  - "group of Mobius transformations"
  - "linear fractional group"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - homomorphism
  - quotient-group
  - first-isomorphism-theorem
extends: []
related:
  - general-linear-group
  - centre-of-a-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Mobius group?"
  - "How is the Mobius group related to GL2(C)?"
---

# Quick Definition

The Mobius group consists of all Mobius transformations $z \mapsto (az + b)/(cz + d)$ of the extended complex plane. It is isomorphic to the quotient of $GL_2(\mathbb{C})$ by its centre.

# Core Definition

Each element $\begin{bmatrix} a & b \\ c & d \end{bmatrix}$ of $GL_2(\mathbb{C})$ gives rise to a Mobius transformation $z \to \frac{az+b}{cz+d}$ of the extended complex plane $\mathbb{C} \cup \{\infty\}$. These transformations form a group, the **Mobius group**, under composition of functions, and this group is isomorphic to the quotient of $GL_2(\mathbb{C})$ by its centre (Armstrong, Ch. 16, Exercise 16.7, p. 96).

# Prerequisites

- **Homomorphism** — The map $GL_2(\mathbb{C}) \to$ Mobius group is a homomorphism
- **Quotient group** — The Mobius group is a quotient
- **First isomorphism theorem** — Identifies the Mobius group as $GL_2(\mathbb{C})/Z(GL_2(\mathbb{C}))$

# Key Properties

1. Mobius transformations form a group under composition
2. The map $GL_2(\mathbb{C}) \to$ Mobius group sending a matrix to its transformation is a surjective homomorphism
3. The kernel is the centre of $GL_2(\mathbb{C})$ (scalar matrices $\lambda I$ with $\lambda \neq 0$)
4. Therefore: Mobius group $\cong GL_2(\mathbb{C})/Z(GL_2(\mathbb{C}))$
5. Equivalently: Mobius group $\cong PGL_2(\mathbb{C})$

# Construction / Recognition

## To Construct:
1. Start with $\begin{bmatrix} a & b \\ c & d \end{bmatrix} \in GL_2(\mathbb{C})$
2. Define the transformation $z \mapsto (az + b)/(cz + d)$
3. Handle $\infty$: if $c \neq 0$, the transformation sends $\infty \mapsto a/c$ and $-d/c \mapsto \infty$

# Context & Application

The Mobius group connects linear algebra ($GL_2(\mathbb{C})$), complex analysis (conformal mappings), and group theory (quotient by centre). Armstrong presents it as an exercise illustrating the First Isomorphism Theorem in a geometric setting.

# Examples

**Example 1** (Exercise 16.7): The identity matrix and $2I$ both give the same Mobius transformation $z \mapsto z$, illustrating that scalar matrices form the kernel.

# Relationships

## Builds Upon
- **First isomorphism theorem** — Identifies the group structure
- **Centre of a group** — The kernel is $Z(GL_2(\mathbb{C}))$

## Related
- **General linear group** — $GL_2(\mathbb{C})$ is the source of the homomorphism

# Common Errors

- **Error**: Thinking different matrices always give different transformations
  **Correction**: Matrices differing by a scalar multiple give the same transformation. The correspondence is many-to-one.

# Common Confusions

- **Confusion**: Confusing the Mobius group with $GL_2(\mathbb{C})$
  **Clarification**: The Mobius group is the quotient $GL_2(\mathbb{C})/Z(GL_2(\mathbb{C}))$, not $GL_2(\mathbb{C})$ itself.

# Source Reference

Chapter 16: Homomorphisms, Exercise 16.7, p. 96 (pdf).

# Verification Notes

- Definition source: From Exercise 16.7
- Confidence rationale: MEDIUM — defined in an exercise rather than the main text; details left to the reader
- Uncertainties: Verification details are left as exercise
